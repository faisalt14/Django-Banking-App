from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db.models import Field
from django.forms import Field
from django.http import HttpResponse, request
from django.shortcuts import render



