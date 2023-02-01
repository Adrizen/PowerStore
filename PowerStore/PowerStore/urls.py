"""PowerStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from ordersManagement import views

urlpatterns = [
    path('admin/', admin.site.urls), # Admin panel
    path('home/', views.home, name="home"),
    path('services/', views.services, name="services"),
    path('store/', views.store, name="store"),
    path('blog/', views.blog, name="blog"),
    path('search_item/', views.search_item, name="searchItem"),
    path('search/', views.search, name="search"),
    path('contact/', views.contact, name="contact"),
]
