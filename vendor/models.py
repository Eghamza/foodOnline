
from django.db import models
from accounts.models import User, UserProfile
from accounts import utils

from datetime import date, datetime,time

# Create your models here.


class Vendor(models.Model):
    user = models.OneToOneField( User, related_name="user", on_delete=models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, related_name="user_profile", on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    vendor_licence = models.ImageField(upload_to='vendor/licence')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.vendor_name
    
    def is_open(self):
        today_date = date.today()
        today = today_date.isoweekday()
        tday = OpeningHours.objects.filter(vendor=self,day=today)
        now = datetime.now()
        current_date = now.strftime('%I:%M:%p')
    
        is_open = None
        for opening in tday:
            start = opening.from_hour
            end = opening.to_hour
            
            if current_date >start and current_date< end:
                is_open = True
                break
            else:
                is_open = False
        return is_open
    

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
    
DAYS = [
    (1,('Monday')),
    (2,('Tuesday')),
    (3,('Wednesday')),
    (4,('Thursday')),
    (5,('Friday')),
    (6,('Saturday')),
    (7,('Sunday')),
]
HOURS_OF_OPENING = [(time(h,m).strftime('%I:%M:%p'),time(h,m).strftime('%I:%M:%p')) for h in range(0,24) for m in range(0,30)]    
class OpeningHours(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAYS)
    from_hour = models.CharField(choices=HOURS_OF_OPENING,max_length=10)
    to_hour = models.CharField(choices=HOURS_OF_OPENING,max_length=10)
    is_closed = models.BooleanField(default=False)

   

    class Meta:
        ordering = ('day','from_hour')
        unique_together = ('vendor','day','from_hour','to_hour')

    def __str__(self): 
        return self.get_day_display()    
