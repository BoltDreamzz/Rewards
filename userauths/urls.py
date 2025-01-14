from django.urls import path

from . import views

app_name = "userauths"

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('splash/', views.splash, name='splash'),
    path('user_profile/', views.user_profile, name='user_profile'),

    
]












