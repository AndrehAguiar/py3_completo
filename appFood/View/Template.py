class Template(object):

    def __init__(self):
        super(Template, self).__init__()
        self.__page = ""
        self.__title = f"Time2eat | "
        self.__content = ""
        self.__client = ""
        self.template = ""

    def _setPage(self, page):
        self.__page = page
        self.__title += f"{page}"

    def _setClient(self, client):
        self.__client = client

    def _setContent(self, content):
        self.__content = content
        self.template = self.__getTemplate()

    def __getHead(self):
        head = f"""
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>{self.__title}</title>
            <link rel='stylesheet' href='../static/style.css' />
        </head>"""
        return head

    def __getHeader(self):
        name = "" if self.__client == "" else self.__client.get('name')
        points = "" if self.__client == "" else self.__client.get('points')
        header = f"""<header>
        <div id='logo'>Time2eat</div>
        <span id='sp-client'>{name} | {points}pts.</span>
        <div id='basket' onclick='showBasket()'>
        <div id='bar'></div><div id='bar'></div><div id='bar'></div>
        </div>
        </header>"""
        return header

    def __getSection(self):
        section = f"""
        <section class='container'>
            <div id='dv-basket'><div id='basket-items'>Nenhum item adicionado!</div><button type='submit' id='btn-chkout' disabled >CHECKOUT</button></div>
            {self.__content}
        </section>
        """
        return section

    def __getFooter(self):
        footer = """
        <footer>Curso Python Avançado | Flask</footer>
        """
        return footer

    def __getTemplate(self):
        template = f"""
        <html lang="pt-br" dir="ltr">
            {self.__getHead()}
            <body>
            {self.__getHeader()}
            {self.__getSection()}
            {self.__getFooter()}
            </body>
            <script src='../static/script.js'></script>
        </html>"""
        return template
