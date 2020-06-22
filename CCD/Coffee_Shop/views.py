from django.shortcuts import render
from Coffee_Shop.forms import UserForm,UserProfileInfoForm

from django.urls import  reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

# from . import forms
# Create your views here.
def index(arg):
    return render(arg,'Coffee_Shop/index.html')

@login_required
def special(arg):
    return HttpResponse("You are logged in , NICE!")


@login_required
def user_logout(arg):
    logout(arg)
    return HttpResponseRedirect(reverse('index'))

# def users(request):
#     form = new_user()
#
#     if request.method == 'POST':
#         form = new_user(request.POST)
#
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print("Error Form Invalid")
#
#     return render(request,'Coffee_Shop/users.html',{'form':form})

# def other(arg):
#     return render(arg,'Coffee_Shop/other.html')
#
# def relative(arg):
#     return render(arg,'Coffee_Shop/relative.html')


def register(request):
    registered = False

    if request.method == "post":
        User_Form=UserForm(data=request.POST)
        Profile_Form=UserProfileInfoForm(data=request.POST)

        if User_Form.is_valid() and Profile_Form.is_valid():
            user = User_Form.save()
            user.set_password(user.password)
            user.save()

            profile = Profile_Form.save(commit=False)
            profile.user = user


            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(User_Form.errors,Profile_Form.errors)
    else:
        User_Form = UserForm()
        Profile_Form = UserProfileInfoForm()

    return render(request,'Coffee_Shop/registration.html',{
        'User_Form':User_Form,'Profile_Form':Profile_Form,'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Account not active')
        else:
            print("Someone tried to login and failed!")
            print("Username:{} and Password:{}".format(username,password))
            return HttpResponse("Invalid Credentials")

    else:
        return render(request,'Coffee_shop/login.html',{})
