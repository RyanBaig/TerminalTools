"""
EnvHub Python SDK.

Available Commands:
- Get Environment Variable
"""
import requests
from requests.exceptions import ConnectionError

def get_var(name):
    r = requests.get('https://envhub.ryanbaig.vercel.app/api/vars?varName=' + name)
    if r.status_code == 200:
        return r.json()["value"]
    else:
        raise ConnectionError(r.json())