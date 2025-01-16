from django.db import models


class RaffleEntry(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    state_of_origin = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField()
    submitted_at = models.DateTimeField(auto_now_add=True)


from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=10, unique=True)
    referred_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="referrals"
    )
    referral_count = models.PositiveIntegerField(default=0)
    is_claimed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Referral(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="referrer_referrals")
    referred = models.ForeignKey(User, on_delete=models.CASCADE, related_name="referred_by_user")
    date_referred = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.referrer.username} referred {self.referred.username}"

class Testimonial(models.Model):
    full_name = models.CharField(max_length=255)
    content = models.TextField()
    age = models.PositiveIntegerField(default=55)
    company = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.full_name} testified, age {self.age}"
    
from django.db import models

class PaymentType(models.Model):
    logo = models.ImageField(upload_to='payment_logos/')
    name = models.CharField(max_length=100)
    instructions = models.TextField()
    link= models.CharField(blank=True, max_length=255, null=True)
    color = models.CharField(max_length=100, default='warning', null=True)
    

    def __str__(self):
        return self.name
