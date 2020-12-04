import abc


class Strategy(metaclass=abc.ABCMeta):
    """
    Declare an interface common to all supported methods reads. Context

    """
    @abc.abstractmethod
    def read_data(self, name_file):
        pass
