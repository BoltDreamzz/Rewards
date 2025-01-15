from datetime import date
from django import forms
from django.core.exceptions import ValidationError

class RaffleDrawForm(forms.Form):
    full_name = forms.CharField(max_length=255, label="Full Name", widget=forms.TextInput(attrs={
        'class': 'input input-bordered', 'placeholder': 'Enter your full name'
    }))
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={
        'class': 'input input-bordered', 'placeholder': 'Enter your email'
    }))
    phone_number = forms.CharField(max_length=15, label="Phone Number", widget=forms.TextInput(attrs={
        'class': 'input input-bordered', 'placeholder': 'Enter your phone number'
    }))
    state_of_origin = forms.CharField(max_length=255, required=False, label="State of Origin", widget=forms.TextInput(attrs={
        'class': 'input input-bordered', 'placeholder': 'Enter your state of origin (optional)'
    }))
    country = forms.CharField(max_length=255, required=False, label="Country", widget=forms.TextInput(attrs={
        'class': 'input input-bordered', 'placeholder': 'Enter your country (optional)'
    }))
    city = forms.CharField(max_length=255, required=False, label="City", widget=forms.TextInput(attrs={
        'class': 'input input-bordered', 'placeholder': 'Enter your city (optional)'
    }))
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={
        'class': 'input input-bordered', 'type': 'date', 'placeholder': 'Enter your date of birth'
    }))

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        if dob:
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 55:
                raise ValidationError("You must be 55 years old or above and retired to participate.")
        return dob



from django import forms
from .models import PaymentType

class PaymentTypeForm(forms.ModelForm):
    class Meta:
        model = PaymentType
        fields = ['name']
