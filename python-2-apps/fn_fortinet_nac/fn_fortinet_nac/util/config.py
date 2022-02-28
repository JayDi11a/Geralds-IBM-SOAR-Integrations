# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_fortinet_nac"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_fortinet_nac]
user_name=xxx
api_key=xxx
server_name=xxx
#"""
    return config_data
