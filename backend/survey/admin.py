from django.contrib import admin
from .models import User, Event, Survey


class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)


class SurveyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Survey, SurveyAdmin)
