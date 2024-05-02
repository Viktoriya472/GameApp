from django.forms import ModelForm
from main.models import Profile, Contact
from django import forms


class ProfileForm(ModelForm):
    first_name = forms.CharField(label="Имя", max_length=30)
    last_name = forms.CharField(label="Фамилия", max_length=30)

    class Meta:
        model = Profile
        fields = ['avatar']


class ContactForm(ModelForm):
    class Meta:
        model = Contact 
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={"class":
                                             "form-control bg-transparent text-white w-100 py-3 ps-4 pe-5",
                                             "placeholder": "Ваш email.."})
        }
