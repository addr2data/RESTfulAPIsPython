"""ex_03.

Usage:
    ex_03 disks [-j]
    ex_03 each_disk [-j]

Arguments:
    disks

Options:
    -j      Show response body(json)

"""

import sys
from docopt import docopt
import simplejson as json
from vxrail_interface_3c import VxrailInterface, VxrailError


def print_helper(title, data, pretty=False):
    print(f"\n{title}")
    print("-".rjust(len(title), "-"))
    if pretty:
        print(json.dumps(data, indent=4, sort_keys=False))
    else:
        print(data)


def main():
    """The excessive commenting in not Pythonic."""
    args = docopt(__doc__)

    #Instantiate the class

    # Step 15
    api = VxrailInterface(address="127.0.0.1", port=8443, username="test", password="test")

    # Step 17
    # api = VxrailInterface(address="127.0.0.1", port=8443, username="test", password="badpassword")

    if args['disks']:

        # Make the API call
        try:
            # Step 19a
            results = api.get("v1/disks")

            # Step 19b
            # results = api.get("v1/system1234")

        except VxrailError as err: 
            sys.exit(err)

        # Show response body(json)
        print_helper("Response body(json)", results, pretty=args['-j'])


    elif args['each_disk']:
        print("To be completed by attendees.")
        
        """ Attendee notes.

        - Start with GET v1/disks
        - Extract 'sn' for each disk
        - Use GET v1/disks{disk_sn} on subsequent calls.
        """


if __name__ == "__main__":
    main()
        
