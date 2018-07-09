import os
from urllib.request import urlretrieve 
import requests
#os.makedirs('./img/', exist_ok=True)

IMAGE_URL = "http://img.92demo.com/dilidili/d/file/titlepic/1_1757469641.jpg"

urlretrieve(IMAGE_URL, './img/image1.png')

r = requests.get(IMAGE_URL)
with open('./img/image2.png', 'wb') as f:
    f.write(r.content)

r = requests.get(IMAGE_URL, stream=True)    # stream loading

with open('./img/image3.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)