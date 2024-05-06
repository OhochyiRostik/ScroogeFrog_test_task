from django.contrib import admin
from django.contrib.admin import ModelAdmin

from events.models import Event, Registration


@admin.register(Event)
class EventAdmin(ModelAdmin):
    pass


@admin.register(Registration)
class RegistrationAdmin(ModelAdmin):
    pass
