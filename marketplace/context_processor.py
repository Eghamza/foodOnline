from .models import Cart
from menu.models import FoodItem

def get_cart_count(request):
    cart_counter = 0
    try:
        cart_items = Cart.objects.filter(user = request.user)
        if cart_items:
            for cart_item in cart_items:
                cart_counter += cart_item.quentity
        else:
            cart_counter= 0        

    except:
        cart_counter = 0
    return dict(cart_counter=cart_counter)


def get_cart_amounts(request):
    subtotal= 0
    tex = 0
    grandtotal= 0
    try:
        cart_items = Cart.objects.filter(user = request.user)
        for item in cart_items:
            fooditem = FoodItem.objects.get(pk = item.fooditem.id)
            subtotal += fooditem.price * item.quentity
        grandtotal = tex + subtotal
        
        return dict(grandtotal=grandtotal, tex=tex, subtotal=subtotal)
    except:
        subtotal= 0
        tex = 0
        grandtotal= 0
        return dict(grandtotal=grandtotal, tex=tex, subtotal=subtotal)