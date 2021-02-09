"""ex_01.

Usage:
    ex_01 get (endpts | user)  (-s | -j | -t | -r) [-pz]

Arguments:
    get

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
import requests


class GithubApi(object):

    def __init__(self, url):
        self.url = url

    def _get(self):
        return requests.get(self.url)

    def default(self):
        return self._get()

    def status(self):
        return self._get().status_code

    def json(self):
        return self._get().json()

    def text(self):
        return self._get().text

    def headers(self):
        return self._get().headers


def main():
    """The excessive commenting in not Pythonic."""
    args = docopt(__doc__)

    #Instantiate the class
    api = GithubApi("https://api.github.com/")

    if args['get_endpts']:

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
