from .Template import Template
from Controller.CtrlSale import CtrlSale

class Sale(Template):
    """docstring for Sale."""

    def __init__(self):
        super(Sale, self).__init__()
        self.__sale = None
        self.__ctrlSale = None
        self.__client = None
        self.__products = None
        self.__qtd = None
        self._setPage("Check Sale")

    def setSale(self, sale):
        self.__ctrlSale = CtrlSale()
        return self.__ctrlSale._setSale(sale)

    def setShop(self):
        self.__ctrlSale = CtrlSale()
        saleID = self.__ctrlSale._id - 1
        _, checkoutSale = self.__ctrlSale._getSale(saleID)
        self.__client = self.__ctrlSale._getClient(checkoutSale[0][1])
        self.__products, self.__qtd = self.__ctrlSale._getProducts(checkoutSale)
        self.__sale = self.__ctrlSale._setShop(self.__client, self.__products, self.__qtd)


    def setContent(self, status):
        self._setContent(self.__getContent(status))

    def __getContent(self, status):
        content = ""
        if status == 'success':
            content+=f"""
            <div id='content' class='resume'>
            <h1>SUCCESS!!</h1>
            <div id='resume-user'>
            <h3>{self.__client.getName()}</h3>
            <div id='resume-items'>
                <div id='resume-item-n'>Item</div>
                <div id='resume-item-image'>Image</div>
                <div id='resume-item-name'>Product</div>
                <div id='resume-item-qtd'>Quantity</div>
                <div id='resume-item-price'>Value</div>
            </div>"""
            total = 0
            for i, item in enumerate(self.__products):
                content+=f"""
                <div id='resume-items'>
                    <div id='resume-item-n'>{i+1}</div>
                    <div id='resume-item-image'><img src={item.getImage()} /></div>
                    <div id='resume-item-name'>{item.getName()}</div>
                    <div id='resume-item-qtd'>{self.__qtd[i]}</div>
                    <div id='resume-item-price'>{"{:.2f}".format(item.getPrice() * self.__qtd[i])}</div>
                </div>"""

            content+=f"""</div>
            <div id='resume-total'><span> TOTAL </span><span>R$  {"{:.2f}".format(self.__sale.getTotal())}</span></div>
            <div id='resume-discount'><span> DISCOUNT </span><span>R$  {"{:.2f}".format(self.__sale.getDiscount())}</span></div>
            <div id='resume-payable'><span> PAYABLE </span><span>R$  {"{:.2f}".format(self.__sale.getPayable())}</span></div>
            </div>"""
        else:
            content+="""<h1>ERROR!!</h1>"""
        #content += """<script>setTimeout(function(){window.location.href = './success'; }, 10000);</script>"""
        return f'{content}'

    def __repr__(self):
        return self.template
