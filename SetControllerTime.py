import requests
import time
from requests.auth import HTTPBasicAuth

# Script Parameter
username = "admin"
password = "wago"
ipAddress = "192.168.2.105"



# Ziel-URL
url = "https://"+ipAddress+"/wda/parameters/0-0-systemtime-now"


current_timestamp = int(time.time())

# JSON:API-konforme Payload
payload = {
    "data": {
        "id": "0-0-systemtime-now",
        "type": "parameters",
        "attributes": {
            "value": current_timestamp
        }
    }
}

# Header mit korrektem Content-Type
headers = {
    "Content-Type": "application/vnd.api+json"
}


# PATCH-Request senden
response = requests.patch(
    url,
    json=payload,
    headers=headers,
    auth=HTTPBasicAuth(username, password),
    verify=False  # Nur bei selbstsignierten Zertifikaten
)

# Antwort ausgeben
print("Status Code:", response.status_code)
