# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_passive_total"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_passive_total]
user_name=xxx
password=xxx
#"""
    return config_data