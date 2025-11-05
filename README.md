# pxgrid-direct-pusher - Cisco ISE 3.4+
## Setup pxGrid Direct Pusher Connector
1. Create a new ERS Admin user if you haven't already
2. Navigate to ***Administration -> Network Resources -> pxGrid Direct Connectors***
3. Click "Add", then click "Let's Do It"
4. Enter Name for connector "Test-Pusher"
5. Select "URL Pusher", then click "Next"
6. Select your admin groups to allow access, by default "Super Admin" and "ERS Admin" will be selected for Read & Write
7. Click "Next"
8. Enter Sample JSON
```
{
    "id": "00001",
    "mac": "55:55:55:55:55:55",
    "hostname": "sjc-hv-01",
    "type": "iot",
    "role": "hvac",
    "location": "San Jose"
}
```
9. Click "Next"
10. Enable CoA
11. Select "Include all in Dictionary" and "Enable CoA for all"
12. Click "Next"
13. For "Unique Identifier" dropdown, select "id"
14. For "Correlation Identifier" dropdown, select "mac"
15. Click "Next"
16. Review Summary, then click "Done"

## View Endpoints in Dictionary
1. Navigate to ***Context Visibility -> Endpionts -> pxGrid Direct***
2. If you have multiple pxGrid Direct Connectors, select "Test-Pusher" from the dropdown
