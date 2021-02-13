"""ex_02.

Usage:
    ex_02 (endpts | user) [-srjt] [--type]

Arguments:
    endpts
    user

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


def print_helper(title, data, pretty=False, object_type=False):
    print(f"\n{title}")
    print("-".rjust(len(title), "-"))
    if pretty:
        print(json.dumps(data, indent=4, sort_keys=False))
    else:
        """
        if isinstance(data, str):
            print(json.dumps(data, indent=4, sort_keys=False))
            # print(json.dumps(json.loads(data), indent=4, sort_keys=False))
            return
        """
        print(data)

    if object_type:
        print(type(data))


def main():
    """The excessive commenting in not Pythonic."""
    args = docopt(__doc__)

    #Instantiate the class
    api = GithubApi()

    if args['endpts']:
        results = api.get("https://api.github.com/")

        # Show status code
        if args['-s']:
            print_helper("Response status code", results.status_code, object_type=args['--type'])

        # Show headers
        if args['-r']:
            print_helper("Response headers", dict(results.headers), pretty=True, object_type=args['--type'])

        # Show response body(json)
        if args['-j']:
            print_helper("Response body(json)", results.json(), pretty=True, object_type=args['--type'])

        # Show response body(text)
        if args['-t']:
            print_helper("Response body(text)", results.text, object_type=args['--type'])

        # Show response
        if not any([args['-s'], args['-r'], args['-j'], args['-t']]):
            print_helper("Response ", results, object_type=args['--type'])

    elif args['user']:
        print("To be completed by attendees.")


if __name__ == "__main__":
    main()
