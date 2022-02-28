# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import requests
import json
import datetime


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'passive_total_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_passive_total", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_passive_total", {})

    @function("passive_total_query")
    def _passive_total_query_function(self, event, *args, **kwargs):
        """Function: This function takes a URL/Domain artifact and returns classification, date of when it was first and last seen, subdomains, and tags associated with it to a data table."""

        # - method that retreives specific attributes needed for the function to run like credentials, etc...
        def get_config_option(option_name, optional=False):
            """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
            option = self.options.get(option_name)

            if option is None and optional is False:
                err = "'{0}' is mandatory and is not set in ~/.resilient/app.config file. You must set this value to run this function".format(
                    option_name)
                raise ValueError(err)
            else:
                return option

        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number
            artifact_type = kwargs.get("artifact_type")  # text
            artifact_value = kwargs.get("artifact_value")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("artifact_id: %s", artifact_id)
            log.info("artifact_type: %s", artifact_type)
            log.info("artifact_value: %s", artifact_value)

            # retreive the Passive Total credentials from the config file to be set
            uid = get_config_option("user_name")
            creds = get_config_option("password")



            # The header that corresponds to object return type
            headers = {
                'Content-Type':'application/json',
            }

            data = (
                ('query', ('{}').format(artifact_value)),
            )

            if artifact_value.startswith('http'):
                http_value = artifact_value.replace("http://","")
                http_value = http_value.replace("www.","")
                http_value = http_value.split('/',1)[0]
                #log.debug(http_value)

                data = (
                    ('query', ('{}').format(http_value)),
                )


            if artifact_value.startswith('https'):
                https_value = artifact_value.replace("https://","")
                https_value = https_value.replace("www.","")
                https_value = https_value.split('/',1)[0]
                #log.debug(https_value)

                data = (
                    ('query', ('{}').format(https_value)),
                )


            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")



            # This gets the first seen and last seen of the URL/Domain
            dns_response = requests.get('https://api.passivetotal.org/v2/dns/passive', headers=headers,
                                     params=data, auth=(uid, creds))
            dns_response.raise_for_status()

            dns_response_json = dns_response.json()
            log.debug(dns_response_json['firstSeen'])
            log.debug(dns_response_json['lastSeen'])
            # dns_response_string = json.dumps(dns_response_json, sort_keys=True, indent=4)



            # This gets the classification of the URL/Domain
            classification_response = requests.get('https://api.passivetotal.org/v2/actions/classification', headers=headers,
                                     params=data, auth=(uid, creds))
            classification_response.raise_for_status()

            classification_response_json = classification_response.json()
            log.debug(classification_response_json['classification'])
            # classificaiton_response_string = json.dumps(classification_response_json, sort_keys=True, indent=4)



            # This gets the subdomains associated with the URL/Domain
            subdomain_response = requests.get('https://api.passivetotal.org/v2/enrichment/subdomains', headers=headers,
                                     params=data, auth=(uid, creds))
            subdomain_response.raise_for_status()

            subdomain_response_json = subdomain_response.json()
            log.debug(subdomain_response_json['subdomains'][:10])
            # subdomain_response_string = json.dumps(subdomain_response_json, sort_keys=True, indent=4)



            # This gets the tags associated with the URL/Domain
            tag_response = requests.get('https://api.passivetotal.org/v2/actions/tags', headers=headers, params=data, auth=(uid, creds))
            tag_response.raise_for_status()

            tag_response_json = tag_response.json()
            log.debug(tag_response_json['tags'])
            # tag_response_string = json.dumps(tag_response_json, sort_keys=True, indent=4)

            # Stringifying the elements from the lists from the return objects
            subdomains = subdomain_response_json['subdomains'][:10]
            subdomans_string = ', '.join(str(e) for e in subdomains)

            tags = tag_response_json['tags']
            tags_string = ', '.join(str(e) for e in tags)

            # Create a dictionary object set it to a value to be set as a results value
            passive_total_object = {
                "url_or_domain": artifact_value,
                "classification": classification_response_json['classification'],
                "first_seen": dns_response_json['firstSeen'],
                "last_seen": dns_response_json['lastSeen'],
                "subdomains": subdomans_string,
                "tags": tags_string
            }

            # Assignment for successful completion of the code
            if passive_total_object.get('url_or_domain') and passive_total_object.get('classification') and passive_total_object.get('first_seen') and passive_total_object.get('last_seen') and passive_total_object.get('subdomains') and passive_total_object.get('tags') is None:
                results = False
            else:
                results = True

            yield StatusMessage("done...")

            results = {
                "value": passive_total_object,
                "success": results
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()