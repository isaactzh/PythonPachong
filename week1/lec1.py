
#
Soup = BeautifulSoup(html, 'lxml')
#css selector: body > div.main-content > ul > li:nth-child(1) > img
#Xpath : /html/body/div[2]/ul/li[1]/img

#查看路径然后进行选择

Soup = BeautifulSoup(Web_data, 'lxml')
info = [] #新建列表
#删除nth-child可以选择所有的图片
images = Soup.select(' body > div.main-content > ul > li:nth-child(1) > img')
titles = Soup.select('body > div.main-content > ul > li:nth-child(1) > div.')
descs = Soup.select('body > div.main-content > ul > li > div.rate > span')
rates = Soup.select('body > div.main-content > ul > li > div.rate.span')
cates = Soup.select('body > div.main-content > ul > li:nth-child(1) > div.artical-info > p.meta-info > span:nth-child(2)')

for title, image, desc, rate, cate in zip(titles, images, descs, rates, cates):
	data = {
		'title':title.get_text(),#获取文本
		'rate':rate.get_text(),
		'desc':desc.get_text(),
		'cate':list(cate.stripped_strings),#多对一的属性，用列表储存
		'image':image.get('src')#获取属性
	}

#选出所有大于三分的文章：
for i in info:
	if float(i['rate']) > 3:
		print(i['title'], i['cate'])