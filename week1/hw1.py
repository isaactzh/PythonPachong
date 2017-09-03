from bs4 import BeautifulSoup
import requests
import time

url = 'http://bj.58.com/pbdn/0/'
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text, 'lxml')
items = soup.select('td.t > a[onclick="clickLog(\'from=zzpc_infoclick\');"]')
storage = {}
for item in items:
    storage[item.get_text()]= item.get('href')
#print(storage)
#url_item = 'http://zhuanzhuan.58.com/detail/903230789619417097z.shtml?fullCate=5%2C38484%2C23094&fullLocal=1&from=pc'

def item_detail(url_item, data=None):
    item_data = requests.get(url_item)
    soup1 = BeautifulSoup(item_data.text, 'lxml')
    title = soup1.select('div.box_left_top > h1')
    place = soup1.select('div.palce_li > span > i')
    price = soup1.select('div.price_li > span > i')
    look_time = soup1.select('div.box_left_top > p > span.look_time')
    data = {
        'title': title[0].get_text(),
        'place': place[0].get_text(),
        'price': price[0].get_text(),
        'look_time':look_time[0].get_text()
    }
    print(data)

for each in storage.keys():
    item_detail(storage[each])
    time.sleep(3)

