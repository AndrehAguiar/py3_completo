class Client(object):
    """docstring for Client."""

    def __init__(self, name, points, email):
        super(Client, self).__init__()
        self.__name = name
        self.__points = points
        self.__email = email

    def getName(self):
        return self.__name

    def getPoints(self):
        return self.__points

    def getEmail(self):
        return self.__email

    def updatePoints(self):
        self.__points += 1
