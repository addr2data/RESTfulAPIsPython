"""Class(es) for ex_01."""

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
