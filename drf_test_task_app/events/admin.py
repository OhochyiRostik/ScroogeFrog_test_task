from django.contrib import admin
from django.contrib.admin import ModelAdmin

from events.models import Event


@admin.register(Event)
class EventAdmin(ModelAdmin):
    pass
