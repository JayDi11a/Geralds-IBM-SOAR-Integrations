# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_cisco_firepower_management"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_cisco_firepower_management]
host=xxx
port=xxx
username=xxx
password=xxx
"""
    return config_data
