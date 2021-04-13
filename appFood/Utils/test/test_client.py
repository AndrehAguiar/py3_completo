import unittest
from Conn import Conn

class TestClient(unittest.TestCase):
    """docstring for TestClient."""

    def test_data(self):

        name = ["Alex Green","James Brown","Robert Gray","Jessy Blue"]

        points = [600, 100, 500, 1000]

        email = ["alex.green@emal.com",
        "james.brown@email.com",
        "robert.gray@email.com",
        "jessy.blue@email.com"]
        fields = "name,points,email"
        for i, _ in enumerate(name):
            values=f"'{name[i]}','{points[i]}','{str(email[i])}'"
            try:
                conn = Conn()
                self.assertEqual(conn._insertItem(fields, values, table="client"), True)
            except Exception as e:
                print("TEST_CLIENT============>", e)

    if __name__ == '__main__':
        unittest.main()
