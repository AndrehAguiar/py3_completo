from Utils.Conn import Conn
from Controller.CtrlClient import CtrlClient

class TestClient(object):
    """docstring for TestClient."""

    def __init__(self):
        super(TestClient, self).__init__()
        self.name = ["Alex Green","James Brown","Robert Gray","Jessy Blue"]

        self.points = [600, 100, 500, 1000]

        self.email = ["alex.green@emal.com",
        "james.brown@email.com",
        "robert.gray@email.com",
        "jessy.blue@email.com"]

    def testData(self):
        fields = "name,points,email"
        for i, _ in enumerate(self.name):
            values=f"'{self.name[i]}','{self.points[i]}','{str(self.email[i])}'"
            try:
                self.__conn = Conn()
                self.__conn._insertItem(fields, values, table="client")
            except Exception as e:
                print("TEST_CLIENT============>", e)
