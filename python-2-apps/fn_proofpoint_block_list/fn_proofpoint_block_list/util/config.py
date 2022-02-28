# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_proofpoint_block_list"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_proofpoint_block_list]
api_user=xxx
api_user_credentials=xxx
endpoint=xxx
port=xxx
"""
    return config_data
