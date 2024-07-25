"""
URL configuration for dog_walk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', views.profile_page, name='profile'),
    path('dogs/', views.dogs_list_page, name='dogs_list'),
    path('dogs/<int:id>/', views.dogs_view_page, name='dog_view'),
    path('dogs/<int:id>/edit/', views.dogs_edit_page, name='dog_edit'),
    path('dogs/create/', views.dogs_create_page, name='dog_create'),

]
