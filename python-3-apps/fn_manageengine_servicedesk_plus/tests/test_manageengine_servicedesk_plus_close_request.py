# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_manageengine_servicedesk_plus"
FUNCTION_NAME = "manageengine_servicedesk_plus_close_request"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_manageengine_servicedesk_plus_close_request_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("manageengine_servicedesk_plus_close_request", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("manageengine_servicedesk_plus_close_request_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestManageengineServicedeskPlusCloseRequest:
    """ Tests for the manageengine_servicedesk_plus_close_request function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("request_id, requester_ack_resolution, requester_ack_comments, closure_comments, closure_code, expected_results", [
        ("text", 'true', "text", "text", 'success', {"value": "xyz"}),
        ("text", 'true', "text", "text", 'success', {"value": "xyz"})
    ])
    def test_success(self, circuits_app, request_id, requester_ack_resolution, requester_ack_comments, closure_comments, closure_code, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "request_id": request_id,
            "requester_ack_resolution": requester_ack_resolution,
            "requester_ack_comments": requester_ack_comments,
            "closure_comments": closure_comments,
            "closure_code": closure_code
        }
        results = call_manageengine_servicedesk_plus_close_request_function(circuits_app, function_params)
        assert(expected_results == results)