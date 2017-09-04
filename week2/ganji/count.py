import time
from page_link import url_ganji, item_ganji

while True:
    print('url list count is ', url_ganji.find().count())
    print('item count is ', item_ganji.find().count())
    time.sleep(5)

