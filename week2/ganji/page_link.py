from bs4 import BeautifulSoup
import requests
import pymongo
import time
import random
import lxml #比BS 快10倍，还有异步非阻塞式的方式

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_ganji = ganji['url_ganji']
item_ganji = ganji['item_ganji']
url = 'http://bj.ganji.com/jiaju/'


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Connection': 'keep-alive'
}

#从cn-proxy.com上找IP地址，防止网站查封IP
#http://ip.zdaye.com/
proxy_list = [
    'http://58.211.142.2:8080',
    'http://124.206.133.219:3128',
    'http://202.202.90.20:8080',
]
proxy_ip = random.choice(proxy_list) #随即获取代理IP
proxies = {'http': proxy_ip}

def get_links(channel,page):
    page_view = '{}o{}'.format(channel, str(page))
    print(page_view)
    # response = requests.get(page_view, headers = headers, proxies=proxies)
    response = requests.get(page_view, headers = headers)
    #通过404判断网页是否存在
    if response.status_code == 404:
        pass
    else:
        soup = BeautifulSoup(response.text, 'lxml')
        if soup.find('div', 'noinfotishi'):
            pass
        else:
            #print(soup.select('tr.zzinfo > td.t > a.t'))
            for link in soup.select('tr.zzinfo > td.t > a.t'):
                if link.get('href').split('//')[1].startswith('bj'):
                    pass
                else:
                    item_link = link.get('href')
                    url_ganji.insert_one({'url': item_link})
                    get_item_info(item_link)
                    print(item_link)



def get_item_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    no_item_exist = soup.find('span', 'soldout_btn')
    if no_item_exist:
        pass
    else:
        try:

            # title = soup.select('h1.info_titile')[0].text
            # area = soup.select('div.palce_li > span > i')[0].text
            # price = soup.select('div.price_li > span.price_now > i')[0].text
            # look_time = soup.select('span.look_time')[0].text
            data = {
                'title': soup.select('h1.info_titile')[0].text,
                'cate': soup.select('span.crb_i')[-1].text.strip(),
                'area' : soup.select('div.palce_li > span > i')[0].text,
                'price': soup.select('div.price_li > span.price_now > i')[0].text,
                'look_time': soup.select('span.look_time')[0].text,
                'url': url
            }
            item_ganji.insert_one(data)
            print(data)
        except AttributeError:
            pass
        except IndexError:
            pass

if __name__ == '__main__':
    #get_item_info(url = 'http://zhuanzhuan.ganji.com/detail/904186675474448909z.shtml')
    get_links('http://bj.ganji.com/jiaju/', 8)

#lambda 函数 和 map：
#'area': list(map(lambda x:x.text,soup.select('ul.det-infor > li:nth-of-type(3) > a'))),
#map 函数将list内的每个值用于逗号前的函数，然后再将获得的值用list列表化