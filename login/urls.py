from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/login', views.login, name='login'),
    
    # path('accounts/', include('allauth.urls')),
    # path('login/', views.login, name='login'),
    # path('profile/', views.post_list, name = 'profile'),
]
