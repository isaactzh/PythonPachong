#什么是异步加载：
#访问网站时，除有些网页不需要换页就可以持续加载，这就是异步数据
#一次请求只能获得部分数据，持续部分由JS加载
#找出URL的规律
from bs4 import BeautifulSoup
import requests
import time
url = 'https://knewone.com/discover?page=3'
def get_page(url, data=None):

    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    imgs = soup.select('a.cover-inner > img')
    titles = soup.select('section.content > h4 > a')
    links = soup.select('section.content > h4 > a')

    if data == None:
        for img, title, link in zip(imgs, titles, links):
            data = {
                'img': img.get('src'),
                'title': title.get('title'),
                'link': link.get('href')
            }
            print(data)

#自控页码的函数
def get_more_pages(start, end):
    for one in range (start, end):
        get_page(url+str(one))
    time.sleep(2)

get_more_pages(1,10)