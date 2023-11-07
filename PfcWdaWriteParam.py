# Script for Write WDA Data out of Wago PFC
# More information on http://<pfc_ip>/openapi/wda.openapi.html
# Author:        Michael Drost
# Version:       0.2
# PythonVersion: 3.7.3

import requests
import json
import time
import os


# ++++ Controller IP
ip = '192.168.2.129'
# ++++ Authorization for Wago Controller
username = "admin"
password = "wago"


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ++++ The Api Endpoints 
#"https://192.168.2.129/wda/devices"
#"https://192.168.2.129/wda/parameters"
#"https://192.168.2.129/wda/features"
#"https://192.168.2.129/wda/methods"


# ++++ The Api Endpoint 
url = "https://"+ip+"/wda/parameters"

# ++++ write Parameter
# 1. Set acutal Time
# 2. activate Docker
headers={'Content-Type': 'application/vnd.api+json'}
print(bcolors.WARNING + "write parameters")

parameter = {
    "data": [
        {"id": "0-0-systemtime-now",
        "type": "parameters",
        "attributes": {
            "value": 1686037778
        }},
        {"id": "0-0-docker-enabled",
        "type": "parameters",
        "attributes": {
            "value": True
        }}
    ]       
}
# set actual millis
ts = time.time()
parameter["data"][0]["attributes"]["value"] = int(ts)
response  = requests.patch(url, auth=(username, password), data=json.dumps(parameter), headers=headers, verify=False)
print(bcolors.OKGREEN + "done!")

# ++++ Check if Docker is Running
print(bcolors.WARNING + "check parameters")
url             = "https://"+ip+"/wda/parameters/0-0-docker-isRunning"
response        = requests.get(url, auth=(username, password), verify=False)
response_json   = response.json()
print("Docker state is: " + str(response_json["data"]["attributes"]["value"]))
print(bcolors.OKGREEN + "Done!")


