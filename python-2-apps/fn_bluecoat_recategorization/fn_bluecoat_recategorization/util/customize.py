# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_bluecoat_recategorization"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_bluecoat_recategorization package"""
    reload_params = {"package": u"fn_bluecoat_recategorization",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "function_params": [u"artifact_value", u"categorization_id", u"categorization_name", u"incident_id", u"submission_comments"], 
                    "datatables": [], 
                    "message_destinations": [u"bluecoat_recategorization"], 
                    "functions": [u"bluecoat_site_review_recategorization"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [u"bluecoat_site_review_resubmission"], 
                    "actions": [] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     artifact_value
    #     categorization_id
    #     categorization_name
    #     incident_id
    #     submission_comments
    #   Message Destinations:
    #     bluecoat_recategorization
    #   Functions:
    #     bluecoat_site_review_recategorization
    #   Workflows:
    #     bluecoat_site_review_resubmission


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbeyJ1dWlkIjogImZmNzAxNjY4LTg5NWEt
NDAxMC1iMTE1LWVmNGZhOGM0ZjZkYiIsICJkZXNjcmlwdGlvbiI6ICJUaGlzIHdvcmtmbG93IGxl
dmVyYWdlcyB0aGUgYmx1ZWNvYXQgZnVuY3Rpb24gdGhhdCBpbXBsZW1lbnRzIHJlY2F0ZWdvcml6
YXRpb24gc3VibWlzc2lvbiBvZiBhIHVybCBhbmQgcmV0dXJucyBhIHN1Ym1pc3Npb24gaWQgdXBv
biBjb21wbGV0aW9uLiIsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJleHBvcnRfa2V5Ijog
ImJsdWVjb2F0X3NpdGVfcmV2aWV3X3Jlc3VibWlzc2lvbiIsICJ3b3JrZmxvd19pZCI6IDE1MCwg
Imxhc3RfbW9kaWZpZWRfYnkiOiAiZ2VyYWxkLnRyb3RtYW5AaWJtLmNvbSIsICJjb250ZW50Ijog
eyJ4bWwiOiAiPD94bWwgdmVyc2lvbj1cIjEuMFwiIGVuY29kaW5nPVwiVVRGLThcIj8+PGRlZmlu
aXRpb25zIHhtbG5zPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9NT0RF
TFwiIHhtbG5zOmJwbW5kaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQv
RElcIiB4bWxuczpvbWdkYz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RD
XCIgeG1sbnM6b21nZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9ESVwi
IHhtbG5zOnJlc2lsaWVudD1cImh0dHA6Ly9yZXNpbGllbnQuaWJtLmNvbS9icG1uXCIgeG1sbnM6
eHNkPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWFcIiB4bWxuczp4c2k9XCJodHRw
Oi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZVwiIHRhcmdldE5hbWVzcGFjZT1c
Imh0dHA6Ly93d3cuY2FtdW5kYS5vcmcvdGVzdFwiPjxwcm9jZXNzIGlkPVwiYmx1ZWNvYXRfc2l0
ZV9yZXZpZXdfcmVzdWJtaXNzaW9uXCIgaXNFeGVjdXRhYmxlPVwidHJ1ZVwiIG5hbWU9XCJCbHVl
Y29hdCBTaXRlIFJldmlldyBSZXN1Ym1pc3Npb25cIj48ZG9jdW1lbnRhdGlvbj5UaGlzIHdvcmtm
bG93IGxldmVyYWdlcyB0aGUgYmx1ZWNvYXQgZnVuY3Rpb24gdGhhdCBpbXBsZW1lbnRzIHJlY2F0
ZWdvcml6YXRpb24gc3VibWlzc2lvbiBvZiBhIHVybCBhbmQgcmV0dXJucyBhIHN1Ym1pc3Npb24g
aWQgdXBvbiBjb21wbGV0aW9uLjwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1cIlN0YXJ0
RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMWQ1dnJ5ajwvb3V0Z29pbmc+
PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzF3Y3R0NnZcIiBuYW1l
PVwiQmx1ZWNvYXQgU2l0ZSBSZXZpZXcgUmVjYXRlZ29yaXphLi4uXCIgcmVzaWxpZW50OnR5cGU9
XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9
XCI1ZTg2YTc4NS01OTdhLTRjNTMtYWQ0ZS0zY2ViZTVmM2U3MTVcIj57XCJpbnB1dHNcIjp7fSxc
InByZV9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiaW5wdXRzLmluY2lkZW50X2lkID0gaW5jaWRlbnQu
aWRcXG5pbnB1dHMuYXJ0aWZhY3RfdmFsdWUgPSBhcnRpZmFjdC52YWx1ZVxcblwifTwvcmVzaWxp
ZW50OmZ1bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18x
ZDV2cnlqPC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzBzZnJrbXE8L291dGdvaW5n
Pjwvc2VydmljZVRhc2s+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xZDV2cnlqXCIg
c291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tf
MXdjdHQ2dlwiLz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVudF8wemt4dzljXCI+PGluY29taW5nPlNl
cXVlbmNlRmxvd18wc2Zya21xPC9pbmNvbWluZz48L2VuZEV2ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9
XCJTZXF1ZW5jZUZsb3dfMHNmcmttcVwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzF3Y3R0NnZc
IiB0YXJnZXRSZWY9XCJFbmRFdmVudF8wemt4dzljXCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRl
eHRBbm5vdGF0aW9uXzFreHhpeXRcIj48dGV4dD5TdGFydCB5b3VyIHdvcmtmbG93IGhlcmU8L3Rl
eHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4
XCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90
YXRpb25fMWt4eGl5dFwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5E
aWFncmFtXzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1cInVuZGVmaW5lZFwiIGlk
PVwiQlBNTlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlN0YXJ0RXZl
bnRfMTU1YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+PG9tZ2RjOkJvdW5kcyBo
ZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQ
TU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjE1N1wi
IHk9XCIyMjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRp
OkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIiBpZD1cIlRl
eHRBbm5vdGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjMwXCIgd2lk
dGg9XCIxMDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRp
OkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIGlkPVwiQXNzb2Np
YXRpb25fMXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTY5XCIgeHNpOnR5cGU9XCJv
bWdkYzpQb2ludFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIxNTNcIiB4c2k6dHlw
ZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQ
TU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzF3Y3R0NnZcIiBpZD1cIlNlcnZpY2VU
YXNrXzF3Y3R0NnZfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBc
IiB4PVwiMzc2XCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRn
ZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18xZDV2cnlqXCIgaWQ9XCJTZXF1ZW5jZUZsb3df
MWQ1dnJ5al9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQ
b2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIzNzZcIiB4c2k6dHlwZT1cIm9t
Z2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhl
aWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjI4N1wiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBN
TkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwi
RW5kRXZlbnRfMHpreHc5Y1wiIGlkPVwiRW5kRXZlbnRfMHpreHc5Y19kaVwiPjxvbWdkYzpCb3Vu
ZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjcxN1wiIHk9XCIxODhcIi8+PGJwbW5k
aTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI3
MzVcIiB5PVwiMjI3XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJw
bW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18wc2Zya21xXCIgaWQ9XCJT
ZXF1ZW5jZUZsb3dfMHNmcmttcV9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiNDc2XCIgeHNpOnR5
cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI3MTdcIiB4
c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21n
ZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjU5Ni41XCIgeT1cIjE4NFwi
Lz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5l
PjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+IiwgIndvcmtmbG93X2lkIjogImJs
dWVjb2F0X3NpdGVfcmV2aWV3X3Jlc3VibWlzc2lvbiIsICJ2ZXJzaW9uIjogMX0sICJsYXN0X21v
ZGlmaWVkX3RpbWUiOiAxNTQ0NDQxMjU3OTk2LCAiY3JlYXRvcl9pZCI6ICJnZXJhbGQudHJvdG1h
bkBpYm0uY29tIiwgImFjdGlvbnMiOiBbXSwgInByb2dyYW1tYXRpY19uYW1lIjogImJsdWVjb2F0
X3NpdGVfcmV2aWV3X3Jlc3VibWlzc2lvbiIsICJuYW1lIjogIkJsdWVjb2F0IFNpdGUgUmV2aWV3
IFJlc3VibWlzc2lvbiJ9XSwgImFjdGlvbnMiOiBbXSwgImxheW91dHMiOiBbXSwgImV4cG9ydF9m
b3JtYXRfdmVyc2lvbiI6IDIsICJpZCI6IDQ2LCAiaW5kdXN0cmllcyI6IG51bGwsICJwaGFzZXMi
OiBbXSwgImFjdGlvbl9vcmRlciI6IFtdLCAiZ2VvcyI6IG51bGwsICJsb2NhbGUiOiBudWxsLCAi
c2VydmVyX3ZlcnNpb24iOiB7Im1ham9yIjogMzEsICJ2ZXJzaW9uIjogIjMxLjAuNDI1NCIsICJi
dWlsZF9udW1iZXIiOiA0MjU0LCAibWlub3IiOiAwfSwgInRpbWVmcmFtZXMiOiBudWxsLCAid29y
a3NwYWNlcyI6IFtdLCAiYXV0b21hdGljX3Rhc2tzIjogW10sICJmdW5jdGlvbnMiOiBbeyJkaXNw
bGF5X25hbWUiOiAiQmx1ZWNvYXQgU2l0ZSBSZXZpZXcgUmVjYXRlZ29yaXphdGlvbiIsICJkZXNj
cmlwdGlvbiI6IHsiY29udGVudCI6ICJUaGlzIGZ1bmN0aW9uIHRha2VzIGluIGEgdXJsIGFuZCBh
IGNhdGVnb3JpemF0aW9uIGlkIHRvIGJlIHN1Ym1pdHRlZCBmb3IgcmV2aWV3LiIsICJmb3JtYXQi
OiAidGV4dCJ9LCAiY3JlYXRvciI6IHsiZGlzcGxheV9uYW1lIjogIkdlcmFsZCBUcm90bWFuIiwg
InR5cGUiOiAidXNlciIsICJpZCI6IDQsICJuYW1lIjogImdlcmFsZC50cm90bWFuQGlibS5jb20i
fSwgInZpZXdfaXRlbXMiOiBbeyJzaG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUiOiAiX19mdW5j
dGlvbiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZpZWxkX3V1aWQi
LCAiY29udGVudCI6ICJlYWQyMTRjMi0xM2ZlLTQzZjYtYTNjNy02NzZhODgzMzhkYmIiLCAic3Rl
cF9sYWJlbCI6IG51bGx9LCB7InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0
aW9uIiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIs
ICJjb250ZW50IjogIjliYTQ5ODg3LTBkY2YtNDBjZS1hNWVhLTljMGM0M2Y4MzFiZiIsICJzdGVw
X2xhYmVsIjogbnVsbH0sIHsic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rp
b24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwg
ImNvbnRlbnQiOiAiZTcwMTllN2MtYmVmMy00ZWY5LTk2NjAtOTRkYWQ4NGYxYTZhIiwgInN0ZXBf
bGFiZWwiOiBudWxsfSwgeyJzaG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlv
biIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAi
Y29udGVudCI6ICIzNzlkMDQzYi1jZWM1LTQ0YmItOGU5YS1hM2FiMGRmYzA4ZDUiLCAic3RlcF9s
YWJlbCI6IG51bGx9LCB7InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9u
IiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJj
b250ZW50IjogIjkyZTg0Zjc0LWZhYzctNDQ4Yy1iNTA5LTJhYjgwNDU3MTY4OCIsICJzdGVwX2xh
YmVsIjogbnVsbH1dLCAiZXhwb3J0X2tleSI6ICJibHVlY29hdF9zaXRlX3Jldmlld19yZWNhdGVn
b3JpemF0aW9uIiwgInV1aWQiOiAiNWU4NmE3ODUtNTk3YS00YzUzLWFkNGUtM2NlYmU1ZjNlNzE1
IiwgImxhc3RfbW9kaWZpZWRfYnkiOiB7ImRpc3BsYXlfbmFtZSI6ICJHZXJhbGQgVHJvdG1hbiIs
ICJ0eXBlIjogInVzZXIiLCAiaWQiOiA0LCAibmFtZSI6ICJnZXJhbGQudHJvdG1hbkBpYm0uY29t
In0sICJ2ZXJzaW9uIjogNCwgIndvcmtmbG93cyI6IFt7ImRlc2NyaXB0aW9uIjogbnVsbCwgIm9i
amVjdF90eXBlIjogImFydGlmYWN0IiwgImFjdGlvbnMiOiBbXSwgIm5hbWUiOiAiQmx1ZWNvYXQg
U2l0ZSBSZXZpZXcgUmVzdWJtaXNzaW9uIiwgIndvcmtmbG93X2lkIjogMTUwLCAicHJvZ3JhbW1h
dGljX25hbWUiOiAiYmx1ZWNvYXRfc2l0ZV9yZXZpZXdfcmVzdWJtaXNzaW9uIiwgInV1aWQiOiBu
dWxsfV0sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTQ0NTE4ODg3MjYyLCAiZGVzdGluYXRpb25f
aGFuZGxlIjogImJsdWVjb2F0X3JlY2F0ZWdvcml6YXRpb24iLCAiaWQiOiAxNjksICJuYW1lIjog
ImJsdWVjb2F0X3NpdGVfcmV2aWV3X3JlY2F0ZWdvcml6YXRpb24ifV0sICJub3RpZmljYXRpb25z
IjogbnVsbCwgInJlZ3VsYXRvcnMiOiBudWxsLCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJjcmVhdGVf
ZGF0ZSI6IDE1NDQ1NDgzMzMyNDUsICJkZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2th
Z2VzIChpbnRlcm5hbCkiLCAiZXhwb3J0X2tleSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChp
bnRlcm5hbCkiLCAiaWQiOiAwLCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRl
cm5hbCkiLCAidXBkYXRlX2RhdGUiOiAxNTQ0NTQ4MzMzMjQ1LCAidXVpZCI6ICJiZmVlYzJkNC0z
NzcwLTExZTgtYWQzOS00YTAwMDQwNDRhYTAiLCAiZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVtIjog
ZmFsc2UsICJwYXJlbnRfaWQiOiBudWxsLCAiaGlkZGVuIjogZmFsc2V9XSwgInNjcmlwdHMiOiBb
XSwgInR5cGVzIjogW10sICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFt7InV1aWQiOiAiMzhhMjgw
YjAtYzViZS00NmQ3LTgyMGQtMTJjOGZiNzc3N2U0IiwgImV4cG9ydF9rZXkiOiAiYmx1ZWNvYXRf
cmVjYXRlZ29yaXphdGlvbiIsICJuYW1lIjogIkJsdWVjb2F0IFJlY2F0ZWdvcml6YXRpb24iLCAi
ZGVzdGluYXRpb25fdHlwZSI6IDAsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJibHVlY29hdF9yZWNh
dGVnb3JpemF0aW9uIiwgImV4cGVjdF9hY2siOiB0cnVlLCAidXNlcnMiOiBbXX1dLCAiaW5jaWRl
bnRfYXJ0aWZhY3RfdHlwZXMiOiBbXSwgInJvbGVzIjogW10sICJmaWVsZHMiOiBbeyJvcGVyYXRp
b25zIjogW10sICJ0eXBlX2lkIjogMCwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJT
aW11bGF0aW9uIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVsbCwgImNoYW5n
ZWFibGUiOiB0cnVlLCAiaWQiOiAzNywgInJlYWRfb25seSI6IHRydWUsICJ1dWlkIjogImMzZjBl
M2VkLTIxZTEtNGQ1My1hZmZiLWZlNWNhMzMwOGNjYSIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0
X3R5cGUiOiAiYm9vbGVhbiIsICJ0b29sdGlwIjogIldoZXRoZXIgdGhlIGluY2lkZW50IGlzIGEg
c2ltdWxhdGlvbiBvciBhIHJlZ3VsYXIgaW5jaWRlbnQuICBUaGlzIGZpZWxkIGlzIHJlYWQtb25s
eS4iLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjog
W10sICJleHBvcnRfa2V5IjogImluY2lkZW50L2luY190cmFpbmluZyIsICJoaWRlX25vdGlmaWNh
dGlvbiI6IGZhbHNlLCAibmFtZSI6ICJpbmNfdHJhaW5pbmciLCAiZGVwcmVjYXRlZCI6IGZhbHNl
LCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJ2YWx1ZXMiOiBbXX0sIHsib3Bl
cmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDExLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ0ZXh0
IjogImFydGlmYWN0X3ZhbHVlIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVs
bCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAxNDksICJyZWFkX29ubHkiOiBmYWxzZSwgInV1
aWQiOiAiOWJhNDk4ODctMGRjZi00MGNlLWE1ZWEtOWMwYzQzZjgzMWJmIiwgImNob3NlbiI6IGZh
bHNlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiIiwgImludGVybmFsIjogZmFs
c2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tleSI6ICJf
X2Z1bmN0aW9uL2FydGlmYWN0X3ZhbHVlIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJw
bGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJhcnRpZmFjdF92YWx1ZSIsICJkZXByZWNhdGVkIjog
ZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVlcyI6IFtdfSwg
eyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMTEsICJvcGVyYXRpb25fcGVybXMiOiB7fSwg
InRleHQiOiAiaW5jaWRlbnRfaWQiLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiBu
dWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDExNSwgInJlYWRfb25seSI6IGZhbHNlLCAi
dXVpZCI6ICJlYWQyMTRjMi0xM2ZlLTQzZjYtYTNjNy02NzZhODgzMzhkYmIiLCAiY2hvc2VuIjog
ZmFsc2UsICJpbnB1dF90eXBlIjogIm51bWJlciIsICJ0b29sdGlwIjogIiIsICJpbnRlcm5hbCI6
IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgImV4cG9ydF9rZXki
OiAiX19mdW5jdGlvbi9pbmNpZGVudF9pZCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAi
cGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAiaW5jaWRlbnRfaWQiLCAiZGVwcmVjYXRlZCI6IGZh
bHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJ2YWx1ZXMiOiBbXX0sIHsi
b3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDExLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ0
ZXh0IjogImNhdGVnb3JpemF0aW9uX2lkIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4
IjogbnVsbCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAyNzYsICJyZWFkX29ubHkiOiBmYWxz
ZSwgInV1aWQiOiAiMzc5ZDA0M2ItY2VjNS00NGJiLThlOWEtYTNhYjBkZmMwOGQ1IiwgImNob3Nl
biI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJudW1iZXIiLCAidG9vbHRpcCI6ICIiLCAiaW50ZXJu
YWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJleHBvcnRf
a2V5IjogIl9fZnVuY3Rpb24vY2F0ZWdvcml6YXRpb25faWQiLCAiaGlkZV9ub3RpZmljYXRpb24i
OiBmYWxzZSwgInBsYWNlaG9sZGVyIjogIiIsICJuYW1lIjogImNhdGVnb3JpemF0aW9uX2lkIiwg
ImRlcHJlY2F0ZWQiOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAi
dmFsdWVzIjogW119LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAxMSwgIm9wZXJhdGlv
bl9wZXJtcyI6IHt9LCAidGV4dCI6ICJjYXRlZ29yaXphdGlvbl9uYW1lIiwgImJsYW5rX29wdGlv
biI6IGZhbHNlLCAicHJlZml4IjogbnVsbCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAyNzgs
ICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiZTcwMTllN2MtYmVmMy00ZWY5LTk2NjAtOTRk
YWQ4NGYxYTZhIiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0
aXAiOiAiIiwgImludGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRl
cyI6IFtdLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL2NhdGVnb3JpemF0aW9uX25hbWUiLCAi
aGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgInBsYWNlaG9sZGVyIjogIiIsICJuYW1lIjogImNh
dGVnb3JpemF0aW9uX25hbWUiLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5f
Ynlfc2VydmVyIjogZmFsc2UsICJ2YWx1ZXMiOiBbXX0sIHsib3BlcmF0aW9ucyI6IFtdLCAidHlw
ZV9pZCI6IDExLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ0ZXh0IjogInN1Ym1pc3Npb25fY29t
bWVudHMiLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJs
ZSI6IHRydWUsICJpZCI6IDI3NywgInJlYWRfb25seSI6IGZhbHNlLCAidXVpZCI6ICI5MmU4NGY3
NC1mYWM3LTQ0OGMtYjUwOS0yYWI4MDQ1NzE2ODgiLCAiY2hvc2VuIjogZmFsc2UsICJpbnB1dF90
eXBlIjogInRleHQiLCAidG9vbHRpcCI6ICIiLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4
dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vc3Vi
bWlzc2lvbl9jb21tZW50cyIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xk
ZXIiOiAiIiwgIm5hbWUiOiAic3VibWlzc2lvbl9jb21tZW50cyIsICJkZXByZWNhdGVkIjogZmFs
c2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVlcyI6IFtdfV0sICJv
dmVycmlkZXMiOiBbXSwgImV4cG9ydF9kYXRlIjogMTU0NDUxODg5NjIxN30=
"""
    )