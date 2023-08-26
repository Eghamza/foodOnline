from django.shortcuts import render,get_object_or_404,redirect
from accounts.forms import UserProfileForm
from accounts.models import UserProfile
from .models import Vendor
from  .forms import vendonForm
from menu.models import Categry, FoodItem
from django.contrib import messages
from menu.forms import add_category_forms
from django.template.defaultfilters import slugify
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



def add_category(request):
    form = add_category_forms(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            vendor = Vendor.objects.get(user = request.user)
            category=form.save(commit=False)
            category_name = form.cleaned_data['category_name']
            category.vendor = vendor
            category.slug = slugify(category_name)
            category.save()
            messages.success(request,"category added successfully")
            return redirect('menu_builder')
        else:
            print(form.errors)
    else:
        form = add_category_forms()


    context ={
        'form':form

    }
    return render(request, 'vendor/add_category.html',context)



def edit_category(request, pk=None):
    categry = get_object_or_404(Categry, pk=pk)
    if request.method == 'POST':
        form = add_category_forms(request.post, instance=categry)
        if form.is_valid():
            vendor = Vendor.objects.get(user = request.user)
            category=form.save(commit=False)
            category_name = form.cleaned_data['category_name']
            category.vendor = vendor
            category.slug = slugify(category_name)
            category.save()
            messages.success(request,"category Edit successfully")
            return redirect('menu_builder')
        else:
            pass
    else:
        form = add_category_forms(instance= categry)

    context= {
        'form': form,
        'category': categry

    }
    return render(request, 'vendor/edit_category.html',context)