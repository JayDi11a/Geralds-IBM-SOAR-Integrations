# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_phishcheck.util.selftest as selftest
import requests
import json
import xmltodict


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'phishcheck_check_url"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_phishcheck", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_phishcheck", {})

    @function("phishcheck_check_url")
    def _phishcheck_check_url_function(self, event, *args, **kwargs):
        """Function: This function takes in a url value and passes it to the Phishcheck endpoint to be analyzed. Then it returns the results back to the incident."""

        requests.urllib3.disable_warnings()



        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number
            artifact_value = kwargs.get("artifact_value")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("artifact_id: %s", artifact_id)
            log.info("artifact_value: %s", artifact_value)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            url = 'https://phishcheck.me/'

            sess = requests.Session()

            g = sess.get(url)

            print(type(g.content))
            print(g.content)

            # DATA = {
            #     'url': 'http://apple.com',  # <- url you scanning
            #     'useragent': '0',
            #     'csrfmiddlewaretoken': g.cookies['csrftoken'],
            #     'recheck': 'True'  # <- False if you don't wanna recheck the link again
            # }
            #
            # p = sess.post(url + '/submit/', data=DATA)
            #
            # print(type(p.content))
            # print(p.content)


            # d = sess.get('https://phishcheck.me/' + str(p.json()['sid']) + '/details')

            yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()