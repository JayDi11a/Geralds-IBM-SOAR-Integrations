# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import pyodbc
import json
import resilient
import datetime
import time
from fn_bluecoat_sql_server.util.constants import UNBLOCKABLE_URLS

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'bluecoat_sql_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_bluecoat_sql_server", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_bluecoat_sql_server", {})

    @function("bluecoat_sql_query")
    def _bluecoat_sql_query_function(self, event, *args, **kwargs):
        """Function: This function takes in a query statement and specifically for the purposes of this use case, allows the user the ability to check if domain/url exists, get the category id for new domain/url insertion, and ultimately insert the newly defined domain/url"""

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

            # Message to be reported back into the case
            analyst_message = ''

            # Current Time Stamp to be passed into the recategorization database
            # time_stamp = datetime.datetime.utcnow().strftime("%Y:%m:%d %H:%M:%S")
            ts = int(time.time())

            # Converts URLs to Base Domains to be uploaded to Bluecoat DB
            if artifact_value.startswith('https'):
                log.info(artifact_value)
                http_value = artifact_value.replace("https://", "")
                log.info(http_value)
                http_value = http_value.replace("www.", "")
                http_value = http_value.split('/', 1)[0]
            elif artifact_value.startswith('http'):
                http_value = artifact_value.replace("http://", "")
                http_value = http_value.replace("www.", "")
                http_value = http_value.split('/', 1)[0]
            else:
                http_value = artifact_value

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            # This section connects to the Bluecoat DB handles the scenarios of if the SQL queries either correspond to checking for the url or writing to the database
            # Otherwies, it just handles arbitrary SQL queries.
            server_connection = pyodbc.connect('DSN=MyOtherMSSQLServer;UID={};PWD={}'.format(uid, creds))
            cursor = server_connection.cursor()
            if "SELECT count(1) FROM seceng..bluecoat_resources WHERE resource=" in sql_query_statement:
                log.info(http_value)
                #sql_query_statement = "SELECT count(1) FROM seceng..bluecoat_resources WHERE resource='{}' and (category='14' OR category='13' OR category='12') ;".format(artifact_value)
                sql_query_statement = "SELECT count(1) FROM seceng..bluecoat_resources WHERE resource='{}' and (category='14' OR category='13' OR category='12') ;".format(http_value)
                cursor.execute(sql_query_statement)

                # identifies the column headers for the data table
                columns = [column[0] for column in cursor.description]
                print columns

                # instantiating what is later to be used as a data table object
                sql_returns = []

                # creates a key/value pairing of the column header and the corresponding row value
                for row in cursor.fetchall():
                    sql_returns.append(dict(zip(columns, row)))

                sql_value_returns = [d[''] for d in sql_returns if '' in d]

                # This handles reporting back to incident whether or not the url already exists in the database for the analyst to decide what to do next
                if 0 in sql_value_returns:
                    analyst_message = 'The Domain or URL has not yet been categorized...please run the manual Menu Action called "Run Bluecoat DB Submit" on:\n {} \nin order to provide the correct categorization...'.format(
                        http_value)
                elif 1 in sql_value_returns:
                    analyst_message = '{}\n is already in the Bluecoat Definitions Database under category:\n Malware'.format(
                        http_value)
                else:
                    analyst_message = 'Either your query is wrong or you are running a query for a different use case?'



            elif "INSERT INTO seceng..bluecoat_resources (resource, category, username, requests, updated) VALUES ('<domain>','<category_id>','svcresilient','<tickets_separated_by_comma>',<unix_timestamp>) ;" in sql_query_statement:
                if http_value.lower() in UNBLOCKABLE_URLS:
                    analyst_message = '{} is on the Alexa top domain list and will not be added to the Bluecoat definitions database. Contact ATR for details'.format(http_value)
                else:
                    sql_query_statement = "INSERT INTO seceng..bluecoat_resources (resource, category, username, requests, updated) VALUES ('{}','{}','svcresilient','{}','{}');".format(http_value, 14, incident_id, ts)
                    log.info(sql_query_statement) # - to see if it is going through as it should.
                    cursor.execute(sql_query_statement)
                    cursor.commit() # - for INSERT, you need to commit after the execution is performed
                    analyst_message = '{} was successfully added and categorized to the Bluecoat Database...'.format(http_value)

            else:
                analyst_message = 'Something went wrong...'
                #cursor.execute(sql_query_statement)
                #analyst_message = 'Your ad hoc query ran successfully'


            yield StatusMessage("done...")

            results = {
                "value": analyst_message
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()