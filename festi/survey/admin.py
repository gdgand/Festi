# coding: utf8
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Event, Speaker, Survey
from .tasks import event_notification


class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('event', 'idx', 'name', 'keyword', 'topic')
admin.site.register(Speaker, SpeakerAdmin)


class SurveyResource(resources.ModelResource):
    class Meta:
        model = Survey
        fields = ('event__name', 'user__email', 'is_approved', 'is_notified', 'is_attended', 'created_at', 'updated_at')


class SurveyAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('id', 'event', 'user_detail', 'is_approved', 'is_notified', 'is_attended', 'created_at', 'updated_at')
    list_display_links = ('id', 'user_detail',)
    list_editable = ('is_approved', 'is_attended')
    list_filter = ('is_approved', 'is_notified', 'is_attended')
    ordering = ('created_at', 'updated_at')
    search_fields = ('user__email',)
    actions = ['send_approve_email']
    exclude = ('props',)

    def user_detail(self, survey):
        return survey.user.email

    def props_detail(self, survey):
        return '\n\n'.join(u'Q : {question}\nA : {answer}'.format(**prop) for prop in survey.props)

    def send_approve_email(self, request, queryset):
        count = 0
        for survey in queryset:
            if survey.is_approved and survey.event.approve_email_content and survey.user.email:
                lines = survey.event.approve_email_content.strip().splitlines()
                title = lines[0]
                content = '\n'.join(lines[1:])
                event_notification.s(survey.id, title, content, [survey.user.email]).delay()
                count += 1
        if count == 0:
            self.message_user(request, u'전송할 유저가 없습니다.')
        else:
            self.message_user(request, u'{} 명의 유저에게 이메일을 전송 중입니다.'.format(count))
    send_approve_email.short_description = u'선택/승인된 survey 유저에게 승인메일 보내기'

    resource_class = SurveyResource

    def get_readonly_fields(self, request, obj=None):
        return ('event', 'user', 'props_detail')

    def has_add_permission(self, request):
        return False

admin.site.register(Survey, SurveyAdmin)

