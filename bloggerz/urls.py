
from django.urls import path
#from . import views
from bloggerz.views import *

urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name= 'detail'),
    path('blogcreate', AddPostView.as_view(), name='add'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete'),
]