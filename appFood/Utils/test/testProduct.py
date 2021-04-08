from Utils.Conn import Conn
from flask import url_for, redirect

class TestProduct(object):
    """docstring for TestProduct."""

    def __init__(self):
        super(TestProduct, self).__init__()

        self.__conn = None

        self.name = ["Hamburguer de Frango","Hamburguer de Picanha","Hamburguer Vegano","Pizza Calabresa","Pizza de Frango","Batata Frita","Refrigerante"]

        self.price = [12.90, 15.90, 12.90, 19.90, 17.90, 9.90, 4.90]

        self.description = ["Mussum Ipsum, cacilds vidis litro abertis. Sapien in monti palavris qui num significa nadis i pareci latim. Detraxit consequat et quo num tendi nada. Manduma pindureta quium dia nois paga. Diuretics paradis num copo é motivis de denguis.",
        "Mussum Ipsum, cacilds vidis litro abertis. Diuretics paradis num copo é motivis de denguis. Si u mundo tá muito paradis? Toma um mé que o mundo vai girarzis! Quem num gosta di mim que vai caçá sua turmis! Nec orci ornare consequat. Praesent lacinia ultrices consectetur. Sed non ipsum felis.",
        "Mussum Ipsum, cacilds vidis litro abertis. Detraxit consequat et quo num tendi nada. Quem manda na minha terra sou euzis! Leite de capivaris, leite de mula manquis sem cabeça. Interessantiss quisso pudia ce receita de bolis, mais bolis eu num gostis.",
        "Mussum Ipsum, cacilds vidis litro abertis. Aenean aliquam molestie leo, vitae iaculis nisl. Si u mundo tá muito paradis? Toma um mé que o mundo vai girarzis! Viva Forevis aptent taciti sociosqu ad litora torquent. Vehicula non. Ut sed ex eros. Vivamus sit amet nibh non tellus tristique interdum.",
        "Mussum Ipsum, cacilds vidis litro abertis. Vehicula non. Ut sed ex eros. Vivamus sit amet nibh non tellus tristique interdum. Quem num gosta di mé, boa gentis num é. Praesent vel viverra nisi. Mauris aliquet nunc non turpis scelerisque, eget. Suco de cevadiss, é um leite divinis, qui tem lupuliz, matis, aguis e fermentis.",
        "Mussum Ipsum, cacilds vidis litro abertis. Nec orci ornare consequat. Praesent lacinia ultrices consectetur. Sed non ipsum felis. Pra lá , depois divoltis porris, paradis. Aenean aliquam molestie leo, vitae iaculis nisl. Si num tem leite então bota uma pinga aí cumpadi!",
        "Mussum Ipsum, cacilds vidis litro abertis. Quem num gosta di mé, boa gentis num é. Praesent vel viverra nisi. Mauris aliquet nunc non turpis scelerisque, eget. Pra lá , depois divoltis porris, paradis. Copo furadis é disculpa de bebadis, arcu quam euismod magna."]

        self.image = ["https://exame.com/wp-content/uploads/2020/09/the-sandwich-popeyes-burger-king-e1599567751664.jpg?quality=70&strip=info&w=1024",
        "https://upload.wikimedia.org/wikipedia/commons/6/62/NCI_Visuals_Food_Hamburger.jpg",
        "https://aletp.com.br/wp-content/uploads/2017/10/mcvegan.jpg",
        "https://www.alegrafoods.com.br/wp-content/uploads/2020/07/9-img-blog.png",
        "https://www.hojetemfrango.com.br/wp-content/uploads/2019/01/shutterstock_333724454.jpg",
        "https://s2.glbimg.com/6TYFXwek9ZpNXFeOzas09KizMKk=/0x0:1280x853/924x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2020/T/K/Hh8h2GR96v392DAkAqyA/912c9713-321e-4dfd-bca9-888c05c5ce50.jpeg",
        "http://i.mlcdn.com.br/portaldalu/fotosconteudo/43225.jpg"]

    def testData(self):
        fields = "name,description,price,image"
        for i, _ in enumerate(self.name):
            values=f"'{self.name[i]}','{self.description[i]}','{str(self.price[i])}','{self.image[i]}'"

            self.__conn = Conn()
            response = self.__conn._insertItem(fields, values, table="product")

        return redirect(url_for('index'))
