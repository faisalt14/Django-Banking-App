from builtins import super, format

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed, request
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse
from django.views import View


class Register(View):

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'accounts/register.html')

    def post(self, request, *args, **kwargs):

        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')

        context = {'username': [], 'password1': [], 'password2': [], 'email': [], 'username_value': username,
                   'email_value': email, 'first_name_value': first_name, 'last_name_value': last_name}

        if password1 != password2:
            context['password1'].append("The two password fields didn't match")
            context['password2'].append("The two password fields didn't match")

        if len(password1) < 8:
            context['password1'].append("This password is too short. It must contain at least 8 characters")
        if password1 is None:
            context['password1'].append("This field is required")

        if len(password2) < 8:
            context['password2'].append("This password is too short. It must contain at least 8 characters")
        if password2 is None:
            context['password2'].append("This field is required")

        if username is None:
            context['username'].append("This field is required")

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            pass
        else:
            context['username'].append("A user with that username already exists")

        try:
            validate_email(email)
        except ValidationError:
            context['email'].append("Enter a valid email address")
        else:
            pass

        if len(context['username']) > 0 or len(context['password1']) > 0 or len(context['password2']) > 0 or len(
                context['email']) > 0:
            return TemplateResponse(request, 'accounts/register.html',
                                    context=context)
        else:
            User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                                     last_name=last_name)

            return HttpResponseRedirect('/accounts/login/')

    HttpResponseNotAllowed(['GET', 'POST'])


class Login(View):

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'accounts/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        context = {'errors': [], "username_value": username}

        if user := authenticate(username=username, password=password):
            login(request, user)
            return HttpResponseRedirect('/accounts/profile/view/')
        else:
            context['errors'].append('Username or password is invalid')
            return TemplateResponse(request, 'accounts/login.html', context=context)


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/accounts/login/')


class ProfileView(View):
    def get(self, *args, **kwargs):
        return HttpResponse('hello')
