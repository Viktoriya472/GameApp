from django.forms import ModelForm
from main.models import Profile
from django.contrib.auth.models import User
from django import forms

class ProfileForm(ModelForm):
    first_name = forms.CharField(label="Имя", max_length=30)
    last_name  = forms.CharField(label="Фамилия", max_length=30)
    class Meta:
        model = Profile
        fields = ['avatar']