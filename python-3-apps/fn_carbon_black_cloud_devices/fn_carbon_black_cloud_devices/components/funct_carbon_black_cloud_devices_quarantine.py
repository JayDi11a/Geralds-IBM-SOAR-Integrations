# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import requests
import json
import time

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'carbon_black_cloud_devices_quarantine"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_carbon_black_cloud_devices", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_carbon_black_cloud_devices", {})

    @function("carbon_black_cloud_devices_quarantine")
    def _carbon_black_cloud_devices_quarantine_function(self, event, *args, **kwargs):
        """Function: This function is part of the Carbon Black Platform API functionality focusing solely on the Devices API subset of endpoints that solely queries a device and implements a quarantine."""

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

        # Authentication specific settings
        host = get_config_option("hostname")
        api_id = get_config_option("api_id")
        api_key = get_config_option("api_secret_key")
        org_key = get_config_option("org_key")
        limit = get_config_option("result_limit")

        # Declaring an empty ID List
        device_ids = []


        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            carbon_black_device_query_string = kwargs.get("carbon_black_device_query_string")  # text
            device_action_type = self.get_select_param(kwargs.get("device_action_type"))  # select, values: "BACKGROUND_SCAN", "BYPASS", "UNINSTALL_SENSOR", "DELETE_SENSOR", "QUARANTINE", "UPDATE_POLICY", "UPDATE_SENSOR_VERSION"
            toggle = self.get_select_param(kwargs.get("toggle"))  # select, values: "ON", "OFF"

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("carbon_black_device_query_string: %s", carbon_black_device_query_string)
            log.info("device_action_type: %s", device_action_type)
            log.info("toggle: %s", toggle)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            # Sets the authentication parameters as part of the header
            headers = {
                'X-Auth-Token': '{}/{}'.format(api_key, api_id),
                'Content-Type': 'application/json',
                'User-Agent': 'IBM Resilient Integration',
            }

            # The Device payload used to query a device and return the corresponding device id.
            # It takes the query string, you can specify the amount of return results.
            device_data = '{"query":"%s", ' \
                   '"rows": %s, ' \
                   '"start": 0}' % (carbon_black_device_query_string, limit)

            # The Device Query Endpoint that performs the search based on wild card device tags
            device_query_results = requests.post(
                'https://{}/appservices/v6/orgs/{}/devices/_search'.format(host, org_key),
                headers=headers, data=device_data)

            # Extracts the contents out of the return object and converts the return to JSON
            device_query_results_objects = device_query_results.content
            device_query_results_objects_json = json.loads(device_query_results_objects)


            # Assigns variable to list of device result objects
            # TODO: Handle no results
            device_query_results_objects_list = device_query_results_objects_json['results']

            for device_query_result_object_json in device_query_results_objects_list:
                device_ids.append(device_query_result_object_json['id'])

            # The Device payload used to facilitate actions being passed to the Device Actions Endpoint
            # It takes  the action type, the device id, and the ability to toggle the action on or off.
            action_data = '{"action_type":"%s", ' \
                          '"device_id": %s, ' \
                          '"options": {"toggle": "%s"}}' % (device_action_type, device_ids, toggle)

            # The Device Actions Endpoint that performs the configuring against specified devices
            device_actions_results = requests.post(
                'https://{}/appservices/v6/orgs/{}/device_actions'.format(host, org_key), headers=headers,
                data=action_data)

            # Set a pause to let the API gather its latest state since there is a slight lag between the POST that performs the query
            # and the GET on the result object to finish rendering in the UI
            time.sleep(45)

            # Gets specific device id.
            device_id = device_ids[0]
            device_status_results = requests.get('https://{}/appservices/v6/orgs/{}/devices/{}'.format(host,org_key,device_id), headers=headers)
            device_status_results_object = device_status_results.content
            device_status_results_object_json = json.loads(device_status_results_object)
            device_status = device_status_results_object_json['quarantined']
            print(type(device_status_results_object_json['quarantined']))

            if device_status is True:
                quarantine_state = 'The host: {} Quarantine State has been turned ON'.format(carbon_black_device_query_string)
            else:
                quarantine_state = 'The host: {} Quarantine State has been turned OFF'.format(carbon_black_device_query_string)

            yield StatusMessage("done...")

            results = {
                "value": quarantine_state
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()