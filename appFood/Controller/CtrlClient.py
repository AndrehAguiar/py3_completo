from Model.Client import Client
from Utils.Conn import Conn

class CtrlClient(object):
    """docstring for CtrlClient."""

    def __init__(self):
        super(CtrlClient, self).__init__()
        self.__conn = None
        self.__clients = []
        self.__items = []
        self.__loadClients()

    def __loadClients(self):
        self.__conn = Conn()
        try:
            flag, clients = self.__conn._selectAll(table="client")
            if not flag:
                self.__setClients()
            self.__items = clients
        except Exception as e:
            self.__setClients()

    def __setClients(self):
        self.__conn = Conn()
        name = "name text"
        email = "email text"
        points = "points integer"
        if not self.__conn._createTable(name, points, email, table="client"):
            self.__loadClients()

    def getClients(self):
        if self.__items == None:
            self.__loadClients()
        for client in self.__items:
            self.__setClient(client)
            print(self.__clients.__dict__)
        return self.__clients

    def getClient(self, email):
        self.__conn = Conn()
        try:
            flag, client = self.__conn._selectEach("email", email, table="client")
            client = Client(*client)
            return flag, client
        except Exception as e:
            return flag


    def __setClient(self, client):
        item = Client(*client)
        self.__clients.append(item)
