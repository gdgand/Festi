# coding: utf8
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import SurveyForm
from .models import Event, Survey


def facebook_user_required(fn):
    def wrap(request, *args, **kwargs):
        facebook_account = request.user.socialaccount_set.filter(provider='facebook').first()
        if not facebook_account:
            messages.error(request, u'페이스북 유저가 아닙니다.')
            return redirect('account_logout')
        request.facebook_account = facebook_account

        return fn(request, *args, **kwargs)
    return login_required(wrap)



def index(request):
    return render(request, 'survey/index.html', {
    })


@facebook_user_required
def form(request, event_id):
    event = get_object_or_404(Event, id=event_id, is_public=True)

    try:
        survey = Survey.objects.get(event=event, user=request.user)
    except Survey.DoesNotExist:
        survey = None

    if request.method == 'POST':
        form = SurveyForm(request.POST, instance=survey)
        if form.is_valid():
            if survey:
                survey = form.save()
                messages.info(request, u'신청이 접수되었습니다.')
            else:
                survey = form.save(commit=False)
                survey.event = event
                survey.user = request.user
                survey.save()
                messages.info(request, u'신청내역이 수정되었습니다.')
            return redirect('conference:index')
    else:
        form = SurveyForm(instance=survey)

    return render(request, 'survey/form.html', {
        'event': event,
        'survey': survey,
        'form': form,
        'avatar_url': request.facebook_account.get_avatar_url(),
    })

