from django.shortcuts import render
from .models import RaffleEntry
from django.http import HttpResponse
from django.contrib import messages

from .forms import RaffleDrawForm

# Create your views here.
def index(request):
    return render(request, 'travels/index.html')

def contact_info(request):
    if request.method == "POST":
        form = RaffleDrawForm(request.POST)
        if form.is_valid():
            RaffleEntry.objects.create(**form.cleaned_data)
            messages.success(request, 'Thank You! Expect the result.')
            return redirect('travels:success')
            # return HttpResponse("Thank you for entering the raffle draw!")
        else:
            messages.error(request, 'Something happened, try again.')
            return render(request, 'travels/contact_info.html', {'form': form})
    else:
        form = RaffleDrawForm()
    return render(request, 'travels/contact_info.html', {'form': form})
    
    # return render(request, 'travels/contact_info.html')
    
from django.shortcuts import redirect, render, get_object_or_404
from .models import UserProfile, Referral
from django.contrib.auth.decorators import login_required

def success(request):
    return render(request, 'travels/success.html')


@login_required
def handle_referral(request, code):
    try:
        referrer_profile = UserProfile.objects.get(referral_code=code)
    except UserProfile.DoesNotExist:
        return redirect('travels:index')  # Redirect to a default page if the code is invalid.

    # Save referral if the user is authenticated and has no referrer
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        messages.success(request, 'Your profile')

        if not user_profile.referred_by and referrer_profile.user != request.user:
            user_profile.referred_by = referrer_profile.user
            user_profile.save()

            # Create a referral record
            Referral.objects.create(referrer=referrer_profile.user, referred=request.user)

            # Increment the referrer's referral count
            if referrer_profile.referral_count >= 5:
                messages.success(request, 'Maximum referrals gained')
                return redirect('travels:index') 
            
            referrer_profile.referral_count += 1
            referrer_profile.save()

    return redirect('travels:index')  # Redirect to the home page or another page.

@login_required
def leaderboard(request):
    messages.success(request, 'Leaderboard')
    top_referrers = UserProfile.objects.order_by('-referral_count')[:5]
    return render(request, 'travels/leaderboard.html', {'top_referrers': top_referrers})

@login_required
def user_entries(request):
    messages.success(request, 'All people ')
    entries = RaffleEntry.objects.all() 
    count = entries.count()
    # top_referrers = UserProfile.objects.order_by('-referral_count')[:5]
    return render(request, 'travels/entries.html', {
        'entries': entries,
        'count': count,
        })