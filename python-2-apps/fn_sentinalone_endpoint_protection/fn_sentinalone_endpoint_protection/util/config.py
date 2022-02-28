# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_sentinalone_endpoint_protection"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_sentinalone_endpoint_protection]
api_key=xxx
server=xxx
#"""
    return config_data