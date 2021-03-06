import json
from .CtrlProduct import CtrlProduct
from .CtrlClient import CtrlClient
from Model.Checkout import Checkout

class CtrlCheckout(object):
    """docstring for CtrlCheckout."""

    def __init__(self, shop):
        super(CtrlCheckout, self).__init__()
        self.checkout = None
        self.content = ""
        self.__shopItems = ""
        self.__products = []
        self.__shopItems = json.loads(shop)
        self.__ctrlProduct = CtrlProduct()
        self.__ctrlClient = CtrlClient()
        self.__setShop()
        self.__setContent()

    def __setShop(self):
        dctItems = {}
        products = []
        qtd = []
        shop = self.__shopItems
        for i, item in enumerate(shop['userBasket']):
            qtd.append(int(self.__shopItems['userBasket'][str(i)]['qtd']))
            dctItems.setdefault(shop['userBasket'][str(i)]['item'], 0)
            _, product = self.__ctrlProduct.getProduct(shop['userBasket'][str(i)]['item'])
            dctItems[shop['userBasket'][str(i)]['item']]+=1
            self.__products.append(product)

        name = shop['userLogged']
        flag, client = self.__ctrlClient.getClient('name', name)
        self.checkout = Checkout(client, self.__products, qtd)
        return client

    def __setContent(self):
        total = 0
        self.content = f"""<div id='checkout'>"""
        for i, product in enumerate(self.__products):
            qtd = int(self.__shopItems['userBasket'][str(i)]['qtd'])
            price = float(product.getPrice())
            total += (price*qtd)
            self.content += f"""<div id='content'>
            <div id='basket-item-{i}'><img src={product.getImage()} /></div>
            <div id='item-{i}-descr'>
            <div>{product.getName()} </div>
            <div>qtd. {qtd} <div> R$ {price}</div>
            </div>
            <div><small> R$ </small> {"{:.2f}".format(price*qtd)}</div>
            </div>
            </div>"""

        self.content +=f"""<div id='total'><span>Total da compra</span><small>R$ </small> {"{:.2f}".format(self.checkout.getTotal())}</div>
        <div id='discount'><span>Desconto</span><small>- R$ </small> {"{:.2f}".format(self.checkout.getDiscount())}</div>
        <div id='payable'><span>Total a pagar</span><small>R$ </small> {"{:.2f}".format(self.checkout.getPayable())}</div>
        <form action='/confirm/check' method='POST'>
        <input type='hidden' value='{json.dumps(self.__shopItems)}' name='userShop' />
        <button type='submit'>Confirmar</button>
        </form>
        </div>"""

    def __repr__(self):
        return self.content
