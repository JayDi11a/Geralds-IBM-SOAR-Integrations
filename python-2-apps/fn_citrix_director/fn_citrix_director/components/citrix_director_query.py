# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import requests
import json


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'citrix_director_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_citrix_director", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_citrix_director", {})

    @function("citrix_director_query")
    def _citrix_director_query_function(self, event, *args, **kwargs):
        """Function: This function takes the NT ID (login id or hostname) and returns the assigned workstation, the OS type, IP Address (and any other information contained in the Citrix Director Data Base)"""
        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_value = kwargs.get("artifact_value")  # text
            artifact_type = kwargs.get("artifact_type")  # text
            hostname = kwargs.get("hostname")  # text
            login_id = kwargs.get("login_id")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("artifact_value: %s", artifact_value)
            log.info("artifact_type: %s", artifact_type)
            log.info("hostname: %s", hostname)
            log.info("login_id: %s", login_id)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            query_machines = requests.get('http://director.nb.com/Citrix/Monitor/Odata/v1/Data/Machines')

            print(query_machines)

            yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()