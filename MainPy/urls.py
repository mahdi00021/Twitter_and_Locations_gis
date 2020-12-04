"""MainPy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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


import location_finder
import tweeter_crawler
from tweeter_crawler import views
from location_finder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/twitter/online-tweets-save', tweeter_crawler.views.read_and_save),
    path('api/twitter/save-images', tweeter_crawler.views.save_images),
    path('api/twitter/read-all', tweeter_crawler.views.read_data_from_mongodb),
    path('api/twitter/find-data', tweeter_crawler.views.find_data),
    path('api/location/all-locations-find',  location_finder.views.all_locations_find),
    path('api/menu', tweeter_crawler.views.menu),
]
