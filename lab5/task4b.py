import yaml
import json
import requests
import logging
from requests.auth import HTTPBasicAuth

logging.basicConfig(level=logging.INFO)

USER = "student"
PASS = "Meilab123"

def set_interface(host, interface):

    url = f"http://{host}/restconf/api/running/interfaces/interface/{interface['name']}"

    headers = {
        "Accept": "application/vnd.yang.data+json",
        "Content-Type": "application/vnd.yang.data+json"
    }

    payload = {
        "ietf-interfaces:interface": {
            "name": interface["name"],
            "description": "Configured via YAML automation",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": interface["ip"],
                        "netmask": interface["mask"]
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    }

    response = requests.put(
        url,
        auth=HTTPBasicAuth(USER, PASS),
        headers=headers,
        data=json.dumps(payload)
    )

    if response.status_code in [200, 201, 204]:
        logging.info(f"{interface['name']} configured successfully on {host}")
    else:
        logging.error(f"Failed on {host} {interface['name']}: {response.text}")


# Load YAML
with open("routers_question1.yaml", "r") as f:
    data = yaml.safe_load(f)

# Loop through routers and interfaces
for router in data["routers"]:
    host = router["host"]

    for interface in router["interfaces"]:
        set_interface(host, interface)
