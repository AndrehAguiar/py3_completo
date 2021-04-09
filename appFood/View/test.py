from .Template import Template
from Utils.test.testProduct import TestProduct
from Utils.test.testClient import TestClient

class TestData(Template):
    """docstring for TestData."""
    __testProduct = TestProduct()
    __testClient = TestClient()

    def __init__(self):
        super(TestData, self).__init__("Test Data", self.__getContent())
        self.__testClient.testData()
        self.__testProduct.testData()

    def __getContent(self):
        content = """
        <div id='loader' class='loader'></div>
        <script>setTimeout(function(){window.location.href = './'; }, 3000);</script>"""
        return f'{content}'

    def __repr__(self):
        return self.template
