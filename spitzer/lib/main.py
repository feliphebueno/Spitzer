from spitzer.lib.config.loader import ConfigLoader
from spitzer.lib.core.create import Create
from spitzer.lib.drivers.connector import Connector
from spitzer.lib.core.install import Install


class Main(object):

    __command = str
    __working_dir = str
    __config_loader = object

    def __init__(self, command: str, wd: str):
        self.__command = command
        self.__working_dir = wd
        self.__config_loader = ConfigLoader(wd)

    def run(self):
        config_connections = self.__config_loader.get_connection_tartgets()
        connector = Connector(config_connections['connections'])
        targets = connector.get_connected_targets()

        cmd = self.__command

        if cmd == 'install':
            Install(targets).run()
        elif cmd == 'create':
            Create(targets, config_connections['path']).run()
        elif cmd == 'migrations':
            pass
        elif cmd == 'migrate':
            pass
        elif cmd == 'rollback':
            pass

        connector.release_targets()
