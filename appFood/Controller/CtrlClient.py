import logging

from Model.Client import Client
from Utils.Conn import Conn

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('./Utils/logs/controlClient.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class CtrlClient(object):
    """docstring for CtrlClient."""

    def __init__(self):
        super(CtrlClient, self).__init__()
        self.__conn = None
        self.__client = None
        self.__clients = []
        self.__items = []
        self.__loadClients()

    def __loadClients(self):
        try:
            self.__conn = Conn()
            flag, clients = self.__conn._selectAll(table="client")
            if not flag:
                self.__setClients()
            self.__items = clients
        except Exception as e:
            self.__setClients()

    def __setClients(self):
        name = "name text"
        email = "email text"
        points = "points integer"
        try:
            self.__conn = Conn()
            if not self.__conn._createTable(name, points, email, table="client"):
                self.__loadClients()
        except Exception as e:
            print(e)

    def getClients(self):
        if self.__items == None:
            self.__loadClients()
        for client in self.__items:
            self.__setClient(client)
        return self.__clients

    def getClient(self, *args):
        logger.debug(f'Arguments "{args}"')
        try:
            self.__conn = Conn()
            flag, client = self.__conn._selectEach(f'{args[0]}', f'{args[1]}', table="client")
            logger.debug(f'Return===>Client "{client}" / Flag "{flag}"')
            self.__client = Client(*client)
            logger.debug(f'Client===>ObjClient "{self.__client}"')
            return flag, self.__client
        except Exception as e:
            print("Exception GetClient", e)
            return flag, None


    def __setClient(self, client):
        item = Client(*client)
        self.__clients.append(item)
