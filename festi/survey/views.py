# coding: utf8
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import SurveyForm
from .models import Event, Speaker, Survey


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


def detail(request, event_slug):
    event = get_object_or_404(Event, slug=event_slug)

    survey = None
    if request.user.is_authenticated():
        try:
            survey = Survey.objects.get(event=event, user=request.user)
        except Survey.DoesNotExist:
            pass

    speaker_list = Speaker.objects.filter(event=event).order_by('idx')

    return render(request, 'survey/detail.html', {
        'event': event,
        'survey': survey,
        'speaker_list': speaker_list,
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
            if not survey:
                survey = form.save(commit=False)
                survey.event = event
                survey.user = request.user
                messages.info(request, u'신청이 접수되었습니다.')
            else:
                survey = form.save(commit=False)
                messages.info(request, u'신청내역이 수정되었습니다.')
            survey.save()

            return redirect('conference:index')
        else:
            for error in form.errors['props']:
                messages.error(request, error)
    else:
        props = []
        if survey:
            props = survey.props

        for event_prop in (event.props or []):
            for prop in props:
                if int(prop['id']) == int(event_prop['id']):
                    if event_prop.get('answer_type', None):
                        prop['answer_type'] = event_prop['answer_type']
                    break
            else:
                prop = {
                    'id': event_prop['id'],
                    'question': event_prop['question'],
                    'answer': '',
                }
                if event_prop.get('answer_type', None):
                    prop['answer_type'] = event_prop['answer_type']
                props.append(prop)

        if not props:
            messages.info(request, u'참가신청 입력폼을 준비 중입니다.')
            return redirect('conference:index')

        props = sorted(props, key=lambda _p: int(_p['id']))

        form = SurveyForm(instance=survey, initial={'props': props})

    return render(request, 'survey/form.html', {
        'event': event,
        'survey': survey,
        'form': form,
        'avatar_url': request.facebook_account.get_avatar_url(),
    })


@login_required
def export(request, event_slug):
    if not request.user.is_superuser:
        return HttpResponse('Unauthorized', status=401)

    event = get_object_or_404(Event, slug=event_slug)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    return event.export_csv(response)

