from django import forms
from .models import User, Event, Survey


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('uid', 'name', 'profile_image_url', 'email')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'profile_image_url', 'email')


class EventForm(forms.ModelForm):
    class Meta:
        model = Event


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey

