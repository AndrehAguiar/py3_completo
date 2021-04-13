import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('./Utils/logs/client.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Client(object):
    """docstring for Client."""

    def __init__(self, *args):
        super(Client, self).__init__()
        self.__name = args[0]
        self.__points = args[1]
        self.__email = args[2]
        logger.info(f'Client "{self.__name}"\npoints "{self.__points}"\nemail "{self.__email}"')

    def getName(self):
        return self.__name

    def getPoints(self):
        return self.__points

    def getEmail(self):
        return self.__email

    def updatePoints(self):
        self.__points += 1
