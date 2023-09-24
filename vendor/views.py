from django.shortcuts import render, get_object_or_404, redirect
from accounts.forms import UserProfileForm
from accounts.models import UserProfile
from .models import Vendor,OpeningHours
from .forms import vendonForm, openingForm
from menu.models import Categry, FoodItem
from django.contrib import messages
from menu.forms import add_category_forms,food_item_forms
from django.http import HttpResponse,JsonResponse
from django.template.defaultfilters import slugify
from .models import OpeningHours
from django.db import IntegrityError
# Create your views here.


def profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    vender_instance = get_object_or_404(Vendor, user=request.user)
    # update
    if request.method == 'POST':
        user_p = UserProfileForm(
            request.POST, request.FILES, instance=user_profile)
        vendor = vendonForm(request.POST, request.FILES,
                            instance=vender_instance)
        if user_p.is_valid() and vendor.is_valid():
            user_p.save()
            vendor.save()
            messages.success(request, "Profile updated")
            return redirect('vprofile')
        else:
           pass

    else:
        vendor = vendonForm(instance=vender_instance)
        user_p = UserProfileForm(instance=user_profile)

    context = {
        'profile': user_p,
        'vendorform': vendor,
        'user_p': user_profile,
        'vender_instance': vender_instance,
    }
    return render(request, 'vendor/vprofile.html', context)


def menu_builder(request):
    vendor = Vendor.objects.get(user=request.user)
    print(vendor)
    categories = Categry.objects.filter(vendor=vendor).order_by('created')
    context = {'categories': categories}
    return render(request, 'vendor/menu_builder.html', context)


def food_item_category(request, pk=None):
    vendor = Vendor.objects.get(user=request.user)
    categories = get_object_or_404(Categry, pk=pk)
    fooditem = FoodItem.objects.filter(vendor=vendor, categry=categories)
    context = {'categories': categories,
               'fooditem': fooditem,
               }

    return render(request, 'vendor/food_item_item.html', context)


def add_category(request):
    form = add_category_forms(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            vendor = Vendor.objects.get(user=request.user)
            category = form.save(commit=False)
            category_name = form.cleaned_data['category_name']
            category.vendor = vendor
            category.slug = slugify(category_name)
            category.save()
            messages.success(request, "category added successfully")
            return redirect('menu_builder')
        else:
            print(form.errors)
    else:
        form = add_category_forms()

    context = {
        'form': form

    }
    return render(request, 'vendor/add_category.html', context)


def edit_category(request, pk=None):
    categry = get_object_or_404(Categry, pk=pk)

    if request.method == 'POST':
        form = add_category_forms(request.POST, instance=categry)
        if form.is_valid():
            vendor = Vendor.objects.get(user=request.user)
            category = form.save(commit=False)
            category_name = form.cleaned_data['category_name']
            category.vendor = vendor
            category.slug = slugify(category_name)
            category.save()
            messages.success(request, "category Edit successfully")
            return redirect('menu_builder')
        else:
            pass
    else:
        form = add_category_forms(instance=categry)

    context = {
        'form': form,
        'category': categry

    }
    return render(request, 'vendor/edit_category.html', context)


def delete_category(request,pk=None):
    categry = get_object_or_404(Categry, pk=pk)
    categry.delete()
    return redirect('menu_builder')



def add_food(request):
    vendor = Vendor.objects.get(user = request.user)
    form = food_item_forms(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            food = form.save(commit=False)
            food.vendor = vendor
            food_title = form.cleaned_data['food_title']
            food.slug = slugify(food_title)
            food.save()
            messages.success(request, 'food added successfully')
            return redirect('food_item_category',food.categry.id)
        else:
            form.errors
    else:
        form = food_item_forms()
        #modified from
        form.fields['categry'].queryset = Categry.objects.filter(vendor = vendor)

    context = {'food':form}
    return render(request, 'vendor/add_food.html',context)


def edit_food(request, pk=None):
    food = get_object_or_404(FoodItem,pk=pk)
    form = food_item_forms(request.POST,request.FILES,instance= food)
    vendor = Vendor.objects.get(user = request.user)
    if request.method == 'POST':
        if form.is_valid():
            food = form.save(commit=False)
            food_title = form.cleaned_data['food_title']
            food.slug = slugify(food_title)
            food.vendor = vendor
            food.save()
            messages.success(request, 'food edite successfully')
            return redirect('food_item_category',food.categry.id)
        else:
            form.errors
    else:
        form =food_item_forms(instance=food)
        form.fields['categry'].queryset = Categry.objects.filter(vendor = vendor)

    context = {'food':form, 'form':food}
    return render(request, 'vendor/edit_food.html',context)

def delete_food(request,pk=None):
    food = get_object_or_404(FoodItem,pk=pk)
    food.delete()
    return redirect('food_item_category',food.categry.id)



def opening_hours(request):
    vender = Vendor.objects.get(user = request.user)
    opening = OpeningHours.objects.filter(vendor= vender)
    form = openingForm
    context = {
        'form': form,
        'opening': opening
    }
    
    return render(request, 'vendor/opening_hours.html',context)


def add_opening_hours(request):
   if request.user.is_authenticated:
       if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
           vender = Vendor.objects.get(user = request.user)
           day = request.POST.get('day')
           from_hour = request.POST.get('from_hour')
           to_hour = request.POST.get('to_hour')
           is_close = request.POST.get('check')
           try:
              hour = OpeningHours(vendor= vender,day=day,from_hour=from_hour, to_hour=to_hour, is_closed=is_close)
              hour.save()
              if hour:
                  days = OpeningHours.objects.get(id=hour.id)
                  if days.is_closed:
                    response = {'status':'success','message':'Add Hour Successfully','id':hour.id, 'day':days.get_day_display(),'is_closed':'Closed'}
                    return JsonResponse(response)                  
                  else:
                    response = {'status':'success','message':'Add Hour Successfully','id':hour.id, 'day':days.get_day_display(),'from_hour':hour.from_hour,'to_hour':to_hour}
              return JsonResponse(response)
           except IntegrityError as e:
               
               response ={'status':'Failed','message': from_hour+'-'+to_hour+ 'already exists'}
               return JsonResponse(response)
           
   return JsonResponse({'status':'Failed','message':'adding hours successfully'})

def remove_opening_hours(request,pk=None):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            hour = get_object_or_404(OpeningHours,pk=pk)
            hour.delete()
            return JsonResponse({'status':'success','message':'Removing hours successfully'})