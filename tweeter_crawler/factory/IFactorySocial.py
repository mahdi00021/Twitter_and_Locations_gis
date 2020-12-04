""" this class is interface for implement factory pattern"""
import abc


class IFactorySocial(metaclass=abc.ABCMeta):

    @staticmethod
    def read_and_save(request):
        pass

    @staticmethod
    def save_images(request):
        pass

    @staticmethod
    def read_data_from_mongodb():
        pass

    @staticmethod
    def find_data(request):
        pass
