# coding: utf8
from django.conf.urls import patterns
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from .models import Event, Survey
from .tasks import event_notification


class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)


class SurveyResource(resources.ModelResource):
    class Meta:
        model = Survey
        fields = ('event__name', 'user__email', 'is_approved', 'is_notified', 'is_attended', 'created_at', 'updated_at')


class SurveyAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('event', 'user', 'is_approved', 'is_notified', 'is_attended', 'created_at', 'updated_at')
    list_editable = ('is_approved', 'is_attended')
    list_filter = ('is_approved', 'is_notified', 'is_attended')
    ordering = ('created_at', 'updated_at')
    search_fields = ('user__email',)
    actions = ['send_approve_email']
    exclude = ('props',)

    def get_urls(self):
        urls = super(SurveyAdmin, self).get_urls()
        return urls + patterns('',
            (r'^props/$', self.admin_site.admin_view(self.props_view)),
        )

    def props_view(self):
        return 'props_view : {}'.format(self)

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

    def has_add_permission(self, request):
        return False

admin.site.register(Survey, SurveyAdmin)

