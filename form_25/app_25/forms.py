from django import forms
from .models import form_model

class user_form(forms.ModelForm):
    class Meta:
        model = form_model
        fields = '__all__'

# class StudentRegistration(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()


#clean data with specified field:

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput)
    # check if name feild has 7 char or not

    def clean_name(self):
        valname = self.cleaned_data['name']
        if len(valname)<7:
            raise forms.ValidationError('in name Enter more than 7 char')
        return valname

    #form validation to match two field value

    def clean(self):
        clean_data = super().clean()
        valuepwd = clean_data['password']
        valueconfirmpwd = clean_data['ConfirmPassword']
        if valuepwd != valueconfirmpwd:
            raise forms.ValidationError('password does not match')