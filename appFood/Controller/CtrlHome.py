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
        for i, product in enumerate(products):
            self.content+=f"""<div id='content'>
            <div class='item-name' id='item-{i}-name'><h3>{product.getName()}</h3></div>
            <div class='item-image' id='item-{i}-image'><img src={product.getImage()} /></div>
            <div class='item-description' id='item-{i}-description'>{product.getDescription()}</div>
            <div id='options'>
            <button class='item-sub' type='button' id='sub-{i}' onclick='subItem({i})' disabled> - </button>
            <span class='item-qtd' id='item-{i}-qtd'>0</span>
            <button class='item-sum' type='button' id='sum-{i}' onclick='sumItem({i})'> + </button>
            <div><small>R$ </small><span class='item-price' id='item-{i}-price'> {"{:.2f}".format(product.getPrice())}</span></div>
            </div>
            <button class='item-add' type='button' id='item-{i}-add' onclick='addItem({i})' disabled>ADD ITEM</button>
            </div>"""

    def __repr__(self):
        return self.content
