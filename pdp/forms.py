from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = models.Mentor
    #    fields = ('username', 'email', 'password')