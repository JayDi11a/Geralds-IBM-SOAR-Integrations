# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_palo_alto_panorama"
FUNCTION_NAME = "palo_alto_create_security_policy_rule"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_palo_alto_create_security_policy_rule_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("palo_alto_create_security_policy_rule", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("palo_alto_create_security_policy_rule_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestPaloAltoCreateSecurityPolicyRule:
    """ Tests for the palo_alto_create_security_policy_rule function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("incident_id, policy_rule_name, location, policy_to, policy_from, source_user, application, service, hipprofiles, action, category, source, destination, expected_results", [
        (123, "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", {"value": "xyz"}),
        (123, "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", {"value": "xyz"})
    ])
    def test_success(self, circuits_app, incident_id, policy_rule_name, location, policy_to, policy_from, source_user, application, service, hipprofiles, action, category, source, destination, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "incident_id": incident_id,
            "policy_rule_name": policy_rule_name,
            "location": location,
            "policy_to": policy_to,
            "policy_from": policy_from,
            "source_user": source_user,
            "application": application,
            "service": service,
            "hipprofiles": hipprofiles,
            "action": action,
            "category": category,
            "source": source,
            "destination": destination
        }
        results = call_palo_alto_create_security_policy_rule_function(circuits_app, function_params)
        assert(expected_results == results)