from Model.Product import Product
from Utils.Conn import Conn

class CtrlProduct(object):
    """docstring for CtrlProduct."""

    def __init__(self):
        super(CtrlProduct, self).__init__()
        self.__conn = None
        self.__products = []
        self.__items = []
        self.__loadProducts()

    def __loadProducts(self):
        self.__conn = Conn()
        try:
            flag, products = self.__conn._selectAll(table="product")
            if not flag:
                self.__setProducts()
            self.__items = products
        except:
            self.__setProducts()

    def __setProducts(self):
        self.__conn = Conn()
        name = "name text"
        description = "description text"
        price = "price real"
        image = "image text"
        if not self.__conn._createTable(name, description, price, image, table="product"):
            self.__loadProducts()

    def getProducts(self):
        if self.__items == None:
            self.__loadProducts()
        for product in self.__items:
            self.__setProduct(product)
        return self.__products

    def __setProduct(self, product):
        item = Product(*product)
        self.__products.append(item)
