# -*- coding: utf-8 -*-
import pymysql
from DB_methods import DB_methods
from DB_handler import DB_handler
from getRank import getRank
from resetRecords import resetRecords
import random
import time

conn = pymysql.connect(host='39.97.100.184', user='root', passwd='8612260', db='gaokao', charset='utf8')
cursor = conn.cursor()

DBm = DB_methods()
DBh = DB_handler()

'''
#result = DBm.GetDict(['test' ],["avg_score",'schoolID'],["provinceID=28","year=2016","subject='science'"],para_repeated = False)
result = DBm.insertRank('test' ,['schoolID = 8','provinceID = 28','year = 2016','subject = "science"'],score = '610')
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
'''
str1 = ''
for i in range(50000):
    k = random.randint(300,700)
    str1 = str1+str(k)+'.'

DBh.update('intension_school_table', ['block =' +'\"'+ str1+'\"'], ['schoolID = 1'])

print(len(DBh.select(['intension_school_table'], ['block '], ['schoolID = 1'])[0]))
'''
'''
id = 0
for i in range(6):
    school = i+1
    for j in range(6):
        zhuanye = j+1
        for k in range(6):
            id = id+1

            serial = k+1
            Conditionlist = [
                             school,
                             1,
                             'science',
                             2,
                             2016,
                             zhuanye,
                            serial,
                             None,
                             None,
                             None,
                             None,
                             None]
            DBh.insert('intension_zhuanye_table',Conditionlist)
'''
#DBh.insert('intension_zhuanye_table',[['schoolID','provinceID','subject','pici','year','zhuanye','serialnumber','block1','block2','block3','block4','block5'],[[1],[1],['science'],[2],[2016],[1],[1],[None],[None],[None],[None],[None]]])
#DBh.insert('intension_zhuanye_table',[[1],[1],['science'],[2],[2016],[1],[1],[None],[None],[None],[None],[None]])
#DBh.insert('intension_zhuanye_table',[1,1,'science',2,2016,1,1,'1','2','3','4','5'])

#cursor.execute("INSERT INTO intension_zhuanye_table(schoolID,provinceID,subject,pici,year,zhuanye,serialnumber,block1,block2,block3,block4,block5) VALUES(1,1,'science',2,2016,1,1,'','','','','')")
#conn.commit()

#测试getRank函数，计时。
start = time.clock()
user = resetRecords('1')
result = user.update()
print(result)
#print(len(result))
#print(len(result[0]))
#print(len(result[0][0]))
end = time.clock()
print(end-start)


#DBh.insert('client',[4,'test3',550,1,'science',2012,1,None,None])
'''
request = []
val = []
Conditionlist = ['schoolID =1',
                 'provinceID =1',
                 'subject ="science"',
                 'pici =1',
                 'serialnumber =1']
for condition in Conditionlist:
    request.append(condition.split('=')[0])
    val.append(condition.split('=')[1])
print(request)
print(val)
'''
#result = DBh.select(['client'],['score'],['user_ID=2','user_nickname =test2','provinceID=1','subject=science','year = 2012','pici = 1'],para_debug=True)
#print(result)
#DBh.update('client',['score=200'],['user_ID=2','user_nickname = test2','provinceID=1','subject=science','year = 201'])
