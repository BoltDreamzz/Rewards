from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from travels.models import UserProfile, RaffleEntry
from django.contrib.auth.decorators import login_required



def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        referral_code = request.POST.get('referral_code', None)

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('userauths:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('userauths:register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('userauths:register')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Handle referral
        if referral_code:
            try:
                referrer_profile = UserProfile.objects.get(referral_code=referral_code)
                user_profile = UserProfile.objects.get(user=user)
                user_profile.referred_by = referrer_profile.user
                user_profile.save()
                referrer_profile.referral_count += 1
                referrer_profile.save()
            except UserProfile.DoesNotExist:
                messages.warning(request, "Invalid referral code.")

        # Log the user in after registration
        login(request, user)
        messages.success(request, "Registration successful!")
        return redirect('travels:index')

    return render(request, 'userauths/register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('travels:index')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('userauths:login')

    return render(request, 'userauths/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('userauths:splash')

def splash(request):
    return render(request, 'userauths/splash.html')

@login_required
def user_profile(request):
    user = request.user
    try:
        raffle_entry = RaffleEntry.objects.get(email=user.email)
    except RaffleEntry.DoesNotExist:
        raffle_entry = None

    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = None

    context = {
        "user": user,
        "raffle_entry": raffle_entry,
        "user_profile": user_profile,
    }
    return render(request, "userauths/user_profile.html", context)