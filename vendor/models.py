from django.db import models
from accounts.models import User, UserProfile
from accounts import utils

# Create your models here.


class Vendor(models.Model):
    user = models.OneToOneField( User, related_name="user", on_delete=models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, related_name="user_profile", on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=50)
    vendor_licence = models.ImageField(upload_to='vendor/licence')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.vendor_name

    def save(self, *args, **kwargs):
        if self.pk is not None: #check if the state of is_approved is changed
            org = Vendor.objects.get(pk=self.pk)
            if org.is_approved != self.is_approved:

                mail_template = "accounts/email/admin_approval.html"
                context= {
                    'user': self.user,
                    'is_approved': self.is_approved,
                }

                if self.is_approved == True:
                    #send email notification
                    mail_subject = "Congratulations! You restarent has been approved"
                    utils.send_email_notification(mail_subject,mail_template,context)
                  
                else:

                    #send notification 
                    mail_subject = "we are sorry! you are not eligible for publishing your food menu on our marketplace "
                    utils.send_email_notification(mail_subject,mail_template,context)
                    

                
        return super(Vendor, self).save(*args, **kwargs)
