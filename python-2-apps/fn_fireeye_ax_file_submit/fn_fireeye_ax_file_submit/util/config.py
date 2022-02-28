# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_fireeye_ax_file_submit"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_fireeye_ax_file_submit]
# Credentials for accessing the FireEye AX Endpoint:

user_name=xxx
user_credentials=xxx
endpoint=xxx
port=xxx

# set this in the event that the endpoint requires a cert or not
# set to False by default
verify_cert=False

# This supports versions v1.2.0 or v2.0.0 
version=v2.0.0

# Optional file submission settings:

# Specifies the ID of the application to be used for the analysis. 0 allows the 
# AX Series appliance to choose the application for you
application=0

# Sets the analysis timeout (in seconds)
timeout=500

# Set analysis priority: (0 is Normal, 1 is Urgent)
priority=0

# Selects the AX Series profile to be used
# Can be specified if known, otherwise, assigned from the results of the config call
profiles=win7-sp1

# Specifies the analysis mode: 1 is Live: analysis from the MVX engine. 2 is Sandbox: analysis
# in a closed protected environment
analysis_type=1

# Perform analysis on potential duplicate file or not
force=true

# Specifies whether file has predetermined location or browse target location
prefetch=0


"""
    return config_data
