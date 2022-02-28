# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_ivanti_service_manager"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_ivanti_service_manager]
api_user=xxx
role=xxx
api_user_credentials=xxx
endpoint=xxx
"""
    return config_data
