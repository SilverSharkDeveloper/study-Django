from django.db.models import Sum, Count, Max, Subquery, F
from django.test import TestCase

from cart.models import Cart
from member.models import Member
from product.models import Product


# Create your tests here.
class CartTest(TestCase):
    # member = Member.objects.get(id=2)
    # product = Product.objects.get(product_name="마우스")
    # Cart.objects.create(product=product,member=member,product_count=5).save()


    # 각 회원의 장바구니 목록 조회
    # member1 = Member.objects.get(id=1)
    # member2 = Member.objects.get(id=2)
    # cart1= Cart.objects.values("member").annotate(product=Subquery())
    # print(cart1)
    # for cart in cart1:
    #     print(cart)
    # cart2 = Cart.objects.filter(member=member2)
    # for cart in cart2:
    #     print(cart)

    # 전체 회원의 장바구니에서 가장 많이 담긴 상품 정보 조회
    total = Cart.objects.values("product").annotate(total=Sum("product_count")).values("total","product__product_name").order_by("-total").first()
    print(total)

    # 장바구니에 담긴 상품의 전체 개수가 가장 많은 회원의 정보 조회
    total= Cart.objects.values("member").annotate(total = Sum("product_count")).values("total","member__member_name").order_by("-total").first()
    print(total)
    # 장바구니에 아무것도 담지 않은 회원의 정보 조회
    members = Member.objects.filter(cart__isnull=True)
    print(members)
    # 장바구니에 한 번이라도 담긴 상품 목록 조회
    products = Cart.objects.filter(product__isnull=False).distinct().values("product__product_name")
    print(products)
    pass
