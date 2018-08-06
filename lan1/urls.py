from django.contrib import admin
from django.urls import path, include

#추가
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landi1.urls')),
    path('accounts/', include('login.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/logout', views.logout, name = 'logout'),
]
