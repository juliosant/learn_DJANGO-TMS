from django import forms
from django.forms import ModelForm

from . models import *

class CrudingForm(forms.ModelForm): #create fornulários
    class Meta:
        model = Cruding
        fields = '__all__' #todos os fields
    

