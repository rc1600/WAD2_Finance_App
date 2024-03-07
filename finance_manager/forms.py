from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  

class CustomUserCreationForm(UserCreationForm):  
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.exists():
            raise ValidationError("Email already exists")
        return email

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
