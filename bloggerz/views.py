from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from .forms import RegisterloginForm
from .forms import InformationForm
from .forms import BlogcreationForm
from .models import *
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView



class Homeview(ListView):
    model = Blogcreation
    template_name = 'blog_app/homepage.html'


def registerlogin(request):
    if request.method == 'POST':
        form = RegisterloginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        try:
            post = Register.objects.get(username=username)
            if post.password == password:
                return HttpResponseRedirect('/blogcreate')
                #blog = blogcreate(request)
                #return render(request, 'blog_app/homepage.html', {'blogs': blog})
            else:
                return render(request, 'blog_app/error.html')
        except Register.DoesNotExist:
            return HttpResponseRedirect('/register')

    else:
        form = RegisterloginForm()

    return render(request, 'blog_app/login.html',{'form':form} )

def information(request):
    if request.method == 'POST':
        form = InformationForm(request.POST)
        if form.is_valid():
            username1 = form.cleaned_data['username']
            password1 = form.cleaned_data['password']
            Fname1 = form.cleaned_data['Fname']
            Lname1 = form.cleaned_data['Lname']
            Email1 = form.cleaned_data['email_id']

            post = Register(
                username= username1,
                password= password1,
                Fname= Fname1,
                Lname= Lname1,
                email_id= Email1,
            )
            post.save()
            return HttpResponseRedirect('/login')
            
    else:
        form = InformationForm()

    return render(request, 'blog_app/register.html',{'form':form})
    
def blogcreate(request):
    if request.method == 'POST':
        form = BlogcreationForm(request.POST)
        if form.is_valid():
            title1 = form.cleaned_data['title']
            status1 = form.cleaned_data['status']
            content1 = form.cleaned_data['content']
            image1 = form.cleaned_data['image']
        
         
        post = Blogcreation(
                title= title1,
                #author= Register.objects.get(username) ,
                status= status1,
                content= content1,
                image=image1
            )
        post.save() 

        return render(request, 'blog_app/homepage.html', {
           'title':title1,
           'content':content1,
           'image':image1,
        })
    else:
        form = BlogcreationForm()
    return render(request, 'blog_app/createblog.html', {'form':form})
    






