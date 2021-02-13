"""ex_03.

Usage:
    ex_03 collect [-j]

Arguments:
    collect

Options:
    -j      Show response body(json)

"""

import sys
from docopt import docopt
import simplejson as json
from vxrail_interface import VxrailInterface, VxrailError


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
    api = VxrailInterface("127.0.0.1", "test", "test")

    if args['collect']:
        try:
            results = api.get("v1/system")
        except VxrailError as err:
            sys.exit(err)

        # Show response body(json)
        if args['-j']:
            print_helper("Response body(json)", results, pretty=True)



if __name__ == "__main__":
    main()