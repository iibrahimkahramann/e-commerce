from decimal import Decimal
from .models import CartItem

def calculate_total_price(cart):
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = Decimal(0)

    for cart_item in cart_items:
        product_price = cart_item.product.price
        quantity = cart_item.quantity
        total_price += product_price * quantity

    return total_price
