
from django.urls import path
from . import views
from bloggerz.views import *

urlpatterns = [
    path('', Homeview.as_view()),
    path('register', views.information),
    path('login', views.registerlogin),
    path('blogcreate', views.blogcreate),
]