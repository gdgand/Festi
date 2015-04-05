from django.http import Http404
from django.shortcuts import redirect
from survey.models import Event

def index(request):
    event = Event.objects.order_by('-id').first()
    if not event:
        raise Http404
    return redirect('survey:detail', event.slug)

