# -*- coding: utf-8 -*-

import requests
from lxml import etree
import time
import re
import pymysql

schoolName = []
schoolIDset = []
provinceset = []
for i in range(30, 1651):
    schoolIDset.append(str(i))
for j in range(10000, 10032):
    provinceset.append(str(j))
keleiset = ['10034','10035','10166']    #文科、理科、文理不分
piciset = ['10162','10163','10164','10165','10154','10036','10037','10038','10155','10149']       

bset_school = []
for schoolID in schoolIDset:
    print("第" + str(int(schoolID)-int(schoolIDset[0])+1) + "个学校")
    bset_province = []
    for province in provinceset:
        print("第" + str(int(province)-int(provinceset[0])+1) + "个省份")
        bset_kelei = []
        for kelei in keleiset:
            bset_pici = []
            for pici in piciset:
                url = "http://gkcx.eol.cn/schoolhtm/schoolAreaPoint/" + schoolID + "/" + province + "/" + kelei + "/" + pici + ".htm"
                while 1: 
                    try:
                        r=requests.get(url,timeout=3.05)
                        break
                    except Exception as e:
                        print("Exception: {}".format(e))
                        time.sleep(5)
                selector=etree.HTML(r.text)
                name = selector.xpath("p[@class='li-school-label']//span")
                for i in name:
                    if i.span:
                        schoolName.append(i.span.get_text())
                        print('getname')
                        flag = 1
                        break
                    else:
                        print('getname fail')
                
                
                b = [] 
                for i in info:
                    if i.span:
                        b.append(i.span.get_text())
                    else:
                        b.append(i.get_text())
                
                bset_pici.append(b)
            bset_kelei.append(bset_pici)
        bset_province.append(bset_kelei) 
    bset_school.append(bset_province)


for i in range(len(schoolIDset[10:80])):
    with open(schoolName[i] + ".csv", "w", newline='', encoding = 'utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["province", "kelei", "year", "max", "avg", "min","provinceline" ,"pici"])
        for j in range(len(bset_school[i])):
            for k in range(len(bset_school[i][j])):
                for l in range(len(bset_school[i][j][k])):
                    if (len(bset_school[i][j][k][l]) > 3):
                        for temp in range(6):
                            if temp*8 <len(bset_school[i][j][k][l]):
                                bset_school[i][j][k][l].insert(temp*8,j + int(provinceset[0]))
                                if int(kelei[k]) == 0:
                                    bset_school[i][j][k][l].insert(temp*8+1, "文科")
                                if int(kelei[k]) == 1:
                                    bset_school[i][j][k][l].insert(temp*8+1, "理科")
                                if int(kelei[k]) == 2:
                                    bset_school[i][j][k][l].insert(temp*8+1, "文理不分")
                        for temp in range(6):
                            if temp*8 <len(bset_school[i][j][k][l]):
                                writer.writerow(bset_school[i][j][k][l][temp*8:(temp+1)*8])

endtime = datetime.datetime.now()
print ("用时" + str(endtime - starttime))