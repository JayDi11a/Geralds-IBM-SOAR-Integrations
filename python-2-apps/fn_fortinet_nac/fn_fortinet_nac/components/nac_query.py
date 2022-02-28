# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import requests
import json
import xmltodict
import resilient
from requests.exceptions import ConnectionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'nac_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_fortinet_nac", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_fortinet_nac", {})

    @function("nac_query")
    def _nac_query_function(self, event, *args, **kwargs):
        """Function: This function takes a hostname (NT ID) or user ID and returns the corresponding endpoint information (location - switch and port name, system ip address, etc)"""

        # talks to the config file and gets the auth credentials necessary to talk to Resilient Endpoint
        parser = resilient.ArgumentParser(config_file=resilient.get_config_file())
        opts = parser.parse_args()
        client = resilient.get_client(opts)

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
            # Gate Logic Error Handling
            success = True

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_value = kwargs.get("artifact_value")  # text
            artifact_id = kwargs.get("artifact_id")  # number
            artifact_type = kwargs.get("artifact_type")  # text
            hostname = kwargs.get("hostname")  # text
            login_id = kwargs.get("login_id")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("artifact_value: %s", artifact_value)
            log.info("artifact_id: %s", artifact_id)
            log.info("artifact_type: %s", artifact_type)
            log.info("hostname: %s", hostname)
            log.info("login_id: %s", login_id)

            # retreive the Fortinet NAC API username and key to pass to the Fortinet NAC endpoint
            user = get_config_option("user_name")
            key = get_config_option("api_key")
            server = get_config_option("server_name")

            query_results = ""

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            headers = {
                'accept': 'application/xml',
            }

            if login_id is not None:
                # This request takes the login user id and returns the corresponding results
                params = (
                    ('loggedOnUserId', login_id),

                )


                try:
                    login_user_query = requests.get('https://{}:8443/api/host/'.format(server), headers=headers,
                                                params=params, verify=False,
                                                auth=(user, key), timeout=30)

                    # This converts the XML object to JSON and then to string
                    login_user_query_object = json.dumps(xmltodict.parse(login_user_query.content), sort_keys=True,
                                                     indent=4)

                    # print(login_user_query_object)
                    # print(type(login_user_query_object))  # - confirms that I am converting that query results object to a string

                    # This converts the String back to a JSON Object for the Data Table
                    login_user_query_json = json.loads(login_user_query_object)

                    #print(type(login_user_query_json))  # - confirms that I am converting the query results object back to a dict


                    #if 'endpoint' not in login_user_query_json:
                    if login_user_query_json['endpointSearchResult']['endpoints'] is None:
                        query_results = 'no results'
                    else:
                        query_results = {
                            "user": login_user_query_json['endpointSearchResult']['endpoints']['endpoint']['loggedOnUserId'],
                            "location": login_user_query_json['endpointSearchResult']['endpoints']['endpoint']['location'],
                            "ip_address": login_user_query_json['endpointSearchResult']['endpoints']['endpoint']['ipAddress'],
                            "hostname": login_user_query_json['endpointSearchResult']['endpoints']['endpoint']['hostName'],
                            "mac_address": login_user_query_json['endpointSearchResult']['endpoints']['endpoint']['macAddress'],
                            "os": login_user_query_json['endpointSearchResult']['endpoints']['endpoint']['os']
                        }
                except ConnectionError as e:
                    print e
                    query_results = 'no response'

            if hostname is not None:
                # This request takes the hostname and returns the corresponding results
                params = (
                    ('hostName', hostname),

                )


                try:
                    hostname_query = requests.get('https://{}:8443/api/host/'.format(server), headers=headers,
                                              params=params,
                                              verify=False,
                                              auth=(user, key), timeout=30)

                    # This converts the XML object to JSON and then to string
                    hostname_query_object = json.dumps(xmltodict.parse(hostname_query.content), sort_keys=True, indent=4)

                    # This converts the String back to a JSON Object for the data table
                    hostname_query_json = json.loads(hostname_query_object)


                    #if 'endpoint' not in hostname_query_json:
                    if hostname_query_json['endpointSearchResult']['endpoints'] is None:
                        query_results = "no results"
                        success = False
                    else:
                        query_results = {
                            "user": hostname_query_json['endpointSearchResult']['endpoints']['endpoint']['loggedOnUserId'],
                            "location": hostname_query_json['endpointSearchResult']['endpoints']['endpoint']['location'],
                            "ip_address": hostname_query_json['endpointSearchResult']['endpoints']['endpoint']['ipAddress'],
                            "hostname": hostname_query_json['endpointSearchResult']['endpoints']['endpoint']['hostName'],
                            "mac_address": hostname_query_json['endpointSearchResult']['endpoints']['endpoint']['macAddress'],
                            "os": hostname_query_json['endpointSearchResult']['endpoints']['endpoint']['os']
                        }
                except ConnectionError as e:
                    print e
                    query_results = 'no response'

            yield StatusMessage("done...")

            results = {
                "value": query_results,
                "success": success
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except ConnectionError:
            print
        except Exception:
            yield FunctionError()