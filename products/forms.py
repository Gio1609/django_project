from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoadLogsForm(forms.Form):
    file  = forms.FileField() # for creating file input 
    sql = forms.CharField( widget=forms.Textarea(attrs={'rows': 5, 'cols': 60}))
