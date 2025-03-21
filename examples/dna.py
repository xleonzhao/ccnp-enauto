import requests
import urllib3
from retrying import retry
from timeout_decorator import timeout
from pprint import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

######################
# DNA Center Settings
######################
dnac = "sandboxdnac2.cisco.com"
username="devnetuser"
password="Cisco123!"
token = None
dna_api = {
    "get_site": f"https://{dnac}/dna/intent/api/v1/site",
    "get_site_health": f"https://{dnac}/dna/intent/api/v1/site-health",
    "get_devices": f"https://{dnac}/dna/intent/api/v1/network-device",
    "get_device": f"https://{dnac}/dna/intent/api/v1/network-device/_ARG0_",
}

######################
# Functions
######################
@retry(stop_max_attempt_number=3, wait_fixed=2000)
@timeout(10)
def get_token(username, password):
    url = f"https://{dnac}/dna/system/api/v1/auth/token"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, auth=(username, password), verify=False)

    token = None
    if response.status_code == 200:
        token = response.json().get("Token")  # Extract token from response
    else:
        print(f"Failed to get token! Status Code: {response.status_code}, Error: {response.text}")

    return token

@retry(stop_max_attempt_number=3, wait_fixed=2000)
@timeout(10)
def call_dna_api(token, url):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Auth-Token": token
    }

    response = requests.get(url, headers=headers, verify=False)

    data = None
    if response.status_code == 200:
        data = response.json().get("response")
        print(f"data retrieved successfully! Status Code: {response.status_code}")
    else:
        print(f"Failed to get data! Status Code: {response.status_code}, Error: {response.text}")

    return data

def call_dna(token, api, *args):
    if not token:
        return

    if api not in dna_api.keys():
        print(f"Invalid API: {api}")
        return
    
    resp = None
    try:
        url = dna_api[api]
        if args:
            for i in range(len(args)):
                url = url.replace(f"_ARG{i}_", args[i])
        resp = call_dna_api(token, url)
        pprint(resp) if debug else None
    except Exception as e:
        print(f"System health retrieval failed: {e}")

    return resp

######################
# Main Function
######################
debug = False
if __name__ == "__main__":
    try:
        token = get_token(username, password)
        print(f"Authentication Token: {token}")
    except Exception as e:
        print(f"Token retrieval failed: {e}")

    # call_dna(token, "get_site")
    # call_dna(token, "get_site_health")
        
    data = call_dna(token, "get_devices")
    for i in range(len(data)):
        dev_id = data[i]['id']
        print(f"device ID = {dev_id}")
        dev_data = call_dna(token, "get_device", dev_id)
        pprint(dev_data)

    