# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import resilient
import tempfile

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'incident_attachment_converter"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_incident_attachment_converter", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_incident_attachment_converter", {})

    @function("incident_attachment_converter")
    def _incident_attachment_converter_function(self, event, *args, **kwargs):
        """Function: This function converts attachments from the incident level and adds them as attachments. For now, this only applies to the use case of converting attachments to artifacts of type email attachment."""
        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)

            # Talks to the config file and gets the auth credentials necessary to talk to Resilient REST API
            parser = resilient.ArgumentParser(config_file=resilient.get_config_file())
            opts = parser.parse_args()
            client = resilient.get_client(opts)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            uri = "/incidents/{}/attachments".format(incident_id)
            incident_attachments = client.get(uri)

            # Stores the attachments from the incident into a list object
            attachment_objects = list()


            for incident_attachment in incident_attachments:
                uri_incident_attachment = "/incidents/{}/attachments/{}/contents".format(incident_id, incident_attachment['id'])
                incident_attachment_content = client.get_content(uri_incident_attachment)
                incident_attachment_object = {
                    "attachment_name": incident_attachment['name'],
                    "attachment_id": incident_attachment['id'],
                    "attachment_contents": incident_attachment_content
                }


                attachment_objects.append(incident_attachment_object)

            # TODO: Error handle if the file can't be downloaded
            for attachment_object in attachment_objects:
                temp = tempfile.NamedTemporaryFile()
                try:
                    temp.write(attachment_object['attachment_contents'])
                    temp.seek(0)

                    # post the newly created artifact of type email attachment
                    client.post_artifact_file('/incidents/{}/artifacts/files'.format(incident_id), 7, temp.name, value=attachment_object['attachment_name'])
                    yield StatusMessage("Incident attachment: {} has been successfully posted as Artifact of Type Email Attachment".format(attachment_object['attachment_name']))


                finally:
                    temp.close()

                # delete the incident attachment after it's been processed
                client.delete('/incidents/{}/attachments/{}'.format(incident_id, attachment_object['attachment_id']))
                yield StatusMessage("Incident Attachment: {} has been successfully removed from the Incident".format(attachment_object['attachment_name']))

            yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()