from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings


#get user role and redirect spasific page
def detect_user(user):
    if user.role == 1:
        redirecturl = 'vendorDashboard'
        return redirecturl
    if user.role == 2:
           redirecturl = 'customerDashboard'
           return redirecturl
    if user.role == 'none' and user.role == 'is_superadmin':
            redirecturl = '/admin'
            return redirecturl
    

#send email verification 
def  email_verification(request, user):
      from_email = settings.DEFAULT_FROM_EMAIL
      current_site = get_current_site(request)
      mail_subject = "please Activate your account"
      message = render_to_string('accounts/email/email_verification.html',{
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user)

      })
      to_email= user.email
      mail =EmailMessage(mail_subject,message,from_email,to=[to_email])
      mail.send()
                         
        
#send email verification to reset password
def send_reset_password_email(request, user):
      from_email = settings.DEFAULT_FROM_EMAIL
      current_site = get_current_site(request)
      mail_subject = "please Activate your account"
      message = render_to_string('accounts/email/reset_email_verification.html',{
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user)

      })
      to_email= user.email
      mail =EmailMessage(mail_subject,message,from_email,to=[to_email])
      mail.send()



def send_email_notification(mail_subject,mail_template,context):
      from_email = settings.DEFAULT_FROM_EMAIL
      message = render_to_string(mail_template,context)
      to_email = context['user'].email
      mail = EmailMessage(mail_subject,message,from_email,to=[to_email])
      mail.send()
      
