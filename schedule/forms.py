from django.forms import ModelForm
from schedule.models import tt
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
class tt1(ModelForm):
	class Meta:#returns fields
		model=tt
		fields='__all__'


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your username"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter your password"}
        )
    )
	




