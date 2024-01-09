# signals.py
#You can use Django signals to automatically create a UserProfile for each new user. 
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

# Signal to create a UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'userprofile'):
        print("Signal executed! Creating UserProfile for user:", instance.username)
        UserProfile.objects.create(user=instance, latitude="28.4709° N", longitude="77.1830° E")
post_save.connect(create_user_profile, sender=User)
# Signal to save the UserProfile when a User is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
     # Save the associated UserProfile if it exists
    if hasattr(instance, 'userprofile'):
    #The code hasattr(instance, 'userprofile') is a Python built-in function that checks if the instance (in this case, a User instance) has an attribute named 'userprofile'. If the attribute exists, it returns True; otherwise, it returns False.
        instance.userprofile.save()
