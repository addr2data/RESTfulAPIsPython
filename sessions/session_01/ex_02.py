"""ex_02.

Usage:
    ex_02 get (endpts | user) [-srjt]

Arguments:
    get

Options:
    -s      Show response status code
    -r      Show response headers
    -j      Show response body(json)
    -t      Show response body(text)
"""

from docopt import docopt
import simplejson as json
import requests


class GithubApi(object):
    """The begining of an API wrapper."""

    def __init__(self):
        pass

    def get(self, url):
        return requests.get(url)


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
    api = GithubApi()

    if args['get'] and args['endpts']:
        results = api.get("https://api.github.com/")

        # Show status code
        if args['-s']:
            print_helper("Response status code", results.status_code)

        # Show headers
        if args['-r']:
            print_helper("Response headers", dict(results.headers), pretty=True)

        # Show response body(json)
        if args['-j']:
            print_helper("Response body(json)", results.json(), pretty=True)

        # Show response body(text)
        if args['-t']:
            print_helper("Response body(text)", results.text)

        if not any([args['-s'], args['-r'], args['-j'], args['-t']]):
            print_helper("Response ", results)

    elif args['user']:
        print("To be completed by attendees.")


if __name__ == "__main__":
    main()
