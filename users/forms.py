from django import forms
from django.contrib.auth.models import User #importing the model we created in database to make changes to it
# from django.contrib.auth.forms import UserCreationForm #we'll add new feilds to this existing form
from .templates.users import register


class UserRegisterForm(register):
    email = forms.EmailField() #field added in form
    Fname = forms.f()

    class Meta: #this class tells that info is in user and sequence of form
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #sequence of form