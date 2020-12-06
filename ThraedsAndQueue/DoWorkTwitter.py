import queue
import threading
from OrmMongodbRepository.OrmRepository import OrmRepository


class DoWorkTwitter:

    q = queue.Queue()
    threads = []
    len = 0
    num_worker_threads = len

    @staticmethod
    def do_work(item):
        if not OrmRepository.insert(item):
            OrmRepository.insert(item)

    @staticmethod
    def source():
        return range(DoWorkTwitter.num_worker_threads)

    @staticmethod
    def worker():
        while True:
            item = DoWorkTwitter.q.get()
            if item is None:
                break
            DoWorkTwitter.do_work(item)
            DoWorkTwitter.q.task_done()

    @staticmethod
    def doing():

        for i in range(DoWorkTwitter.len):
            t = threading.Thread(target=DoWorkTwitter.worker)
            t.start()
            DoWorkTwitter.threads.append(t)

        DoWorkTwitter.q.join()

        print('stopping workers!')

    @staticmethod
    def add_qeueu(item):
            DoWorkTwitter.q.put(item)

        # block until all tasks are done


