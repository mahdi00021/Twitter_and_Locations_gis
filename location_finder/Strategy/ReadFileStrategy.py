from location_finder.Strategy.Strategy import Strategy
from location_finder.models import LocationM
from location_finder.serializers import LocationMSerializer


class ReadFileStrategy(Strategy):
    """
    This class is read polygon's of txt file and put on query
    """

    def read_data(self, name_file):
        data_serializer = []
        file = open(name_file, 'r')
        lines = file.readlines()

        for line in lines:
                raw_query = """SELECT id ,latitude, name_point,longitude FROM location_finder_locationm WHERE ST_Contains( ST_SetSRID( 'POLYGON(( """+ line +""" ))'::GEOMETRY, 4326 ), the_geom );"""
                cursor = LocationM.objects.raw(raw_query)
                data_serializer = LocationMSerializer(cursor, many=True).data

        return data_serializer
