from bs4 import BeautifulSoup as BS
import requests

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def get_glide_link(html):
    soup = BS(html,'html.parser')
    content = soup.find('div',class_='main-content')
    posts = content.find('div', class_='listings-wrapper')
    post = posts.find_all('div', class_='listing')
    links = []
    for p in post:
        r_info = p.find('div', class_='right-info')
        title = r_info.find('p', class_='title')
        link = title.find('a').get('href')
        full_link = 'https://www.house.kg' + link
        links.append(full_link)        

        # print(title.text.strip())
        # r_side = r_info.find('div', class_='right-side')
        # sep_main = r_side.find('div', class_='sep main')
        # price = sep_main.find('div', class_='price')
        # print(price.text.strip())
        # price_addit = sep_main.find('div', class_='price-addition')
        # print(price_addit.text.strip())
        # l_side = r_info.find('div', class_='left-side')
        # t_add = l_side.find('p', class_='title-addition')
        # if t_add:
        #     print(t_add.text.strip())
        # else:
        #     print('Нет ЖК')
        # address = l_side.find('div', class_='address')
        # print(address.text.strip())
        # desc = r_info.find('div', class_='description')
        # print(desc.text.strip())

    return links

def get_data(html):
    soup = BS(html, 'html.parser')
    content = soup.find('div', class_='content-wrapper')
    # phone_block = content.find('div', class_='phone-fixable-block')
    # user = phone_block.find('a', class_='name').text.strip()
    # phone = phone_block.find('div', class_='number').text.strip()
    # print(user,phone)
    # details = content.find('div', class_='details-main')
    # left = details.find('div', class_='left')
    # label = left.find_all('div', class_='label')
    # info = left.find_all('div', class_='info')
    # for i,l in zip(label, info):
    #     print(l.text.strip(), ':', i.text.strip())
    detials = content.find('div', class_='details-header')
    left = detials.find('div', class_='left')
    left1 = left.find('h1')
    print(left1.text.strip())
    c_name = left.find('div', class_='c-name')
    if c_name:
        print(c_name.find('a').text.strip())
    else:
        print('Нет ЖК')
    address = left.find('div', class_='address').text.strip()
    print(address)
    prices_block = detials.find('div',class_='right prices-block')
    price = prices_block.find_all('div', class_='price-dollar')
    price_m = prices_block.find_all('div', class_='price-som')
    for i,l in zip(price, price_m):
        print(i.text.strip(), ':', l.text.strip())
    det_m =content.find('div', class_='details-main')
    right = det_m.find('div', class_='right')
    desc = right.find('div', class_='description')
    if desc:
        print(desc.text.strip())
    else:
        print('Нет описания')

    
    



def main():
    URL = 'https://www.house.kg/kupit-kvartiru?'
    html = get_html(url=URL)
    links = get_glide_link(html=html)

    for link in links:
        html2 = get_html(url=link)
        get_data(html=html2)
    
 
if __name__ == '__main__':
    main()
































