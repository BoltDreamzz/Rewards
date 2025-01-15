from django.contrib import admin

# Register your models here.
from .models import RaffleEntry, UserProfile, Referral, Testimonial, PaymentType

admin.site.register(RaffleEntry)
admin.site.register(UserProfile)
admin.site.register(Referral)
admin.site.register(Testimonial)
admin.site.register(PaymentType)