from flask import Flask, render_template, render_template_string
from utilities.View.vwScraper import ViewScraper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scraper')
def scraper():
    scraper = ViewScraper()
    template = scraper.getTemplate()
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)
