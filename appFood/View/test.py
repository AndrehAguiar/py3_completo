from .Template import Template
from Utils.test.testProduct import TestProduct
from Utils.test.testClient import TestClient

class TestData(Template):
    """docstring for TestData."""

    def __init__(self):
        super(TestData, self).__init__()
        self.__testProduct = TestProduct()
        self.__testClient = TestClient()
        self.__setContent()
        self._setPage("Test Data")

    def __setContent(self):
        self.__testClient.testData()
        self.__testProduct.testData()
        self._setContent(self.__getContent())

    def __getContent(self):
        content = """
        <div id='loader' class='loader'></div>
        <script>setTimeout(function(){window.location.href = './'; }, 3000);</script>"""
        return f'{content}'

    def __repr__(self):
        return self.template
