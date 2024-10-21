import factory
from myapp.models import Product

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    category = factory.Faker('word')
    available = factory.Faker('boolean')
