from .models import Cart


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