

class ContextStrategy:
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def context(self, name_file):
        return self._strategy.read_data(self, name_file)
