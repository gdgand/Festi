from django.contrib import admin
from .models import Speaker

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('idx', 'name', 'topic')
admin.site.register(Speaker, SpeakerAdmin)

