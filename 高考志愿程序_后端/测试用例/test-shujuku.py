import pymysql
from DB_methods import DB_methods
from DB_handler import DB_handler

conn = pymysql.connect(host='39.96.168.183', user='root', passwd='123456', db='gaokao', charset='utf8')
cursor = conn.cursor()

DBm = DB_methods()
DBh = DB_handler()
'''
#result = DBm.GetDict(['test' ],["avg_score",'schoolID'],["provinceID=28","year=2016","subject='science'"],para_repeated = False)
result = DBm.getRank('test' ,['schoolID = 8','provinceID = 28','year = 2016','subject = "science"'],score = '610')
#result = DBm.GetDict(['majors' ],["录取平均分",'学校名称'],["学校名称='东京大学'","年份=2012","科类='理科'"],para_repeated = False)
#result = DBh.select(['test'],['self_rank'],['year=2016','provinceID=28','schoolID=8'])
#DBh.update('test',['self_rank = 400'],[])
#DBh.update('test',['self_rank = "616.610.600."'],['schoolID = 8','provinceID = 28','year = 2016','subject = "science"'])
print(result)
'''
'''
referencelist1 = ['8','13','15']
referencelist2 = ['8','13','15','17']
referencelist3 = ['11','13','17']
referencelist4 = ['8','11','13','15','17']


results1 = DBm.setRecords('1',referencelist1)
results2 = DBm.setRecords('2',referencelist2)
results3 = DBm.setRecords('3',referencelist3)
results4 = DBm.setRecords('4',referencelist4)


#result1 = DBh.select(['client'], ['score'], ['user_ID=' + user_ID])
print(results1)

#result = DBh.select(['client'],['year'],['user_ID = 1'])[0]
#print(isinstance(result,str ))
'''

DBm.deleteRecords('1')
