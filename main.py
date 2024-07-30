from bs4 import BeautifulSoup as BS
import requests

def get_html(url):
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        return response.text
    return None


def get_glide_link(html):
    soup = BS(html,'html.parser')
    content = soup.find('div',class_='main-content')
    posts = content.find('div', class_='listings-wrapper')
    post = posts.find_all('div', class_='listing')
    for p in post:
        r_side = p.find('div', class_='right-info')
        title = r_side.find('p', class_='title')
        print(title.text.strip())
   


def main():
    URL = 'https://www.house.kg/kupit-kvartiru?'
    html = get_html(url=URL)
    get_glide_link(html=html)
    
 
if __name__ == '__main__':
    main()
































