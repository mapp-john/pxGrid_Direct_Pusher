import requests
import json

ise_pan = "1.1.1.1"
connector_name = "Test-Pusher"
unique_id = "00001"
pxgrid_direct_user = "pxgrid_user"
pxgrid_direct_password = "pxgrid_password"

pxgrid_direct_url = f"https://{ise_pan}/api/v1/pxgrid-direct/push/{connector_name}/{unique_id}"

pxgrid_direct_data = {
    "id": "00001",
    "mac": "55:55:55:55:55:55",
    "hostname": "sjc-hv-01",
    "type": "iot",
    "role": "hvac",
    "location": "San Diego",
}

r = requests.put(
    pxgrid_direct_url,
    auth=(pxgrid_direct_user, pxgrid_direct_password),
    verify=False,
    json=pxgrid_direct_data,
)

# Raise an exception for HTTP errors
r.raise_for_status()
# Print response
print(json.dumps(r.json(), indent=4))
