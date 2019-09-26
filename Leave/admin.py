from django.contrib import admin
from .models import *
# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = []


    class Meta:
        model = LeaveAppUser

admin.site.register(LeaveAppUser, Admin)