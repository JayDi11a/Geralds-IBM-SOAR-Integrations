# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_palo_alto_panorama"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_palo_alto_panorama]
user_name = xxx
user_password = xxx
server_name = xxx
panorama_version = xxx
#"""
    return config_data
