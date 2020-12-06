import queue
import threading
from OrmMongodbRepository.OrmRepository import OrmRepository
from location_finder.models import LocationM
from location_finder.serializers import LocationMSerializer


class DoWorkLocations:

    q = queue.Queue()
    threads = []
    len = 0
    num_worker_threads = len
    data_serializer = []

    @staticmethod
    def do_work(item):

        raw_query = """SELECT id ,latitude, name_point,longitude FROM location_finder_locationm WHERE ST_Contains( ST_SetSRID( 'POLYGON(( """ + item + """ ))'::GEOMETRY, 4326 ), the_geom );"""
        cursor = LocationM.objects.raw(raw_query)
        DoWorkLocations.data_serializer = LocationMSerializer(cursor, many=True).data


    @staticmethod
    def source():
        return range(DoWorkLocations.num_worker_threads)

    @staticmethod
    def worker():
        while True:
            item = DoWorkLocations.q.get()
            if item is None:
                break
            DoWorkLocations.do_work(item)
            DoWorkLocations.q.task_done()

    @staticmethod
    def doing():

        for i in range(DoWorkLocations.len):
            t = threading.Thread(target=DoWorkLocations.worker)
            t.start()
            DoWorkLocations.threads.append(t)

        DoWorkLocations.q.join()
        print("doing..........")
        return True

    @staticmethod
    def add_queue(item):
            DoWorkLocations.q.put(item)

        # block until all tasks are done

    @staticmethod
    def get_data():
           return DoWorkLocations.data_serializer
