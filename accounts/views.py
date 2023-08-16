from django.shortcuts import redirect, render

from vendor.forms import vendonForm
from .forms import UserForm
from .models import User, UserProfile
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # read password field from  form
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, "User registration successful ")
            return redirect('register')
    else:
        # print("Invalid username or password")
        # print(form.errors)

        form = UserForm()
    contex = {
        'form': form,
        'errors': form.errors
    }
    return render(request, 'accounts/registerUser.html', contex)


def registervendor(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        v_form = vendonForm(request.POST, request.FILES)
        
        if form.is_valid() and v_form.is_valid:
        
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)  # make the password Hash
            user.role = User.RESTAURENT
            user.save()

            vendor_username = v_form.save(commit=False)
            vendor_username.user = user #get the created user
            vendor_user_profile = UserProfile.objects.get(user=user) #get the created user profile
            vendor_username. user_profile = vendor_user_profile
            vendor_username.save()
            messages.success(
                request, "User registration successful ! Please wait approving")
            return redirect('registervendor')
        else:
            print("invali")

    else:

        form = UserForm()
        v_form = vendonForm()

    contex = {
        'form': form,
        'v_form': v_form
    }
    return render(request, 'accounts/registerVendor.html', contex)
