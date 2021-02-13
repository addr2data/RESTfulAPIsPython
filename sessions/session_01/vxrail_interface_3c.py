"""VxRail interface class."""

import requests
import base64

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailError(Exception):
    # Exception class for VxRail interface.

    def __init__(self, message):
        err_msg = 'error:  ' + message
        super().__init__(err_msg)


class VxrailInterface(object):
    """Wrapper for VxRail API."""

    def __init__(self, address, port, username, password):

        """Setup initial values."""
        self.base_path = f"https://{address}:{port}/rest/vxm"
        encoded_u = base64.b64encode(f'{username}:{password}'.encode('ascii')).decode('ascii')
        self.headers = {"Authorization" : f"Basic {encoded_u}"}


    def get(self, url):

        try:
            response = requests.get(f"{self.base_path }/{url}", headers=self.headers, verify=False)

            try:
                response.raise_for_status()
                return response.json()

            except requests.HTTPError:

                if str(response.status_code) == "401":
                    errmsg = "Login failed. Check username/password."

                elif str(response.status_code) == "404":
                    errmsg = "Bad url."

                raise VxrailError(errmsg)

        except requests.exceptions.RequestException as errmsg:
            raise VxrailError("General requests error occured")