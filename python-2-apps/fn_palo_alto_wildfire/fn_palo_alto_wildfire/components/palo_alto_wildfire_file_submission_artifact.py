# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_palo_alto_wildfire.util.selftest as selftest
from pyldfire import WildFire
from resilient_lib import get_file_attachment, get_file_attachment_name
from fn_palo_alto_wildfire.util import function_utils
import tempfile
import json

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'palo_alto_wildfire_file_submission_artifact"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_palo_alto_wildfire", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_palo_alto_wildfire", {})

    @function("palo_alto_wildfire_file_submission_artifact")
    def _palo_alto_wildfire_file_submission_artifact_function(self, event, *args, **kwargs):
        """Function: This function pulls down the file from the artifact in the Resilient Incident and submits the file to Palo Alto WildFire. The results of the file submission are returned to the Incident."""

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

        # Authentication for WildFire Endpoint
        api_key = get_config_option("wildfire_api_key")

        # Assign API key to the WildFire object
        wildfire = WildFire(api_key)

        # Resilient object that allows leveraging the Resilient Rest API
        # and its library
        res_client = self.rest_client()

        # Global Empty Dictionary object to be appended to
        submission = {}

        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("artifact_id: %s", artifact_id)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            # pull down the contents of the file, assign path and open it
            artifact_file = get_file_attachment(res_client=res_client, incident_id=incident_id, artifact_id=artifact_id,
                                                task_id=None, attachment_id=None)

            # get name of the corresponding file content
            artifact_file_name = get_file_attachment_name(res_client=res_client, incident_id=incident_id,
                                                          artifact_id=artifact_id, task_id=None, attachment_id=None)
            log.info(artifact_file_name)
            temp = tempfile.NamedTemporaryFile()

            try:
                temp.write(artifact_file)
                temp.seek(0)

                # Returns a dictionary object
                submission_results = wildfire.submit_file(temp,artifact_file_name)

            finally:
                temp.close()

            #log.info(submission_results)
            #log.info(submission_results.values()[3])
            submission_sha256 = submission_results.values()[3]

            # TODO: Figure out if you simply want to return verdict versus report itself
            # versus pdf of results
            submission_report = wildfire.get_report(submission_sha256)
            log.info(submission_report)


            # Gets just the verdict of submission and adds the result to the submission
            # dictionary object
            submission_verdict = wildfire.get_verdicts(submission_sha256)
            log.info(submission_verdict)
            verdict_object = dict({'verdict':str(submission_verdict)})
            log.info(type(verdict_object))
            submission.update(verdict_object)


            # Redundant?
            # for found in listRecursive(submission_report, 'malware'):
            #     log.info(type(found))
            #     malware_object = dict({'malware':str(found)})
            #     log.info(type(malware_object))
            #     submission.update(malware_object)

            # Takes the filetype key finds the corresponding value and appends the pair to
            # the submission dictionary
            for found in function_utils.listRecursive(submission_report, 'filetype'):
                log.info(found)
                filetype_object = dict({'filetype':str(found)})
                log.info(type(filetype_object))
                submission.update(filetype_object)

            # Takes the software key finds the corresponding value and appends the pair to
            # the submission dictionary
            for found in function_utils.listRecursive(submission_report, 'software'):
                log.info(found)
                software_object = dict({'software':str(found)})
                log.info(type(software_object))
                submission.update(software_object)

            # Takes the doc_embedded_files key finds the corresponding value and appends the pair to
            # the submission dictionary
            for found in function_utils.listRecursive(submission_report, 'doc_embedded_files'):
                log.info(found)
                doc_embedded_object = dict({'doc_embedded_files':str(found)})
                log.info(type(doc_embedded_object))
                submission.update(doc_embedded_object)

            # Takes the score key finds the corresponding value and appends the pair to
            # the submission dictionary
            for found in function_utils.listRecursive(submission_report, '@score'):
                log.info(found)
                score_object = dict({'score':str(found)})
                log.info(type(score_object))
                submission.update(score_object)

            # Takes the text key finds the corresponding value and appends the pair to
            # the submission dictionary
            for found in function_utils.listRecursive(submission_report, '#text'):
                log.info(found)
                text_object = dict({'text':str(found)})
                log.info(type(text_object))
                submission.update(text_object)

            # Takes the details key finds the corresponding value and appends the pair to
            # the submission dictionary
            for found in function_utils.listRecursive(submission_report, '@details'):
                log.info(found)
                details_object = dict({'details':str(found)})
                log.info(type(details_object))
                submission.update(details_object)

            log.info(submission)
            log.info(type(submission))

            yield StatusMessage("done...")

            results = {
                "value": submission
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()