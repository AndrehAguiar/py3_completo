import json
from Model.Sale import Sale
from Utils.Conn import Conn
from .CtrlProduct import CtrlProduct
from .CtrlClient import CtrlClient

class CtrlSale(object):
    """docstring for CtrlSale."""

    def __init__(self):
        super(CtrlSale, self).__init__()
        self._id = None
        self.__con = None
        self.__sale = None
        self._sales = []
        self.__loadSales()
        self.__status = False
        self.__ctrlProduct = CtrlProduct()
        self.__ctrlClient = CtrlClient()

    def _setShop(self, *args):
        self.__sale = Sale(*args)
        return self.__sale

    def _getClient(self, name):
        _, client = self.__ctrlClient.getClient('name', name)
        return client

    def _getProducts(self, sale):
        products = []
        qtd = []
        for item in sale:
            _, product = self.__ctrlProduct.getProduct(item[2])
            qtd.append(item[3])
            products.append(product)
        return products, qtd

    def __loadSales(self):
        try:
            self.__conn = Conn()
            flag, sales = self.__conn._selectAll(table="sale")
            if not flag:
                self.__setSales()
            self._sales = sales
            self._id = self._sales[-1][0] + 1
            print(self._id)
        except Exception as e:
            print("EXCEPTION LOAD_SALES", e)
            self.__setSales()

    def _getSale(self, id):
        try:
            self.__conn = Conn()
            flag, sale = self.__conn._selectAllWhere("id", id, table="sale")
            return flag, sale
        except Exception as e:
            print(e)
            return flag

    def __setSales(self):
        id = "id integer"
        client = "client text"
        product = "product text"
        quantity = "quantity integer"
        value = "value real"
        try:
            self.__conn = Conn()
            if not self.__conn._createTable(id, client, product, quantity, value, table="sale"):
                self.__loadSales()
        except Exception as e:
            print("SET SALES", e)

    def __insertSale(self, *args):
        try:
            self.__conn = Conn()
            self.__conn._insertItem(args[0], args[1], table="sale")
        except Exception as e:
            print("INSERT_SALE============>", e)

    def _setSale(self, sale):
        fields = "id,client,product,quantity,value"
        sale = json.loads(sale)
        if self._id == None:
            self.__loadSales()

        for i, _ in enumerate(sale['userBasket']):

            values=f"'{self._id}','{sale['userLogged']}','{sale['userBasket'][str(i)]['item']}','{sale['userBasket'][str(i)]['qtd']}','{sale['userBasket'][str(i)]['price']}'"

            try:
                self.__insertSale(fields, values)
                self.__status = True
            except Exception as e:
                self.__status = False
                print("INSERT_STATUS ============>", e)
        return self.__status

    def __repr__(self):
        return self.content
