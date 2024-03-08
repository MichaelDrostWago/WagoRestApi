# Script for Reading WDA Data out of Wago PFC
# More information on http://<pfc_ip>/openapi/wda.openapi.html
# Author:        Michael Drost
# Version:       0.1
# PythonVersion: 3.7.3

import requests
import json
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

# ++++ The Api Endpoint 
url = "https://"+ip+"/wda/devices"

# ++++ Get Request
print(bcolors.WARNING + "read parameter")
response = requests.get(url, auth=(username, password), verify=False)
os.system("clear")

# ++++ print response
response_json = response.json()
#print(response_json)

# ++++ display order number and fw version
data = response_json["data"]
firmwareVersion = data[0]["attributes"]["firmwareVersion"]
orderNumber     = data[0]["attributes"]["orderNumber"]
print("Order Number: " + orderNumber)
print("FW-Version:   " + firmwareVersion)
print(bcolors.OKGREEN + "done!")

# ++++ The Api Endpoint 
url = "https://"+ip+"/wda/parameters"

# ++++ Get Request
print(bcolors.WARNING + "write actConfig.txt")
response = requests.get(url, auth=(username, password), verify=False)
os.system("clear")

# ++++ print response
response_json = response.json()
data          = response_json["data"]

f = open("actConfig.txt", "w")
for x in data:
    id = x["id"] 
    value = x["attributes"]["value"]
    f.write(id + " = " + str(value) + "\n")
    print(id + " = " + str(value))
f.close()    

print(bcolors.OKGREEN + "done!")
print(bcolors.ENDC)
