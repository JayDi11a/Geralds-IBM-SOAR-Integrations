# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_sumologic"
FUNCTION_NAME = "sumo_logic_search"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_sumo_logic_search_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("sumo_logic_search", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("sumo_logic_search_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestSumoLogicSearch:
    """ Tests for the sumo_logic_search function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("sumo_logic_query, sumo_logic_query_param1, sumo_logic_query_param2, sumo_logic_query_param3, sumo_logic_query_param4, sumo_logic_query_param5, sumo_logic_query_range_from, sumo_logic_query_range_to, sumo_logic_timezone, sumo_logic_receipt_time, expected_results", [
        ({"type": "text", "content": "line1\nline2"}, "text", "text", "text", "text", "text", "text", "text", 'IST', 'false', {"value": "xyz"}),
        ({"type": "text", "content": "line1\nline2"}, "text", "text", "text", "text", "text", "text", "text", 'IST', 'false', {"value": "xyz"})
    ])
    def test_success(self, circuits_app, sumo_logic_query, sumo_logic_query_param1, sumo_logic_query_param2, sumo_logic_query_param3, sumo_logic_query_param4, sumo_logic_query_param5, sumo_logic_query_range_from, sumo_logic_query_range_to, sumo_logic_timezone, sumo_logic_receipt_time, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "sumo_logic_query": sumo_logic_query,
            "sumo_logic_query_param1": sumo_logic_query_param1,
            "sumo_logic_query_param2": sumo_logic_query_param2,
            "sumo_logic_query_param3": sumo_logic_query_param3,
            "sumo_logic_query_param4": sumo_logic_query_param4,
            "sumo_logic_query_param5": sumo_logic_query_param5,
            "sumo_logic_query_range_from": sumo_logic_query_range_from,
            "sumo_logic_query_range_to": sumo_logic_query_range_to,
            "sumo_logic_timezone": sumo_logic_timezone,
            "sumo_logic_receipt_time": sumo_logic_receipt_time
        }
        results = call_sumo_logic_search_function(circuits_app, function_params)
        assert(expected_results == results)