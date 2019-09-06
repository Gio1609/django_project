from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_tables2 import tables, TemplateColumn
from .models import HDFS_Browser

class HDFSBrowserForm(forms.Form):
    file  = forms.FileField() # for creating file input 
    name = forms.CharField(max_length=50)


class TrainingTable(tables.Table):
    class Meta:
         model = HDFS_Browser
         attrs = {'class': 'table table-sm'}
         fields = ['date', 'description', 'tags', 'points', 'edit']

    edit = TemplateColumn(template_name='browser/index.html')