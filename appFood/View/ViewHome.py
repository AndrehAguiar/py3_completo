from .Template import Template
from Controller.CtrlHome import CtrlHome
from Controller.CtrlClient import CtrlClient

class Home(Template):
    """docstring for Home."""

    def __init__(self):
        """"Home", self.__getContent()"""
        super(Home, self).__init__()
        self._setPage("Home")

    def setContent(self):
        self._setContent(self.__getContent())

    def __getContent(self):
        content = CtrlHome()
        return f'{content}'

    def __repr__(self):
        return self.template
