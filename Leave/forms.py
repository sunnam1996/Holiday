from django.contrib.auth.forms import UserCreationForm
from .models import LeaveAppUser
# from django.forms import ModelForm, Textarea
# from django import forms
# from django.contrib.auth.forms import PasswordResetForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = LeaveAppUser
        fields = ['username','email','first_name','last_name']

# class UserUpdateForm(ModelForm):
#     class Meta:
#         model = LeaveAppUser
#         fields = ('username','first_name','last_name','profile_image')
#         widgets = {
#             'name': Textarea(attrs={'cols': 80, 'rows': 20}),
#         }