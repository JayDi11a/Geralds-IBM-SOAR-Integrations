# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_incident_attachment_converter"""

from __future__ import print_function
from resilient_circuits.util import *


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     incident_id
    #   Message Destinations:
    #     attachment_conversion
    #   Functions:
    #     incident_attachment_converter


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbXSwgImFjdGlvbnMiOiBbXSwgImxheW91
dHMiOiBbXSwgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6IDIsICJpZCI6IDI2LCAiaW5kdXN0cmll
cyI6IG51bGwsICJwaGFzZXMiOiBbXSwgImFjdGlvbl9vcmRlciI6IFtdLCAiZ2VvcyI6IG51bGws
ICJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMCwgInZlcnNpb24iOiAiMzAuMi44OCIsICJi
dWlsZF9udW1iZXIiOiA4OCwgIm1pbm9yIjogMn0sICJ0aW1lZnJhbWVzIjogbnVsbCwgIndvcmtz
cGFjZXMiOiBbXSwgImF1dG9tYXRpY190YXNrcyI6IFtdLCAiZnVuY3Rpb25zIjogW3siZGlzcGxh
eV9uYW1lIjogIkluY2lkZW50IEF0dGFjaG1lbnQgQ29udmVydGVyIiwgImRlc2NyaXB0aW9uIjog
eyJjb250ZW50IjogIlRoaXMgZnVuY3Rpb24gY29udmVydHMgYXR0YWNobWVudHMgZnJvbSB0aGUg
aW5jaWRlbnQgbGV2ZWwgYW5kIGFkZHMgdGhlbSBhcyBhdHRhY2htZW50cy4gRm9yIG5vdywgdGhp
cyBvbmx5IGFwcGxpZXMgdG8gdGhlIHVzZSBjYXNlIG9mIGNvbnZlcnRpbmcgYXR0YWNobWVudHMg
dG8gYXJ0aWZhY3RzIG9mIHR5cGUgZW1haWwgYXR0YWNobWVudC4iLCAiZm9ybWF0IjogInRleHQi
fSwgImNyZWF0b3IiOiB7ImRpc3BsYXlfbmFtZSI6ICJHZXJhbGQgVHJvdG1hbiIsICJ0eXBlIjog
InVzZXIiLCAiaWQiOiA0LCAibmFtZSI6ICJnZXJhbGQudHJvdG1hbkBpYm0uY29tIn0sICJ2aWV3
X2l0ZW1zIjogW3sic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAi
c2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImNvbnRl
bnQiOiAiZWFkMjE0YzItMTNmZS00M2Y2LWEzYzctNjc2YTg4MzM4ZGJiIiwgInN0ZXBfbGFiZWwi
OiBudWxsfV0sICJleHBvcnRfa2V5IjogImluY2lkZW50X2F0dGFjaG1lbnRfY29udmVydGVyIiwg
InV1aWQiOiAiYjI4ZTQzYjAtYzJhMC00MjgzLTk0ZmYtZmYxYzIzMDM2ZDMzIiwgImxhc3RfbW9k
aWZpZWRfYnkiOiB7ImRpc3BsYXlfbmFtZSI6ICJHZXJhbGQgVHJvdG1hbiIsICJ0eXBlIjogInVz
ZXIiLCAiaWQiOiA0LCAibmFtZSI6ICJnZXJhbGQudHJvdG1hbkBpYm0uY29tIn0sICJ2ZXJzaW9u
IjogMSwgIndvcmtmbG93cyI6IFtdLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTUzNzE2OTY1NTcy
NiwgImRlc3RpbmF0aW9uX2hhbmRsZSI6ICJhdHRhY2htZW50X2NvbnZlcnNpb24iLCAiaWQiOiAx
MDIsICJuYW1lIjogImluY2lkZW50X2F0dGFjaG1lbnRfY29udmVydGVyIn1dLCAibm90aWZpY2F0
aW9ucyI6IG51bGwsICJyZWd1bGF0b3JzIjogbnVsbCwgImluY2lkZW50X3R5cGVzIjogW3siY3Jl
YXRlX2RhdGUiOiAxNTM3MTk5NzI4NzczLCAiZGVzY3JpcHRpb24iOiAiQ3VzdG9taXphdGlvbiBQ
YWNrYWdlcyAoaW50ZXJuYWwpIiwgImV4cG9ydF9rZXkiOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdl
cyAoaW50ZXJuYWwpIiwgImlkIjogMCwgIm5hbWUiOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAo
aW50ZXJuYWwpIiwgInVwZGF0ZV9kYXRlIjogMTUzNzE5OTcyODc3MywgInV1aWQiOiAiYmZlZWMy
ZDQtMzc3MC0xMWU4LWFkMzktNGEwMDA0MDQ0YWEwIiwgImVuYWJsZWQiOiBmYWxzZSwgInN5c3Rl
bSI6IGZhbHNlLCAicGFyZW50X2lkIjogbnVsbCwgImhpZGRlbiI6IGZhbHNlfV0sICJzY3JpcHRz
IjogW10sICJ0eXBlcyI6IFtdLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbeyJ1dWlkIjogIjg1
NTE1MDY2LTFmM2EtNGI1OC05ZWVmLWUxZTE4ZDYxOTg1OCIsICJleHBvcnRfa2V5IjogImF0dGFj
aG1lbnRfY29udmVyc2lvbiIsICJuYW1lIjogIkF0dGFjaG1lbnQgQ29udmVyc2lvbiIsICJkZXN0
aW5hdGlvbl90eXBlIjogMCwgInByb2dyYW1tYXRpY19uYW1lIjogImF0dGFjaG1lbnRfY29udmVy
c2lvbiIsICJleHBlY3RfYWNrIjogdHJ1ZSwgInVzZXJzIjogWyJnZXJhbGQudHJvdG1hbkBpYm0u
Y29tIl19XSwgImluY2lkZW50X2FydGlmYWN0X3R5cGVzIjogW10sICJyb2xlcyI6IFtdLCAiZmll
bGRzIjogW3sib3BlcmF0aW9ucyI6IFtdLCAicmVhZF9vbmx5IjogdHJ1ZSwgIm5hbWUiOiAiaW5j
X3RyYWluaW5nIiwgInRlbXBsYXRlcyI6IFtdLCAidHlwZV9pZCI6IDAsICJjaG9zZW4iOiBmYWxz
ZSwgInRleHQiOiAiU2ltdWxhdGlvbiIsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxz
ZSwgImV4cG9ydF9rZXkiOiAiaW5jaWRlbnQvaW5jX3RyYWluaW5nIiwgInRvb2x0aXAiOiAiV2hl
dGhlciB0aGUgaW5jaWRlbnQgaXMgYSBzaW11bGF0aW9uIG9yIGEgcmVndWxhciBpbmNpZGVudC4g
IFRoaXMgZmllbGQgaXMgcmVhZC1vbmx5LiIsICJyaWNoX3RleHQiOiBmYWxzZSwgIm9wZXJhdGlv
bl9wZXJtcyI6IHt9LCAicHJlZml4IjogbnVsbCwgImludGVybmFsIjogZmFsc2UsICJ2YWx1ZXMi
OiBbXSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJib29sZWFuIiwgImNo
YW5nZWFibGUiOiB0cnVlLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzcsICJ1
dWlkIjogImMzZjBlM2VkLTIxZTEtNGQ1My1hZmZiLWZlNWNhMzMwOGNjYSJ9LCB7Im9wZXJhdGlv
bnMiOiBbXSwgInR5cGVfaWQiOiAxMSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJp
bmNpZGVudF9pZCIsICJibGFua19vcHRpb24iOiBmYWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFu
Z2VhYmxlIjogdHJ1ZSwgImlkIjogMTE1LCAicmVhZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogImVh
ZDIxNGMyLTEzZmUtNDNmNi1hM2M3LTY3NmE4ODMzOGRiYiIsICJjaG9zZW4iOiBmYWxzZSwgImlu
cHV0X3R5cGUiOiAibnVtYmVyIiwgInRvb2x0aXAiOiAiIiwgImludGVybmFsIjogZmFsc2UsICJy
aWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0
aW9uL2luY2lkZW50X2lkIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRl
ciI6ICIiLCAibmFtZSI6ICJpbmNpZGVudF9pZCIsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIi
OiBmYWxzZSwgInZhbHVlcyI6IFtdfV0sICJvdmVycmlkZXMiOiBbXSwgImV4cG9ydF9kYXRlIjog
MTUzNzE3MDI2NTE3Mn0=
"""
    )
