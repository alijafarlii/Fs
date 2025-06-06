from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'image', 'info',]
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'image': forms.FileInput(attrs={'class':'form-control','placeholder':'Image'}),
            'info': forms.Textarea(attrs={'class':'form-control','placeholder':'Info'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        }