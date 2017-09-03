# 在真实网页中获取信息：
# 每次点击页面就是一次request，然后接受response:http协议
# request: get/post
from bs4 import BeautifulSoup
import requests
import time
#伪造手机端：
headers = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1'
}

url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-oa60-New_York_City_New_York.html#ATTRACTION_LIST'

wb_data = requests.get(url, headers = headers)
soup = BeautifulSoup(wb_data.text, 'lxml')
print(soup)
imgs = soup.select('div.thumb.thumbLLR.soThumb > img')
for i in imgs:
    print(i.get('src'))

