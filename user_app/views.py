import random

from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=email, first_name=f_name, last_name=l_name, email=email,
                                        password=password)
        user.save()
        messages.success(request, "Registered Successfully!")

        return redirect('login')
    return render(request, 'signup.html')


def app_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            messages.success(request, "Logged In Successfully!")

            return redirect('/home')

        else:
            messages.error(request, "Incorrect login credentials!")

    return render(request, 'login.html')


def app_logout(request):
    logout(request)
    messages.info(request, "Logged Out!")

    return redirect('/')
#
#
# def forget_password(request):
#     if request.method == "POST":
#         global email_auth
#         email_auth = request.POST.get('email')
#
#         try:
#             User.objects.get(username=email_auth)
#             request.session['auth_permission'] = True
#
#             return redirect('/code-auth')
#
#         except:
#             request.session['auth_permission'] = False
#
#             messages.warning(request, "Email Address Doesn't Exist!")
#
#     context = {}
#     return render(request, 'forget-password.html', context=context)
#
#
# def reset_forget_pass(request):
#     if 'reset_permission' in request.session and request.session['reset_permission']:
#
#         if request.method == "POST":
#             new_password = request.POST['new_password']
#
#             user = User.objects.get(username=email_auth)
#             user.set_password(new_password)
#             user.save()
#
#             request.session['reset_permission'] = False
#
#             messages.success(request, "Password Reset Successful!")
#
#             return redirect('/login')
#
#         return render(request, 'reset_forget_pass.html')
#
#     else:
#         messages.warning(request, "You Don't Have Persmission To Proceed!")
#         return redirect('/')
#
#
# def reset_password(request):
#     if request.user.is_authenticated:
#
#         if request.method == "POST":
#             new_password = request.POST['new_password']
#
#             user = User.objects.get(username=request.user)
#             user.set_password(new_password)
#             user.save()
#
#             messages.success(request, "Password Reset Successful!")
#
#             return redirect('/login')
#
#         context = {}
#         return render(request, 'reset-password.html', context=context)
#
#     else:
#         messages.warning(request, "You Must Be Logged In")
#         return redirect('/login')
