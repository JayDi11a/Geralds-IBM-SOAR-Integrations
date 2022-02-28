# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_ip_address.util.selftest as selftest
from requests import get

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'get_ip_address"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_ip_address", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ip_address", {})

    @function("get_ip_address")
    def _get_ip_address_function(self, event, *args, **kwargs):
        """Function: This is a simple function that returns the IPv4 Address of ones machine."""
        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            ip = get('https://api.ipify.org').text
            yield StatusMessage("done...")

            results = {
                "value": ip
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
