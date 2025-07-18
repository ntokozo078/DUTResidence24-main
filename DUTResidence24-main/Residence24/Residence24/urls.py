"""
URL configuration for Residence24 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from main import views  # Assuming your home view is in the main app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),  # URL for the home page
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('', include('main.urls')),  # Include the main app URLs for the homepage and other pages
    path('student/', include('student.urls')),  # Include student app URLs
    path('housing/', include('housing.urls')),  # Include housing app URLs
    path('users/', include('usermanagement.urls')),  # Include authentication URLs

     # This line will redirect the root URL to the home view
    path('', views.home, name='home'),  # Empty path now points to home

]
