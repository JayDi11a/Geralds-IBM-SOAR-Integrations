# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_palo_alto_panorama.util.selftest as selftest
import requests
import json
import xmltodict
import time
from bs4 import BeautifulSoup as BS


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

            policy_added = True

            # retreive the API username and key to pass to the endpoint
            user = get_config_option("user_name")
            password = get_config_option("user_password")
            server = get_config_option("server_name")
            version = get_config_option("panorama_version")

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            rule_path = "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase/security/rules"
            sample_rule = """
            <entry name="{}">
                <source>
                    <member>{}</member>
                </source>
                <destination>
                    <member>{}</member>
                </destination>
                <service>
                    <member>{}</member>
                </service>
                <application>
                    <member>{}</member>
                </application>
                <action>{}</action>
                <log-end>yes</log-end>
                <from>
                    <member>{}</member>
                </from>
                <to>
                    <member>{}</member>
                </to>

            </entry>
            """.format(policy_rule_name,source,destination,service,application,action,policy_from,policy_to)

            try:
                response = requests.get("https://{}/api/?type=keygen&user={}&password={}".format(server,user,password),verify=False, timeout=5)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                policy_added = False
                print(e)
            except requests.exceptions.HTTPError as httperr:
                policy_added = False
                print(httperr)
            except requests.exceptions.Timeout as timeouterr:
                policy_added = False
                print(timeouterr)
            except requests.exceptions.ConnectionError as connerr:
                policy_added = False
                print(connerr)
            except requests.exceptions.ConnectTimeout as conntimeout:
                policy_added = False
                print(conntimeout)

            try:
                soup = BS(response.content, 'html.parser')
                key = soup.find('key').text
            except AttributeError as ae:
                policy_added = False
                print("Error while parsing response:", ae)

            try:
                r = requests.post("https://{}/api/?type=config&action=set&key={}&xpath={}&element={}".format(server,key,rule_path,sample_rule),verify=False, timeout=5)
                r.raise_for_status()
                log.info(r.content)
            except requests.exceptions.RequestException as e:
                policy_added = False
                print(e)
            except requests.exceptions.HTTPError as httperr:
                policy_added = False
                print(httperr)
            except requests.exceptions.Timeout as timeouterr:
                policy_added = False
                print(timeouterr)
            except requests.exceptions.ConnectionError as connerr:
                policy_added = False
                print(connerr)
            except requests.exceptions.ConnectTimeout as conntimeout:
                policy_added = False
                print(conntimeout)
            time.sleep(3)


            try:
                commit_response = requests.post("https://{}/api/?type=commit&key={}&cmd=<commit></commit>".format(server,key), verify=False,timeout=5)
                commit_response.raise_for_status()
                log.info(commit_response.content)
            except requests.exceptions.RequestException as e:
                policy_added = False
                print(e)
            except requests.exceptions.HTTPError as httperr:
                policy_added = False
                print(httperr)
            except requests.exceptions.Timeout as timeouterr:
                policy_added = False
                print(timeouterr)
            except requests.exceptions.ConnectionError as connerr:
                policy_added = False
                print(connerr)
            except requests.exceptions.ConnectTimeout as conntimeout:
                policy_added = False
                print(conntimeout)


            yield StatusMessage("done...")

            results = {
                "success": policy_added
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()