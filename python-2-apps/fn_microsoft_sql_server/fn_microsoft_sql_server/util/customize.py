# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_microsoft_sql_server"""

from __future__ import print_function
from resilient_circuits.util import *


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     artifact_type
    #     artifact_value
    #     incident_id
    #     sql_query_statement
    #   Message Destinations:
    #     microsoft_sql
    #   Functions:
    #     microsoft_sql_query
    #   Workflows:
    #     microsoft_sql_search


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbeyJ1dWlkIjogIjQzN2M2N2MzLWI2Y2Et
NDgyYy1iMTY4LTViYWU0NjExNTg3NSIsICJkZXNjcmlwdGlvbiI6ICJUaGlzIHdvcmtmbG93IGxl
dmVyYWdlcyB0aGUgTWljcm9zb2Z0IFNRTCBRdWVyeSBmdW5jdGlvbiB3aGljaCB0YWtlcyBhbiBT
UUwgUXVlcnkgU3RhdGVtZW50IGFuZCByZXR1cm5zIGl0cyByZXN1bHRzIiwgIm9iamVjdF90eXBl
IjogImFydGlmYWN0IiwgImV4cG9ydF9rZXkiOiAibWljcm9zb2Z0X3NxbF9zZWFyY2giLCAid29y
a2Zsb3dfaWQiOiAxNDIsICJsYXN0X21vZGlmaWVkX2J5IjogImdlcmFsZC50cm90bWFuQGlibS5j
b20iLCAiY29udGVudCI6IHsieG1sIjogIjw/eG1sIHZlcnNpb249XCIxLjBcIiBlbmNvZGluZz1c
IlVURi04XCI/PjxkZWZpbml0aW9ucyB4bWxucz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQ
TU4vMjAxMDA1MjQvTU9ERUxcIiB4bWxuczpicG1uZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3Bl
Yy9CUE1OLzIwMTAwNTI0L0RJXCIgeG1sbnM6b21nZGM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3Bl
Yy9ERC8yMDEwMDUyNC9EQ1wiIHhtbG5zOm9tZ2RpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMv
REQvMjAxMDA1MjQvRElcIiB4bWxuczpyZXNpbGllbnQ9XCJodHRwOi8vcmVzaWxpZW50LmlibS5j
b20vYnBtblwiIHhtbG5zOnhzZD1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hXCIg
eG1sbnM6eHNpPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2VcIiB0
YXJnZXROYW1lc3BhY2U9XCJodHRwOi8vd3d3LmNhbXVuZGEub3JnL3Rlc3RcIj48cHJvY2VzcyBp
ZD1cIm1pY3Jvc29mdF9zcWxfc2VhcmNoXCIgaXNFeGVjdXRhYmxlPVwidHJ1ZVwiIG5hbWU9XCJN
aWNyb3NvZnQgU1FMIFNlYXJjaFwiPjxkb2N1bWVudGF0aW9uPlRoaXMgd29ya2Zsb3cgbGV2ZXJh
Z2VzIHRoZSBNaWNyb3NvZnQgU1FMIFF1ZXJ5IGZ1bmN0aW9uIHdoaWNoIHRha2VzIGFuIFNRTCBR
dWVyeSBTdGF0ZW1lbnQgYW5kIHJldHVybnMgaXRzIHJlc3VsdHM8L2RvY3VtZW50YXRpb24+PHN0
YXJ0RXZlbnQgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIj48b3V0Z29pbmc+U2VxdWVuY2VGbG93
XzE0YXFhbjk8L291dGdvaW5nPjwvc3RhcnRFdmVudD48c2VydmljZVRhc2sgaWQ9XCJTZXJ2aWNl
VGFza18wb3Q3Y2E1XCIgbmFtZT1cIk1pY3Jvc29mdCBTUUwgUXVlcnlcIiByZXNpbGllbnQ6dHlw
ZT1cImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVp
ZD1cIjE3ZDA4ZGJkLTBhMjktNDQzYi1hOThiLTg2MzBhZWMzZGM0MlwiPntcImlucHV0c1wiOnt9
fTwvcmVzaWxpZW50OmZ1bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGluY29taW5nPlNlcXVl
bmNlRmxvd18xNGFxYW45PC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzAwMnEzNXo8
L291dGdvaW5nPjwvc2VydmljZVRhc2s+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18x
NGFxYW45XCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2Vy
dmljZVRhc2tfMG90N2NhNVwiLz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVudF8xcmZ1a2xxXCI+PGlu
Y29taW5nPlNlcXVlbmNlRmxvd18wMDJxMzV6PC9pbmNvbWluZz48L2VuZEV2ZW50PjxzZXF1ZW5j
ZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMDAycTM1elwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNr
XzBvdDdjYTVcIiB0YXJnZXRSZWY9XCJFbmRFdmVudF8xcmZ1a2xxXCIvPjx0ZXh0QW5ub3RhdGlv
biBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIj48dGV4dD5TdGFydCB5b3VyIHdvcmtmbG93
IGhlcmU8L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlv
bl8xc2V1ajQ4XCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwi
VGV4dEFubm90YXRpb25fMWt4eGl5dFwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBp
ZD1cIkJQTU5EaWFncmFtXzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1cInVuZGVm
aW5lZFwiIGlkPVwiQlBNTlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1c
IlN0YXJ0RXZlbnRfMTU1YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+PG9tZ2Rj
OkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIgeT1cIjE4OFwiLz48
YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIg
eD1cIjE1N1wiIHk9XCIyMjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFw
ZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRc
IiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1c
IjMwXCIgd2lkdGg9XCIxMDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5TaGFw
ZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIGlk
PVwiQXNzb2NpYXRpb25fMXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTY5XCIgeHNp
OnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIxNTNc
IiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1ORWRnZT48
YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzBvdDdjYTVcIiBpZD1c
IlNlcnZpY2VUYXNrXzBvdDdjYTVfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lk
dGg9XCIxMDBcIiB4PVwiMzg3XCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5k
aTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18xNGFxYW45XCIgaWQ9XCJTZXF1
ZW5jZUZsb3dfMTRhcWFuOV9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9
XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIzODdcIiB4c2k6
dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6
Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjI5Mi41XCIgeT1cIjE4NFwiLz48
L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBt
bkVsZW1lbnQ9XCJFbmRFdmVudF8xcmZ1a2xxXCIgaWQ9XCJFbmRFdmVudF8xcmZ1a2xxX2RpXCI+
PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiNjY0XCIgeT1cIjE4
OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9
XCIwXCIgeD1cIjY4MlwiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQ
TU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzAwMnEz
NXpcIiBpZD1cIlNlcXVlbmNlRmxvd18wMDJxMzV6X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0
ODdcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQg
eD1cIjY2NFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBN
TkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNTc1LjVc
IiB5PVwiMTg0XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48L2JwbW5k
aTpCUE1OUGxhbmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4iLCAid29ya2Zs
b3dfaWQiOiAibWljcm9zb2Z0X3NxbF9zZWFyY2giLCAidmVyc2lvbiI6IDF9LCAibGFzdF9tb2Rp
ZmllZF90aW1lIjogMTU0MTc4ODgxNjkzNiwgImNyZWF0b3JfaWQiOiAiZ2VyYWxkLnRyb3RtYW5A
aWJtLmNvbSIsICJhY3Rpb25zIjogW10sICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJtaWNyb3NvZnRf
c3FsX3NlYXJjaCIsICJuYW1lIjogIk1pY3Jvc29mdCBTUUwgU2VhcmNoIn1dLCAiYWN0aW9ucyI6
IFtdLCAibGF5b3V0cyI6IFtdLCAiZXhwb3J0X2Zvcm1hdF92ZXJzaW9uIjogMiwgImlkIjogMzIs
ICJpbmR1c3RyaWVzIjogbnVsbCwgInBoYXNlcyI6IFtdLCAiYWN0aW9uX29yZGVyIjogW10sICJn
ZW9zIjogbnVsbCwgInNlcnZlcl92ZXJzaW9uIjogeyJtYWpvciI6IDMwLCAidmVyc2lvbiI6ICIz
MC40LjIzNyIsICJidWlsZF9udW1iZXIiOiAyMzcsICJtaW5vciI6IDR9LCAidGltZWZyYW1lcyI6
IG51bGwsICJ3b3Jrc3BhY2VzIjogW10sICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgImZ1bmN0aW9u
cyI6IFt7ImRpc3BsYXlfbmFtZSI6ICJNaWNyb3NvZnQgU1FMIFF1ZXJ5IiwgImRlc2NyaXB0aW9u
IjogeyJjb250ZW50IjogIlRoaXMgZnVuY3Rpb24gdGFrZXMgTWljcm9zb2Z0IFNRTCBTZXJ2ZXIg
cXVlcmllcyBhbmQgc2ltcGx5IHJldHVybnMgdGhlIHJlc3VsdHMgb2YgdGhhdCBxdWVyeS4iLCAi
Zm9ybWF0IjogInRleHQifSwgImNyZWF0b3IiOiB7ImRpc3BsYXlfbmFtZSI6ICJHZXJhbGQgVHJv
dG1hbiIsICJ0eXBlIjogInVzZXIiLCAiaWQiOiA0LCAibmFtZSI6ICJnZXJhbGQudHJvdG1hbkBp
Ym0uY29tIn0sICJ2aWV3X2l0ZW1zIjogW3sic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBlIjog
Il9fZnVuY3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJmaWVs
ZF91dWlkIiwgImNvbnRlbnQiOiAiZWFkMjE0YzItMTNmZS00M2Y2LWEzYzctNjc2YTg4MzM4ZGJi
IiwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJzaG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUiOiAi
X19mdW5jdGlvbiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZpZWxk
X3V1aWQiLCAiY29udGVudCI6ICIzYTJlMzQ3Yi02NzJlLTQyNjMtODc4Ny1hM2U5ZWJhNGFjOTEi
LCAic3RlcF9sYWJlbCI6IG51bGx9LCB7InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlwZSI6ICJf
X2Z1bmN0aW9uIiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAiZmllbGRf
dXVpZCIsICJjb250ZW50IjogIjliYTQ5ODg3LTBkY2YtNDBjZS1hNWVhLTljMGM0M2Y4MzFiZiIs
ICJzdGVwX2xhYmVsIjogbnVsbH0sIHsic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBlIjogIl9f
ZnVuY3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJmaWVsZF91
dWlkIiwgImNvbnRlbnQiOiAiODY3NzUwZDYtOTZjNy00NjJlLWJlZDktZDkwYjdmNzFmMTI3Iiwg
InN0ZXBfbGFiZWwiOiBudWxsfV0sICJleHBvcnRfa2V5IjogIm1pY3Jvc29mdF9zcWxfcXVlcnki
LCAidXVpZCI6ICIxN2QwOGRiZC0wYTI5LTQ0M2ItYTk4Yi04NjMwYWVjM2RjNDIiLCAibGFzdF9t
b2RpZmllZF9ieSI6IHsiZGlzcGxheV9uYW1lIjogIkdlcmFsZCBUcm90bWFuIiwgInR5cGUiOiAi
dXNlciIsICJpZCI6IDQsICJuYW1lIjogImdlcmFsZC50cm90bWFuQGlibS5jb20ifSwgInZlcnNp
b24iOiAxLCAid29ya2Zsb3dzIjogW3siZGVzY3JpcHRpb24iOiBudWxsLCAib2JqZWN0X3R5cGUi
OiAiYXJ0aWZhY3QiLCAiYWN0aW9ucyI6IFtdLCAibmFtZSI6ICJNaWNyb3NvZnQgU1FMIFNlYXJj
aCIsICJ3b3JrZmxvd19pZCI6IDE0MiwgInByb2dyYW1tYXRpY19uYW1lIjogIm1pY3Jvc29mdF9z
cWxfc2VhcmNoIiwgInV1aWQiOiBudWxsfV0sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTQxNzgx
OTQ4NDI0LCAiZGVzdGluYXRpb25faGFuZGxlIjogIm1pY3Jvc29mdF9zcWwiLCAiaWQiOiAxNjIs
ICJuYW1lIjogIm1pY3Jvc29mdF9zcWxfcXVlcnkifV0sICJub3RpZmljYXRpb25zIjogbnVsbCwg
InJlZ3VsYXRvcnMiOiBudWxsLCAiaW5jaWRlbnRfdHlwZXMiOiBbeyJjcmVhdGVfZGF0ZSI6IDE1
NDE3ODkyOTIwNzcsICJkZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRl
cm5hbCkiLCAiZXhwb3J0X2tleSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCki
LCAiaWQiOiAwLCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAi
dXBkYXRlX2RhdGUiOiAxNTQxNzg5MjkyMDc3LCAidXVpZCI6ICJiZmVlYzJkNC0zNzcwLTExZTgt
YWQzOS00YTAwMDQwNDRhYTAiLCAiZW5hYmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJw
YXJlbnRfaWQiOiBudWxsLCAiaGlkZGVuIjogZmFsc2V9XSwgInNjcmlwdHMiOiBbXSwgInR5cGVz
IjogW10sICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFt7InV1aWQiOiAiYzliYzE4OWMtN2E1NC00
M2ExLTkxYjctMDlkMzk1NTgwNmM1IiwgImV4cG9ydF9rZXkiOiAibWljcm9zb2Z0X3NxbCIsICJu
YW1lIjogIk1pY3Jvc29mdCBTUUwiLCAiZGVzdGluYXRpb25fdHlwZSI6IDAsICJwcm9ncmFtbWF0
aWNfbmFtZSI6ICJtaWNyb3NvZnRfc3FsIiwgImV4cGVjdF9hY2siOiB0cnVlLCAidXNlcnMiOiBb
XX1dLCAiaW5jaWRlbnRfYXJ0aWZhY3RfdHlwZXMiOiBbXSwgInJvbGVzIjogW10sICJmaWVsZHMi
OiBbeyJvcGVyYXRpb25zIjogW10sICJyZWFkX29ubHkiOiB0cnVlLCAibmFtZSI6ICJpbmNfdHJh
aW5pbmciLCAidGVtcGxhdGVzIjogW10sICJ0eXBlX2lkIjogMCwgImNob3NlbiI6IGZhbHNlLCAi
dGV4dCI6ICJTaW11bGF0aW9uIiwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAi
ZXhwb3J0X2tleSI6ICJpbmNpZGVudC9pbmNfdHJhaW5pbmciLCAidG9vbHRpcCI6ICJXaGV0aGVy
IHRoZSBpbmNpZGVudCBpcyBhIHNpbXVsYXRpb24gb3IgYSByZWd1bGFyIGluY2lkZW50LiAgVGhp
cyBmaWVsZCBpcyByZWFkLW9ubHkuIiwgInJpY2hfdGV4dCI6IGZhbHNlLCAib3BlcmF0aW9uX3Bl
cm1zIjoge30sICJwcmVmaXgiOiBudWxsLCAiaW50ZXJuYWwiOiBmYWxzZSwgInZhbHVlcyI6IFtd
LCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJpbnB1dF90eXBlIjogImJvb2xlYW4iLCAiY2hhbmdl
YWJsZSI6IHRydWUsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiAzNywgInV1aWQi
OiAiYzNmMGUzZWQtMjFlMS00ZDUzLWFmZmItZmU1Y2EzMzA4Y2NhIn0sIHsib3BlcmF0aW9ucyI6
IFtdLCAidHlwZV9pZCI6IDExLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ0ZXh0IjogImFydGlm
YWN0X3R5cGUiLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdl
YWJsZSI6IHRydWUsICJpZCI6IDE1MCwgInJlYWRfb25seSI6IGZhbHNlLCAidXVpZCI6ICIzYTJl
MzQ3Yi02NzJlLTQyNjMtODc4Ny1hM2U5ZWJhNGFjOTEiLCAiY2hvc2VuIjogZmFsc2UsICJpbnB1
dF90eXBlIjogInRleHQiLCAidG9vbHRpcCI6ICIiLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hf
dGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24v
YXJ0aWZhY3RfdHlwZSIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIi
OiAiIiwgIm5hbWUiOiAiYXJ0aWZhY3RfdHlwZSIsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIi
OiBmYWxzZSwgInZhbHVlcyI6IFtdfSwgeyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMTEs
ICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAiaW5jaWRlbnRfaWQiLCAiYmxhbmtfb3B0
aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDEx
NSwgInJlYWRfb25seSI6IGZhbHNlLCAidXVpZCI6ICJlYWQyMTRjMi0xM2ZlLTQzZjYtYTNjNy02
NzZhODgzMzhkYmIiLCAiY2hvc2VuIjogZmFsc2UsICJpbnB1dF90eXBlIjogIm51bWJlciIsICJ0
b29sdGlwIjogIiIsICJpbnRlcm5hbCI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1w
bGF0ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9pbmNpZGVudF9pZCIsICJoaWRl
X25vdGlmaWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAiaW5jaWRl
bnRfaWQiLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJ2YWx1ZXMiOiBbXX0s
IHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDExLCAib3BlcmF0aW9uX3Blcm1zIjoge30s
ICJ0ZXh0IjogImFydGlmYWN0X3ZhbHVlIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4
IjogbnVsbCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAxNDksICJyZWFkX29ubHkiOiBmYWxz
ZSwgInV1aWQiOiAiOWJhNDk4ODctMGRjZi00MGNlLWE1ZWEtOWMwYzQzZjgzMWJmIiwgImNob3Nl
biI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiIiwgImludGVybmFs
IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tl
eSI6ICJfX2Z1bmN0aW9uL2FydGlmYWN0X3ZhbHVlIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFs
c2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJhcnRpZmFjdF92YWx1ZSIsICJkZWZhdWx0
X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVlcyI6IFtdfSwgeyJvcGVyYXRpb25zIjog
W10sICJ0eXBlX2lkIjogMTEsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAic3FsX3F1
ZXJ5X3N0YXRlbWVudCIsICJibGFua19vcHRpb24iOiBmYWxzZSwgInByZWZpeCI6IG51bGwsICJj
aGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMjE2LCAicmVhZF9vbmx5IjogZmFsc2UsICJ1dWlkIjog
Ijg2Nzc1MGQ2LTk2YzctNDYyZS1iZWQ5LWQ5MGI3ZjcxZjEyNyIsICJjaG9zZW4iOiBmYWxzZSwg
ImlucHV0X3R5cGUiOiAidGV4dCIsICJ0b29sdGlwIjogIiIsICJpbnRlcm5hbCI6IGZhbHNlLCAi
cmljaF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAiX19mdW5j
dGlvbi9zcWxfcXVlcnlfc3RhdGVtZW50IiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJw
bGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJzcWxfcXVlcnlfc3RhdGVtZW50IiwgImRlZmF1bHRf
Y2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAidmFsdWVzIjogW119XSwgIm92ZXJyaWRlcyI6IFtd
LCAiZXhwb3J0X2RhdGUiOiAxNTQxNzg4ODU0MjQ4fQ==
"""
    )
