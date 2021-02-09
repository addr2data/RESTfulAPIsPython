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


def main():
    """The excessive commenting in not Pythonic."""
    args = docopt(__doc__)

    #Instantiate the class
    api = GithubApi()

    if args['get'] and args['endpts']:
        results = api.get("https://api.github.com/")

        # Show status code
        if args['-s']:
            print("\nResponse status code")
            print("--------------------")
            print(results.status_code)

        # Show headers
        if args['-r']:
            print("\nResponse Headers")
            print("----------------")
            print(json.dumps(dict(results.headers), indent=4, sort_keys=False))

        # Show response body(json)
        if args['-j']:
            print("\nResponse body(json)")
            print("-------------------")
            print(json.dumps(dict(results.json()), indent=4, sort_keys=False))

        # Show response body(text)
        if args['-t']:
            print("\nResponse body(text)")
            print("-------------------")
            print(results.text)

        if not any([args['-s'], args['-r'], args['-j'], args['-t']]):
            print("\nResponse")
            print("--------")
            print(results)

    elif args['user']:
        results = api.get("https://api.github.com/")
        url = results.json()['user_url'].replace("{user}", "addr2data")
        results = api.get(url)
        print(results.status_code)
        print(results.headers)
        print(results.json())


if __name__ == "__main__":
    main()
