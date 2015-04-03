from django.shortcuts import render

def index(request):
    return render(request, 'conference/index.html')

def speaker(request):
    return render(request, 'conference/speaker.html')

def about(request):
    return render(request, 'conference/about.html')

