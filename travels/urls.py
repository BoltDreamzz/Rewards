from django.urls import path

from . import views

app_name = "travels"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact_info, name="contact_info"),
    path('referral/<str:code>/', views.handle_referral, name='handle_referral'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('user_entries/', views.user_entries, name='user_entries'),
    path('success/', views.success, name='success'),
    path('payment-form/', views.payment_type_form, name='payment_type_form'),
    path('payment/<int:pk>/', views.payment_detail, name='payment_detail'),

    
    
]












