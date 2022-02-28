# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_crowdstrike_query"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_crowdstrike_query]
user_name=put-crowdstrike-user-here
api_key=put-password-here
#"""
    return config_data