import re
import base64
import requests
import matplotlib.pyplot as plt

from io import BytesIO
from wordcloud import WordCloud
from ..Model.Scraper import Scraper

class CtrlScraper(object):
    """docstring for CtrlScraper."""

    def __init__(self):
        super(CtrlScraper, self).__init__()

        self.__response = requests.get('http://127.0.0.1:5000/')
        self.__scraper = Scraper(self.__response)

    def getResponse(self):
        if self.__response.status_code == 200:
            return self.__response
        else:
            return f'Não foi possível estabeler a conexão.\n Status code: {self.__response.status_code}'

    def getRaw(self):
            raw = self.__scraper.getRaw()
            return raw

    def getSummary(self):
        summary = ''
        tags, freq = self.__scraper.getSummary()
        for tag, occur in zip(tags, freq):
            summary+=f'<li><div onclick="showDiv(\'{tag}\')">{tag}: {occur}</div></li>'
        return summary

    def getContent(self):
        tags, freq  = self.__scraper.getSummary()
        content = ''
        for j, tag in enumerate(tags):
            content+=f'<div class="tag" id="dv-{tag}">'
            for i in range(freq[j]):
                text = self.__scraper.getContent(tag,i)
                content+=f'<div><xmp>{text}</xmp></div>'
            content+='</div>'
        return content

    def wordCounter(self):
        index = {}
        p = re.compile(r'\w+')
        wordFreq = []
        text = self.__scraper.getText()
        for match in p.finditer(text):
            word = match.group()
            loc = (match.span(),)
            index.setdefault(word, []).append(loc)

        for word in sorted(index, key=str.upper):
            wordFreq.append((word, len(index[word])))
        return dict(wordFreq)

    def wordsFreq(self):
        contWords = ""
        dctWords = self.wordCounter()
        dctWords = dict(sorted(dctWords.items(), key=lambda x: x[1], reverse=True))
        for key in dctWords.keys():
            contWords+=f'<li>{key}: {dctWords[key]}</li>'
        return contWords

    def wordCloud(self):
        tmpfile = BytesIO()
        cloud = WordCloud(background_color='white')
        cloud.generate_from_frequencies(self.wordCounter())

        fig, ax = plt.subplots(figsize=(20,8), dpi=300)
        plt.imshow(cloud)
        plt.axis('off')
        fig.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
        return encoded
