"""VxRail interface class."""

import requests
import base64

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailInterface(object):
    """Wrapper for VxRail API."""

    def __init__(self, address, port, username, password):

        """Setup initial values."""
        self.base_path = f"https://{address}:{port}/rest/vxm"
        encoded_u = base64.b64encode(f'{username}:{password}'.encode('ascii')).decode('ascii')
        self.headers = {"Authorization" : f"Basic {encoded_u}"}


    def get(self, url):
        
        try:
            # Step 11
            # response = requests.get(f"{self.base_path }/{url}", headers=self.headers)

            # Step 13
            response = requests.get(f"{self.base_path }/{url}", headers=self.headers, verify=False)
            return response.json()
        except requests.exceptions.RequestException:
            raise

        
        
