# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_proofpoint_block_list.util.selftest as selftest
import resilient
import requests


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'proofpoint_add_to_block_group"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_proofpoint_block_list", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_proofpoint_block_list", {})

    @function("proofpoint_add_to_block_group")
    def _proofpoint_add_to_block_group_function(self, event, *args, **kwargs):
        """Function: This function runs on the incident and extracts artifacts of type Email Sender and Email Receiver passing the sender email address into the block list of the email receivers address."""

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


        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)

            # Talks to the config file and gets the auth credentials necessary to talk to Resilient REST API
            parser = resilient.ArgumentParser(config_file=resilient.get_config_file())
            opts = parser.parse_args()
            client = resilient.get_client(opts)

            headers = {
                'Content-Type': 'application/json',
            }

            # Authentication specific settings
            user_name = get_config_option("api_user")
            password = get_config_option("api_user_credentials")
            host = get_config_option("endpoint")
            port = get_config_option("port")


            completion = False

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            uri = "/incidents/{}/artifacts".format(incident_id)
            incident_artifacts = client.get(uri)

            # Stores the attachments from the incident into a list object
            email_senders = list()
            email_recipients = list()

            # For filtering on the Email Sender Artifact type and adding it to
            # the email sender list
            for incident_artifact in incident_artifacts:
                if incident_artifact['type'] is 9:
                    email_senders.append(str(incident_artifact['value']))


            # For filtering on the Email Recipient Artifact type and adding it to
            # the email recipient list
            for incident_artifact in incident_artifacts:
                if incident_artifact['type'] is 20:
                    email_recipients.append(str(incident_artifact['value']))


            # Gets the first item from each list and assigns it to the Proofpoint
            # Endpoint call that adds the sender email address to the blocklist of
            # the recipient email address account
            # TODO: Handle multiple additions to block list per recipient

            sender = email_senders[0]
            recipient = email_recipients[0]

            #data = '{"blocklist" : "%s"}' % email_senders - troubleshooting to isolate for just one element
            data = '{"blocklist" : "%s"}' % sender

            response = requests.put('https://{}:{}/rest/v1/enduser/{}'.format(host,port,recipient), headers=headers, data=data, verify=False,
                                    auth=(user_name, password))

            #log.info(response.headers)
            #log.info(response.content)

            # TODO: extract either header or body information and write it to value variable
            # TODO: expand success in the code more around response
            submission_result = response.content
            completion = True


            yield StatusMessage("done...")

            results = {
                "success": completion,
                "payload": submission_result
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()