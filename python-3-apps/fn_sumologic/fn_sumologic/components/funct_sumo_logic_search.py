# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_sumologic.util import function_utils
from time import sleep
import fn_sumologic.util.selftest as selftest
import requests
import json

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'sumo_logic_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_sumologic", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_sumologic", {})

    @function("sumo_logic_search")
    def _sumo_logic_search_function(self, event, *args, **kwargs):
        """Function: Searches Sumo Logic for search job results for a given query."""

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
        url_offset = get_config_option("offset")
        url_limit = get_config_option("limit")

        # Global variable for results return
        search_jobs_results = ""
        search_results_found = True

        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            sumo_logic_query = self.get_textarea_param(kwargs.get("sumo_logic_query"))  # textarea
            sumo_logic_query_param1 = kwargs.get("sumo_logic_query_param1")  # text
            sumo_logic_query_param2 = kwargs.get("sumo_logic_query_param2")  # text
            sumo_logic_query_param3 = kwargs.get("sumo_logic_query_param3")  # text
            sumo_logic_query_param4 = kwargs.get("sumo_logic_query_param4")  # text
            sumo_logic_query_param5 = kwargs.get("sumo_logic_query_param5")  # text
            sumo_logic_query_range_from = kwargs.get("sumo_logic_query_range_from")  # text
            sumo_logic_query_range_to = kwargs.get("sumo_logic_query_range_to")  # text
            sumo_logic_timezone = self.get_select_param(kwargs.get("sumo_logic_timezone"))  # select, values: "IST"
            sumo_logic_receipt_time = self.get_select_param(kwargs.get("sumo_logic_receipt_time"))  # select, values: "true", "false"

            log = logging.getLogger(__name__)
            log.info("sumo_logic_query: %s", sumo_logic_query)
            log.info("sumo_logic_query_param1: %s", sumo_logic_query_param1)
            log.info("sumo_logic_query_param2: %s", sumo_logic_query_param2)
            log.info("sumo_logic_query_param3: %s", sumo_logic_query_param3)
            log.info("sumo_logic_query_param4: %s", sumo_logic_query_param4)
            log.info("sumo_logic_query_param5: %s", sumo_logic_query_param5)
            log.info("sumo_logic_query_range_from: %s", sumo_logic_query_range_from)
            log.info("sumo_logic_query_range_to: %s", sumo_logic_query_range_to)
            log.info("sumo_logic_timezone: %s", sumo_logic_timezone)
            log.info("sumo_logic_receipt_time: %s", sumo_logic_receipt_time)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            headers = {
                'Content-type': 'application/json',
                'Accept': 'application/json',
            }

            query_string = function_utils.make_query_string(sumo_logic_query,
                                                            [sumo_logic_query_param1,
                                                             sumo_logic_query_param2,
                                                             sumo_logic_query_param3,
                                                             sumo_logic_query_param4,
                                                             sumo_logic_query_param5])

            data = '{"query":"%s", ' \
                   '"from":"%s", ' \
                   '"to":"%s", ' \
                   '"timeZone":"%s", ' \
                   '"byReceiptTime":"%s"}' % (
                   query_string, sumo_logic_query_range_from, sumo_logic_query_range_to, sumo_logic_timezone,
                   sumo_logic_receipt_time)

            # Passes the query paramaters to search job endpoint and returns search job ID
            search_job_response = requests.post('https://{}/api/v1/search/jobs'.format(host), headers=headers,
                                                data=data,
                                                auth=(user_name,
                                                      password))

            search_job_response_object = search_job_response.content
            search_job_response_objects_json = json.loads(search_job_response_object)

            # log.info(json.dumps(search_job_response_objects_json, indent=4, sort_keys=True))

            search_job_id = search_job_response_objects_json['id']

            # Polling of job status endpoint that pulls back results after its status has changed to completing gathering
            # results
            while True:
                # Passes in the job id and gets the status back
                search_job_status_response = requests.get(
                    'https://{}/api/v1/search/jobs/{}'.format(host, search_job_id),
                    headers=headers, auth=(
                        user_name, password))

                search_job_status_object = search_job_status_response.content
                search_job_status_object_json = json.loads(search_job_status_object)

                # log.info(json.dumps(search_job_status_object_json, indent=4, sort_keys=True))

                # This handles if the search id is even valid
                # Gets out of the loop and logs back the nature of failure
                if 'message' in search_job_status_object_json:
                    # log.info(search_job_status_object_json['message'])
                    search_results_found = False
                    break

                # Otherwise assumes that the search id has a state
                if 'state' in search_job_status_object_json:
                    search_job_status = search_job_status_object_json['state']
                    # log.info(search_job_status)

                    # Gets out of the while loop when endpoint status has changed to what we are looking for
                    # and polls otherwise for other states.
                    if search_job_status == 'DONE GATHERING RESULTS':
                        break
                    else:
                        time.sleep(10)

            # Handles passing in the search id and retrieving event results or
            # Reporting that something went wrong after looking up the search id
            # TODO: convert if/else to try catch for better error handling
            if search_results_found is True:
                params = (
                    ('offset', url_offset),
                    ('limit', url_limit),
                )

                search_job_result_response = requests.get(
                    'https://{}/api/v1/search/jobs/{}/messages'.format(host, search_job_id), headers=headers,
                    params=params, auth=(user_name, password))

                search_job_result_object = search_job_result_response.content
                search_job_result_object_json = json.loads(search_job_result_object)

                # log.info(json.dumps(search_job_result_object_json, indent=4, sort_keys=True))

                # Pull out list object from 'messages' key and return it
                search_job_results = search_job_result_object_json['messages']
                # log.info(search_job_results)
                # log.info(type(search_job_results))

                # test_result = {"events": [row['map'] for row in search_job_results]}
                # log.info(test_result)
                # Extracts the map key from each dictionary object and creates a list of the final
                # result objects
                sumo_logic_result = [row['map'] for row in search_job_results]

            else:
                sumo_logic_result = search_job_status_object_json['message']
                log.info(sumo_logic_result)

            yield StatusMessage("done...")


            results = {
                "value": sumo_logic_result,
                "success": search_results_found
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()