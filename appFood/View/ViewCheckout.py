from .Template import Template
from Controller.CtrlCheckout import CtrlCheckout

class Checkout(Template):
    """docstring for Checkout."""

    def __init__(self):
        super(Checkout, self).__init__()
        self._setPage("Chekout")
        self.__shop = None

    def setContent(self):
        self._setContent(self.__getContent())

    def setShop(self, shop):
        self.__shop = shop

    def __getContent(self):
        content = CtrlCheckout(self.__shop)
        return f'{content}'

    def __repr__(self):
        return self.template
