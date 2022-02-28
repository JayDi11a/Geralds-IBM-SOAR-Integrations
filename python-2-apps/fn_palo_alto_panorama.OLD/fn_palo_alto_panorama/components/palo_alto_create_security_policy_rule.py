# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_palo_alto_panorama.util.selftest as selftest


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'palo_alto_create_security_policy_rule"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_palo_alto_panorama", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_palo_alto_panorama", {})

    @function("palo_alto_create_security_policy_rule")
    def _palo_alto_create_security_policy_rule_function(self, event, *args, **kwargs):
        """Function: This function creates a security policy rule against the firewall."""

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
            policy_rule_name = kwargs.get("policy_rule_name")  # text
            location = kwargs.get("location")  # text
            policy_to = kwargs.get("policy_to")  # text
            policy_from = kwargs.get("policy_from")  # text
            source_user = kwargs.get("source_user")  # text
            application = kwargs.get("application")  # text
            service = kwargs.get("service")  # text
            hipprofiles = kwargs.get("hipprofiles")  # text
            action = kwargs.get("action")  # text
            category = kwargs.get("category")  # text
            source = kwargs.get("source")  # text
            destination = kwargs.get("destination")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("policy_rule_name: %s", policy_rule_name)
            log.info("location: %s", location)
            log.info("policy_to: %s", policy_to)
            log.info("policy_from: %s", policy_from)
            log.info("source_user: %s", source_user)
            log.info("application: %s", application)
            log.info("service: %s", service)
            log.info("hipprofiles: %s", hipprofiles)
            log.info("action: %s", action)
            log.info("category: %s", category)
            log.info("source: %s", source)
            log.info("destination: %s", destination)

            # retreive the API username and key to pass to the endpoint
            user = get_config_option("user_name")
            password = get_config_option("user_password")
            server = get_config_option("server_name")
            version = get_config_option("panorama_version")


            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            # Get the API key and set it to a variable to be passed in for later API calls
            params_api = (
                ('type', 'keygen'),
                ('user', '{}'.format(user)),
                ('password', '{}'.format(password)),
            )

            api_key_response = requests.get('https://{}/api/'.format(server), params=params_api, verify=False)

            # This converts the XML object to JSON and then to string
            api_key_response_object = json.dumps(xmltodict.parse(api_key_response.content), sort_keys=True, indent=4)
            log.debug(api_key_response_object)
            # This converts the String back to a JSON Object
            api_key_response_object_json = json.loads(api_key_response_object)

            # Assigns the API key to a variable
            api_key = api_key_response_object_json['response']['result']['key']

            # Security Rule header that takes the API key as its only value
            headers = {
                'X-PAN-KEY': '{}'.format(api_key),
            }

            # Gets the params needed for the
            params = (
                ('location', '{}'.format(location)),
                ('vsys', 'vsys1'),
                ('name', '{}'.format(policy_rule_name)),
            )

            # The data field that needs to be passed to the Security Policy REST API POST
            data = {"entry": [{"@name": "{}".format(policy_rule_name), ' \
                                            '"@location": "{}".format(location), ' \
                                            '"@vsys": "vsys1", ' \
                                            '"to": {"member": ["{}"]}.format(policy_to),
                                             "from": {"member": ["{}"]}.format(policy_from), ' \
                                            '"source-user": {"member": ["{}"]}.format(source_user), ' \
                                            '"application": {"member": ["{}"]}.format(applicaiton), ' \
                                            '"service": {"member": ["{}"]}.format(service), ' \
                                            '"hip-profiles": {"member": ["{}"]}.format(hipprofiles), ' \
                                            '"action": "{}".format(action), ' \
                                            '"category": {"member": ["{}"]}.format(category), ' \
                                            '"source": {"member": ["{}"]}.format(source), ' \
                                            '"destination": {"member": ["{}"]}.format(destination)}]}

            response = requests.post('https://{}/restapi/{}/Policies/SecurityRules'.format(server, version),
                                     headers=headers, params=params, data=data)

            print(response)

            yield StatusMessage("done...")

            results = {
                "value": response
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()