from django.shortcuts import get_object_or_404, render
from survey.models import Event, Survey
from .models import Speaker

def index(request):
    event = get_object_or_404(Event, id=1)

    survey = None
    if request.user.is_authenticated():
        try:
            survey = Survey.objects.get(event=event, user=request.user)
        except Survey.DoesNotExist:
            pass

    return render(request, 'conference/index.html', {
        'event': event,
        'survey': survey,
    })

def speaker(request):
    speaker_list = Speaker.objects.all()
    return render(request, 'conference/speaker.html', {
        'speaker_list': speaker_list,
    })

def about(request):
    return render(request, 'conference/about.html')

