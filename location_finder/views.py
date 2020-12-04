from rest_framework.response import Response
from rest_framework.decorators import api_view
from location_finder.Strategy.ContextStrategy import ContextStrategy
from location_finder.Strategy.ReadFileStrategy import ReadFileStrategy
from django.conf import settings
import os

# Create your views here.


# this method return response of locations of postgis
@api_view(['GET'])
def all_locations_find(request):

    context_strategy = ContextStrategy(ReadFileStrategy)
    name_file = os.path.join(settings.BASE_DIR, 'location_finder\locations.txt')

    res = context_strategy.context(name_file)
    return Response(res)
