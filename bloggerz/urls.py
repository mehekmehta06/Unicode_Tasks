
from django.urls import path
from . import views
from bloggerz.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.Homepage, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.registerlogin, name='register'),
    path('createblog', views.blogcreate, name='create'),
    path('update/<int:pk>', updatepost, name='update'),
    path('delete/<int:pk>', deletepost, name='delete'),
    path('detail/<int:pk>', detailpost, name='detail'),
    path('search/', searching, name='search'),

]


"""
path('', Homeview.as_view(), name='home'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name= 'detail'),
    path('blogcreate', AddPostView.as_view(), name='add'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete'),
"""