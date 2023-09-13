from django.test import TestCase

from cart.models import Cart
from member.models import Member
from product.models import Product


# Create your tests here.
class ProductTest(TestCase):

    Product.objects.bulk_create([
        Product(product_name="마우스",product_price=25000,product_stock=20),
        Product(product_name="박카스",product_price=3000,product_stock=20),
        Product(product_name="볼펜",product_price=800,product_stock=100)
    ])

    pass