# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_carbon_black_cloud_devices"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_carbon_black_cloud_devices]
hostname=xxx
api_id=xxx
api_secret_key=xxx
org_key=xxx
result_limit=xxx
"""
    return config_data