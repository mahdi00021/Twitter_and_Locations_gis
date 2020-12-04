from django.shortcuts import render

# Create your views here.
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from tweeter_crawler.factory.Factory import Factory
from tweeter_crawler.factory.TwitterCrawler import TwitterCrawler
from django.http import HttpResponse

@api_view(['POST'])
def read_and_save(request):

   data = Factory.create_class(TwitterCrawler).read_and_save(request)

   return Response(data)

@api_view(['POST'])
def save_images(request):

   data = Factory.create_class(TwitterCrawler).save_images(request)

   return Response(data)

@api_view(['GET'])
def read_data_from_mongodb(request):

   data = Factory.create_class(TwitterCrawler).read_data_from_mongodb()

   return Response(data)

@api_view(['POST'])
def find_data(request):

   data = Factory.create_class(TwitterCrawler).find_data(request)

   return Response(data)

@api_view(['GET'])
def menu(request):

   data = {
      'api/twitter/online-tweets-save' : ' method is POST and have 3 parameter : username, start_date , end_date',
      'api/twitter/save-images': ' method is POST and have 2 parameter : key , value for get from db',
      'api/twitter/read-all':' method is GET have not parameter',
      'api/twitter/find-data': ' method is POST and have 2 parameter : key , value for get from db',
      'api/location/all-locations-find': ' method is GET',
   }

   return Response(data)