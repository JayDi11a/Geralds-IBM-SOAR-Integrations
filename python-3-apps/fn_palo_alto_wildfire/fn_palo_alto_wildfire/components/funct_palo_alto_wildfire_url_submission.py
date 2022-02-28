# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_palo_alto_wildfire.util.selftest as selftest
from pyldfire import WildFire
from fn_palo_alto_wildfire.util import function_utils
import requests
import xmltodict

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'palo_alto_wildfire_url_submission"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_palo_alto_wildfire", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_palo_alto_wildfire", {})

    @function("palo_alto_wildfire_url_submission")
    def _palo_alto_wildfire_url_submission_function(self, event, *args, **kwargs):
        """Function: This function submits a URL in the Resilient Incident and submits it to the Palo Alto WildFire endpoint. The results of the url submission are then returned to the Incident."""

        # - method that retreives specific attributes needed for the function to run like credentials, etc...
        def get_config_option(option_name, optional=False):
            """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
            option = self.options.get(option_name)

            if option is None and optional is False:
                err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function".format(
                    option_name)
                raise ValueError(err)
            else:
                return option

        # Authentication for WildFire Endpoint
        api_key = get_config_option("wildfire_api_key")

        # Assign API key to the WildFire object
        wildfire = WildFire(api_key)

        # Global variable that stores submission id
        # in the form of a sha256 hash
        submission_sha256 = ''

        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_value = kwargs.get("artifact_value")  # text
            artifact_type = kwargs.get("artifact_type")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("artifact_value: %s", artifact_value)
            log.info("artifact_type: %s", artifact_type)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            # Parameters and Endpoint for WildFire REST API
            files = {
                'apikey': (None, api_key),
                'link': (None, artifact_value),
            }

            url_submission_response = requests.post('https://wildfire.paloaltonetworks.com/publicapi/submit/link',
                                                    files=files)
            url_submission_xml = url_submission_response.content
            url_submission_dict = xmltodict.parse(url_submission_xml)

            # Extracts value from ordered dictionary key we submitted
            for found in function_utils.listRecursive(url_submission_dict, 'sha256'):
                submission_sha256 = found

            # Submits the hash and returns the corresponding verdict
            submission_verdict = wildfire.get_verdicts(submission_sha256)
            log.info(submission_verdict)

            yield StatusMessage("done...")

            results = {
                "value": submission_verdict
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()