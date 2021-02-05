from http.client import HTTPSConnection, HTTPConnection
import json


class HttpClient:

    def __init__(self, url, is_https=False, default_header=None, port=None):
        connection = HTTPSConnection if is_https else HTTPConnection
        self.default_header = default_header if default_header else {}
        self.client = connection(url, port=port)

    def request(self, verb, uri, body=None, headers=None):
        body = json.dumps(body) if body else json.dumps({})
        headers = json.dumps(headers) if headers else self.default_header
        self.client.request(verb, uri, body=body, headers=headers)
        data = None

        try:
            response = self.client.getresponse()
            data = response.read().decode()
        except Exception as e:
            response = e
        finally:
            self.client.close()
        return response, json.loads(data)
