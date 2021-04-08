class Client(object):
    """docstring for Client."""

    def __init__(self, name, points):
        super(Client, self).__init__()
        self.__name = name
        self.__points = points

    def getName(self):
        return self.__name

    def getPoints(self):
        return self.__points

    def updatePoints(self):
        self.__points += 1
