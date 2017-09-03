#实现多进程的库：
from multiprocessing import Pool
from channel_extract import channel_list
from page_parsing import get_links_from
#基于get_links_from，用函数填入页码

def get_all_links_from(channel):
    for num in range(1,101):
        get_links_from(channel,num)
        

#创建进程池：
#这样既可以让“模块”文件运行，也可以被其他模块引入，而且不会执行函数2次。这才是关键。
if __name__ == '__main__':
    pool = Pool()
    pool.map(get_all_links_from,channel_list.split())


# def double(x):
#     return x*2
#
# print(list(map(double, [1,2,3,4])))
#
# #[2, 4, 6, 8]

