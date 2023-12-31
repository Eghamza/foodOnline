from django.shortcuts import redirect, render

from vendor.forms import vendonForm
from .forms import UserForm
from .models import User, UserProfile
from django.contrib import messages, auth
from . import utils
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_decode
from django.template.defaultfilters import slugify
from vendor.models import Vendor


# check if user can access vendor dashboard
def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied

# check if user can access custom dashboard


def check_role_custom_dashboard(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied


def register(request):
    if request.user.is_authenticated:
        messages.warning(request, " you already have authenticated")
        return redirect('myaccount')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # read password field from  form
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            user.save()

            utils.email_verification(request, user)

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
    if request.user.is_authenticated:
        messages.warning(request, " you already have authenticated")
        return redirect('myaccount')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        v_form = vendonForm(request.POST, request.FILES)

        if form.is_valid() and v_form.is_valid:

            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)  # make the password Hash
            user.role = User.RESTAURENT
            user.save()

            vendor_username = v_form.save(commit=False)
            vendor_username.user = user  # get the created user
            vendor_user_profile = UserProfile.objects.get(user=user)  # get the created user profile
            vendor_name = v_form.cleaned_data['vendor_name']
            vendor_username.slug = slugify(vendor_name) +'-'+ str(user.id)
            vendor_username. user_profile = vendor_user_profile
            vendor_username.save()
            
            utils.email_verification(request, user)
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


def login(request):
    if request.user.is_authenticated:
        messages.warning(request, " you already have authenticated")
        return redirect('myaccount')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "you are login successful")
            return redirect('myaccount')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, "logout successful")
    return render(request, 'accounts/login.html')

# myaccount


@login_required(login_url='login')
def myAccount(request):
    redirecturl = utils.detect_user(request.user)
    return redirect(redirecturl)


@login_required(login_url='login')
def dashbourd(request):
    return render(request, 'accounts/dashbourd.html')

# custom dashboard


@login_required(login_url='login')
@user_passes_test(check_role_custom_dashboard)
def customerDashboard(request):
    return render(request, 'accounts/customerDashboard.html')

# vendor dashboard


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vendorDashboard(request):
   
    return render(request, 'accounts/vendorDashboard.html')

# activate user account

def activate(request,uidb64,token):
    # Activate user account by setting the is_active=True
    try:
        uid= urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk = uid)
    except(TypeError, ValueError,OverflowError,User.DoesNotExist):
        user = None
        
    
    if user is  not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'congratulation! your account is avtivated')
        return redirect('myaccount')
    else:
        messages.error(request,'Invalid activate link')
        return redirect('myaccount')


#forget password reset
def forget_password(request):
   
    if request.method == 'POST':
        email = request.POST['email']
        if  User.object.filter(email=email).exists():
            user = User.object.get(email__exact = email)
            #send confirmation email
            utils.send_reset_password_email(request, user)
            messages.success(request, 'we sent seccessfull password reset email')
            return redirect('login')
        else:
            messages.error(request,'email doest not exist')
            
    
    return render(request, 'accounts/forget_password.html')

def reset_password_validate(request,uidb64,token):
    try:
        uid= urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk = uid)
    except(TypeError, ValueError,OverflowError,User.DoesNotExist):
        user = None
    if user is  not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.info(request,'please reset your password')
        return redirect('reset_password')
    else:
        messages.error(request,'This link has been expired')
        return redirect('login')


def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if confirm_password == password:
            pk = request.session.get('uid')
            user = User.object.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request,'Seccessfuly reseted you password')
            return redirect('login')
        else:
            messages.error(request,'password do not match!')

    return render(request,'accounts/email/reset_password.html')
    
