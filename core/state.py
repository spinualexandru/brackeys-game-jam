class State(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def set(self, key, value):
        setattr(self, key, value)

    def get(self, key, default=None):
        return getattr(self, key, default)

    def clear(self):
        for key in list(self.__dict__.keys()):
            delattr(self, key)

    def all(self):
        return self.__dict__
