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
        try:
            self.__conn = Conn()
            flag, products = self.__conn._selectAll(table="product")
            if not flag:
                self.__setProducts()
            self.__items = products
        except Exception as e:
            self.__setProducts()

    def __setProducts(self):
        name = "name text"
        description = "description text"
        price = "price real"
        image = "image text"
        try:
            self.__conn = Conn()
            if not self.__conn._createTable(name, description, price, image, table="product"):
                self.__loadProducts()
        except Exception as e:
            print(e)

    def getProduct(self, name):
        try:
            self.__conn = Conn()
            flag, product = self.__conn._selectEach("name", name, table="product")
            product = Product(*product)
            return flag, product
        except Exception as e:
            print(e)
            return flag

    def getProducts(self):
        if self.__items == None:
            self.__loadProducts()
        for product in self.__items:
            self.__setProduct(product)
        return self.__products

    def __setProduct(self, product):
        item = Product(*product)
        self.__products.append(item)
