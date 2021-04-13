import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('./Utils/logs/checkout.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Checkout(object):
    """docstring for Checkout."""

    def __init__(self, *args):
        super(Checkout, self).__init__()
        self.__client = args[0]
        self.__products = args[1]
        self.__qtd = args[2]
        self.__total = self.__setTotal()
        self.__discount = self.__setDiscount()
        self.__payable = self.__total - self.__discount
        logger.info(f'Client "{self.__client.getEmail()}"\nProducts "{[p.getName() for p in self.__products]}"\n\
        Quantity "{self.__qtd}"\nTotal "{self.__total}"\nDiscount "{self.__discount}"\nPayable "{self.__payable}"')

    def getTotal(self):
        return self.__total

    def getDiscount(self):
        return self.__discount

    def getPayable(self):
        return self.__payable

    def __promoTEN(self):
        """MORE THEN de $100"""
        if self.__total > 100:
            discount = self.__total * 0.1
            return discount
        return 0

    def __promoFIVE(self):
        """MORE THEN OR EQUAL 4 items diferent"""
        if  len(set(p.getName() for p in self.__products)) >= 4:
            discount = self.__total * 0.05
            return discount
        return 0

    def __promoTREE(self):
        """MORE THEN OR EQUAL 500 Pts"""
        if self.__client.getPoints() >= 500:
            discount = self.__total * 0.03
            return discount
        return 0

    def __setTotal(self):
        return sum(p.getPrice() * q for p, q in zip(self.__products, self.__qtd))

    def __setDiscount(self):
        return max([self.__promoTEN(), self.__promoFIVE(), self.__promoTREE()])
