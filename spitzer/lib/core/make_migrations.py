from spitzer.lib.core.connection import Connection


class MakeMigrations(Connection):

    __targets = list
    __path = str

    def __init__(self, targets: list, path: str):
        super(MakeMigrations, self).__init__(targets)
        self.__targets = targets
        self.__path = path

    def run(self):
        pass
