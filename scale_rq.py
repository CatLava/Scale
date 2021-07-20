# This file will hold the request framework
import requests
from requests.auth import HTTPBasicAuth




class Get_Frame:
    def __init__(self, url):
        self.url = url
        #self.token = token

    def __call__(self, url, token, params=''):
        print(url)
        print(token)
        headers = {"Accept": "application/json"}

        # Note API keys could be better documented in the UI, no date created or created by what user
        auth = HTTPBasicAuth(token, '')  # No password


        # weak check on params but remains flexible
        if params != '':
            response = requests.request("GET", url, headers=headers, auth=auth, params=params)

        else:
            response = requests.request("GET", url, headers=headers, auth=auth)

        #print(response.text)
        return response.json()