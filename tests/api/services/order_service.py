from tests.api.api_base_test import APIBaseTest
from shared.services.http_client import HttpClient


class OrderService:
    client = HttpClient(APIBaseTest.API_BASE_URL, is_https=True)

    def all(self):
        return self.client.request('GET', f'/order')

    def create(self, data=None, headers=None):
        return self.client.request('POST', f'/order', data, headers)

    def find(self, id):
        return self.client.request('GET', f'/order/{id}')

