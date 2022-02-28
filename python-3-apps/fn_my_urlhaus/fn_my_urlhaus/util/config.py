# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_my_urlhaus"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_my_urlhaus when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_my_urlhaus]
base_url=xxx
"""
    return config_data
