from .CtrlProduct import CtrlProduct

class CtrlHome(object):
    """docstring for CtrlHome."""

    def __init__(self):
        super(CtrlHome, self).__init__()
        self.content = ""
        self.__ctrlProduct = CtrlProduct()
        self.__setContent()

    def __setContent(self):
        products = self.__ctrlProduct.getProducts()
        for product in products:
            self.content+=f"""<div id='content'>
            <div id='item-name'><h3>{product.getName()}</h3></div>
            <div id='item-image'><img src={product.getImage()} /></div>
            <div id='item-price'>{product.getPrice()}</div>
            <div id='item-description'>{product.getDescription()}</div>
            </div>"""

    def __repr__(self):
        return self.content
