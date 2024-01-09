# hello_world_app/models.py
# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    # Create a one-to-one relationship with the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add fields for latitude and longitude
    latitude = models.CharField(max_length=15,null=True, blank=True)
    longitude = models.CharField( max_length=15,null=True, blank=True)

    def __str__(self):
        # Return the username as the string representation of the user profile
        return self.user.username

# Signal to create a UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Get latitude and longitude values from user input or some logic
        latitude = '28.4709° N'
        longitude = '77.1830° E'
        # Create a UserProfile with default latitude and longitude
        UserProfile.objects.create(user=instance, latitude='latitude', longitude='longitude')

# Signal to save the UserProfile when a User is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Save the associated UserProfile
     if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
