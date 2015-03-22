# coding: utf8
from django.contrib import admin
from .models import User, Event, Survey
from .tasks import event_notification


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)


class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'is_approved', 'is_notified', 'created_at', 'updated_at')
    list_editable = ('is_approved',)
    list_filter = ('is_approved', 'is_notified',)
    ordering = ('created_at', 'updated_at')
    search_fields = ('user__name', 'user__email',)
    actions = ['send_approve_email']
    def send_approve_email(self, request, queryset):
        count = 0
        for survey in queryset:
            if survey.is_approved and survey.event.approve_email_content and survey.user.email:
                lines = survey.event.approve_email_content.strip().splitlines()
                title = lines[0]
                content = '\n'.join(lines[1:])
                event_notification(survey.id, title, content, [survey.user.email])
                count += 1
        if count == 0:
            self.message_user(request, u'전송할 유저가 없습니다.')
        else:
            self.message_user(request, u'{} 명의 유저에게 이메일을 전송 중입니다.'.format(count))
    send_approve_email.short_description = u'선택/승인된 survey 유저에게 승인메일 보내기'

admin.site.register(Survey, SurveyAdmin)

