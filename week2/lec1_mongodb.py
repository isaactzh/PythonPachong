#mongodb
#创建数据库，进行数据分类和查找
import pymongo

#激活客户端:(本地)
client = pymongo.MongoClient('localhost',27017)
#给数据库命名：
walden = client['walden']
#创建表单：
sheet_tab = walden['sheet_tab']

# path = '/home/isaac/Desktop/Plan-for-combating-master/week2/2_1/2_1code_of_video/walden.txt'
# with open(path, 'r') as f:
#     lines = f.readlines()
#     for index, line in enumerate(lines):
#         data = {
#             'index':index,
#             'line' :line,
#             'words':len(line.split())
#         }
#         sheet_tab.insert_one(data) #往数据库写入数据：

#展示数据库中数据&数据库的操作：
# for item in sheet_tab.find({'words':0}):
#     print(item)


# for item in sheet_tab.find():
#     print(item['line'])


# $lt/$lte/$gt/$gte/$ne，依次等价于</<=/>/>=/!=。（l表示less g表示greater e表示equal n表示not  ）
for item in sheet_tab.find({'words':{'$lt':5}}):
    print(item)
    