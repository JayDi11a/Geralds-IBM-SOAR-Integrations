# -*- coding: utf-8 -*-
# Copyright IBM Corp. - Confidential Information
"""Function implementation"""

import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import requests
import logging

log = logging.getLogger(__name__)


# This function takes in a SHA-256 Hash and returns the results
# or returns a message on its status
def sha256_hash_function(headers, user, key, artifact_value):

    sha256_behavior_output = None

    # Validate IF IOC Exists in CrowdStrike
    sha256_params = (
        ('ids', 'sha256:{}'.format(artifact_value)),
    )

    sha256_query = requests.get('https://falconapi.crowdstrike.com/indicators/entities/iocs/v1',
                                headers=headers, params=sha256_params, auth=(user, key))
    sha256_query_object = sha256_query.json()
    sha256_query_string = json.dumps(sha256_query_object['resources'])

    # This POSTs the SHA-256 Hash to CrowdStrike because it didn't exist prior to being added into Resilient as an artifact
    if sha256_query_string == "[]":
        sha_data = '[{{"type":"sha256","value":"{}","description":"description","share level":"red","source":"source","policy":"detect"}}]'.format(
            artifact_value)

        sha256_response = requests.post('https://falconapi.crowdstrike.com/indicators/entities/iocs/v1',
                                        headers=headers, data=sha_data,
                                        auth=(user, key))
        sha256_response.raise_for_status() # - exception handling for Client Error

        log.debug(sha256_response.json())
        log.debug("This Malware SHA-256 Hash wasn't in CrowdStrike so I went ahead and uploaded it for you...")

        # Redundant but necessary step to ensure that the IOC was uploaded in the event that it wasn't in CrowdStrike to begin with.
        sha256_request = requests.get('https://falconapi.crowdstrike.com/indicators/entities/iocs/v1',
                                      headers=headers, params=sha256_params, auth=(user, key))
        sha256_request.raise_for_status() # - exception handling for Client Error
        sha256_request_object = sha256_request.json()
        sha256_request_string = json.dumps(sha256_request_object['resources'][0]['value'], sort_keys=True, indent=4)

        log.debug(sha256_request_string)

        # Gets the device the IOC Ran on and returns the device id
        device_params = (
            ('type', 'sha256'),
            ('value', artifact_value),
        )

        device_id_query = requests.get('https://falconapi.crowdstrike.com/indicators/queries/devices/v1',
                                       headers=headers, params=device_params, auth=(user, key))
        device_id_query.raise_for_status() # - exception handling for Client Error

        device_id_object = device_id_query.json()
        device_id_string = json.dumps(device_id_object['resources'])

        log.debug(device_id_string)

        if device_id_string == "[]":
            log.debug("The sensor for this device is not picking up {}".format(artifact_value))

        else:
            detection_params = (
                ('filter', ('behaviors.sha256:\'{}\'').format(artifact_value)),
            )

            # This gets the detection ids to be passed
            detection_id_query = requests.get('https://falconapi.crowdstrike.com/detects/queries/detects/v1',
                                              headers=headers,
                                              params=detection_params, auth=(user, key))

            detection_id_query.raise_for_status() # - exception handling for Client Error

            detection_id_object = detection_id_query.json()
            detection_id_string = json.dumps(detection_id_object['resources'])

            data = '{"ids":' + detection_id_string + "}"

            # This returns the results from the detection ID
            detection_response = requests.post('https://falconapi.crowdstrike.com/detects/entities/summaries/GET/v1',
                                               headers=headers, data=data,
                                               auth=(user, key))
            detection_response.raise_for_status() # - exception handling for Client Error

            detection_response_object = detection_response.json()
            detection_response_string = json.dumps(detection_response_object, sort_keys=True, indent=4)
            sha256_behavior_output = detection_response_string
    else:

        detection_params = (
            ('filter', ('behaviors.sha256:\'{}\'').format(artifact_value)),
        )

        # This gets the detection ids to be passed
        detection_id_query = requests.get('https://falconapi.crowdstrike.com/detects/queries/detects/v1',
                                          headers=headers,
                                          params=detection_params, auth=(user, key))
        detection_id_query.raise_for_status() # - exception handling for Client Error
        detection_id_object = detection_id_query.json()
        detection_id_string = json.dumps(detection_id_object['resources'])

        data = '{"ids":' + detection_id_string + "}"

        # This returns the results from the detection ID
        detection_response = requests.post(
            'https://falconapi.crowdstrike.com/detects/entities/summaries/GET/v1',
            headers=headers, data=data,
            auth=(user, key))
        detection_response.raise_for_status() # - exception handling for Client Error
        detection_response_object = detection_response.json()
        detection_response_string = json.dumps(detection_response_object, sort_keys=True, indent=4)

        if json.dumps(detection_response_object['resources']) == "[]":
            log.debug("There are no detection IDs assoicated with the artifact you just ran but the artifact was in CrowdStrike which is weird...")
        else:
            log.debug(detection_response_string)
            sha256_behavior_output = detection_response_string


    return sha256_behavior_output







# This function takes in an MD5 Hash and returns the results or a message
# on the status.
def md5_hash_function(headers, user, key, artifact_value):

    md5_behavior_output = None

    # Validate IF IOC Exists in CrowdStrike
    md5_params = (
        ('ids', ('md5:{}').format(artifact_value)),
    )

    md5_query = requests.get('https://falconapi.crowdstrike.com/indicators/entities/iocs/v1',
                             headers=headers, params=md5_params, auth=(user, key))
    md5_query.raise_for_status() # - exception handling for Client Error
    md5_query_object = md5_query.json()
    md5_query_string = json.dumps(md5_query_object['resources'])

    # This POSTs the MD5 Hash to CrowdStrike because it didn't exist prior to being added into Resilient as an artifact
    if md5_query_string == "[]":
        md5_data = '[{{"type":"md5","value":"{}","description":"description","share level":"red","source":"source","policy":"detect"}}]'.format(
            artifact_value)

        md5_response = requests.post('https://falconapi.crowdstrike.com/indicators/entities/iocs/v1',
                                     headers=headers, data=md5_data,
                                     auth=(user, key))
        md5_response.raise_for_status() # - exception handling for Client Error

        log.debug(md5_response.json())
        log.debug("This Malware MD5 Hash wasn't in CrowdStrike so I went ahead and uploaded it for you...")

        # Redundant but necessary step to ensure that the IOC was uploaded in the event that it wasn't in CrowdStrike to begin with.
        md5_request = requests.get('https://falconapi.crowdstrike.com/indicators/entities/iocs/v1',
                                   headers=headers, params=md5_params, auth=(user, key))
        md5_request.raise_for_status() # - exception handling for Client Error
        md5_request_object = md5_request.json()
        md5_request_string = json.dumps(md5_request_object['resources'][0]['value'], sort_keys=True,
                                        indent=4)
        log.debug(md5_request_string)

        # Gets the device the IOC Ran on and returns the device id
        device_params = (
            ('type', 'md5'),
            ('value', artifact_value),
        )

        device_id_query = requests.get('https://falconapi.crowdstrike.com/indicators/queries/devices/v1',
                                       headers=headers, params=device_params, auth=(user, key))
        device_id_query.raise_for_status() # - exception handling for Client Error
        device_id_object = device_id_query.json()
        device_id_string = json.dumps(device_id_object['resources'])


        log.debug(device_id_string)

        if device_id_string == "[]":
            log.debug("The sensor for this device is not picking up {}".format(artifact_value))

        else:
            detection_params = (
                ('filter', ('behaviors.md5:\'{}\'').format(artifact_value)),
            )

            # This gets the detection ids to be passed
            detection_id_query = requests.get(
                'https://falconapi.crowdstrike.com/detects/queries/detects/v1',
                headers=headers,
                params=detection_params, auth=(user, key))
            detection_id_query.raise_for_status() # - exception handling for Client Error

            detection_id_object = detection_id_query.json()
            detection_id_string = json.dumps(detection_id_object['resources'])

            data = '{"ids":' + detection_id_string + "}"

            # This returns the results from the detection ID
            detection_response = requests.post(
                'https://falconapi.crowdstrike.com/detects/entities/summaries/GET/v1',
                headers=headers, data=data,
                auth=(user, key))
            detection_response.raise_for_status()
            detection_response_object = detection_response.json() # - exception handling for Client Error
            detection_response_string = json.dumps(detection_response_object, sort_keys=True, indent=4)
            md5_behavior_output = detection_response_string
    else:
        detection_params = (
            ('filter', ('behaviors.md5:\'{}\'').format(artifact_value)),
        )

        # This gets the detection ids to be passed
        detection_id_query = requests.get('https://falconapi.crowdstrike.com/detects/queries/detects/v1',
                                          headers=headers,
                                          params=detection_params, auth=(user, key))
        detection_id_query.raise_for_status() # - exception handling for Client Error

        detection_id_object = detection_id_query.json()
        detection_id_string = json.dumps(detection_id_object['resources'])

        data = '{"ids":' + detection_id_string + "}"

        # This returns the results from the detection ID
        detection_response = requests.post(
            'https://falconapi.crowdstrike.com/detects/entities/summaries/GET/v1',
            headers=headers, data=data,
            auth=(user, key))
        detection_response.raise_for_status() # - exception handling for Client Error

        detection_response_object = detection_response.json()
        detection_response_string = json.dumps(detection_response_object, sort_keys=True, indent=4)

        if json.dumps(detection_response_object['resources']) == "[]":
            log.debug("There are no detection IDs assoicated with the artifact you just ran but the artifact was in CrowdStrike which is weird...")

        else:
            log.debug(detection_response_string)
            md5_behavior_output = detection_response_string



    return md5_behavior_output






# This function handles domain function being passed in and returns
# its results or a message otherwise
def domains_function(headers, user, key, artifact_value):

    domain_behavior_output = None

    ioc_domain_params = (
        ('type', 'domain'),
        ('value', artifact_value),
    )

    # Query returns the devices associated with the domain IOC
    get_devices_from_domain = requests.get(
        'https://falconapi.crowdstrike.com/indicators/queries/devices/v1', headers=headers,
        params=ioc_domain_params, auth=(user, key))
    get_devices_from_domain.raise_for_status() # - exception handling for Client Error

    # converts response object to json, assigns value to a given key and converts that value to a string ultimately printing the string value
    # This takes domain and returns a device ID
    domain_devices = get_devices_from_domain.json()
    domain_devices_string = json.dumps(domain_devices['resources'])

    # TODO: error handle if there are no results being returned...
    # if domain_devices_string != "[]":
    domain_id = domain_devices_string.translate(None, "[]")
    domain_id = domain_id.replace('"', '')

    domain_id_params = (
        ('filter', ('device.device_id:\'{}\'').format(domain_id)),
    )

    get_detection_id = requests.get('https://falconapi.crowdstrike.com/detects/queries/detects/v1', headers=headers,
                                    params=domain_id_params, auth=(user, key))
    get_detection_id.raise_for_status() # - exception handling for Client Error

    device_id_object = get_detection_id.json()
    device_id_string = json.dumps(device_id_object['resources'])

    if device_id_string != "[]":
        data = '{"ids":' + device_id_string + "}"

        detection_response = requests.post(
            'https://falconapi.crowdstrike.com/detects/entities/summaries/GET/v1',
            headers=headers, data=data,
            auth=(user, key))
        detection_response.raise_for_status() # - exception handling for Client Error

        detection_response_object = detection_response.json()
        detection_response_string = json.dumps(detection_response_object, sort_keys=True, indent=4)
        domain_behavior_output = detection_response_string
    else:
        log.debug("There were no resources returned from your query")


    return domain_behavior_output






















