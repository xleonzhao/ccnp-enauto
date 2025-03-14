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
def get_site(token):
    url = f"https://{dnac}/dna/intent/api/v1/site"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Auth-Token": token
    }

    response = requests.get(url, headers=headers, verify=False)

    site = None
    if response.status_code == 200:
        site = response.json().get("response")
        print(f"Site retrieved successfully! Status Code: {response.status_code}")
    else:
        print(f"Failed to get system site! Status Code: {response.status_code}, Error: {response.text}")

    return site

@retry(stop_max_attempt_number=3, wait_fixed=2000)
@timeout(10)
def get_site_health(token):
    url = f"https://{dnac}/dna/intent/api/v1/site-health"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Auth-Token": token
    }

    response = requests.get(url, headers=headers, verify=False)

    health = None
    if response.status_code == 200:
        health = response.json().get("response")
        print(f"Site health retrieved successfully! Status Code: {response.status_code}")
    else:
        print(f"Failed to get system health! Status Code: {response.status_code}, Error: {response.text}")

    return health

######################
# Main Function
######################
debug = True
if __name__ == "__main__":
    try:
        token = get_token(username, password)
        print(f"Authentication Token: {token}")
    except Exception as e:
        print(f"Token retrieval failed: {e}")

    if not token:
        exit()
    
    try:
        site = get_site(token)
        pprint(site) if debug else None
    except Exception as e:
        print(f"System health retrieval failed: {e}")

    try:
        health = get_site_health(token)
        pprint(health) if debug else None
    except Exception as e:
        print(f"System health retrieval failed: {e}")