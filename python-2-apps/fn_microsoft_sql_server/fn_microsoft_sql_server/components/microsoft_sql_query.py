# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import pyodbc
import json
import resilient


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'microsoft_sql_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_microsoft_sql_server", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_microsoft_sql_server", {})

    @function("microsoft_sql_query")
    def _microsoft_sql_query_function(self, event, *args, **kwargs):
        """Function: This function takes Microsoft SQL Server queries and simply returns the results of that query."""

        # talks to the config file and gets the auth credentials necessary to talk to Resilient Endpoint
        parser = resilient.ArgumentParser(config_file=resilient.get_config_file())
        opts = parser.parse_args()
        client = resilient.get_client(opts)


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

        sql_results = ''

        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_type = kwargs.get("artifact_type")  # text
            artifact_value = kwargs.get("artifact_value")  # text
            sql_query_statement = kwargs.get("sql_query_statement")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("artifact_type: %s", artifact_type)
            log.info("artifact_value: %s", artifact_value)
            log.info("sql_query_statement: %s", sql_query_statement)

            # # retreive the Microsoft SQL server credentials from the config file to be set
            # server = get_config_option("server_name")
            # database = get_config_option("db_name")
            # connection = get_config_option("trusted_connection")
            uid = get_config_option("user")
            creds = get_config_option("password")

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            # server_connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=" + server + ";Database=" + database + ";Trusted_Connection=" + connection)
            server_connection = pyodbc.connect('DSN=MyMSSQLServer;UID={};PWD={}'.format(uid, creds))
            cursor = server_connection.cursor()
            if "SELECT [Name], [Domain], [User], [OS Name], [OS Version], [IP Address], [Server], [OS Primary Language], [OS Sub Language], [MAC Address], [System Type], [IsManaged], [IsLocal], [OS Revision] FROM [dbo].[vComputer] where [User] = " in sql_query_statement:
                sql_query_statement = "SELECT [Name], [Domain], [User], [OS Name], [OS Version], [IP Address], [Server], [OS Primary Language], [OS Sub Language], [MAC Address], [System Type], [IsManaged], [IsLocal], [OS Revision] FROM [dbo].[vComputer] where [User] = '{}'".format(artifact_value)
                cursor.execute(sql_query_statement)
            else:
                cursor.execute(sql_query_statement)

            # identifies the column headers for the data table
            columns = [column[0] for column in cursor.description]
            #print columns

            # instantiating what is later to be used as a data table object
            sql_returns = []

            # creates a key/value pairing of the column header and the corresponding row value
            for row in cursor.fetchall():
                sql_returns.append(dict(zip(columns,row)))

            # # Test of the dict object output
            # print sql_returns
            #
            # # Test of isolating the key to get the corresponding value
            # sql_string_objects = json.dumps(sql_returns)
            # sql_json_objects = json.loads(sql_string_objects)
            #
            # print sql_json_objects[0]['Domain']

            sql_dict = next((d for i, d in enumerate(sql_returns) if 'Domain' in d), None)
            # print sql_dict['Domain']



            # for row in cursor:
            #     #print('row = %r' % (row,))
            #     sql_results = unicode(row)


            neuberger_sql_object = {
                "user": sql_dict['User'],
                "location": "",
                "ip_address": sql_dict['IP Address'],
                "hostname": sql_dict['Name'],
                "mac_address": (sql_dict['MAC Address']).replace('-',':'),
                "os": (sql_dict['OS Name']) + ' ' + sql_dict['OS Version']

            }


            yield StatusMessage("done...")

            results = {
                "value": neuberger_sql_object
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
