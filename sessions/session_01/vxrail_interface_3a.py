"""VxRail interface class."""

import requests
import base64

# Step 6
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailInterface(object):
    """Wrapper for VxRail API."""

    def __init__(self, address, port, username, password):

        """Setup initial values."""
        self.base_path = f"https://{address}:{port}/rest/vxm"
        encoded_u = base64.b64encode(f'{username}:{password}'.encode('ascii')).decode('ascii')
        self.headers = {"Authorization" : f"Basic {encoded_u}"}

        # Step 8
        # self.username = username
        # self.password = password


    def get(self, url):

        # Step 2
        response = requests.get(f"{self.base_path }/{url}", headers=self.headers)

        # Step 4
        # response = requests.get(f"{self.base_path }/{url}", headers=self.headers, verify=False)
        
        # Step 8
        # response = requests.get(f"{self.base_path }/{url}", auth=(self.username, self.password), verify=False)
        
        return response.json()
