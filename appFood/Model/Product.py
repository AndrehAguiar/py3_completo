class Product(object):
    """docstring for Product."""

    def __init__(self, name, description, price, image):
        super(Product, self).__init__()
        self.__name = name
        self.__description = description
        self.__price = price
        self.__image = image

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getImage(self):
        return self.__image

    def getDescription(self):
        return self.__description
