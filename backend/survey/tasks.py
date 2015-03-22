from __future__ import absolute_import
from celery import shared_task
from django.core.mail import send_mail
from .models import Survey


@shared_task
def event_notification(survey_id, subject, message, recipient_list):
    send_mail(subject, message, None, recipient_list, fail_silently=False)
    Survey.objects.filter(id=survey_id).update(is_notified=True)

