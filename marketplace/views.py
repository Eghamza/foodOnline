
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from vendor.models import Vendor
from menu.models import Categry,FoodItem
from django.db.models import Prefetch
from.context_processor import get_cart_count,get_cart_amounts
from .models import Cart
from django.contrib.auth.decorators import login_required
from vendor.models import OpeningHours
from datetime import date, datetime

# Create your views here.


def listing(request):

    vendor = Vendor.objects.all()
    vendrList = vendor.count()

    context = {
        "vendors": vendor,
        "vendrList": vendrList
    }

    return render(request, 'marketplace/listing.html',context)


def vendordetail(request,slug):
    vendor =  get_object_or_404(Vendor, slug=slug)
    today_date = date.today()
    today = today_date.isoweekday()
   
    openighours = OpeningHours.objects.filter(vendor=vendor)
    tday = OpeningHours.objects.filter(vendor=vendor,day=today)
    

   

    categry = Categry.objects.filter(vendor=vendor).prefetch_related(
        Prefetch(
            'fooditems',
            queryset = FoodItem.objects.filter(is_available=True)
            ))
    
    if request.user.is_authenticated:
        cart_item = Cart.objects.filter(user = request.user)

    else:
        cart_item = None

    context ={
        "vendors": vendor,
        'categories': categry,
        'cart_item':cart_item,
        'day': openighours,
        'today':tday,
       
    }
    return render(request, 'marketplace/vendordetail.html',context)

#add cart
def add_to_cart(request, food_id):
    #check if the user is logged in
    if request.user.is_authenticated:
        #check if the request is ajax request
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                #check if the food is already existing
                fooditem =  FoodItem.objects.get(id=food_id)
                if fooditem:
                    #check if the user already has the food item in the cart
                    try:
                        chkcart = Cart.objects.get(user = request.user, fooditem=fooditem)

                        #increment the number of items in the cart
                        chkcart.quentity += 1
                        chkcart.save()
                        return JsonResponse({'status':'success','message':'increased quantity','cart_counter':get_cart_count(request),'qty':chkcart.quentity,'amount':get_cart_amounts(request)})
                    except:

                        #create new cart if it not already exists
                        chkcart = Cart.objects.create(user = request.user,fooditem = fooditem, quentity=1)
                        return JsonResponse({'status':'success','message':'added to cart','cart_counter':get_cart_count(request),'qty':chkcart.quentity})
                    
                else: 
                #do the logic
                    return JsonResponse({'status':'failed','message':'this food does not exist'})    
        else:
            return JsonResponse({'status':'failed','message':'invalid request'})   
    else:

        return JsonResponse({'status':'login_requered','message':'You are not logged in login to continue'})      

#dicrease item
def dicrease_cart(request, food_id):
    #check if the user is logged in
    if request.user.is_authenticated:
        #check if the request is ajax request
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                #check if the food is already existing
                fooditem =  FoodItem.objects.get(id=food_id)
                if fooditem:
                    #check if the user already has the food item in the cart
                    try:
                        chkcart = Cart.objects.get(user = request.user, fooditem=fooditem)

                        #decrement the number of items in the cart

                        if chkcart.quentity >= 1:
                            chkcart.quentity -= 1
                            chkcart.save()
                        else:
                            chkcart.delete()
                            chkcart.quentity = 0
                        return JsonResponse({'status':'success','cart_counter':get_cart_count(request),'qty':chkcart.quentity,'amount':get_cart_amounts(request)})
                    except:
                        return JsonResponse({'status':'failed','message':'this food is not available in your cart'})
                    
                else: 
                #do the logic
                    return JsonResponse({'status':'failed','message':'this food does not exist'})    
        else:
            return JsonResponse({'status':'failed','message':'invalid request'})   
    else:

        return JsonResponse({'status':'login_requered','message':'You are not logged in login to continue'})
    
@login_required(login_url='login')
def cart(request):
    cart_items = Cart.objects.filter(user = request.user)
    

    context = {'cart_items': cart_items}

    return render(request, 'marketplace/cart.html',context)



def delete_cart(request,cart_id):

    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(id = cart_id)
            cart.delete()
            return JsonResponse({'status':'success','message':'This cart deleted successfully','cart_counter':get_cart_count(request),'amount':get_cart_amounts(request)})  
        except:
           
            return JsonResponse({'status':'Failed','message':'This cart does not exist'})
    else:
        return JsonResponse({'status':'Failed','message':'This cart does not exist'})