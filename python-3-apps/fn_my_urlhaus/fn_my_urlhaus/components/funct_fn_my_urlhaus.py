# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_my_urlhaus"
FN_NAME = "fn_my_urlhaus"

ARTIFACT_TYPE_MAP = {
    "DNS Name": "host",
    "IP Address": "host",
    "Malware MD5 Hash": "payload:md5_hash",
    "Malware SHA-256 Hash": "payload:sha256_hash",
    "Server Name": "host",
    "String": "tag",
    "URL": "url"
}

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_my_urlhaus'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: None
        Inputs:
            -   fn_inputs.my_urlhaus_artifact_type
            -   fn_inputs.my_urlhaus_artifact_value
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        # Example validating app_configs
        validate_fields([
             {"name": "base_url", "placeholder": "<api-base-url>"}],
             self.app_configs)

        yield self.status_message("base_url: '{0}'".format(self.app_configs.base_url))

        # Example validating required fn_inputs
        validate_fields(["my_urlhaus_artifact_type", "my_urlhaus_artifact_value"], fn_inputs)

        # Example getting access to self.get_fn_msg()
        # fn_msg = self.get_fn_msg()
        # self.LOG.info("fn_msg: %s", fn_msg)

        # Example interacting with REST API
        # res_client = self.rest_client()
        # function_details = res_client.get("/functions/{0}?handle_format=names".format(FN_NAME))

        # Example raising an exception
        # raise IntegrationError("Example raising custom error")

        ##############################################
        # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
        ##############################################

        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        url = "{0}/{1}".format(self.app_configs.base_url, ARTIFACT_TYPE_MAP.get(fn_inputs.my_urlhaus_artifact_type, ""))


        payload = {
            ARTIFACT_TYPE_MAP.get(fn_inputs.my_urlhaus_artifact_type, ""): fn_inputs.my_urlhaus_artifact_value
        }


        response = self.rc.execute(
            method="post",
            headers=headers,
            url=url,
            data=payload
        )

        results = response.json()

        yield self.status_message("Endpoint reached successfully and returning results for App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
        ##############################################

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        # Note this is only used for demo purposes! Put your own key/value pairs here that you want to access on the Platform
        # results = {"mock_key": "Mock Value!"}

        # yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
