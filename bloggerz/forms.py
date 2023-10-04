
from django import forms
from .models import *
from django.contrib.auth.models import User
"""
class BlogcreationForm(forms.ModelForm):
    class Meta:
        model = Blogcreation
        fields = '__all__'
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.URLInput(attrs={'class': 'form-control'}),            
        }
class UpdatepostForm(forms.ModelForm):
    class Meta:
        model = Blogcreation
        fields = ('title', )
class RegisterloginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=8)
class InformationForm(forms.Form):
    username = forms.CharField(max_length=20)
    Fname = forms.CharField(max_length=20)
    Lname = forms.CharField(max_length=20)
    password = forms.CharField(max_length=8 )
    email_id = forms.EmailField() 
"""
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)  
class BlogcreationForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    status = forms.ChoiceField(choices=STATUS)
    content = forms.CharField()
    image = forms.URLField()

    class Meta:
        model = Blogcreation
        fields =['title', 'author', 'status', 'content', 'image']

class SearchForm(forms.Form):
    search= forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'class': 'form-control me-2', 'placeholder': 'Search'}))

