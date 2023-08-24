from django.shortcuts import render,get_object_or_404,redirect
from accounts.forms import UserProfileForm
from accounts.models import UserProfile
from .models import Vendor
from  .forms import vendonForm
from menu.models import Categry, FoodItem
from django.contrib import messages
# Create your views here.


def profile(request):
    user_profile = get_object_or_404(UserProfile,user = request.user)   
    vender_instance = get_object_or_404(Vendor, user = request.user)
    #update 
    if request.method == 'POST':
        user_p = UserProfileForm(request.POST,request.FILES,instance=user_profile)
        vendor =vendonForm(request.POST,request.FILES,instance=vender_instance)
        if user_p.is_valid() and vendor.is_valid():
            user_p.save()
            vendor.save()
            messages.success(request,"Profile updated")
            return redirect('vprofile')
        else:
           print("--------------------",user_p.errors)
           print("--------------------",vendor.errors)
    
    else:
        vendor = vendonForm(instance=vender_instance)
        user_p = UserProfileForm(instance = user_profile)

    context ={
        'profile': user_p,
        'vendorform': vendor,
        'user_p':user_profile,
        'vender_instance': vender_instance,
    }
    return render(request, 'vendor/vprofile.html',context)


def menu_builder(request):
    vendor = Vendor.objects.get(user = request.user)
    print(vendor)
    categories = Categry.objects.filter(vendor = vendor)
    context = {'categories': categories}
    return render(request, 'vendor/menu_builder.html',context)


def food_item_category(request,pk=None):
    vendor = Vendor.objects.get(user = request.user)
    categories = get_object_or_404(Categry, pk=pk)
    fooditem = FoodItem.objects.filter(vendor = vendor, categry = categories)
    context = {'categories': categories,
               'fooditem': fooditem,
               }

    return render(request, 'vendor/food_item_item.html',context)