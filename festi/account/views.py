from urllib import urlencode
from django.contrib.auth import logout as auth_logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render

def login(request):
    next = request.GET.get('next', '')
    redirect_url = reverse('facebook_login') + '?' + urlencode({'next': next})
    return redirect(redirect_url)

def logout(request):
    auth_logout(request)
    return redirect('/')

