"""
URL configuration for djangoProject project.

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
from app.views import (index, main_page, logout_user, add_place, edit_place )
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('main/', main_page, name='main_page'),
    path('logout/', logout_user, name='logout'),
    path('add_place/', add_place, name='add_place'),
    path('edit_place/<int:place_id>', edit_place, name='edit_place'),
    path('', include('social_django.urls', namespace='social')),
]
