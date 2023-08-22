from django.shortcuts import render,get_object_or_404,redirect
from accounts.forms import UserProfileForm
from accounts.models import UserProfile
from .models import Vendor
from  .forms import vendonForm
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
        print("-------------------- hello world")
        vendon = vendonForm(instance=vender_instance)
        p = UserProfileForm(instance = user_profile)

    context ={
        'profile': p,
        'vendorform': vendon,
        'user_p':user_profile,
        'vender_instance': vender_instance,
    }
    return render(request, 'vendor/vprofile.html',context)
