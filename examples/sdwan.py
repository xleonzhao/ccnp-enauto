import requests
from dotenv import load_dotenv
import os
import urllib3
from retrying import retry
from timeout_decorator import timeout

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()

@retry(stop_max_attempt_number=3, wait_fixed=2000)
@timeout(5)
def get_access_token(vmanage_ip, username, password):
    url = f"https://{vmanage_ip}:8443/j_security_check"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "j_username": username,
        "j_password": password
    }

    response = requests.post(url, headers=headers, data=data, verify=False)
    response.raise_for_status()

    return response.cookies.get("JSESSIONID")

@retry(stop_max_attempt_number=3, wait_fixed=2000)
@timeout(5)
def get_device_list(vmanage_ip, token):
    url = f"https://{vmanage_ip}:8443/dataservice/device"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"JSESSIONID={token}"
    }

    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()

    return response.json()

vmanage_ip = "10.10.20.90"
username = os.getenv("vmanager.username")
password = os.getenv("vmanager.password")

access_token = get_access_token(vmanage_ip, username, password)
print(f"Access token: {access_token}")

dev_format="{0:20s}{1:2s}{2:12s}{3:2s}{4:46s}{5:2s}{6:16s}{7:2s}{8:7s}"
print(dev_format.format("Host-Name", "|", "Device Type", "|", "Device ID", "|", "System IP", "|", "Site ID"))
print("-" * 110)

device_list = get_device_list(vmanage_ip, access_token)
for device in device_list["data"]:
    print(dev_format.format(device["host-name"], "|", device["device-type"], "|", device["deviceId"], "|", device["system-ip"], "|", device["site-id"])) 
