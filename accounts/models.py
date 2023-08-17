from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.

#userManager
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None,first_name=None, last_name=None):
        if username is None:
            raise ValueError("username must not be None")
        if email is None:
            raise ValueError("email must not be None")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,


        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None,first_name=None, last_name=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_superadmin = True
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

#user
class User(AbstractBaseUser):
    RESTAURENT = 1
    CUSTOMER = 2
    ROLE_CHOICE= (

        (RESTAURENT,'restaurent'),
        (CUSTOMER,'customer'),
    )
    first_name = models.fields.CharField(max_length=50)
    last_name = models.fields.CharField(max_length=50)
    username = models.fields.CharField(max_length=50,unique=True)
    email = models.fields.CharField(max_length=50,unique=True)
    phone_number = models.fields.CharField(max_length=12,blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    #requerment
    date_join = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    object = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True
    
    #get user role
    def get_role(self):
        if self.role == 1:
            user_role = 'RESTAURENT'
            return user_role
        if self.role == 2:
           user_role = 'CUSTOMER'   
           return user_role 


class UserProfile(models.Model):
    user = models.OneToOneField(User,models.CASCADE,blank=True)
    profile_picture = models.ImageField(upload_to='user/profile_picture', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='user/cover_photo', blank=True, null=True)
    address_line_1 = models.CharField(max_length=50, blank=True, null=True)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city =models.CharField(max_length=15, blank=True, null=True)
    pin_code = models.CharField(max_length=6,blank=True, null=True)
    latitude = models.CharField(max_length=15, blank=True, null=True)
    longtitude = models.CharField(max_length=15, blank=True, null=True)
    create_at =models.DateTimeField(auto_now_add=True)
    modified_at =models.DateTimeField(auto_now=True)

def __str__(self):
    self.user.email

