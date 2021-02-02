from tests.api.api_base_test import APIBaseTest
from tests.api.services.http_client import HttpClient


class SystemOrderTest(APIBaseTest):
    client = HttpClient(APIBaseTest.API_BASE_URL, is_https=True)

    def test_all_orders(self):
        response, data = self.client.request('GET', f'/order')
        status_code = response.getcode()
        self.assertEqual(status_code, 200)
    
    def test_create_order(self):
        response, data = self.client.request('POST', f'/order')
        status_code = response.getcode()
        self.assertEqual(status_code, 200)

    def test_find_order(self):
        response, created_data = self.client.request('POST', f'/order')
        order_id = created_data['OrderId']
        response, found_data = self.client.request('GET', f'/order/{order_id}')
        status_code = response.getcode()
        self.assertEqual(status_code, 200)
        self.assertIsNotNone(found_data)
        self.assertDictEqual(created_data, found_data)
