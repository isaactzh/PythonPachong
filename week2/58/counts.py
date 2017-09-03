#用于计数的监控程序：
import time
from page_parsing import url_list

while True:
    print(url_list.find().count()) #count用于逐个显示
    