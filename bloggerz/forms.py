"""
from django import forms
from .models import *


class RegisterloginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=8)

class InformationForm(forms.Form):
    username = forms.CharField(max_length=20)
    Fname = forms.CharField(max_length=20)
    Lname = forms.CharField(max_length=20)
    password = forms.CharField(max_length=8 )
    email_id = forms.EmailField() 

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)  
class BlogcreationForm(forms.Form):
    title = forms.CharField(max_length=50)
    #author = forms.(Register, on_delete=models.CASCADE)
    status = forms.ChoiceField(choices=STATUS)
    content = forms.CharField()
    image = forms.URLField()
"""   