from .Template import Template
from Controller.CtrlClient import CtrlClient

class Client(Template):
    """docstring for Client."""
    def __init__(self):
        super(Client, self).__init__()
        self.__ctrlClient = CtrlClient()
        self.client = ""
        self._setPage("Client")

    def setContent(self):
        self._setContent(self.__getContent())

    def __getContent(self):
        content = """<form id='form' action='http://127.0.0.1:5000/client' method='post'>
        <label for='email'>Identificação do cliente:
        <input type='email' id='email' name='email' placeholder='Qual o seu e-mail?' required /></label>
        <button type='submit' id='btn-email' value='submit'>OK</button>
        </form>
        """
        return f'{content}'

    def __setClient(self, email):
        _, self.client = self.__ctrlClient.getClient(email)

    def setClient(self, *args):
        self.__setClient(args)

    def __repr__(self):
        return self.template
