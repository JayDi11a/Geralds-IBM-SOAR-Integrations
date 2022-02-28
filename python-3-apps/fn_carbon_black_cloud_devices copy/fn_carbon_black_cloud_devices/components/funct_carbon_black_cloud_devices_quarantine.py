# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import requests
import json

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

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("carbon_black_device_query_string: %s", carbon_black_device_query_string)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            headers = {
                'X-Auth-Token': '{}/{}'.format(api_key,api_id),
                'Content-Type': 'application/json',
                'User-Agent': 'IBM Resilient Integration',
            }

            data = '{"query":"%s", ' \
                   '"rows": %s, ' \
                   '"start": 0}' % (carbon_black_device_query_string, limit)


            device_query_results = requests.post('https://{}/appservices/v6/orgs/{}/devices/_search'.format(host,org_key),
                                     headers=headers, data=data)

            #print(type(device_query_results))

            device_query_results_objects = device_query_results.content
            device_query_results_objects_json = json.loads(device_query_results_objects)

            #log.info(json.dumps(device_query_results_objects_json, indent=4, sort_keys=True))

            #log.info(json.dumps(device_query_results_objects_json['results']))

            #log.info(type(device_query_results_objects_json['results']))

            # Assigns variable to list of device result objects
            device_query_results_objects_list = device_query_results_objects_json['results']

            for device_query_result_object_json in device_query_results_objects_list:
                log.info(type(device_query_result_object_json))
                print(device_query_result_object_json)
                print(device_query_result_object_json['id'])
                device_ids.append(device_query_result_object_json['id'])

            print(device_ids)

            yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()