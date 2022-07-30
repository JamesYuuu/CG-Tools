from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup
import os

class PictureSpider(object):
    def __init__(self,url):
        self.url=url

    def get_url_text(self):
        r=requests.get(url=self.url)
        soup=BeautifulSoup(r.content,'lxml')
        return soup

    def search_pictures(self,soup):
        link=list()
        for picture in soup.find_all('img'):
            # FIXME:根据尺寸选取图片，而非根据格式
            if picture.get('data-type')=='png':
                link.append(picture.get('data-src'))
        return link

    def download_picture(self,link):
        if not os.path.exists('./image'):
            os.mkdir('./image')
        i=0
        for img_src in link:
            i=i+1
            image=Image.open(BytesIO(requests.get(img_src).content))

            image = image.resize((1920,1080),resample=Image.LANCZOS)

            image.save(f'./image/{i}.png') 


url='https://mp.weixin.qq.com/s/9a5yTe0RACXLM3Pqqb9sRg'
spider=PictureSpider(url)
soup=spider.get_url_text()
link=spider.search_pictures(soup)
spider.download_picture(link)

