# coding: utf8
from django import forms
from .widgets import SplitJSONWidget
from .models import Survey


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('props',)
        widgets = {
            'props': SplitJSONWidget,
        }

    def clean_props(self):
        props = self.cleaned_data['props']
        for prop in props:
            if not prop.get('answer', '').strip():
                raise forms.ValidationError(u'모든 답변을 채워주세요.')
        return props

