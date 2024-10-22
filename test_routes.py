def test_get_product_by_name(self):
    response = self.client.get("/products?name=TestProduct")
    self.assertEqual(response.status_code, 200)
    self.assertIn("TestProduct", response.data)
