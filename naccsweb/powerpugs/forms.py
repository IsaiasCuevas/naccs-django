from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension
from django.contrib.auth.models import User

IGL_OPTIONS= [
    ('False', 'No '),
    ('True', 'Yes')
    ]

class PowerPugPlayerApp(forms.Form):

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    email = forms.EmailField(label="*Preferred Contact Email", required=True)
    college = forms.CharField(label="*College Name", required=True)
    esea = forms.CharField(label="*ESEA Link", required=True)
    faceit = forms.CharField(label="Faceit Profile Link", required=True)
    curr_team = forms.CharField(label="Current Collegiate Team", required=False)
    igl =  forms.CharField(label='Opt Into Secondary IGL Program', widget=forms.Select(choices=IGL_OPTIONS))
    lan = forms.CharField(label="LAN Exp", widget=forms.Textarea(attrs={'rows': 5, 'cols': 60}), required=False)
    other = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 60}), required=False)
    contract = forms.FileField(required=False)

class PowerPugIGLApp(forms.Form):
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    email = forms.EmailField(label="Preferred Contact Email", required=True)
    esea = forms.CharField(label="ESEA Link", required=True)
    faceit = forms.CharField(label="Faceit Profile Link", required=True)
    curr_team = forms.CharField(label="Current Collegiate Team", required=False)
    lan = forms.CharField(label="LAN Exp", widget=forms.Textarea(attrs={'rows': 5, 'cols': 60}), required=False)
    other = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 60}), required=False)
    contract = forms.FileField(required=False)



    
