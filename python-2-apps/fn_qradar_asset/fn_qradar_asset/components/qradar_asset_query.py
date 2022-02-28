# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_qradar_asset.util.selftest as selftest
import requests
import json

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_asset_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_qradar_asset", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_qradar_asset", {})

    @function("qradar_asset_query")
    def _qradar_asset_query_function(self, event, *args, **kwargs):
        """Function: This function is a simple query of QRadar asset information. This just finds all assets that contains phone numbers and contact name and returns them to a data table."""

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

            # retreive the API username and key to pass to the endpoint
            user = get_config_option("user_name")
            password = get_config_option("user_password")
            server = get_config_option("server_name")

            asset_results = list()

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            get_assets = requests.get('https://{}/api/asset_model/assets'.format(server), verify=False,
                                      auth=(user, password))

            assets = get_assets.json()
            log.debug(json.dumps(assets, indent=4, sort_keys=True)) #in case I need to tu

            # This is the logic that traverses the JSON object gets the fields of interest, puts them in an asset dictionary object, and adds that object to a list
            for i in range(len(assets)):
                for j in range(len(assets[i]['properties'])):
                    # This handles making sure the properties field isn't empty and explicitly handles that the Technical Contact and Technical Owner field populates
                    if assets[i]['properties'][j]['value'] is not None and assets[i]['properties'][j]['name'] == "Technical Contact" or assets[i]['properties'][j]['name'] == "Technical Owner":


                        number_of_properties = len(assets[i]['properties'])  # this handles getting the properties list number more generically

                        asset_object = {
                            "asset_id": assets[i]['id'],
                            "asset_technical_contact": assets[i]['properties'][number_of_properties - 2]['value'],
                            "asset_technical_name": assets[i]['properties'][number_of_properties - 1]['value']
                        }

                        asset_results.append(asset_object)

            # This section deals with handling duplicate objects in a list leveraging
            def remove_duplicates(l):
                seen = set()
                new_l = list()
                for d in l:
                    t = tuple(d.items())
                    if t not in seen:
                        seen.add(t)
                        new_l.append(d)

                return new_l

            unique_asset_results = remove_duplicates(asset_results)

            yield StatusMessage("done...")

            results = {
                "value": unique_asset_results
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()