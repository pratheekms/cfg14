from django.contrib.auth.models import User
from django import forms
from pdp import models

class MentorForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = models.Mentor
    #    fields = ('username', 'email', 'password')