def test_find_by_name(self):
    product = Product(name="TestProduct", category="Electronics", available=True)
    product.save()
    result = Product.find_by_name("TestProduct")
    assert result.name == "TestProduct"
