from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list']
item_info = ceshi['item_info']
url = 'http://zhuanzhuan.58.com/detail/748888669919002628z.shtml'
#spider 1

def get_links_from(channel,pages,who_sells=0):
    #http: // bj.58.com / diannao / pn2 /
    list_view = '{}/{}/pn{}/'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    #用td标签去判断网页内容：
    if soup.find('td','t'):
        for link in soup.select('td.t a.t'):
            if link.get('href').split('//')[1].startswith('jump'):
                pass
            else:
                item_link = link.get('href').split('?')[0]
                print(item_link)
                url_list.insert_one({'url': item_link})
    else:
        pass

def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    no_longer_exist = soup.find('span', 'soldout_btn')
    if no_longer_exist:
        pass
    else:
        title = soup.select('h1.info_titile')[0].text
        price = soup.select('span.price_now')[0].text
        area = soup.select('div.palce_li')[0].text.split('：')[1]
        item_info.insert_one({'title': title, 'price': price,  'area': area, 'url': url})
        print({'title': title, 'price': price,  'area': area, 'url': url})
get_item_info(url)

#判断404页面：
#no_longer_exist = soup.find('span','soldout_btn')
# url = 'http://zhuanzhuan.58.com/detail/9039792658811480z.shtml'
# wb_data = requests.get(url)
# soup = BeautifulSoup(wb_data.text, 'lxml')
#print(soup.prettify())
#no_longer_exist = soup.find('span','soldout_btn')


#get_links_from('http://bj.58.com/shuma/',2)