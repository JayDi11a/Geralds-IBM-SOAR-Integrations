# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_sumologic"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_sumologic]
api_user=xxx
api_user_credentials=xxx
endpoint=xxx
offset=xxx
limit=xxx
"""
    return config_data
