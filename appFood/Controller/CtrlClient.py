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
        field = args[0]
        value = args[1]
        try:
            self.__conn = Conn()
            flag, client = self.__conn._selectEach(f'{field}', f'{value}', table="client")
            print(client)
            client = Client(*client)
            return flag, client
        except Exception as e:
            print("CATCH GetClient", e)
            return flag


    def __setClient(self, client):
        item = Client(*client)
        self.__clients.append(item)
