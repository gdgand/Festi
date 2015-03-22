from django import forms
from .models import User, Survey


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('uid', 'name', 'profile_image_url', 'email')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'profile_image_url', 'email')


class SurveyCreateForm(forms.ModelForm):
    def __init__(self, data=None, *args, **kwargs):
        user_id = data.get('user')
        if user_id:
            try:
                found_user = User.objects.get(uid=user_id)
                data = data.copy()
                data.update({'user': found_user.id})
            except User.DoesNotExist:
                pass

        super(SurveyCreateForm, self).__init__(data, *args, **kwargs)

    class Meta:
        model = Survey
        fields = ('event', 'user', 'props')


class SurveyUpdateForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('props',)

