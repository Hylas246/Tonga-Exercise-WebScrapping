# Import flask and other library
from flask import Flask, render_template

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://gamek.vn/'

app = Flask(__name__)


def get_url(URL):
   
    """Get HTML from URL gamek.vn 
    """
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def crawl(URL):
    """ Get HTML code from the link
        Find all class info (the news article of the website)
        Find information in the info tag and append to the dictionary
    """ 
    soup = get_url(URL)
    infos = soup.find_all('li', class_='top')
    data = []
    for new in infos:
        try:
            d = {'imgurl':'','title':'','content':'','category':'','author':''}
            d['imgurl'] = new.img['src']
            d['title'] = new.a['title']
            d['content'] = new.p.string
            d['category'] = new.find(a,class_='categame').string
            d['author'] = new.find(a,class_='author').string
            
        except:
            pass
        data.append(d)
    return data

@app.route('/')
def index():
    data = crawl_vnexpress(BASE_URL)
    return render_template('main.html', data=data)

if __name__ == '__main__':
  app.run(host='0.0.0.1', port=5000, debug=True)
