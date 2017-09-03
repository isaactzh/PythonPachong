# 在真实网页中获取信息：
# 每次点击页面就是一次request，然后接受response:http协议
# request: get/post
from bs4 import BeautifulSoup
import requests

url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-oa60-New_York_City_New_York.html#ATTRACTION_LIST'
#url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text, 'lxml')
# print(soup.prettify())

titles = soup.select('div.listing_title > a[target="_blank"]')


for title in titles:
   print(title.get_text())

imgs = soup.select('img[width="180"]')
print(imgs)
cates = soup.select('div.p13n_reasoning_v2')

#print(cates)
#for cate in cates:
   # print(list(cate.stripped_strings))

print(6666)

for title, img, cate in zip(titles, imgs, cates):
    data = {
        'title': title.get_text(),
        'img': img.get('src'),
        'cate': list(cate.stripped_strings)
    }
    print(data)











