from django.contrib import admin
from django.contrib.admin import ModelAdmin

from services.models import Service, Plan, Subscription


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ('name', 'full_price')


@admin.register(Plan)
class PlanAdmin(ModelAdmin):
    list_display = ('plan_type', 'discount_percent')


@admin.register(Subscription)
class SubscriptionAdmin(ModelAdmin):
    pass
