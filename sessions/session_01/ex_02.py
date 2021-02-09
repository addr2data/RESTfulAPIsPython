"""ex_01.

Usage:
    ex_01 get_endpts (-s | -j | -t | -r) [-pz]
    ex_01 get_user [-v]
    ex_01 show_args

Arguments:
    get_endpts
    get_user
    show_args

Options:
    -s      Return status Code
    -j      Return json data
    -t      Return text
    -r      Return headers
    -p      Print pretty
    -z      Print type
"""

from docopt import docopt
import simplejson as json
import prettyprinter
from ex_01_classes import GithubApi


def main():
    """The excessive commenting in not Pythonic."""
    args = docopt(__doc__)

    #Instantiate the class
    api = GithubApi("https://api.github.com/")

    # Make decisions based on arguments and options
    if args['show_args'] is True:  # This is not Pythonic
        print(args)

    elif args['get_endpts']:  # This is Pythonic

        # Gets status code
        if args['-s']:
            results = api.status()

        # Gets headers
        elif args['-r']:
            # results = api.headers()
            results = dict(api.headers())

        # Gets json
        elif args['-j']:
            results = api.json()

        # Gets text
        elif args['-t']:
            # results = api.text()
            results = json.loads(api.text())

        # Print pretty option
        if args['-p']:
            # prettyprinter.pprint(results)
            print(json.dumps(results, indent=4, sort_keys=False))
        else:
            print(results)

        # Print data type option
        if args['-z']:
            print(type(results))

    elif args['show_args']:
        get_user()


if __name__ == "__main__":
    main()
