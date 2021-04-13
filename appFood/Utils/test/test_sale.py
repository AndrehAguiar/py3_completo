import unittest
from Conn import Conn

class TestClient(unittest.TestCase):
    """docstring for TestClient."""

    def test_data(self):

        id = [7,8,9,10]
        client = ["Alex Green","James Brown","Robert Gray","Jessy Blue"]

        products = [["Hamburguer de Frango","Hamburguer de Frango","Hamburguer de Picanha","Hamburguer de Picanha"],["Hamburguer Vegano","Hamburguer de Picanha","Pizza Calabresa"],["Pizza Calabresa","Refrigerante"],["Pizza de Frango","Batata Frita","Refrigerante"]]

        qtd = [[2,3,1,2],[1,2,1],[1,2,3],[1,3,3]]
        value = [90.5,75.5,50.9,101.3]

        fields = "id,client,product,quantity,value"
        for i, _ in enumerate(name):
            values=f"'{id[i]}','{client[i]}','{products[i]}','{qtd[i]}','{value[i]}'"
            try:
                conn = Conn()
                self.assertEqual(conn._insertItem(fields, values, table="client"), True)
            except Exception as e:
                print("TEST_CLIENT============>", e)

    if __name__ == '__main__':
        unittest.main()
