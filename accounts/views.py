from django.shortcuts import redirect, render

from vendor.forms import vendonForm
from .forms import UserForm
from .models import User
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
    form = UserForm()
    v_form = vendonForm()

    contex = {
        'form': form,
        'v_form': v_form
    }
    return render(request, 'accounts/registerVendor.html',contex)
