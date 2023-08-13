from django.db.models.signals import post_save,pre_save
from .models import User, UserProfile
from django.dispatch import receiver


@receiver(post_save,sender=User)
def post_save_create_userprofile(sender, instance, created,**kwargs):
    if created :
        profile = UserProfile.objects.create(user = instance) # create a new profile
        profile.save()

    else :
        try :
            profile = UserProfile.objects.get(user = instance) # update if the user already have profile
            profile.save()

        except:
            profile = UserProfile.objects.create(user = instance) # if the use have already been created and have not  profile. then create a new profile
            profile.save()  

@receiver(pre_save,sender=User)
def pre_save_create_userprofile(sender, instance, **kwargs):
    print(instance.username,"create user profile")

