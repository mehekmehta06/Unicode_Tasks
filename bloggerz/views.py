from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import BlogcreationForm
from .forms import SearchForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views import View
#from django.shortcuts import render, HttpResponseRedirect
#from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.urls import reverse_lazy
"""
class Homeview(ListView):
    model = Blogcreation
    template_name = 'bloggerz/homepage.html'
    ordering= ['-created_on']
class BlogDetailView(DetailView):
    model = Blogcreation
    template_name = 'bloggerz/Blog-detail.html'
class AddPostView(CreateView):
    model = Blogcreation
    form_class = BlogcreationForm
    template_name = 'bloggerz/createblog.html'
class UpdatePostView(UpdateView):
    model = Blogcreation
    template_name= 'bloggerz/updatepost.html'
    fields= ['title', 'content', 'image']
class DeletePostView(DeleteView):
    model = Blogcreation
    template_name= 'bloggerz/deletepost.html'
    success_url= reverse_lazy('home')
"""
def Homepage(request):
        display = Blogcreation.objects.all()
        return render(request, 'bloggerz/homepage.html' ,{'display':display})

def registerlogin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def updatepost(request, pk):
    blog_post = get_object_or_404(Blogcreation, pk=pk)
    if request.method == 'POST':
        form = BlogcreationForm(request.POST, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogcreationForm(instance=blog_post)
    return render(request, 'bloggerz/updatepost.html', {'form': form})


def deletepost(request, pk):
    blog_post = get_object_or_404(Blogcreation, pk=pk)
    
    if request.method == 'POST':
        if request.user.is_authenticated and request.user == blog_post.author:
            blog_post.delete()
            return redirect('home')      
    return render(request, 'bloggerz/deletepost.html', {'Blogcreation': blog_post})

def detailpost(request, pk):
    blog_post = get_object_or_404(Blogcreation, pk=pk)
    return render(request, 'bloggerz/blog-detail.html', {'display':blog_post})

def searching(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        print('hello')
        if form.is_valid():
            search = form.cleaned_data['search']
            show = Blogcreation.objects.filter(author=search)
            return render(request, 'bloggerz/searchpost.html', {'show': show})
    else:
        form = SearchForm()
    return render(request, 'bloggerz/search.html', {'form': form})



"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        try:
            post = User.objects.get(username=username)
            if post.password == password:
                return HttpResponseRedirect('/blogcreate')
                #blog = blogcreate(request)
                #return render(request, 'blog_app/homepage.html', {'blogs': blog})
            else:
                return render(request, 'bloggerz/error.html')
        except User.DoesNotExist:
            return HttpResponseRedirect('/register')
    else:
        form = UserCreationForm()

    return render(request, 'bloggerz/login.html',{'form':form} )

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
"""
    
def blogcreate(request):
    if request.method == 'POST':
        form = BlogcreationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('home') 
    else:
        form = BlogcreationForm()
    return render(request, 'bloggerz/createblog.html', {'form':form})
  

"""           
            title1 = form.cleaned_data['title']
            status1 = form.cleaned_data['status']
            content1 = form.cleaned_data['content']
            image1 = form.cleaned_data['image']
            author1 =  form.cleaned_data['author']
            
        post = Blogcreation(
                title= title1,
                author= author1 ,
                status= status1,
                content= content1,
                image=image1,
            ) 
"""       






