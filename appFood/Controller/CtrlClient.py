from Model.Client import Client
from Utils.Conn import Conn

class CtrlClient(object):
    """docstring for CtrlClient."""

    def __init__(self):
        super(CtrlClient, self).__init__()
        self.__conn = None
        self.__clients = []
        self.__loadClients()

    def __loadClients(self):
        self.__conn = Conn()
        try:
            flag, clients = self.__conn._selectAll(table="client")
            if not flag:
                self.__setClients()

            self.__clients = clients
        except:
            self.__setClients()

    def __setClients(self):
        self.__conn = Conn()
        name = "name text"
        email = "email text"
        points = "points int"
        if not self.__conn._createTable(name, points, email, table="client"):
            self.__loadClients()

    def getClients(self):
        return self.__clients
