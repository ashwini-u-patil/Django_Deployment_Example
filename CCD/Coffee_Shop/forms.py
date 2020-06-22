from django import  forms
from django.core import validators
from Coffee_Shop.models import  UserProfileInfo
from django.contrib.auth.models import  User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('first_name','last_name','username','password','email',)

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_picture')



# class new_user(forms.ModelForm):
#     class  Meta:
#         model = User
#         fields = '__all__'
