from django import forms
from .models import *


class UpdateUnitForm(forms.Form):
    id = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    name = forms.CharField(label='Nom', max_length=100)


class AddUnitForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=100)
