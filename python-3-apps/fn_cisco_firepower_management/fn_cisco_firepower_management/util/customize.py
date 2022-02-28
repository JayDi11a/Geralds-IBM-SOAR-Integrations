# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_cisco_firepower_management"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_cisco_firepower_management package"""
    reload_params = {"package": u"fn_cisco_firepower_management",
                    "incident_fields": [], 
                    "action_fields": [u"access_control_policy_name", u"access_rule_name", u"destination_ip", u"enable", u"policy_action", u"rule_action", u"source_ip"], 
                    "function_params": [u"access_control_policy_name", u"access_rule_name", u"destination_ip", u"enable", u"policy_action", u"rule_action", u"source_ip"], 
                    "datatables": [], 
                    "message_destinations": [u"cisco_firepower_management_center"], 
                    "functions": [u"cisco_fmc_create_access_control_policy_rule"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [u"example_cisco_fmc_create_access_control_policy_rule"], 
                    "actions": [u"Example: Cisco FMC Create Access Control Policy Rule"], 
                    "incident_artifact_types": [] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Action fields:
    #     access_control_policy_name
    #     access_rule_name
    #     destination_ip
    #     enable
    #     policy_action
    #     rule_action
    #     source_ip
    #   Function inputs:
    #     access_control_policy_name
    #     access_rule_name
    #     destination_ip
    #     enable
    #     policy_action
    #     rule_action
    #     source_ip
    #   Message Destinations:
    #     cisco_firepower_management_center
    #   Functions:
    #     cisco_fmc_create_access_control_policy_rule
    #   Workflows:
    #     example_cisco_fmc_create_access_control_policy_rule
    #   Rules:
    #     Example: Cisco FMC Create Access Control Policy Rule


    yield ImportDefinition(u"""
eyJhY3Rpb25fb3JkZXIiOiBbXSwgImFjdGlvbnMiOiBbeyJhdXRvbWF0aW9ucyI6IFtdLCAiY29u
ZGl0aW9ucyI6IFtdLCAiZW5hYmxlZCI6IHRydWUsICJleHBvcnRfa2V5IjogIkV4YW1wbGU6IENp
c2NvIEZNQyBDcmVhdGUgQWNjZXNzIENvbnRyb2wgUG9saWN5IFJ1bGUiLCAiaWQiOiAxOTYsICJs
b2dpY190eXBlIjogImFsbCIsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtdLCAibmFtZSI6ICJF
eGFtcGxlOiBDaXNjbyBGTUMgQ3JlYXRlIEFjY2VzcyBDb250cm9sIFBvbGljeSBSdWxlIiwgIm9i
amVjdF90eXBlIjogImFydGlmYWN0IiwgInRhZ3MiOiBbXSwgInRpbWVvdXRfc2Vjb25kcyI6IDg2
NDAwLCAidHlwZSI6IDEsICJ1dWlkIjogIjUyMzZjODQyLTRjOTctNGI4ZS1hNzZlLWM1MzhkYWFk
MGQ5YiIsICJ2aWV3X2l0ZW1zIjogW3siY29udGVudCI6ICJiNzU4NzUxMy03MWEzLTRiN2EtYTRl
MC00ZTNiNjdmNmY5ZmEiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAi
YWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBm
YWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjkxZjAzMzMyLTFkYTYtNDM4
ZC1iZGVmLTgyOWVkMjJlOWIxMCIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlw
ZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRl
ciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiYTkyMDNjNDYtYTg4
Mi00YmU4LWFkMDAtYjg1MzY2ZTRlZmI5IiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVs
ZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtf
aGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICIxMThiOTcw
NC1kMGQ2LTQ1MjgtYWMzOS1lMDJkNDJkNGNkNTUiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwg
ImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3df
bGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjJm
Yzk3YTBmLTBjOTItNGFhYy1iZWMwLWI2ZWQ4MGQzYTBmMiIsICJlbGVtZW50IjogImZpZWxkX3V1
aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAi
c2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQi
OiAiODY0YTM2NjAtYmFiNy00Mzk5LTljZDEtNDdiODg5OGI5NzdkIiwgImVsZW1lbnQiOiAiZmll
bGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51
bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29u
dGVudCI6ICIzZDQ5YmI0Zi1jMmEwLTRlNDEtYWViNC00ZWNmZjQ1NjA5Y2UiLCAiZWxlbWVudCI6
ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lm
IjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfV0s
ICJ3b3JrZmxvd3MiOiBbImV4YW1wbGVfY2lzY29fZm1jX2NyZWF0ZV9hY2Nlc3NfY29udHJvbF9w
b2xpY3lfcnVsZSJdfV0sICJhcHBzIjogW10sICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgImV4cG9y
dF9kYXRlIjogMTYwNzM3MjEyMjE4NCwgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6IDIsICJmaWVs
ZHMiOiBbeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxz
ZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFs
c2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxz
ZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9lbmFibGUiLCAiaGlkZV9ub3RpZmljYXRpb24i
OiBmYWxzZSwgImlkIjogODA1LCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogZmFs
c2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogImVuYWJsZSIsICJvcGVyYXRpb25fcGVy
bXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiBu
dWxsLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbXSwg
InRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJlbmFibGUiLCAidG9vbHRpcCI6ICIiLCAidHlwZV9p
ZCI6IDExLCAidXVpZCI6ICI4Yjg1ZDY2MC1hMjk4LTRiNDUtOTlmMC0yYmZjNDUzNTI2ZmYiLCAi
dmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlv
biI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9z
ZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRl
ZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL3BvbGljeV9hY3Rpb24iLCAiaGlk
ZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogODE0LCAiaW5wdXRfdHlwZSI6ICJzZWxlY3Qi
LCAiaW50ZXJuYWwiOiBmYWxzZSwgImlzX3RyYWNrZWQiOiBmYWxzZSwgIm5hbWUiOiAicG9saWN5
X2FjdGlvbiIsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgInBsYWNl
aG9sZGVyIjogIiIsICJwcmVmaXgiOiBudWxsLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3Rl
eHQiOiBmYWxzZSwgInRhZ3MiOiBbXSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJwb2xpY3lf
YWN0aW9uIiwgInRvb2x0aXAiOiAiIiwgInR5cGVfaWQiOiAxMSwgInV1aWQiOiAiMGRiYTAyZjct
MGY2Yy00ZGZkLTlmYjAtNzE4YjAyNTU0Y2U2IiwgInZhbHVlcyI6IFt7ImRlZmF1bHQiOiB0cnVl
LCAiZW5hYmxlZCI6IHRydWUsICJoaWRkZW4iOiBmYWxzZSwgImxhYmVsIjogIkJMT0NLIiwgInBy
b3BlcnRpZXMiOiBudWxsLCAidXVpZCI6ICI2M2FjNzIwMC05NmQ4LTRjZjctOTVhNS1iYmY0OTIw
ZDVlODYiLCAidmFsdWUiOiA0Mjh9LCB7ImRlZmF1bHQiOiBmYWxzZSwgImVuYWJsZWQiOiB0cnVl
LCAiaGlkZGVuIjogZmFsc2UsICJsYWJlbCI6ICJBTExPVyIsICJwcm9wZXJ0aWVzIjogbnVsbCwg
InV1aWQiOiAiY2I4NzNkMzgtMzA1MS00YWE2LWI5NDktYjBjYzlmMWQzZTA4IiwgInZhbHVlIjog
NDMzfSwgeyJkZWZhdWx0IjogZmFsc2UsICJlbmFibGVkIjogdHJ1ZSwgImhpZGRlbiI6IGZhbHNl
LCAibGFiZWwiOiAiVFJVU1QiLCAicHJvcGVydGllcyI6IG51bGwsICJ1dWlkIjogImIyYmU3YWI4
LWU0OGItNGEyMi05MjQzLTFmM2YxZmM5NjE3NiIsICJ2YWx1ZSI6IDQzNH0sIHsiZGVmYXVsdCI6
IGZhbHNlLCAiZW5hYmxlZCI6IHRydWUsICJoaWRkZW4iOiBmYWxzZSwgImxhYmVsIjogIk1PTklU
T1IiLCAicHJvcGVydGllcyI6IG51bGwsICJ1dWlkIjogImRhMzBmMWIwLTUzOGUtNDEwMi1hMmI2
LTQ0OWEwMTI4NjZjMyIsICJ2YWx1ZSI6IDQzNX1dfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjog
ZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5n
ZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIi
OiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9y
dWxlX2FjdGlvbiIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiA4MTYsICJpbnB1
dF90eXBlIjogInNlbGVjdCIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNl
LCAibmFtZSI6ICJydWxlX2FjdGlvbiIsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgIm9wZXJhdGlv
bnMiOiBbXSwgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiBudWxsLCAicmVhZF9vbmx5Ijog
ZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbXSwgInRlbXBsYXRlcyI6IFtdLCAi
dGV4dCI6ICJydWxlX2FjdGlvbiIsICJ0b29sdGlwIjogIiIsICJ0eXBlX2lkIjogMTEsICJ1dWlk
IjogImQzNGFmOGFjLWVjMWQtNDRiNC1iNTdmLWVmN2E2MmEyNDI4NCIsICJ2YWx1ZXMiOiBbeyJk
ZWZhdWx0IjogdHJ1ZSwgImVuYWJsZWQiOiB0cnVlLCAiaGlkZGVuIjogZmFsc2UsICJsYWJlbCI6
ICJCTE9DSyIsICJwcm9wZXJ0aWVzIjogbnVsbCwgInV1aWQiOiAiNDQ1ZDMzNzQtZmYzYi00MTdh
LWE2MzctZjFhMTcyZWM1ZjMwIiwgInZhbHVlIjogNDI5fSwgeyJkZWZhdWx0IjogZmFsc2UsICJl
bmFibGVkIjogdHJ1ZSwgImhpZGRlbiI6IGZhbHNlLCAibGFiZWwiOiAiQUxMT1ciLCAicHJvcGVy
dGllcyI6IG51bGwsICJ1dWlkIjogImZhZWU5ZTA0LTA2ZjAtNGQzNC05NTNiLTljODdjYThmNTRh
MiIsICJ2YWx1ZSI6IDQzMH0sIHsiZGVmYXVsdCI6IGZhbHNlLCAiZW5hYmxlZCI6IHRydWUsICJo
aWRkZW4iOiBmYWxzZSwgImxhYmVsIjogIlRSVVNUIiwgInByb3BlcnRpZXMiOiBudWxsLCAidXVp
ZCI6ICJjZWUzZjRhMi0yNjU1LTQ4NzMtOTI3OC0yYTU5YzcyMWM0OTUiLCAidmFsdWUiOiA0MzF9
LCB7ImRlZmF1bHQiOiBmYWxzZSwgImVuYWJsZWQiOiB0cnVlLCAiaGlkZGVuIjogZmFsc2UsICJs
YWJlbCI6ICJNT05JVE9SIiwgInByb3BlcnRpZXMiOiBudWxsLCAidXVpZCI6ICIyMWNmN2MzYS04
M2E3LTRmY2UtODMwMS0wMjY0MWZkNWEyN2EiLCAidmFsdWUiOiA0MzJ9XX0sIHsiYWxsb3dfZGVm
YXVsdF92YWx1ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVkIjog
ZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9z
ZW5fYnlfc2VydmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5Ijog
Il9fZnVuY3Rpb24vYWNjZXNzX3J1bGVfbmFtZSIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNl
LCAiaWQiOiA4MTUsICJpbnB1dF90eXBlIjogInRleHQiLCAiaW50ZXJuYWwiOiBmYWxzZSwgImlz
X3RyYWNrZWQiOiBmYWxzZSwgIm5hbWUiOiAiYWNjZXNzX3J1bGVfbmFtZSIsICJvcGVyYXRpb25f
cGVybXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgi
OiBudWxsLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBb
XSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJhY2Nlc3NfcnVsZV9uYW1lIiwgInRvb2x0aXAi
OiAiIiwgInR5cGVfaWQiOiAxMSwgInV1aWQiOiAiNGFlOWQ5NTYtNGExMi00MzBjLTkyMjMtZTBh
Yjg3OTIxNjRiIiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2Us
ICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUi
OiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxz
ZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9zb3VyY2Vf
aXAiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogODAxLCAiaW5wdXRfdHlwZSI6
ICJ0ZXh0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjog
InNvdXJjZV9pcCIsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgInBs
YWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiBudWxsLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNo
X3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbXSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJzb3Vy
Y2VfaXAiLCAidG9vbHRpcCI6ICIiLCAidHlwZV9pZCI6IDExLCAidXVpZCI6ICJiNjA1NDc4Zi03
MjYyLTRlNTYtYTVmOC1hMWYxMDAzNjk1NzEiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1
bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZh
bHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2Vu
X2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJf
X2Z1bmN0aW9uL2Rlc3RpbmF0aW9uX2lwIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJp
ZCI6IDgwMiwgImlucHV0X3R5cGUiOiAidGV4dCIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJh
Y2tlZCI6IGZhbHNlLCAibmFtZSI6ICJkZXN0aW5hdGlvbl9pcCIsICJvcGVyYXRpb25fcGVybXMi
OiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiBudWxs
LCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbXSwgInRl
bXBsYXRlcyI6IFtdLCAidGV4dCI6ICJkZXN0aW5hdGlvbl9pcCIsICJ0b29sdGlwIjogIiIsICJ0
eXBlX2lkIjogMTEsICJ1dWlkIjogIjgwYzk2YjQ3LTBmNTgtNDQ5YS04NDJhLWFhNDhjYjc4YWU0
MiIsICJ2YWx1ZXMiOiBbXX0sIHsiYWxsb3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAiYmxhbmtf
b3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwg
ImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJkZXBy
ZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vYWNjZXNzX2NvbnRyb2xf
cG9saWN5X25hbWUiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogODAwLCAiaW5w
dXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2Us
ICJuYW1lIjogImFjY2Vzc19jb250cm9sX3BvbGljeV9uYW1lIiwgIm9wZXJhdGlvbl9wZXJtcyI6
IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGws
ICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFtdLCAidGVt
cGxhdGVzIjogW10sICJ0ZXh0IjogImFjY2Vzc19jb250cm9sX3BvbGljeV9uYW1lIiwgInRvb2x0
aXAiOiAiIiwgInR5cGVfaWQiOiAxMSwgInV1aWQiOiAiZDVmYTNmMTgtYWFjNC00Y2ZkLWIzNGUt
MDJiZTZlYTY0OTE2IiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFs
c2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFi
bGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBm
YWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiYWN0aW9uaW52b2NhdGlv
bi9kZXN0aW5hdGlvbl9pcCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiA4MDgs
ICJpbnB1dF90eXBlIjogInRleHQiLCAiaW50ZXJuYWwiOiBmYWxzZSwgImlzX3RyYWNrZWQiOiBm
YWxzZSwgIm5hbWUiOiAiZGVzdGluYXRpb25faXAiLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJv
cGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIiLCAicHJlZml4IjogInByb3BlcnRpZXMi
LCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbXSwgInRl
bXBsYXRlcyI6IFtdLCAidGV4dCI6ICJEZXN0aW5hdGlvbiBJUCIsICJ0b29sdGlwIjogIiIsICJ0
eXBlX2lkIjogNiwgInV1aWQiOiAiYTkyMDNjNDYtYTg4Mi00YmU4LWFkMDAtYjg1MzY2ZTRlZmI5
IiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19v
cHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAi
Y2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJl
Y2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiYWN0aW9uaW52b2NhdGlvbi9hY2Nlc3NfY29u
dHJvbF9wb2xpY3lfbmFtZSIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiA4MDYs
ICJpbnB1dF90eXBlIjogInRleHQiLCAiaW50ZXJuYWwiOiBmYWxzZSwgImlzX3RyYWNrZWQiOiBm
YWxzZSwgIm5hbWUiOiAiYWNjZXNzX2NvbnRyb2xfcG9saWN5X25hbWUiLCAib3BlcmF0aW9uX3Bl
cm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIiLCAicHJlZml4Ijog
InByb3BlcnRpZXMiLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRh
Z3MiOiBbXSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJBY2Nlc3MgQ29udHJvbCBQb2xpY3kg
TmFtZSIsICJ0b29sdGlwIjogIiIsICJ0eXBlX2lkIjogNiwgInV1aWQiOiAiYjc1ODc1MTMtNzFh
My00YjdhLWE0ZTAtNGUzYjY3ZjZmOWZhIiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0
X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxz
ZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9i
eV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiYWN0
aW9uaW52b2NhdGlvbi9hY2Nlc3NfcnVsZV9uYW1lIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFs
c2UsICJpZCI6IDgxMSwgImlucHV0X3R5cGUiOiAidGV4dCIsICJpbnRlcm5hbCI6IGZhbHNlLCAi
aXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJhY2Nlc3NfcnVsZV9uYW1lIiwgIm9wZXJhdGlv
bl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZp
eCI6ICJwcm9wZXJ0aWVzIiwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2Us
ICJ0YWdzIjogW10sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAiQWNjZXNzIFJ1bGUgTmFtZSIs
ICJ0b29sdGlwIjogIiIsICJ0eXBlX2lkIjogNiwgInV1aWQiOiAiMmZjOTdhMGYtMGM5Mi00YWFj
LWJlYzAtYjZlZDgwZDNhMGYyIiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVl
IjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNo
YW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2
ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiYWN0aW9uaW52
b2NhdGlvbi9wb2xpY3lfYWN0aW9uIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6
IDgxMiwgImlucHV0X3R5cGUiOiAic2VsZWN0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFj
a2VkIjogZmFsc2UsICJuYW1lIjogInBvbGljeV9hY3Rpb24iLCAib3BlcmF0aW9uX3Blcm1zIjog
e30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIiLCAicHJlZml4IjogInByb3Bl
cnRpZXMiLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBb
XSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJQb2xpY3kgQWN0aW9uIiwgInRvb2x0aXAiOiAi
IiwgInR5cGVfaWQiOiA2LCAidXVpZCI6ICIxMThiOTcwNC1kMGQ2LTQ1MjgtYWMzOS1lMDJkNDJk
NGNkNTUiLCAidmFsdWVzIjogW3siZGVmYXVsdCI6IHRydWUsICJlbmFibGVkIjogdHJ1ZSwgImhp
ZGRlbiI6IGZhbHNlLCAibGFiZWwiOiAiQkxPQ0siLCAicHJvcGVydGllcyI6IG51bGwsICJ1dWlk
IjogIjViZjI4NjQ0LTc0NWItNDJjMC04ZDIwLTY4ZjBjMWMyZDg2YSIsICJ2YWx1ZSI6IDQyNn0s
IHsiZGVmYXVsdCI6IGZhbHNlLCAiZW5hYmxlZCI6IHRydWUsICJoaWRkZW4iOiBmYWxzZSwgImxh
YmVsIjogIkFMTE9XIiwgInByb3BlcnRpZXMiOiBudWxsLCAidXVpZCI6ICJkM2M2NjlhMy1kZmY1
LTQ3NjUtYjYxMS0wOTg3ODM4NGY0M2UiLCAidmFsdWUiOiA0MzZ9LCB7ImRlZmF1bHQiOiBmYWxz
ZSwgImVuYWJsZWQiOiB0cnVlLCAiaGlkZGVuIjogZmFsc2UsICJsYWJlbCI6ICJUUlVTVCIsICJw
cm9wZXJ0aWVzIjogbnVsbCwgInV1aWQiOiAiY2QwNmRiZTAtMjRiNy00MDI5LTliMzMtZjQzZDFj
MTVjODQ0IiwgInZhbHVlIjogNDM3fSwgeyJkZWZhdWx0IjogZmFsc2UsICJlbmFibGVkIjogdHJ1
ZSwgImhpZGRlbiI6IGZhbHNlLCAibGFiZWwiOiAiTU9OSVRPUiIsICJwcm9wZXJ0aWVzIjogbnVs
bCwgInV1aWQiOiAiZGQ4NmRhYTEtMjczOC00OTM1LTkzODAtNWYxZDY2NDc2M2U1IiwgInZhbHVl
IjogNDM4fV19LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6
IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4i
OiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6
IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJhY3Rpb25pbnZvY2F0aW9uL3J1bGVfYWN0aW9uIiwgImhp
ZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDgxMywgImlucHV0X3R5cGUiOiAic2VsZWN0
IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInJ1bGVf
YWN0aW9uIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vo
b2xkZXIiOiAiIiwgInByZWZpeCI6ICJwcm9wZXJ0aWVzIiwgInJlYWRfb25seSI6IGZhbHNlLCAi
cmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW10sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAi
UnVsZSBBY3Rpb24iLCAidG9vbHRpcCI6ICIiLCAidHlwZV9pZCI6IDYsICJ1dWlkIjogIjg2NGEz
NjYwLWJhYjctNDM5OS05Y2QxLTQ3Yjg4OThiOTc3ZCIsICJ2YWx1ZXMiOiBbeyJkZWZhdWx0Ijog
dHJ1ZSwgImVuYWJsZWQiOiB0cnVlLCAiaGlkZGVuIjogZmFsc2UsICJsYWJlbCI6ICJCTE9DSyIs
ICJwcm9wZXJ0aWVzIjogbnVsbCwgInV1aWQiOiAiOTBlYTE1MDktMTc0MS00NTRhLWI3YjgtN2Nm
NDc1ZjliMmRiIiwgInZhbHVlIjogNDI3fSwgeyJkZWZhdWx0IjogZmFsc2UsICJlbmFibGVkIjog
dHJ1ZSwgImhpZGRlbiI6IGZhbHNlLCAibGFiZWwiOiAiQUxMT1ciLCAicHJvcGVydGllcyI6IG51
bGwsICJ1dWlkIjogIjFmMzRlNjY0LThhNjAtNGQzOS1hMmNkLWQzYmNmMDhkOGMyZiIsICJ2YWx1
ZSI6IDQzOX0sIHsiZGVmYXVsdCI6IGZhbHNlLCAiZW5hYmxlZCI6IHRydWUsICJoaWRkZW4iOiBm
YWxzZSwgImxhYmVsIjogIlRSVVNUIiwgInByb3BlcnRpZXMiOiBudWxsLCAidXVpZCI6ICJlMjM5
MzNlZi01MzliLTQ2NWQtODNhMy0wZjRjZjgzYjYzNmEiLCAidmFsdWUiOiA0NDB9LCB7ImRlZmF1
bHQiOiBmYWxzZSwgImVuYWJsZWQiOiB0cnVlLCAiaGlkZGVuIjogZmFsc2UsICJsYWJlbCI6ICJN
T05JVE9SIiwgInByb3BlcnRpZXMiOiBudWxsLCAidXVpZCI6ICI5MDA0ZjVmOC00MjBjLTRlYTkt
ODk2MC1hNGUzNWQ1ZTc3ZWMiLCAidmFsdWUiOiA0NDF9XX0sIHsiYWxsb3dfZGVmYXVsdF92YWx1
ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJj
aGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2Vy
dmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogImFjdGlvbmlu
dm9jYXRpb24vZW5hYmxlIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDgxMCwg
ImlucHV0X3R5cGUiOiAic2VsZWN0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjog
ZmFsc2UsICJuYW1lIjogImVuYWJsZSIsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgIm9wZXJhdGlv
bnMiOiBbXSwgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiAicHJvcGVydGllcyIsICJyZWFk
X29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFtdLCAidGVtcGxhdGVz
IjogW10sICJ0ZXh0IjogIkVuYWJsZSIsICJ0b29sdGlwIjogIiIsICJ0eXBlX2lkIjogNiwgInV1
aWQiOiAiM2Q0OWJiNGYtYzJhMC00ZTQxLWFlYjQtNGVjZmY0NTYwOWNlIiwgInZhbHVlcyI6IFt7
ImRlZmF1bHQiOiB0cnVlLCAiZW5hYmxlZCI6IHRydWUsICJoaWRkZW4iOiBmYWxzZSwgImxhYmVs
IjogInRydWUiLCAicHJvcGVydGllcyI6IG51bGwsICJ1dWlkIjogIjFmNzdkMGQzLTkzNzMtNDI2
MC1hZmQyLTBiOTRmOWRlYTM5OSIsICJ2YWx1ZSI6IDQyNH0sIHsiZGVmYXVsdCI6IGZhbHNlLCAi
ZW5hYmxlZCI6IHRydWUsICJoaWRkZW4iOiBmYWxzZSwgImxhYmVsIjogImZhbHNlIiwgInByb3Bl
cnRpZXMiOiBudWxsLCAidXVpZCI6ICIzMjYxZmMyMy02NmZlLTRhNmQtYjY1Ny1jZDk3NjE5MDEz
YzgiLCAidmFsdWUiOiA0MjV9XX0sIHsiYWxsb3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAiYmxh
bmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1
ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJk
ZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogImFjdGlvbmludm9jYXRpb24vc291cmNl
X2lwIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDgwNywgImlucHV0X3R5cGUi
OiAidGV4dCIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6
ICJzb3VyY2VfaXAiLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJw
bGFjZWhvbGRlciI6ICIiLCAicHJlZml4IjogInByb3BlcnRpZXMiLCAicmVhZF9vbmx5IjogZmFs
c2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbXSwgInRlbXBsYXRlcyI6IFtdLCAidGV4
dCI6ICJTb3VyY2UgSVAiLCAidG9vbHRpcCI6ICIiLCAidHlwZV9pZCI6IDYsICJ1dWlkIjogIjkx
ZjAzMzMyLTFkYTYtNDM4ZC1iZGVmLTgyOWVkMjJlOWIxMCIsICJ2YWx1ZXMiOiBbXX0sIHsiYWxs
b3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxh
dGVkIjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVs
dF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRf
a2V5IjogImluY2lkZW50L2luY190cmFpbmluZyIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNl
LCAiaWQiOiA1MSwgImlucHV0X3R5cGUiOiAiYm9vbGVhbiIsICJpbnRlcm5hbCI6IGZhbHNlLCAi
aXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJpbmNfdHJhaW5pbmciLCAib3BlcmF0aW9uX3Bl
cm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJwcmVmaXgiOiBudWxsLCAicmVhZF9vbmx5Ijog
dHJ1ZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFtdLCAidGVtcGxhdGVzIjogW10sICJ0
ZXh0IjogIlNpbXVsYXRpb24iLCAidG9vbHRpcCI6ICJXaGV0aGVyIHRoZSBpbmNpZGVudCBpcyBh
IHNpbXVsYXRpb24gb3IgYSByZWd1bGFyIGluY2lkZW50LiAgVGhpcyBmaWVsZCBpcyByZWFkLW9u
bHkuIiwgInR5cGVfaWQiOiAwLCAidXVpZCI6ICJjM2YwZTNlZC0yMWUxLTRkNTMtYWZmYi1mZTVj
YTMzMDhjY2EiLCAidmFsdWVzIjogW119XSwgImZ1bmN0aW9ucyI6IFt7ImNyZWF0b3IiOiB7ImRp
c3BsYXlfbmFtZSI6ICJHZXJhbGQgVHJvdG1hbiIsICJpZCI6IDEzLCAibmFtZSI6ICJnZXJhbGQu
dHJvdG1hbkBpYm0uY29tIiwgInR5cGUiOiAidXNlciJ9LCAiZGVzY3JpcHRpb24iOiB7ImZvcm1h
dCI6ICJ0ZXh0IiwgImNvbnRlbnQiOiAiVGhpcyBmdW5jdGlvbiBhbGxvd3MgeW91IHRvIHNwZWNp
ZnkgYSBnaXZlbiBBY2Nlc3MgQ29udHJvbCBQb2xpY3kgYW5kIGNyZWF0ZXMgYW4gQWNjZXNzIFJ1
bGUgd2l0aGluIGl0LiBOb3RlIHRoYXQgaXQgYXNzdW1lcyB0aGUgQWNjZXNzIENvbnRyb2wgUG9s
aWN5IGhhcyBhbHJlYWR5IGJlZW4gY3JlYXRlZCBhbmQgaXQgb25seSBjcmVhdGVzIEFjY2VzcyBS
dWxlcyJ9LCAiZGVzdGluYXRpb25faGFuZGxlIjogImNpc2NvX2ZpcmVwb3dlcl9tYW5hZ2VtZW50
X2NlbnRlciIsICJkaXNwbGF5X25hbWUiOiAiQ2lzY28gRk1DOiBDcmVhdGUgQWNjZXNzIENvbnRy
b2wgUG9saWN5IFJ1bGUiLCAiZXhwb3J0X2tleSI6ICJjaXNjb19mbWNfY3JlYXRlX2FjY2Vzc19j
b250cm9sX3BvbGljeV9ydWxlIiwgImlkIjogMTQ0LCAibGFzdF9tb2RpZmllZF9ieSI6IHsiZGlz
cGxheV9uYW1lIjogIkdlcmFsZCBUcm90bWFuIiwgImlkIjogMTMsICJuYW1lIjogImdlcmFsZC50
cm90bWFuQGlibS5jb20iLCAidHlwZSI6ICJ1c2VyIn0sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAx
NjA3MzcwNjQ2NTI4LCAibmFtZSI6ICJjaXNjb19mbWNfY3JlYXRlX2FjY2Vzc19jb250cm9sX3Bv
bGljeV9ydWxlIiwgInRhZ3MiOiBbXSwgInV1aWQiOiAiN2E0ZDVhZjYtMDkwZS00NzFlLWI2YTMt
ZDUxN2M1YThkYjc3IiwgInZlcnNpb24iOiA1LCAidmlld19pdGVtcyI6IFt7ImNvbnRlbnQiOiAi
ZDVmYTNmMTgtYWFjNC00Y2ZkLWIzNGUtMDJiZTZlYTY0OTE2IiwgImVsZW1lbnQiOiAiZmllbGRf
dXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93
X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICJi
NjA1NDc4Zi03MjYyLTRlNTYtYTVmOC1hMWYxMDAzNjk1NzEiLCAiZWxlbWVudCI6ICJmaWVsZF91
dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3df
bGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjgw
Yzk2YjQ3LTBmNTgtNDQ5YS04NDJhLWFhNDhjYjc4YWU0MiIsICJlbGVtZW50IjogImZpZWxkX3V1
aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19s
aW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiMGRi
YTAyZjctMGY2Yy00ZGZkLTlmYjAtNzE4YjAyNTU0Y2U2IiwgImVsZW1lbnQiOiAiZmllbGRfdXVp
ZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xp
bmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICI0YWU5
ZDk1Ni00YTEyLTQzMGMtOTIyMy1lMGFiODc5MjE2NGIiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlk
IiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlu
a19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogImQzNGFm
OGFjLWVjMWQtNDRiNC1iNTdmLWVmN2E2MmEyNDI4NCIsICJlbGVtZW50IjogImZpZWxkX3V1aWQi
LCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5r
X2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiOGI4NWQ2
NjAtYTI5OC00YjQ1LTk5ZjAtMmJmYzQ1MzUyNmZmIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIs
ICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtf
aGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH1dLCAid29ya2Zsb3dzIjogW3siYWN0
aW9ucyI6IFtdLCAiZGVzY3JpcHRpb24iOiBudWxsLCAibmFtZSI6ICJFeGFtcGxlOiBDaXNjbyBG
TUMgQ3JlYXRlIEFjY2VzcyBDb250cm9sIFBvbGljeSBSdWxlIiwgIm9iamVjdF90eXBlIjogImFy
dGlmYWN0IiwgInByb2dyYW1tYXRpY19uYW1lIjogImV4YW1wbGVfY2lzY29fZm1jX2NyZWF0ZV9h
Y2Nlc3NfY29udHJvbF9wb2xpY3lfcnVsZSIsICJ0YWdzIjogW10sICJ1dWlkIjogbnVsbCwgIndv
cmtmbG93X2lkIjogMTc3fV19XSwgImdlb3MiOiBudWxsLCAiZ3JvdXBzIjogbnVsbCwgImlkIjog
MTksICJpbmJvdW5kX21haWxib3hlcyI6IG51bGwsICJpbmNpZGVudF9hcnRpZmFjdF90eXBlcyI6
IFtdLCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJ1cGRhdGVfZGF0ZSI6IDE2MDczNzIxODg4NzAsICJj
cmVhdGVfZGF0ZSI6IDE2MDczNzIxODg4NzAsICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1h
ZDM5LTRhMDAwNDA0NGFhMCIsICJkZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2Vz
IChpbnRlcm5hbCkiLCAiZXhwb3J0X2tleSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRl
cm5hbCkiLCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZW5h
YmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJwYXJlbnRfaWQiOiBudWxsLCAiaGlkZGVu
IjogZmFsc2UsICJpZCI6IDB9XSwgImluZHVzdHJpZXMiOiBudWxsLCAibGF5b3V0cyI6IFtdLCAi
bG9jYWxlIjogbnVsbCwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW3siYXBpX2tleXMiOiBbImQ5
NGZjMDI2LTAzZTktNGY1ZC1iZDQ3LWQ4MDgwMTQ0NTZjYiJdLCAiZGVzdGluYXRpb25fdHlwZSI6
IDAsICJleHBlY3RfYWNrIjogdHJ1ZSwgImV4cG9ydF9rZXkiOiAiY2lzY29fZmlyZXBvd2VyX21h
bmFnZW1lbnRfY2VudGVyIiwgIm5hbWUiOiAiQ2lzY28gRmlyZXBvd2VyIE1hbmFnZW1lbnQgQ2Vu
dGVyIiwgInByb2dyYW1tYXRpY19uYW1lIjogImNpc2NvX2ZpcmVwb3dlcl9tYW5hZ2VtZW50X2Nl
bnRlciIsICJ0YWdzIjogW10sICJ1c2VycyI6IFsiZ2VyYWxkLnRyb3RtYW5AaWJtLmNvbSJdLCAi
dXVpZCI6ICI1NDQ3M2U0MC1kODQ3LTRlOWMtYjdjMy1hZDAwMTM3ODhjNDkifV0sICJub3RpZmlj
YXRpb25zIjogbnVsbCwgIm92ZXJyaWRlcyI6IFtdLCAicGhhc2VzIjogW10sICJyZWd1bGF0b3Jz
IjogbnVsbCwgInJvbGVzIjogW10sICJzY3JpcHRzIjogW10sICJzZXJ2ZXJfdmVyc2lvbiI6IHsi
YnVpbGRfbnVtYmVyIjogNzYsICJtYWpvciI6IDM2LCAibWlub3IiOiAyLCAidmVyc2lvbiI6ICIz
Ni4yLjc2In0sICJ0YWdzIjogW10sICJ0YXNrX29yZGVyIjogW10sICJ0aW1lZnJhbWVzIjogbnVs
bCwgInR5cGVzIjogW10sICJ3b3JrZmxvd3MiOiBbeyJhY3Rpb25zIjogW10sICJjb250ZW50Ijog
eyJ2ZXJzaW9uIjogMTIsICJ3b3JrZmxvd19pZCI6ICJleGFtcGxlX2Npc2NvX2ZtY19jcmVhdGVf
YWNjZXNzX2NvbnRyb2xfcG9saWN5X3J1bGUiLCAieG1sIjogIjw/eG1sIHZlcnNpb249XCIxLjBc
IiBlbmNvZGluZz1cIlVURi04XCI/PjxkZWZpbml0aW9ucyB4bWxucz1cImh0dHA6Ly93d3cub21n
Lm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvTU9ERUxcIiB4bWxuczpicG1uZGk9XCJodHRwOi8vd3d3
Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L0RJXCIgeG1sbnM6b21nZGM9XCJodHRwOi8vd3d3
Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9EQ1wiIHhtbG5zOm9tZ2RpPVwiaHR0cDovL3d3dy5v
bWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRElcIiB4bWxuczpyZXNpbGllbnQ9XCJodHRwOi8vcmVz
aWxpZW50LmlibS5jb20vYnBtblwiIHhtbG5zOnhzZD1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEv
WE1MU2NoZW1hXCIgeG1sbnM6eHNpPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEt
aW5zdGFuY2VcIiB0YXJnZXROYW1lc3BhY2U9XCJodHRwOi8vd3d3LmNhbXVuZGEub3JnL3Rlc3Rc
Ij48cHJvY2VzcyBpZD1cImV4YW1wbGVfY2lzY29fZm1jX2NyZWF0ZV9hY2Nlc3NfY29udHJvbF9w
b2xpY3lfcnVsZVwiIGlzRXhlY3V0YWJsZT1cInRydWVcIiBuYW1lPVwiRXhhbXBsZTogQ2lzY28g
Rk1DIENyZWF0ZSBBY2Nlc3MgQ29udHJvbCBQb2xpY3kgUnVsZVwiPjxkb2N1bWVudGF0aW9uPlRo
aXMgZXhhbXBsZSB3b3JrIGZsb3cgY2FsbHMgdGhlIENpc2NvIEZpcmVwb3dlciBNYW5hZ2VtZW50
IENlbnRlciBBUEkgZW5kcG9pbnQsIG1ha2VzIHRoZSBhdXRoZW50aWNhdGlvbiBhbmQgdGhlbiBn
aXZlcyB5b3UgdGhlIG9wcG9ydHVuaXR5IHRvIHNwZWNpZnkgdGhlIGFjY2VzcyBjb250cm9sIHBv
bGljeSB0byB0aGVuIGNyZWF0ZSBhIG5ldHdvcmsgc3BlY2lmaWMgcnVsZSBmb3IuIFlvdSBjYW4g
c3BlY2lmeSB0aGUgc291cmNlIGFuZCBkZXN0aW5hdGlvbiBJUCwgdGhlIGFjdGlvbiB0eXBlLCBh
bmQgd2hldGhlciB0byB0dXJuIHRoZSBwb2xpY3kgb24gb3Igb2ZmLjwvZG9jdW1lbnRhdGlvbj48
c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZs
b3dfMW5yeWNrczwvb3V0Z29pbmc+PC9zdGFydEV2ZW50PjxlbmRFdmVudCBpZD1cIkVuZEV2ZW50
XzFoNGlpNGFcIj48aW5jb21pbmc+U2VxdWVuY2VGbG93XzFqaHd0aW88L2luY29taW5nPjwvZW5k
RXZlbnQ+PHNlcnZpY2VUYXNrIGlkPVwiU2VydmljZVRhc2tfMGd6anZpcVwiIG5hbWU9XCJDaXNj
byBGTUM6IENyZWF0ZSBBY2Nlc3MgQ29udHJvbCAuLi5cIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0
aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cIjdhNGQ1
YWY2LTA5MGUtNDcxZS1iNmEzLWQ1MTdjNWE4ZGI3N1wiPntcImlucHV0c1wiOntcIjBkYmEwMmY3
LTBmNmMtNGRmZC05ZmIwLTcxOGIwMjU1NGNlNlwiOntcImlucHV0X3R5cGVcIjpcInN0YXRpY1wi
LFwic3RhdGljX2lucHV0XCI6e1wibXVsdGlzZWxlY3RfdmFsdWVcIjpbXSxcInNlbGVjdF92YWx1
ZVwiOlwiNjNhYzcyMDAtOTZkOC00Y2Y3LTk1YTUtYmJmNDkyMGQ1ZTg2XCJ9fSxcImQzNGFmOGFj
LWVjMWQtNDRiNC1iNTdmLWVmN2E2MmEyNDI4NFwiOntcImlucHV0X3R5cGVcIjpcInN0YXRpY1wi
LFwic3RhdGljX2lucHV0XCI6e1wibXVsdGlzZWxlY3RfdmFsdWVcIjpbXSxcInNlbGVjdF92YWx1
ZVwiOlwiNDQ1ZDMzNzQtZmYzYi00MTdhLWE2MzctZjFhMTcyZWM1ZjMwXCJ9fX0sXCJwb3N0X3By
b2Nlc3Npbmdfc2NyaXB0XCI6XCJpbmNpZGVudC5hZGROb3RlKHJlc3VsdHMudmFsdWUpXCIsXCJw
cmVfcHJvY2Vzc2luZ19zY3JpcHRcIjpcImlucHV0cy5hY2Nlc3NfY29udHJvbF9wb2xpY3lfbmFt
ZSA9IHJ1bGUucHJvcGVydGllcy5hY2Nlc3NfY29udHJvbF9wb2xpY3lfbmFtZVxcbmlucHV0cy5z
b3VyY2VfaXAgPSBydWxlLnByb3BlcnRpZXMuc291cmNlX2lwXFxuaW5wdXRzLmRlc3RpbmF0aW9u
X2lwID0gcnVsZS5wcm9wZXJ0aWVzLmRlc3RpbmF0aW9uX2lwXFxuaW5wdXRzLnBvbGljeV9hY3Rp
b24gPSBydWxlLnByb3BlcnRpZXMucG9saWN5X2FjdGlvblxcbmlucHV0cy5hY2Nlc3NfcnVsZV9u
YW1lID0gcnVsZS5wcm9wZXJ0aWVzLmFjY2Vzc19ydWxlX25hbWVcXG5pbnB1dHMucnVsZV9hY3Rp
b24gPSBydWxlLnByb3BlcnRpZXMucnVsZV9hY3Rpb25cXG5pbnB1dHMuZW5hYmxlID0gcnVsZS5w
cm9wZXJ0aWVzLmVuYWJsZVwiLFwicmVzdWx0X25hbWVcIjpcIlwifTwvcmVzaWxpZW50OmZ1bmN0
aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18xbnJ5Y2tzPC9p
bmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzFqaHd0aW88L291dGdvaW5nPjwvc2Vydmlj
ZVRhc2s+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xbnJ5Y2tzXCIgc291cmNlUmVm
PVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMGd6anZpcVwi
Lz48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzFqaHd0aW9cIiBzb3VyY2VSZWY9XCJT
ZXJ2aWNlVGFza18wZ3pqdmlxXCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMWg0aWk0YVwiLz48dGV4
dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+U3RhcnQgeW91
ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwi
QXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRh
cmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PC9wcm9jZXNzPjxicG1uZGk6QlBN
TkRpYWdyYW0gaWQ9XCJCUE1ORGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1OUGxhbmUgYnBtbkVsZW1l
bnQ9XCJ1bmRlZmluZWRcIiBpZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5kaTpCUE1OU2hhcGUgYnBt
bkVsZW1lbnQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bV9k
aVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjE2MlwiIHk9
XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIwXCIgd2lk
dGg9XCI5MFwiIHg9XCIxNTdcIiB5PVwiMjIzXCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5k
aTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlv
bl8xa3h4aXl0XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0X2RpXCI+PG9tZ2RjOkJvdW5k
cyBoZWlnaHQ9XCIzMFwiIHdpZHRoPVwiMTAwXCIgeD1cIjk5XCIgeT1cIjI1NFwiLz48L2JwbW5k
aTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzFz
ZXVqNDhcIiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1c
IjE2OVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjIwXCIvPjxvbWdkaTp3YXlwb2lu
dCB4PVwiMTUzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyNTRcIi8+PC9icG1uZGk6
QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJFbmRFdmVudF8xaDRpaTRh
XCIgaWQ9XCJFbmRFdmVudF8xaDRpaTRhX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwi
IHdpZHRoPVwiMzZcIiB4PVwiNzM4XCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21n
ZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjc1NlwiIHk9XCIyMjdcIi8+
PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBi
cG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzBnemp2aXFcIiBpZD1cIlNlcnZpY2VUYXNrXzBnemp2
aXFfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwiMzg1
XCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxl
bWVudD1cIlNlcXVlbmNlRmxvd18xbnJ5Y2tzXCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMW5yeWNrc19k
aVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9
XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIzODVcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50
XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEz
XCIgd2lkdGg9XCIwXCIgeD1cIjI5MS41XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+
PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNl
Rmxvd18xamh3dGlvXCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMWpod3Rpb19kaVwiPjxvbWdkaTp3YXlw
b2ludCB4PVwiNDg1XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2Rp
OndheXBvaW50IHg9XCI3MzhcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48
YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIg
eD1cIjYxMS41XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVk
Z2U+PC9icG1uZGk6QlBNTlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+
In0sICJjb250ZW50X3ZlcnNpb24iOiAxMiwgImNyZWF0b3JfaWQiOiAiZ2VyYWxkLnRyb3RtYW5A
aWJtLmNvbSIsICJkZXNjcmlwdGlvbiI6ICJUaGlzIGV4YW1wbGUgd29yayBmbG93IGNhbGxzIHRo
ZSBDaXNjbyBGaXJlcG93ZXIgTWFuYWdlbWVudCBDZW50ZXIgQVBJIGVuZHBvaW50LCBtYWtlcyB0
aGUgYXV0aGVudGljYXRpb24gYW5kIHRoZW4gZ2l2ZXMgeW91IHRoZSBvcHBvcnR1bml0eSB0byBz
cGVjaWZ5IHRoZSBhY2Nlc3MgY29udHJvbCBwb2xpY3kgdG8gdGhlbiBjcmVhdGUgYSBuZXR3b3Jr
IHNwZWNpZmljIHJ1bGUgZm9yLiBZb3UgY2FuIHNwZWNpZnkgdGhlIHNvdXJjZSBhbmQgZGVzdGlu
YXRpb24gSVAsIHRoZSBhY3Rpb24gdHlwZSwgYW5kIHdoZXRoZXIgdG8gdHVybiB0aGUgcG9saWN5
IG9uIG9yIG9mZi4iLCAiZXhwb3J0X2tleSI6ICJleGFtcGxlX2Npc2NvX2ZtY19jcmVhdGVfYWNj
ZXNzX2NvbnRyb2xfcG9saWN5X3J1bGUiLCAibGFzdF9tb2RpZmllZF9ieSI6ICJnZXJhbGQudHJv
dG1hbkBpYm0uY29tIiwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE2MDczNzEzMzU5NzEsICJuYW1l
IjogIkV4YW1wbGU6IENpc2NvIEZNQyBDcmVhdGUgQWNjZXNzIENvbnRyb2wgUG9saWN5IFJ1bGUi
LCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3QiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiZXhhbXBs
ZV9jaXNjb19mbWNfY3JlYXRlX2FjY2Vzc19jb250cm9sX3BvbGljeV9ydWxlIiwgInRhZ3MiOiBb
XSwgInV1aWQiOiAiYzFiMzAxZjktZGQ2YS00NDUyLTg1OGUtOTk1MjA5ZTZkOTYxIiwgIndvcmtm
bG93X2lkIjogMTc3fV0sICJ3b3Jrc3BhY2VzIjogW119
"""
    )