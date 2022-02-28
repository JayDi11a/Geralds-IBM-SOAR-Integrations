# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import requests
import json

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'manageengine_servicedesk_plus_close_request"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_manageengine_servicedesk_plus", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_manageengine_servicedesk_plus", {})

    @function("manageengine_servicedesk_plus_close_request")
    def _manageengine_servicedesk_plus_close_request_function(self, event, *args, **kwargs):
        """Function: This function interacts with the ManageEngine ServiceDesk Plus endpoint for the sole purpose of closing a specific request by the provided request id. It gives the option of adding comments for the closure as well."""

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
        host = get_config_option("base_url")
        technican_key = get_config_option("api_key")

        headers = {
            'TECHNICIAN_KEY': technican_key,
        }

        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            request_id = kwargs.get("request_id")  # text
            requester_ack_resolution = self.get_select_param(kwargs.get("requester_ack_resolution"))  # select, values: "true"
            requester_ack_comments = kwargs.get("requester_ack_comments")  # text
            closure_comments = kwargs.get("closure_comments")  # text
            closure_code = self.get_select_param(kwargs.get("closure_code"))  # select, values: "success"

            log = logging.getLogger(__name__)
            log.info("request_id: %s", request_id)
            log.info("requester_ack_resolution: %s", requester_ack_resolution)
            log.info("requester_ack_comments: %s", requester_ack_comments)
            log.info("closure_comments: %s", closure_comments)
            log.info("closure_code: %s", closure_code)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            get_request_config = {
                'input_data': ' { "list_info": { "row_count": 20, "start_index": 1, "sort_field": "subject", "sort_order": "asc", "get_total_count": true, "search_fields": { "subject": "New hire", "priority.name": "high" }, "filter_by": { "name": "Open_System" } } }'
            }

            response = requests.post('http://curl', headers=headers, data=get_request_config)

            get_response_submission = response.content
            print(type(get_response_submission))

            # close_request_config = {
            #     'input_data': ' { "request": { "closure_info": { "requester_ack_resolution": {}, "requester_ack_comments": "{}", "closure_comments": "{}", "closure_code": { "name": "{}" } } } }'.format(requester_ack_resolution, requester_ack_comments, closure_comments, closure_code)
            # }
            #
            # response = requests.put('http://{}/api/v3/requests/{}/close'.format(host, request_id), headers=headers,
            #                          data=close_request_config)
            # close_request_submission = response.content
            # print(type(close_request_submission))

            yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()