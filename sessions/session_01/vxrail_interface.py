"""VxRail interface class."""

import requests
import base64

# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class VxrailError(Exception):
    """Exception raised when an interface error occurs."""

    def __init__(self, message):
        """Class init."""
        err_msg = 'error:  ' + message
        super(VxrailError, self).__init__(err_msg)


class VxrailInterface(object):
    """Wrapper for VxRail API."""

    def __init__(self, address, username, password):
        """Setup initial values."""
        self.username = username
        self.password = password
        self.base_path = f"https://{address}:8443/rest/vxm"

        encoded_u = base64.b64encode(f'{username}:{password}'.encode('ascii')).decode('ascii')
        self.headers = {"Authorization" : f"Basic {encoded_u}"}





    def get(self, url):
        # response = requests.get(f"{self.base_path }/{url}", auth=(self.username, self.password))
        response = requests.get(f"{self.base_path }/{url}", headers=self.headers, verify=False)
        print(response.status_code)
        return response.json()
