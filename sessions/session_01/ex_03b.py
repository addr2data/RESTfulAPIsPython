"""ex_03.

Usage:
    ex_03 system [-j]

Arguments:
    system

Options:
    -j      Show response body(json)

"""

import sys
from docopt import docopt
import simplejson as json
from vxrail_interface_3b import VxrailInterface


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
    api = VxrailInterface(address="127.0.0.1", port=8443, username="test", password="test")

    if args['system']:

        # Using broad exceptions like this is not Pythonic
        try:
            results = api.get("v1/system")
        except Exception as err: 
            sys.exit(err)

        # Show response body(json)
        print_helper("Response body(json)", results, pretty=args['-j'])


if __name__ == "__main__":
    main()
        
