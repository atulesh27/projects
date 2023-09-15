from django import forms
from .models import StudRegistration


class StudRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudRegistration
        fields = '__all__'