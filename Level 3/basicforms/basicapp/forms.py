from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() !="z":
        raise forms.ValidationError("NAME NEEDS TO START WITH Z")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)
    verify_email = forms.EmailField(label = 'Enter Your Email Again')

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("emails don't match")
    