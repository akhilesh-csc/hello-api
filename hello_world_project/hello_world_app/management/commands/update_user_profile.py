# hello_world_app/management/commands/update_user_profiles.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from hello_world_app.models import UserProfile

class Command(BaseCommand):
    help = 'Update user profiles with latitude and longitude'

    def handle(self, *args, **options):
        # Iterate over all existing users
        for user in User.objects.all():
            # Try to get the user's profile; create if it doesn't exist
            profile, created = UserProfile.objects.get_or_create(user=user)

            # Check if the profile is newly created or if latitude/longitude is None
            if created or profile.latitude is None or profile.longitude is None:
                # Set your desired latitude and longitude values
                profile.latitude ="28.4709° N"
                profile.longitude ="77.1830° E"

                # Save the updated profile
                profile.save()
