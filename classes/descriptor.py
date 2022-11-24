class Const:

    def __init__(self, value):
        self.value = value

    def __get__(self, *_):
        return self.value

    def __set__(self, new):
        pass


