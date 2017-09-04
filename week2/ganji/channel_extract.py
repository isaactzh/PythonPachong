from bs4 import BeautifulSoup
import requests

url = 'http://bj.ganji.com/wu/'
url_host = 'http://bj.ganji.com'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# print(soup)

links = soup.select('dl.fenlei > dt > a')
for link in links:
    print(url_host + str(link.get('href')))

channel_list = ['http://bj.ganji.com/jiaju/',
                'http://bj.ganji.com/rirongbaihuo/',
                'http://bj.ganji.com/shouji/',
                'http://bj.ganji.com/bangong/',
                'http://bj.ganji.com/nongyongpin/',
                'http://bj.ganji.com/jiadian/',
                'http://bj.ganji.com/ershoubijibendiannao/',
                'http://bj.ganji.com/ruanjiantushu/',
                'http://bj.ganji.com/yingyouyunfu/',
                'http://bj.ganji.com/diannao/',
                'http://bj.ganji.com/xianzhilipin/',
                'http://bj.ganji.com/fushixiaobaxuemao/',
                'http://bj.ganji.com/meironghuazhuang/',
                'http://bj.ganji.com/shuma/',
                'http://bj.ganji.com/laonianyongpin/',
                'http://bj.ganji.com/xuniwupin/',
                'http://bj.ganji.com/qitawupin/',
                'http://bj.ganji.com/ershoufree/',
                'http://bj.ganji.com/wupinjiaohuan/']