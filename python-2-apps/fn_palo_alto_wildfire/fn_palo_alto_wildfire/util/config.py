# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_palo_alto_wildfire"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_palo_alto_wildfire]
wildfire_api_key=xxx
"""
    return config_data
