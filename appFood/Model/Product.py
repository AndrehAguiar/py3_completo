import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('./Utils/logs/product.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Product(object):
    """docstring for Product."""

    def __init__(self, name, description, price, image):
        super(Product, self).__init__()
        self.__name = name
        self.__description = description
        self.__price = price
        self.__image = image
        logger.info(f'Product "{self.__name}"\ndescription "{self.__description}"\nprice "{self.__price}"')

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getImage(self):
        return self.__image

    def getDescription(self):
        return self.__description
