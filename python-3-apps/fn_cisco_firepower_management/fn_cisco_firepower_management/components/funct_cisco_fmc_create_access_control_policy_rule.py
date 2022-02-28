# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import requests
from requests.auth import HTTPBasicAuth
import urllib3
import json
from fn_cisco_firepower_management.util.fmc_actions import *

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'cisco_fmc_create_access_control_policy_rule"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_firepower_management", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_firepower_management", {})

    @function("cisco_fmc_create_access_control_policy_rule")
    def _cisco_fmc_create_access_control_policy_rule_function(self, event, *args, **kwargs):
        """Function: This function allows you to specify a given Access Control Policy and creates an Access Rule within it. Note that it assumes the Access Control Policy has already been created and it only creates Access Rules"""

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
        host = get_config_option("host")
        username = get_config_option("username")
        password = get_config_option("password")
        port = get_config_option("port")

        # keep ssl warning out of sight (not recommended for production)
        # also request(,,verify=False)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        auth_url = "https://" + host + "/api/fmc_platform/v1/auth/generatetoken"

        resp = requests.post(auth_url, auth=HTTPBasicAuth(username, password), verify=False)

        auth_headers = resp.headers
        auth_token = auth_headers.get('X-auth-access-token', default=None)
        auth_refresh = auth_headers.get('X-auth-refresh-token', default=None)
        auth_uuid = auth_headers.get('domain_uuid', default=None)
        resp.close()

        params = (
            ('expanded', 'true'),
        )

        get_headers = {'accept': 'application/json', 'X-auth-access-token': auth_token }

        post_headers = {'accept': 'application/json', 'Content-Type': 'application/json','X-auth-access-token': auth_token }

        # Error handling for generating uuid and tokens
        if auth_token == None:
            print("auth_token not found. Exiting...")
            sys.exit()
        if auth_refresh == None:
            print("refresh_token not found. Exiting...")
            sys.exit()
        if auth_uuid == None:
            print("domain_uuid not found. Exiting...")
            sys.exit()

        print("domain_uuid: " + auth_uuid)
        print("X-auth-access-token: " + auth_token)
        print("X-auth-refresh-token: " + auth_refresh)

        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            access_control_policy_name = kwargs.get("access_control_policy_name")  # text
            source_ip = kwargs.get("source_ip")  # text
            destination_ip = kwargs.get("destination_ip")  # text
            policy_action = self.get_select_param(kwargs.get("policy_action")) # select, values: "BLOCK", "ACCESS", "MONITOR", "TRUST"
            access_rule_name = kwargs.get("access_rule_name")  # text
            rule_action = self.get_select_param(kwargs.get("rule_action")) # select, values: "BLOCK", "ACCESS", "MONITOR", "TRUST"
            enable = kwargs.get("enable")  # text

            log = logging.getLogger(__name__)
            log.info("access_control_policy_name: %s", access_control_policy_name)
            log.info("source_ip: %s", source_ip)
            log.info("destination_ip: %s", destination_ip)
            log.info("policy_action: %s", policy_action)
            log.info("access_rule_name: %s", access_rule_name)
            log.info("rule_action: %s", rule_action)
            log.info("enable: %s", enable)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            # Creates the Access Control Policy
            access_control_policy_config = '{ "type": "AccessPolicy", "name": "%s", "defaultAction": { "action": "%s" }}' % (access_control_policy_name, policy_action)

            access_control_policy_results = create_access_control_policy(access_control_policy_config, host, auth_uuid, post_headers)
            if access_control_policy_results.get('error'):
            # Handles error and reports message
            # TODO: If Access Policy already exists get the Policy by name and it corresponding ID.
                message = access_control_policy_results["error"]["messages"][0]["description"]
                yield StatusMessage(message)
                #
                # access_control_policy_objects = get_access_control_policies(host, auth_uuid, get_headers, params)
                # print(json.dumps(access_control_policy_objects, indent=4, sort_keys=True))
            else:
                # Extracts and obtains the Access Control Policy ID to be passed to the Access Rule POST
                access_control_policy_id = access_control_policy_results["id"]

                # Creates a Rule Object For Access Policy
                access_rule_config = '{"enabled": %s, "action": "%s", "name": "%s", "type": "AccessRule", "sourceNetworks": { "literals": [ { "type": "Network", "value": "%s/24" } ] }, "destinationNetworks": { "literals": [ { "type": "Network", "value": "%s/24" } ] }}' % (enable, rule_action, access_rule_name, source_ip, destination_ip)

                # Creates Access Rule
                access_rule_results = create_network_access_rule(access_rule_config, host, auth_uuid, post_headers, access_control_policy_id)
                print(json.dumps(access_rule_results, indent=4, sort_keys=True))
                message = 'Access Rule: "{}" was successfully created for Access Control Policy: "{}".'.format(access_rule_name, access_control_policy_name)
                yield StatusMessage(message)


                # Get the list of Devices
                devices = get_devices(host, auth_uuid, get_headers, params)
                for device in devices:
                    # Creates a Device Configuration Object
                    device_config = '{"type" : "PolicyAssignment","policy" : {"type" : "AccessPolicy","name" : "%s","id" : "%s"},"targets" : [{"id": "%s","type": "Device","name": "%s"}]}' % (access_control_policy_name, access_control_policy_id, device["id"], device["name"])

                    # Assign Access Control Policy to Device(s)
                    policy_to_device_results = assign_policy_to_device(device_config, host, auth_uuid, post_headers)
                    print(policy_to_device_results)


                # Get Deployable Device Information
                deployable_device_results = get_deployable_devices(host, auth_uuid, get_headers, params)
                if deployable_device_results.get('error'):
                    # Handle error and report message
                    message = 'The Access Policy: "{}" and Access Rule: "{}" was created, but '.format(access_control_policy_name, access_rule_name) + deployable_device_results["error"]["messages"][0]["description"] + ' to create a Deployment'
                    yield StatusMessage('The Access Policy: "{}" and Access Rule: "{}" was created, but '.format(access_control_policy_name, access_rule_name) + message + ' to create a Deployment')
                else:
                    deployable_devices_list = deployable_device_results["items"]
                    for deployable_device in deployable_devices_list:
                        # Creates a Deployment Configuration Object
                        deployment_config = '{"type": "DeploymentRequst","version": "%s","forceDeploy": true,"ignoreWarning": true,"deviceList": ["%s"]}' % (deployable_device["version"],deployable_device["deviceMembers"][0]["id"])

                        # Intialize Deployment Request
                        deployment_results = create_deployment_submission(deployment_config, host, auth_uuid, post_headers)
                        print(deployment_results)

            yield StatusMessage("done...")

            results = {
                "value": message
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()