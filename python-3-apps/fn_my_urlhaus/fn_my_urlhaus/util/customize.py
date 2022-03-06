# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_my_urlhaus"""

import base64
import os
import io
try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition

RES_FILE = "data/export.res"


def codegen_reload_data():
    """
    Parameters required reload codegen for the fn_my_urlhaus package
    """
    return {
        "package": u"fn_my_urlhaus",
        "message_destinations": [u"fn_my_urlhaus"],
        "functions": [u"fn_my_urlhaus"],
        "workflows": [u"my_urlhaus_workflow"],
        "actions": [u"Example: My Urlhaus Lookup"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 43.1.20

    Contents:
    - Message Destinations:
        - fn_my_urlhaus
    - Functions:
        - fn_my_urlhaus
    - Workflows:
        - my_urlhaus_workflow
    - Rules:
        - Example: My Urlhaus Lookup
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)