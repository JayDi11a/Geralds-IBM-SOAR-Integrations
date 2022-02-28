# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import requests
import json


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ivanti_create_incident"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_ivanti_service_manager", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ivanti_service_manager", {})

    @function("ivanti_create_incident")
    def _ivanti_create_incident_function(self, event, *args, **kwargs):
        """Function: This function allows the analyst to create an Ivanti ticket from within the Resilient incident."""

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
        user_name = get_config_option("api_user")
        password = get_config_option("api_user_credentials")
        host = get_config_option("endpoint")
        role = get_config_option("role")



        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            task_name = kwargs.get("task_name")  # text
            customer = kwargs.get("customer")  # text
            category = kwargs.get("category")  # text
            service = kwargs.get("service")  # text
            status = kwargs.get("status")  # text
            summary = kwargs.get("summary")  # text
            description = self.get_textarea_param(kwargs.get("description"))  # textarea
            urgency = kwargs.get("urgency")  # text
            impact = kwargs.get("impact")  # text
            source = kwargs.get("source")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("task_name: %s", task_name)
            log.info("customer: %s", customer)
            log.info("category: %s", category)
            log.info("service: %s", service)
            log.info("status: %s", status)
            log.info("summary: %s", summary)
            log.info("description: %s", description)
            log.info("urgency: %s", urgency)
            log.info("impact: %s", impact)
            log.info("source: %s", source)

            # Global output variable
            desired_outcome = True
            message = ""

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            # Authenticating to the endpoint
            credentials_headers = {
                'Content-Type': 'application/json',
            }

            credentials_data = '{"tenant":"%s", "username":"%s", "password":"%s", "role":"%s"}' % (
                host, user_name, password, role)

            credentials_response = requests.post('https://{}/api/rest/authentication/login'.format(host),
                                                 headers=credentials_headers,
                                                 data=credentials_data)


            oath_token = (credentials_response.text).replace('"', '')

            # This takes the O-Auth token, passes it to the next header to be passed into the request
            # to obtain the Rec ID
            req_id_headers = {
                'authorization': '{}'.format(oath_token),
            }

            # TODO: Pass customer into request url and provide customer name and parse out just first name
            rec_id_response = requests.get(
                'https://{}/api/odata/businessobject/employees?$search={}'.format(host, customer),
                headers=req_id_headers)

            # Obtain search results for specified user and extracts the corresponding Req Id
            rec_id_response_objects = rec_id_response.text
            rec_id_response_objects_json = json.loads(rec_id_response_objects)

            # For Debugging purposes in identifying the rec id response payload
            # log.info(json.dumps(rec_id_response_objects_json, indent=4, sort_keys=True))


            rec_id_response_object_values = rec_id_response_objects_json['value']

            for rec_id_response_object_value in rec_id_response_object_values:
                rec_ids = rec_id_response_object_value['RecId']
                # log.info(rec_ids)

            # This prints out the rec id for debugging purposes
            log.info(rec_ids)

            # This takes the O-Auth Token and Rec ID and passes it into the payload that ultimately creates the incident in ISM
            incident_headers = {
                'authorization': '{}'.format(oath_token),
            }

            # Example of a working payload that has the correct combination of input fields
            # Turns out that some combination of categories and services DO NOT WORK!
            # incident_data = '{"Category":"Connectivity", ' \
            #                 '"Service":"Desktop Service", ' \
            #                 '"ProfileLink_RecID":"%s", ' \
            #                 '"Status":"%s", ' \
            #                 '"Subject":"%s", ' \
            #                 '"Symptom":"%s", ' \
            #                 '"Urgency":"Low", ' \
            #                 '"Impact":"High", ' \
            #                 '"Source":"AutoTicket"}' % (rec_ids, status, summary, description)
            #
            # log.info(incident_data)

            # Takes the incident data payload and re
            incident_data = '{"Category":"%s", ' \
                            '"Service":"%s", ' \
                            '"ProfileLink_RecID":"%s", ' \
                            '"Status":"%s", ' \
                            '"Subject":"%s", ' \
                            '"Symptom":"%s", ' \
                            '"Urgency":"%s",' \
                            ' "Impact":"%s",' \
                            ' "Source":"%s"}' % (
                            category, service, rec_ids,
                            status, summary, description,
                            urgency, impact, source)

            log.info(incident_data)

            incident_response = requests.post('https://{}/api/odata/businessobject/incidents'.format(host),
                                     headers=incident_headers, data=incident_data)

            # TODO: print link to Ivanti case in note field
            # log.info(incident_response.text)
            incident_string = incident_response.text
            incident_object = json.loads(incident_string)
            # log.info(type(incident_object))

            if 'description' and 'message' in incident_object:
                desired_outcome = False
                message = 'The combination of the Category: "{}" and Service: "{}" are invalid. Please select a valid combination of Category and Service i.e. "Connectivity" and "Desktop Service" for example'.format(category,service)
                log.info(incident_object['message'])
            else:
                message = "Creation of Ivanti Case was successful"
                log.info(incident_object)

            yield StatusMessage("done...")

            results = {
                "value": message,
                "success": desired_outcome
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()