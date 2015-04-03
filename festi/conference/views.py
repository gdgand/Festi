from django.shortcuts import render
from .models import Speaker

def index(request):
    return render(request, 'conference/index.html')

def speaker(request):
    speaker_list = Speaker.objects.all()
    return render(request, 'conference/speaker.html', {
        'speaker_list': speaker_list,
    })

def about(request):
    return render(request, 'conference/about.html')

