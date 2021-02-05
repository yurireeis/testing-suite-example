from tests.api.api_base_test import APIBaseTest
from tests.api.services.order_service import OrderService


class SystemOrderTest(APIBaseTest):
    order_service = OrderService()

    def test_all_orders(self):
        response, data = self.order_service.all()
        self.assertEqual(response.code, 200)


    def test_create_order(self):
        data = {
            "CreateAt": "Mon, 11 Jan 2021 20:13:58 GMT",
            "ExternalId": "9ddec533-b259-42f6-8bf4-9929381d8fd5",
            "Items": [
                {
                "Description": "Cerveja Heineken",
                "Quantity": 1,
                "Price": 7.56
                }
            ],
            "OrderId": "8ccdb422-b259-42f6-8bf4-8829381d7ed4",
            "Status": "paid",
            "TotalOrder": 7.56,
            "LastUpdate": "Mon, 11 Jan 2021 20:13:58 GMT",
            "Wallet": "HappyPay"
        }
        response, data = self.order_service.create(data)
        self.assertEqual(response.code, 201)


    def test_find_order(self):
        data = {}
        response, created_data = self.order_service.create(data)
        order_id = created_data['OrderId']
        response, found_data = self.order_service.find(order_id)
        self.assertEqual(response.code, 200)
        self.assertIsNotNone(found_data)
        self.assertDictEqual(created_data, found_data)

