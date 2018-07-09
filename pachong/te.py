from bs4 import BeautifulSoup
import requests

URL = "http://www.ngchina.com.cn/animals/"
html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
img_div = soup.find_all('div', {"class": "con_l"})
for div in img_div:
    imgs = div.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)