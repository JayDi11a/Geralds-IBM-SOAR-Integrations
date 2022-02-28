# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_sentinalone_endpoint_protection.util.selftest as selftest
import requests
import json

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'sentinalone_initiate_scan"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_sentinalone_endpoint_protection", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_sentinalone_endpoint_protection", {})

    @function("sentinalone_initiate_scan")
    def _sentinalone_initiate_scan_function(self, event, *args, **kwargs):
        """Function: This function takes in an artifact of type IP to be passed in as a filter object value. The filter object returns the corresponding host machine(s) and then executes the scan."""

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


        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_value = kwargs.get("artifact_value")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("artifact_value: %s", artifact_value)

            # retreive the API username and key to pass to the endpoint
            api = get_config_option("api_key")
            host = get_config_option("server")

            # Assignment for successful completion of the code
            result = True

            # Reports message back to user on status of run
            message = ""

            headers = {
                'Content-Type': 'application/json',
            }

            params = (
                ('apiToken', '{}'.format(api)),
            )

            # Hostname parameter
            #data = '{"filter": {"networkInterfaceInet__contains": [' + '"' + str(artifact_value) + '"' + ']}, "data": {}}'

            # Endpoint Name parameter
            data = '{"filter": {"computerName__contains": [' + '"' + str(
                artifact_value) + '"' + ']}, "data": {}}'

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            get_scan_results = requests.post('https://{}/web/api/v2.0/agents/actions/initiate-scan'.format(host),
                                     headers=headers, params=params, data=data)

            #log.info(get_scan_results.content)
            scan_results_json = json.loads(get_scan_results.content)
            #log.info(scan_results_json)


            if scan_results_json['data']['affected'] == 0:
                result = True
                message = "I couldn't find this machine to perform the scan..."
            elif scan_results_json['data']['affected'] > 0:
                result = True
                message = "Scan was successfully initialized..."
            elif scan_results_json['errors']:
                result = False
                message = str(scan_results_json['errors']['detail'])

            # if keys aren't there write error message, set to false
            if scan_results_json is None:
                result = False
                message = "Something went wrong..."


            yield StatusMessage("done...")

            results = {
                "value": message,
                "success": result
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()