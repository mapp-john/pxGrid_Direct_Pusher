import requests
import csv

ise_pan = "1.1.1.1"
connector_name = "Test-Pusher"
pxgrid_direct_user = "pxgrid_user"
pxgrid_direct_password = "pxgrid_password"

pxgrid_direct_url = f"https://{ise_pan}/api/v1/pxgrid-direct/push/{connector_name}/bulk"

data = []
with open("pxdirect_pusher_endpoints_delete.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

## Delete individual entry using bulk call
# pxgrid_direct_data = {
#     "operation": "delete",
#     "data": [
#         {
#             "mac": "66:66:66:66:66:66",
#             "hostname": "nyc-hv-01",
#             "type": "iot",
#             "role": "hvac",
#             "location": "New York",
#         }
#     ],
# }

pxgrid_direct_data = {"operation": "delete", "data": data}

r = requests.post(
    pxgrid_direct_url,
    auth=(pxgrid_direct_user, pxgrid_direct_password),
    verify=False,
    json=pxgrid_direct_data,
)

# Raise an exception for HTTP errors
r.raise_for_status()
