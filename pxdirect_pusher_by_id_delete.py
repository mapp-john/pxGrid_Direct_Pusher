import requests

ise_pan = "1.1.1.1"
connector_name = "Test-Pusher"
unique_id = "66:66:66:66:66:66"
pxgrid_direct_user = "pxgrid_user"
pxgrid_direct_password = "pxgrid_password"

pxgrid_direct_url = f"https://{ise_pan}/api/v1/pxgrid-direct/push/{connector_name}/{unique_id}"

r = requests.delete(
    pxgrid_direct_url,
    auth=(pxgrid_direct_user, pxgrid_direct_password),
    verify=False,
)

# Raise an exception for HTTP errors
r.raise_for_status()
