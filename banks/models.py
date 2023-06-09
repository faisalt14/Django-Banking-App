from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import SET_NULL


class Bank(models.Model):
    name = models.CharField(max_length=100)
    swift_code = models.CharField(max_length=100)
    inst_num = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(to=User, null=True, on_delete=SET_NULL, related_name='banks')

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    transit_num = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(default='admin@utoronto.ca')
    capacity = models.PositiveIntegerField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    bank = models.ForeignKey(to=Bank, null=True, on_delete=SET_NULL)

    def __str__(self):
        return self.name
