from bs4 import BeautifulSoup

class Scraper(object):
    """docstring for Scraper."""

    def __init__(self, response):
        super(Scraper, self).__init__()

        self.__soup = BeautifulSoup(response.text, 'html.parser')

    def getRaw(self):
        return self.__soup.prettify()

    def getSummary(self):
        freq = []
        tags = ['title','h1','h2','h3','h4','h5','h6','a','div','p','img']
        for tag in tags:
            occur = self.__soup.find_all(tag)
            freq.append(len(occur))
        return tags, freq

    def getContent(self, tag, idx, link=False):
        content = self.__soup.find_all(tag)
        if tag == 'a' and not link:
            return f'{content[idx].text} | {content[idx]["href"]}'
        if tag == 'img':
            return f'{content[idx]["src"]}'
        return content[idx].text

    def getText(self):
        tags, freq = self.getSummary()
        content = ''
        for i, tag in enumerate(tags):
            for idx in range(freq[i]):
                if tag != 'img':
                    cont = self.getContent(tag, idx, link=True)
                    cont+=" "
                    content+= cont
        return content
