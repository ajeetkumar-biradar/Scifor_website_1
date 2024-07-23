# carrer/forms.py
from django import forms
from .models import Jobs, Application


class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
