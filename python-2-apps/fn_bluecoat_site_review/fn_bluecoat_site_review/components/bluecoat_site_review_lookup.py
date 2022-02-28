# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import json
import requests
import sys
import xmltodict
import resilient
import datetime

class SiteReview(object):
    def __init__(self):
        self.baseurl = "https://sitereview.bluecoat.com/resource/lookup"
        self.headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}

    def sitereview(self, url):
        payload = {"url": url, "captcha":""}

        try:
            self.req = requests.post(
                self.baseurl,
                headers=self.headers,
                data=json.dumps(payload),
            )

        except requests.ConnectionError:
            sys.exit("[-] ConnectionError: " \
                     "A connection error occurred")

        return(json.dumps(xmltodict.parse(self.req.content), sort_keys=True, indent=4))

    def check_response(self, response):
        if self.req.status_code != 200:
            sys.exit("[-] HTTP {} returned".format(req.status_code))
        else:
            self.category = response["categorization"][0]["name"]
            self.date = response["translatedRateDates"][0]["text"][0:35]
            self.url = response["url"]



class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'bluecoat_site_review_lookup"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_bluecoat_site_review", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_bluecoat_site_review", {})

    @function("bluecoat_site_review_lookup")
    def _bluecoat_site_review_lookup_function(self, event, *args, **kwargs):
        """Function: This function takes an artifact of type URL or DNS name and returns those results as a json object."""

        # talks to the config file and gets the auth credentials necessary to talk to Resilient Endpoint
        parser = resilient.ArgumentParser(config_file=resilient.get_config_file())
        opts = parser.parse_args()
        client = resilient.get_client(opts)

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

            # Assignment for successful completion of the code
            results = True

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            s = SiteReview()
            response = s.sitereview(artifact_value)

            response_json = json.loads(response)
            #log.info(type(response_json))
            #log.info(json.dumps(response_json, indent=4, sort_keys=True)) # Troubleshooting

            # handles if there is no result in the JSON Return Object:
            if response_json is None:
                log.debug("There were no results...")
                results = False

            # This handles if the categorizaton is a list in the JSON object that needs to be traversed/isolated or not
            if response_json.get('FailedResult'):
                results = False
            elif isinstance(response_json['CategorizationResult']['categorization']['categorization'],list):
                categorization_name = response_json['CategorizationResult']['categorization']['categorization'][1]['name']
            else:
                categorization_name = response_json['CategorizationResult']['categorization']['categorization']['name']


            if results is True:
                bluecoat_object = {
                    "url": response_json['CategorizationResult']['url'],
                    "categorization_name": categorization_name,
                    "timestamp": datetime.datetime.utcnow().strftime("%a %b %d %H:%M:%S UTC %Y")
                }
            else:
                bluecoat_object = "There were either no results or the URL is in bad form..."


            yield StatusMessage("done...")

            results = {
                "value": bluecoat_object,
                "success": results
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()