class EcotricityClientException(Exception):

    def __init__(self, message: str, cause=None):
        self.message = message
        self.__cause__ = cause
