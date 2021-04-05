from ..Controller.ctrlScraper import CtrlScraper

class ViewScraper(object):
    """docstring for ViewScraper."""

    def __init__(self):
        super(ViewScraper, self).__init__()

        self.__ctrlScraper = CtrlScraper()
        self.__response = self.__ctrlScraper.getResponse()
        self.__summary = self.__ctrlScraper.getSummary()
        self.__raw = self.__ctrlScraper.getRaw()
        self.__content = self.__ctrlScraper.getContent()
        self.__contWords = self.__ctrlScraper.wordsFreq()
        self.__cloud = self.__ctrlScraper.wordCloud()

        self.__template = None
        self.__head = self.__getHead()
        self.__nav = self.__getNav()
        self.__section = self.__getSection()
        self.__footer = self.__getFooter()

    def __getHead(self):
        head ="""
        <head>
          <meta charset="utf-8">
          <title>WEB Scraping Python/Flask</title>
          <link rel="stylesheet" href="../static/style.css">
        </head>"""
        return head

    def __getNav(self):
        nav = f"""
        <h1>WEB Scraping</h1>
        <nav>
            <div><a href='/'>Voltar</a> | Request status code: {self.__response.status_code}</div>
            <div>
                <button type='button' onclick='showRawCode()'>View Raw</button>
                <button type='button' onclick='showSummary()'>View Summary</button>
                <button type='button' onclick='showWords()'>View word</button>
            </div>
        </nav>"""
        return nav

    def __getSection(self):
        section = f"""
        <section>
            <container>
                <div id='raw-code'>
                    <pre><xmp>{self.__raw}</xmp></pre>
                </div>
                <div id='summary'>
                    <ul>{self.__summary}</ul>
                </div>
                <div id='content'>{self.__content}</div>
                <div id='cont-words'><ol>{self.__contWords}</ol></div>
            </container>
            <div id='cloud'><img src=\'data:image/png;base64,{self.__cloud}\'></div>
        </section>"""
        return section

    def __getFooter(self):
        footer = """
        <footer>Curso Python/Flask - WEB Scraping</footer>"""
        return footer

    def __setTemplate(self):
        self.__template = f"""
        <html lang="pt-br" dir="ltr">
            {self.__head}
            <body>
                {self.__nav}
                {self.__section}
                {self.__footer}
                <script src='../static/scripts.js'></script>
            </body>
        </html>"""

    def getTemplate(self):
        self.__setTemplate()
        return self.__template
