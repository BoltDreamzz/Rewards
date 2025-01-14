from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from .models import UserProfile  # Adjust import to your actual UserProfile model location
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Generate a unique referral code (e.g., based on UUID)
        referral_code = str(uuid.uuid4())[:8]  # Customize length as needed
        UserProfile.objects.create(user=instance, referral_code=referral_code)
