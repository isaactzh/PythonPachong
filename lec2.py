# 在真实网页中获取信息：
# 每次点击页面就是一次request，然后接受response:http协议
# request: get/post
from bs4 import BeautifulSoup
import requests

url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text, 'lxml')
# print(soup.prettify())
# titles = soup.select('.top_attractions > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) >\
#                      div:nth-of-type(2) > div:nth-of-type(1) > a:nth-of-type(1)')
titles = soup.select('div.name > a')
#可以更加精简，具体（titles = soup.select('div.name > a[target ="blank"]')
#titles = soup.find_all('a', {'class': 'poiTitle'})
#print(titles)

#for title in titles:
#    print(title.get_text())

imgs = soup.select('img[width="200"]')
#print(imgs)
cates = soup.select('div.item')
count = 0
real_cates = []
for cate in cates:
    if count < 2:
        count += 1
        continue
    else:
        #print(cate.get_text())
        real_cates.append(cate.get_text())
        count = 0
#print(cates)

for title, img, real_cate in zip(titles, imgs, real_cates):
    data = {
        'title': title.get_text(),
        'img': img.get('src'),
        'cate': real_cate
    }
    print(data)