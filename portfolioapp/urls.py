from django.urls import path, include
from .views import *
#import views

urlpatterns= [
    path('userprofile/',UserProfileAPIView.as_view(),name='user'),
    path('user/<int:pk>/',UserProfileDetailAPIView.as_view(),name='user-delete/put/get'),

    path('portfolio/',PortfolioAPIView .as_view(), name='portfolio-get/post'),
    path('portfolio/<int:pk>/', PortfolioAPIView.as_view(), name='portfolio-delete/put'),

    path('current/', CurrentMarketAPIView.as_view(), name='current-get/post'),
    path('resource/', ResourceAPIView.as_view(), name='resource'),

    path('investments/', InvestmentAPIView.as_view(), name='investment-list'),
    path('investments/<int:pk>/', InvestmentAPIView.as_view(), name='investment-detail'),

    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('payment/',paymentstart,name='mem-payment'),
    #path('payment/orderplace/',payment,name='place order')
    ]



