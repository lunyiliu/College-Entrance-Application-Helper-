import pymysql
from DB_methods import DB_methods
from DB_handler import DB_handler

conn = pymysql.connect(host='39.96.168.183', user='root', passwd='123456', db='gaokao', charset='utf8')
cursor = conn.cursor()

DBm = DB_methods()
DBh = DB_handler()

#result = DBm.GetDict(['test' ],["avg_score",'schoolID'],["provinceID=28","year=2016","subject='science'"],para_repeated = False)
result = DBm.getRank('test' ,['schoolID = 8','provinceID = 28','year = 2016','subject = "science"'],score = '61'
                                                                                                            '0')
#result = DBm.GetDict(['majors' ],["录取平均分",'学校名称'],["学校名称='东京大学'","年份=2012","科类='理科'"],para_repeated = False)
#result = DBh.select(['test'],['self_rank'],['year=2016','provinceID=28','schoolID=8'])
#DBh.update('test',['self_rank = 400'],[])
#DBh.update('test',['self_rank = "616.610.600."'],['schoolID = 8','provinceID = 28','year = 2016','subject = "science"'])
print(result)
'''
str = '1.2.3.'
print(str[:-1].split('.'))
'''
"""
str = '111'
a = 'a='+'\"'+str+'\"'
print(a)
"""