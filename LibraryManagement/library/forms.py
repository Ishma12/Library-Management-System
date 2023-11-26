from django import forms
from .models import User
class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'common-input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'common-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'common-input'}))
    usermode = forms.ChoiceField(
        choices= User.USERTYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'common-input'})

    )
    class Meta:
        model=User
        fields=["username","email","password","usermode"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'common-input', 'required':True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'common-input','required': True}))
