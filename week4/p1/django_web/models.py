from django.db import models

# Create your models here.
from mongoengine import *
from mongoengine import connect
connect('wbsite', host = '127.0.0.1', port = 27017)

#ORM：对象的映射
#django 会使用 mongo engine使用ORM以对象的方式进行操作

class ArtiInfo(Document): #Document继承的类的名称，定义了数据结构
    des = StringField() #字符串结构
    title = StringField()
    scores = StringField()
    tags = ListField(StringField())

    meta = {'collection':'arti_info3'} #仅限于数据库已经存在的状况

for i in ArtiInfo.objects[:1]:
    print(i.title, i.des, i.scores, i.tags)