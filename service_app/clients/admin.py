from django.contrib import admin
from django.contrib.admin import ModelAdmin

from clients.models import Client


@admin.register(Client)
class ClientAdmin(ModelAdmin):
    list_display = ('user', 'company_name', 'full_address')

