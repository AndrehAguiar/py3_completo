from .Template import Template
from Controller.CtrlHome import CtrlHome
from Controller.CtrlClient import CtrlClient

class Home(Template):
    """docstring for Home."""
    def __init__(self):
        super(Home, self).__init__("Home", self.__getContent())
        self.__ctrlHome = CtrlHome()
        self.__ctrlClient = CtrlClient()

    def __getContent(self):
        content = CtrlHome()
        return f'{content}'

    def __repr__(self):
        return self.template
