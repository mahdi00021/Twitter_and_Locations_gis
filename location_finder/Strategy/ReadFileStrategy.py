from ThraedsAndQueue.DoWorkLocations import DoWorkLocations
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
        DoWorkLocations.len = len(lines)
        for line in lines:
                DoWorkLocations.add_queue(line)


        if DoWorkLocations.doing() is True:
            return DoWorkLocations.get_data()
        else:
            return data_serializer
