from django.contrib import admin

# Register your models here.
from banks.models import Branch, Bank

admin.site.register(Branch)
admin.site.register(Bank)

