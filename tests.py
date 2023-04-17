import unittest
import app
class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b'Product Catalog', response.data)

    def test_purchase_item(self):
        response = self.app.post('/purchase', data={
            'product_name': 'Brush',
            'quantity': '2',
            'total_price': '10'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'successfully adding to cart', response.data)

    def test_purchase_history(self):
        response = self.app.get('/cart')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Purchased Items', response.data)

    def test_update_quantity(self):
        response = self.app.post('/update_quantity', data={
            'product_id': '6080cfb8a74e7a454049c123',
            'quantity': '3'
        })
        self.assertEqual(response.status_code, 302)

    def test_delete_product(self):
        response = self.app.post('/remove_product', data={
            'product_id': '6080cfb8a74e7a454049c123'
        })
        self.assertEqual(response.status_code, 302)


if __name__ == '__main__':
    unittest.main()
