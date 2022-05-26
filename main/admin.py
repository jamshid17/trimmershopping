from http import client
from django.contrib import admin
from .models import Client
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'name', 'request_time')
    list_display_links = ('id', 'phone_number', 'name')
