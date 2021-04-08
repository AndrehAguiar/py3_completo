class Template(object):

    def __init__(self, page, content):
        super(Template, self).__init__()
        self.__page = page
        self.__title = f"Time2eat | {page}"
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
        header = """
        <header>Time2eat<button type='button' onclick='window.location.href="/testData"'>Test</button></header>"""
        return header

    def __getSection(self):
        section = f"""
        <section class='container'>
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
        </html>"""
        return template
