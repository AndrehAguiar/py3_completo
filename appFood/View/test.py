from .Template import Template
from Utils.test.testProduct import TestProduct

class TestData(Template):
    """docstring for TestData."""
    __conn = None
    __testProduct = TestProduct()
    def __init__(self):
        super(TestData, self).__init__("Test Data", self.__getContent())

    def __getContent(self):
        content = "<div class='loader'></div>"
        self.__testProduct.testData()
        return f'{content}'

    def __repr__(self):
        return self.template
