from multiprocessing import Pool
from channel_extract import channel_list
from page_link import get_links
from page_link import get_item_info

# 断点续传，先把所有的url抓完，再收集信息的时候可以使用此方法
# db_urls = [item['url'] for item in url_ganji.find()]
# index_url = [item['url'] for item in item_ganji.find()]
# x = set(db_urls)
# y = set(index_url)
# rest_of_urls = x - y


def get_all(channel):
    for i in range (1,100):
        get_links(channel,i)

if __name__ == '__main__':
    pool = Pool()
    #pool = Pool(process=6)
    pool.map(get_all, channel_list)
    pool.close()
    pool.join()


