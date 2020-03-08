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

def find_aut(new):
    """ Find author tag in new then return the author name
    """
    tag_aut = new.find('a',class_='author')
    return tag_aut.string

def find_cat(new):
    """ Find category tag in new, then return the category nae
    """
    tag.cat = new.find('a',class_='categame') 
    return tag_cat.string

def crawl(URL):
    """ Get HTML code from the link
        Find all class info (the news article of the website)
        Find information in the info tag and append to the dictionary
        Repeat for all '
    """ 
    soup = get_url(URL)
    infos = soup.find_all('div', class_='info')
    data = []
    for new in infos:
        try:
            d = {'title':'','content':'','category':'','author':''}
            d['title'] = new.a.string
            d['content'] = new.p.string
            d['category'] = find_cat(new)
            d['author'] = find_aut(new)
            
        except:
            pass
        data.append(d)
    return data

@app.route('/')
def index():
    data = crawl_vnexpress(BASE_URL)
    return render_template('main.html', data=data)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)