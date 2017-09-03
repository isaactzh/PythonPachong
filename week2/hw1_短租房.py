from bs4 import BeautifulSoup
import requests
import pymongo
import time


client = pymongo.MongoClient('localhost',27017)
duanzufang = client['duanzufang']
fangzi1 = duanzufang['fangzi1']

urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(i) for i in range(1,4,1)]
url = 'http://bj.xiaozhu.com/search-duanzufang-p0-0/'


def search(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, "lxml")
    titles = soup.select('div.result_intro > a')
    prices = soup.select('span.result_price > i')
    for title, price in zip(titles, prices):
        data = {
            'title': title.get_text(),
            'price': int(price.get_text()),
        }
        fangzi1.insert_one(data)

for url in urls:
    print(url)
    search(url)
    time.sleep(2)

def find_fangzi():
    # 从xiaozhu数据库的fangzi表，查询所有数据，用find()函数
    for info in fangzi1.find():
        # info 我们插入的数据都有title和price，我们取出每条信息的price，用来比较
        if info['price'] >= 500:
            print(info)

find_fangzi()


