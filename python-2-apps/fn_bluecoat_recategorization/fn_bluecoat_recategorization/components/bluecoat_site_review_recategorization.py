# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_bluecoat_recategorization.util.selftest as selftest
import requests
import json
import xmltodict



class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'bluecoat_site_review_recategorization"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_bluecoat_recategorization", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_bluecoat_recategorization", {})

    @function("bluecoat_site_review_recategorization")
    def _bluecoat_site_review_recategorization_function(self, event, *args, **kwargs):
        """Function: This function takes in a url and a categorization id to be submitted for review."""

        # - method that retreives specific attributes needed for the function to run like credentials, etc...
        def get_config_option(option_name, optional=False):
            """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
            option = self.options.get(option_name)

            if option is None and optional is False:
                err = "'{0}' is mandatory and is not set in ~/.resilient/app.config file. You must set this value to run this function".format(
                    option_name)
                raise ValueError(err)
            else:
                return option

        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_value = kwargs.get("artifact_value")  # text
            categorization_name = kwargs.get("categorization_name")  # text
            categorization_id = kwargs.get("categorization_id")  # number
            submission_comments = kwargs.get("submission_comments")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("artifact_value: %s", artifact_value)
            log.info("categorization_name: %s", categorization_name)
            log.info("categorization_id: %s", categorization_id)
            log.info("submission_comments: %s", submission_comments)

            # retreive the Passive Total credentials from the config file to be set
            uid = get_config_option("user_id")

            # List of security categories to check against
            security_categories = ["Phishing", "Malicious Sources/Malnets", "Malicious Outbound Data/Botnets", "Proxy Avoidance", "Suspicious", "Spam", "Potentially Unwanted Software"]

            # The header that corresponds to object return type
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
            }

            # This data object is what needs to be passed to the request submission
            data = (
                ('userID', ('{}').format(uid)),
                ('url', ('{}').format(artifact_value)),
                ('comments', 'Phishing+email+flagged+by+FireEye+ETP'),
                ('cat1', 18), # - 18: Phishing
                ('cat2', 43), # - 43: Malware
                ('email', 'atr@nb.com'),
            )

            # This keeps track of the results being reported back to the analyst
            recat_status = ""

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            if categorization_name in security_categories:
                recat_status = "The URL or Domain:\n {} \nhas been properly categorized already...".format(artifact_value)
            else:
                recat_submission = requests.post('https://sitereview.bluecoat.com/api/reportThreat', headers=headers, params=data)
                log.debug(recat_submission.status_code)
                log.debug(recat_submission.text)

                # This converts the XML object to JSON and then to string
                recat_submission_object = json.dumps(xmltodict.parse(recat_submission.content), sort_keys=True, indent=4)
                log.debug(recat_submission_object)
                # This converts the String back to a JSON Object for the data table
                recat_submission_json = json.loads(recat_submission_object)

                if 'Error' in recat_submission_json:
                    recat_status = "{}".format(recat_submission_json['Error']['Explanation'])
                elif 'Rejected' in recat_submission_json['SubmissionResult']:
                    recat_status = "{}".format(recat_submission_json['SubmissionResult']['Rejected']['Explanation'])
                elif 'Accepted' in recat_submission_json['SubmissionResult']:
                    recat_status = "Submitted:\n {} \nto Bluecoat for Recategorization with the response:\n {} \nand awaiting approval".format(artifact_value,recat_submission_json['SubmissionResult']['Accepted']['SubmissionId'])
                else:
                    recat_status = "Try running the recategorization at a later time..."

            # # This returns a list of available categories
            # response = requests.get(('https://sitereview.bluecoat.com/api/categories?userID={}').format(uid),
            #                         headers=headers)
            #
            # # This converts the XML object to JSON and then to string
            # response_object = json.dumps(xmltodict.parse(response.content), sort_keys=True,
            #                              indent=4)
            #
            # print(response_object)

            yield StatusMessage("done...")

            results = {
                "value": recat_status
                #"value": recat_submission_json
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()