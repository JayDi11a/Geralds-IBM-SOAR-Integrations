import requests
import json


# access_control_policy_config = '{ "type": "AccessPolicy", "name": "%s", "defaultAction": { "action": "%s" }}' % (access_control_policy_name, policy_action)
def create_access_control_policy(access_control_policy_config, host, auth_uuid, post_headers):
    access_control_policy_submissions = requests.post(
        'https://{}/api/fmc_config/v1/domain/{}/policy/accesspolicies'.format(host, auth_uuid),
        headers=post_headers, data=access_control_policy_config, verify=False)
    access_control_policy_submissions_byte = access_control_policy_submissions.content
    access_control_policy_submissions_string = access_control_policy_submissions_byte.decode('utf-8')
    access_control_policy_submissions_json = json.loads(access_control_policy_submissions_string)

    return access_control_policy_submissions_json



# Obtain the list of Access Control Policies
# TODO: Extract Names and IDs and put them in a List of objects
def get_access_control_policies(host, auth_uuid, get_headers, params):
    access_control_results = requests.get('https://{}/api/fmc_config/v1/domain/{}/policy/accesspolicies'.format(host,auth_uuid), headers=get_headers, params=params, verify=False)
    access_control_results_object_byte = access_control_results.content
    access_control_results_object_string = access_control_results_object_byte.decode('utf-8')
    access_control_results_object_json = json.loads(access_control_results_object_string)

    return access_control_results_object_json


# access_rule_config = '{"enabled": %s, "action": "%s", "name": "%s", "type": "AccessRule", "sourceNetworks": { "literals": [ { "type": "Network", "value": "%s/24" } ] }, "destinationNetworks": { "literals": [ { "type": "Network", "value": "%s/24" } ] }}' % (
# enable, rule_action, access_rule_name, source_ip, destination_ip)
def create_network_access_rule(access_rule_config, host, auth_uuid, post_headers, access_control_policy_id):
    access_rule_submissions = requests.post(
        'https://{}/api/fmc_config/v1/domain/{}/policy/accesspolicies/{}/accessrules'.format(host, auth_uuid,
                                                                                             access_control_policy_id),
        headers=post_headers, data=access_rule_config, verify=False)
    access_rule_submissions_byte = access_rule_submissions.content
    access_rule_submissions_string = access_rule_submissions_byte.decode('utf-8')
    access_rule_submissions_json = json.loads(access_rule_submissions_string)

    return access_rule_submissions_json



def get_devices(host, auth_uuid, get_headers, params):
    device_results = requests.get(
    'https://{}/api/fmc_config/v1/domain/{}/devices/devicerecords'.format(host,auth_uuid),
        headers=get_headers, params=params, verify=False)
    device_results_byte = device_results.content
    device_results_string = device_results_byte.decode('utf-8')
    device_results_json = json.loads(device_results_string)
    device_results_list = device_results_json["items"]

    return device_results_list


# device_config = '{"type" : "PolicyAssignment","policy" : {"type" : "AccessPolicy","name" : "%s","id" : "%s"},"targets" : [{"id": "%s","type": "Device","name": "%s"}]}' % (
# access_control_policy_name, access_control_policy_id, device["id"], device["name"])
def assign_policy_to_device(device_config, host, auth_uuid, post_headers):
    device_policy_submissions = requests.post('https://{}/api/fmc_config/v1/domain/{}/assignment/policyassignments'.format(host, auth_uuid),
                                              headers=post_headers, data=device_config, verify=False)
    device_policy_submissions_byte = device_policy_submissions.content
    device_policy_submissions_string = device_policy_submissions_byte.decode('utf-8')
    device_policy_submissions_json = json.loads(device_policy_submissions_string)

    return device_policy_submissions_json



def get_deployable_devices(host, auth_uuid, get_headers, params):
    deployable_device_results = requests.get('https://{}/api/fmc_config/v1/domain/{}/deployment/deployabledevices'.format(host,auth_uuid), headers=get_headers, params=params, verify=False)
    deployable_device_results_byte = deployable_device_results.content
    deployable_device_results_string = deployable_device_results_byte.decode('utf-8')
    deployable_device_results_json = json.loads(deployable_device_results_string)

    return deployable_device_results_json


# deployment_config = '{"type": "DeploymentRequst","version": "%s","forceDeploy": true,"ignoreWarning": true,"deviceList": ["%s"]}' % (
# deployable_device["version"], deployable_device["deviceMembers"][0]["id"])
def create_deployment_submission(deployment_config, host, auth_uuid, post_headers):
    deployment_submission = requests.post('https://{}/api/fmc_config/v1/domain/{}/deployment/deploymentrequests'.format(host, auth_uuid),
        headers=post_headers, data=deployment_config, verify=False)
    deployment_submissions_byte = deployment_submission.content
    deployment_submissions_string = deployment_submissions_byte.decode('utf-8')
    deployment_submission_json = json.loads(deployment_submissions_string)

    return deployment_submission_json



def get_network_objects(host, auth_uuid, get_headers, params):
    network_results = requests.get('https://{}/api/fmc_config/v1/domain/{}/object/networks'.format(host, auth_uuid), headers=get_headers, params=params, verify=False)
    network_results_object_byte = network_results.content
    network_results_object_string = network_results_object_byte.decode('utf-8')
    network_results_object_json = json.loads(network_results_object_string)

    return network_results_object_json



# network_object = '{ "name": "Solenis-Test-1", "value": "1.0.0.0/24", "overridable": false, "description": "Test REST API Object", "type": "Network"}'
def create_network_object():
    network_submissions = requests.post('https://{}/api/fmc_config/v1/domain/{}/object/networks'.format(host, auth_uuid),
    headers=post_headers, data=network_object, verify=False)
    network_submissions_byte = network_submissions.content
    network_submissions_string = network_submissions_byte.decode('utf-8')
    network_submissions_json = json.loads(network_submissions_string)

    return network_submissions_json
