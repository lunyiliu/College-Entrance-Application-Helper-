# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 00:03:45 2018

@author: lenovvo
"""
import numpy as np
import random
import pymysql
def risk_rank(userrank, line_rank):
    N = 0       # 超过分数线排名年数
    # last1为最近一年，last2为last1前一年
    for i in range(len(line_rank)):
        if userrank <= line_rank[i]:
            N = N + 1
    if N <= 2 :
        r = 500
    else:
        if N == len(line_rank):
            r = 0
        else:
            r = 100
    last1 = userrank - line_rank[0]
    last2 = userrank - line_rank[1]
    avg = userrank - sum(line_rank) / len(line_rank)
    if (line_rank[0] >= line_rank[1]) and (line_rank[1] >= sum(line_rank) / len(line_rank)):	    # 若有下降趋势
        Risk = 0.3 * (0.2 * last1 + 0.2 * last2 + 0.4 / 3 * avg) + r    # 近两年各占0.3权值，其余年份共占0.4
    else:
        if (np.std(line_rank) / (sum(line_rank) / len(line_rank))) <= 0.2:	    # 以差异系数来确定稳定程度
            Risk = 0.3 * avg + r
        else:
            Risk = 0.3 * max(avg, last1, last2) + r
    return Risk


def risk_level(userrank, line_rank):
    r = risk_rank(userrank, line_rank)
    if r >= 800:
        return 2
    else:
        if r <= -300:
            return 0
        else:
            if 400 <= r < 800:
                if random.random() >= 0.4:
                    return 2
                else:
                    return 1

            if -300 < r <= 0:
                if random.random() >= 0.4:
                    return 0
            else:
                return 1
            if 0<r<400:
                return 1


def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)   # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
    val = f'{head:x}{body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str
#number 是想要生成的志愿个数,level表示平行志愿第几档，scoreseed是已经随机生成的分数种子
#函数返回随机生成的分数集，也就是说平行志愿每一档都得用同一分数集
number=1
conn = pymysql.connect(host='39.107.97.123', user='root', passwd='123456', db='gaokao', charset='utf8')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
#1.生成一个17年录取平均分的列表
#生成学校ID-录取平均分数字典
cursor.execute("select avg_score ,schoolID from school where provinceID=9 and year=2017 and subject='science'")
conn.commit()
SchoolIdAndScore_=cursor.fetchall()
SchoolIdAndScore=[]
for Namedic in SchoolIdAndScore_:
    SchoolIdAndScore.append([Namedic["schoolID"],Namedic["avg_score"]])
SchoolIdAndScore=dict(SchoolIdAndScore)
SqlSchoolScore="select avg_score from school where provinceID=9 and year=2017 and subject='science' order by avg_score"
cursor.execute(SqlSchoolScore)
conn.commit()
SchoolScore_=cursor.fetchall()
SchoolScore=[]
for i in range(len (SchoolScore_)):
    SchoolScore.append(int(SchoolScore_[i]["avg_score"]))#SchoolScore改成了int型
#2.随机生成number个新的排名（但是不能超过今年一分一档表规定的排名档位的额数，比如说今年660排1200名，661排1100名，那么1200名挡的人数不能超过100
    #使用2017年的安徽省理科一分一档表作为参考
        #（1）随机生成number个分数（注意排名段人数）
cursor.execute("select score from AnHui_yifenyidang order by score")
conn.commit()
ScoreList_=cursor.fetchall()
ScoreList=[]
for i in range(len (ScoreList_)):
    ScoreList.append(int(ScoreList_[i]["score"]))
cursor.execute("select rank from AnHui_yifenyidang order by score")
conn.commit()
RankList_=cursor.fetchall()
RankList=[]
for i in range(len (RankList_)):
    RankList.append(int(RankList_[i]["rank"]))
#生成学校名称字典
cursor.execute("select 学校名称 ,ID from gaokaowang_schoolname")
conn.commit()
SchoolName_=cursor.fetchall()
SchoolName=[]
for Namedic in SchoolName_:
    SchoolName.append([Namedic["ID"],Namedic["学校名称"]])
SchoolName=dict(SchoolName)
UserScore=[]
UserName=[]
#在生成随机分数的时候没有考虑到当年的已收集到的数据里最低的分数，
#导致生成的分数里低于这个最低分数的最后都选报了同一所大学，乌鲁木齐职业大学
#所以要改一改scorelist
#后面的大学收集到的数据过少，就导致后面的学校出现的频率过高，故先把
RankList=RankList[ScoreList.index(SchoolScore[0]):ScoreList.index(SchoolScore[-1])+1]
ScoreList=ScoreList[ScoreList.index(SchoolScore[0]):ScoreList.index(SchoolScore[-1])+1]
for num in range(number):
    UserScore.append(ScoreList[random.randint(0,len(ScoreList)-1)])
    ScoreIndex=ScoreList.index(UserScore[-1])
    AlreadyIn=cursor.execute("select user_ID from 9__user_sim_zhiyuan where user_rank="+str(RankList[ScoreIndex]))
    if ScoreIndex!=len(ScoreList)-1:
        RankVolume=int(RankList[ScoreIndex])-int(RankList[ScoreIndex+1])-AlreadyIn
    else:
        RankVolume=1-AlreadyIn
    UserName.append(GBK2312()+GBK2312()+GBK2312())
    if np.sum(np.asarray(UserScore)==np.asarray(UserScore[-1]))>RankVolume:
        UserScore.pop()
        UserName.pop()
flag=0
UserScore=[676]
UserName=["张明昕"]
for score in UserScore:
    user_grade=score
    user_rank=RankList[ScoreList.index(score)]
    school_list = []
    temp = []
    provinceID = 9
    kelei = 'science'
    # 筛选出该省份该科类所有学校
    db_school_list = "select schoolID, year, pici, lowest_score, avg_score, highest_score " \
                  "from school" + " where provinceID=" + str(provinceID) + " and subject='" + str(kelei) + "'"
    cursor.execute(db_school_list)
    conn.commit()
    temp.append(cursor.fetchall())
    
    avg_score_avg = [0 for i in range(1601)]
    lowest_score_avg = [0 for i in range(1601)]
    highest_score_avg = [0 for i in range(1601)]
    n = 1       # 计数，学校
    j = 0       # 计数，最低分数据个数
    k = 0       # 计数，最高分数据个数
    m = 0       # 计数，平均分数据个数
    for i in range(len(temp[0])):
        # 因许多省份改革，只取2014以后数据
        if temp[0][i]['year'] == 2017 or temp[0][i]['year'] == 2016 or temp[0][i]['year'] == 2015 or \
                temp[0][i]['year'] == 2014:
            # 若是同一所学校
            if temp[0][i]['schoolID'] == n:
                if temp[0][i]['lowest_score']:      # 若存在最低分数据
                    lowest_score_avg[n] += int(temp[0][i]['lowest_score'])      # 该学校最低分的平均分中加入此数据
                    j += 1      # 最低分数量加一
                if temp[0][i]['highest_score']:     # 同上
                    highest_score_avg[n] += int(temp[0][i]['highest_score'])
                    k += 1
                if temp[0][i]['avg_score']:     # 同上
                    avg_score_avg[n] += int(temp[0][i]['avg_score'])
                    m += 1
            else:
                # 如果存在相应数据则除以对应数据数目求平均
                if j:
                    lowest_score_avg[n] /= j
                if k:
                    highest_score_avg[n] /= k
                if m:
                    avg_score_avg[n] /= m
                # 计数复位，开始下一所学校计数
                j = 0
                k = 0
                m = 0
                # 下一所学校
                n = temp[0][i]['schoolID']
    for i in range(len(lowest_score_avg)):
        if lowest_score_avg[i] and highest_score_avg[i]:
            if min(avg_score_avg[i], lowest_score_avg[i]) - 15 <= user_grade <= max(avg_score_avg[i], highest_score_avg[i]) + 20:
                school_list.append(i)
        else:
            if avg_score_avg[i] - 15 <= user_grade <= avg_score_avg[i] + 20:
                school_list.append(i)
    
    if len(school_list) <= 25:
        delta = 3
        while 1:
            if len(school_list) >= 25:
                break
            for i in range(len(lowest_score_avg)):
                if lowest_score_avg[i] and highest_score_avg[i]:
                    if min(avg_score_avg[i], lowest_score_avg[i]) - 15 - delta <= user_grade\
                            <= max(avg_score_avg[i], highest_score_avg[i]) + 20 + delta and i not in school_list:
                        school_list.append(i)
                else:
                    if avg_score_avg[i] - 15 - delta <= user_grade <= avg_score_avg[i] + 20 + delta and i not in school_list:
                        school_list.append(i)
            delta += 3    
       
    
    
    select_school_list = []
    high_risk_school = []
    normal_risk_school = []
    low_risk_school = []
    temp_list = []
    low_school_rank_list = []
    normal_school_rank_list = []
    high_school_rank_list = []
    for i in school_list:
        db_list = "select year, pici, lowest_score, avg_score, highest_score, avg_rank " \
                         "from school" + " where schoolID=" + str(i) + " and provinceID=" + str(provinceID)\
                  + " and subject='" + str(kelei) + "'"
        cursor.execute(db_list)
        conn.commit()
        temp_list.append(cursor.fetchall())
    
    line_rank = [[] for i in range(len(school_list))]
    SumLineRank=[]
    for i in range(len(school_list)):
        for j in range(len(temp_list[i])):
            if temp_list[i][j]['avg_rank']:
                line_rank[i].append(temp_list[i][j]['avg_rank'])
        SumLineRank.append(sum(line_rank[i])/len(line_rank[i]))
    for i in range(len(school_list)):
        if len(line_rank[i]) >= 3:
            if risk_level(user_rank, line_rank[i]) == 0:
                low_risk_school.append(school_list[i])
            if risk_level(user_rank, line_rank[i]) == 1:
                normal_risk_school.append(school_list[i])
            if risk_level(user_rank, line_rank[i]) == 2:
                high_risk_school.append(school_list[i])
    # 此处应排序，按学校排名学科排名和风险值综合考量对三个数组进行排序，只保留前几个结果
    for i in range(len(low_risk_school)):
        low_school_rank = "select school_rank from gaokaowang_schoolname where ID ='" + \
                          str(low_risk_school[i]) + "'"
        cursor.execute(low_school_rank)
        conn.commit()
        low_school_rank_list.append(cursor.fetchall())
    for i in range(len(normal_risk_school)):
        normal_school_rank = "select school_rank from gaokaowang_schoolname where ID ='" + \
                             str(normal_risk_school[i]) + "'"
        cursor.execute(normal_school_rank)
        conn.commit()
        normal_school_rank_list.append(cursor.fetchall())
    for i in range(len(high_risk_school)):
        high_school_rank = "select school_rank from gaokaowang_schoolname where ID='" + \
                           str(high_risk_school[i]) + "'"
        cursor.execute(high_school_rank)
        conn.commit()
        high_school_rank_list.append(cursor.fetchall())
    
    if len(high_risk_school) == 3:
        for i in range(len(high_risk_school)):
            if high_school_rank_list[i][0]['school_rank'] != 10000:
                select_school_list.append(high_risk_school[i])
                high_school_rank_list[i][0]['school_rank'] = 10000
    elif len(high_risk_school) < 3:
        N = 0
        for i in range(len(high_risk_school)):
            if high_school_rank_list[i][0]['school_rank'] != 10000:
                select_school_list.append(high_risk_school[i])
                high_school_rank_list[i][0]['school_rank'] = 10000
                N += 1
        if len(normal_risk_school) > 0:
            for i in range(3 - N):
                best = 0
                for j in range(len(normal_risk_school)):
                    t = school_list.index(normal_risk_school[j])
                    r = risk_rank(user_rank, line_rank[t])
                    best_rank = risk_rank(user_rank, line_rank[school_list.index(normal_risk_school[best])])
                    if int(normal_school_rank_list[j][0]['school_rank']) > 0 and 0.2 * r + 10 * int(normal_school_rank_list[j][0]['school_rank']) < \
                            0.2 * best_rank + 10 * int(normal_school_rank_list[best][0]['school_rank']):
                        best = j
                if int(normal_school_rank_list[best][0]['school_rank']) != 10000 and int(normal_school_rank_list[best][0]['school_rank']) != 0:
                    select_school_list.append(normal_risk_school[best])
                    normal_school_rank_list[best][0]['school_rank'] = 10000
                    N += 1
        if N < 3:
            for i in range(3 - N):
                best = 0
                for j in range(len(low_risk_school)):
                    t = school_list.index(low_risk_school[j])
                    r = risk_rank(user_rank, line_rank[t])
                    if 0 < int(low_school_rank_list[j][0]['school_rank']) < int(low_school_rank_list[best][0]['school_rank']):
                        best = j
                if int(low_school_rank_list[best][0]['school_rank']) != 10000 and int(low_school_rank_list[best][0]['school_rank']) != 0:
                    select_school_list.append(low_risk_school[best])
                    low_school_rank_list[best][0]['school_rank'] = 10000
    
    else:
        for i in range(3):
            best = 0
            for j in range(len(high_risk_school)):
                t = school_list.index(high_risk_school[j])
                r = risk_rank(user_rank, line_rank[t])
                best_rank = risk_rank(user_rank, line_rank[school_list.index(high_risk_school[best])])
                if int(high_school_rank_list[j][0]['school_rank']) > 0 and 0.2 * r + 10 * int(high_school_rank_list[j][0]['school_rank']) \
                        < 0.2 * best_rank + 10 * int(high_school_rank_list[best][0]['school_rank']):
                    best = j
            if int(high_school_rank_list[best][0]['school_rank']) != 10000 and int(high_school_rank_list[best][0]['school_rank']) != 0:
                select_school_list.append(high_risk_school[best])
                high_school_rank_list[best][0]['school_rank'] = 10000
    
    if len(normal_risk_school) == 4:
        for i in range(len(normal_risk_school)):
            if normal_school_rank_list[i][0]['school_rank'] != 10000:
                select_school_list.append(normal_risk_school[i])
                normal_school_rank_list[i][0]['school_rank'] = 10000
    elif len(normal_risk_school) < 4:
        N = 0
        for i in range(len(normal_risk_school)):
            if normal_school_rank_list[i][0]['school_rank'] != 10000:
                select_school_list.append(normal_risk_school[i])
                normal_school_rank_list[i][0]['school_rank'] = 10000
                N += 1
        if len(high_risk_school) > 0:
            for i in range(4 - N):
                best = 0
                for j in range(len(high_risk_school)):
                    t = school_list.index(high_risk_school[j])
                    r = risk_rank(user_rank, line_rank[t])
                    best_rank = risk_rank(user_rank, line_rank[school_list.index(high_risk_school[best])])
                    if int(high_school_rank_list[j][0]['school_rank']) > 0 and r < best_rank:
                        best = j
                if int(high_school_rank_list[best][0]['school_rank']) != 10000 and int(high_school_rank_list[best][0]['school_rank']) != 0:
                    select_school_list.append(high_risk_school[best])
                    high_school_rank_list[best][0]['school_rank'] = 10000
                    N+=1
        if N < 4:
            for i in range(4 - N):
                best = 0
                for j in range(len(low_risk_school)):
                    t = school_list.index(low_risk_school[j])
                    r = risk_rank(user_rank, line_rank[t])
                    if 0 < int(low_school_rank_list[j][0]['school_rank']) < int(low_school_rank_list[best][0]['school_rank']):
                        best = j
                if int(low_school_rank_list[best][0]['school_rank']) != 10000 and int(low_school_rank_list[best][0]['school_rank']) != 0:
                    select_school_list.append(low_risk_school[best])
                    low_school_rank_list[best][0]['school_rank'] = 10000
    else:
        for i in range(4):
            best = 0
            for j in range(len(normal_risk_school)):
                t = school_list.index(normal_risk_school[j])
                r = risk_rank(user_rank, line_rank[t])
                best_rank = risk_rank(user_rank, line_rank[school_list.index(normal_risk_school[best])])
                if int(normal_school_rank_list[j][0]['school_rank']) > 0 and 0.2 * r + 10 * int(normal_school_rank_list[j][0]['school_rank']) < \
                        0.2 * best_rank + 10 * int(normal_school_rank_list[best][0]['school_rank']):
                    best = j
            if int(normal_school_rank_list[best][0]['school_rank']) != 10000 and int(normal_school_rank_list[best][0]['school_rank']) != 0:
                select_school_list.append(normal_risk_school[best])
                normal_school_rank_list[best][0]['school_rank'] = 10000
    
    if len(low_risk_school) == 3:
        for i in range(len(low_risk_school)):
            if low_school_rank_list[i][0]['school_rank'] != 10000:
                select_school_list.append(low_risk_school[i])
                low_school_rank_list[i][0]['school_rank'] = 10000
    elif len(low_risk_school) < 3:
        N = 0
        for i in range(len(low_risk_school)):
            if low_school_rank_list[i][0]['school_rank'] != 10000:
                select_school_list.append(low_risk_school[i])
                low_school_rank_list[i][0]['school_rank'] = 10000
                N += 1
        if len(normal_risk_school) > 0:
            for i in range(3 - N):
                best = 0
                for j in range(len(normal_risk_school)):
                    t = school_list.index(normal_risk_school[j])
                    r = risk_rank(user_rank, line_rank[t])
                    best_rank = risk_rank(user_rank, line_rank[school_list.index(normal_risk_school[best])])
                    if int(normal_school_rank_list[j][0]['school_rank']) > 0 and 0.2 * r + 10 * int(normal_school_rank_list[j][0]['school_rank']) < \
                            0.2 * best_rank + 10 * int(normal_school_rank_list[best][0]['school_rank']):
                        best = j
                if int(normal_school_rank_list[best][0]['school_rank']) != 10000 and int(normal_school_rank_list[best][0]['school_rank']) != 0:
                    select_school_list.append(normal_risk_school[best])
                    normal_school_rank_list[best][0]['school_rank'] = 10000
                    N+=1
        if N < 3:
            for i in range(3 - N):
                best = 0
                for j in range(len(high_risk_school)):
                    t = school_list.index(high_risk_school[j])
                    r = risk_rank(user_rank, line_rank[t])
                    best_rank = risk_rank(user_rank, line_rank[school_list.index(high_risk_school[best])])
                    if int(high_school_rank_list[j][0]['school_rank']) > 0 and r < best_rank:
                        best = j
                if int(high_school_rank_list[best][0]['school_rank']) != 10000 and int(high_school_rank_list[best][0]['school_rank']) != 0:
                    select_school_list.append(high_risk_school[best])
                    high_school_rank_list[best][0]['school_rank'] = 10000
    else:
        for i in range(3):
            best = 0
            for j in range(len(low_risk_school)):
                t = school_list.index(low_risk_school[j])
                r = risk_rank(user_rank, line_rank[t])
                best_rank = risk_rank(user_rank, line_rank[school_list.index(low_risk_school[best])])
                if 0 < int(low_school_rank_list[j][0]['school_rank']) < int(low_school_rank_list[best][0]['school_rank']):
                    best = j
            if int(low_school_rank_list[best][0]['school_rank']) != 10000 and int(low_school_rank_list[best][0]['school_rank']) != 0:
                select_school_list.append(low_risk_school[best])
                low_school_rank_list[best][0]['school_rank'] = 10000

    #去重
    select_school_list=list(set(select_school_list))
    #排序
    select_school_score=[]
    for ID in select_school_list:
        select_school_score.append(SumLineRank[school_list.index(ID)])
    select_school_sorted=sorted(zip(select_school_score,select_school_list))
    for i in range(len(select_school_sorted)):
        select_school_list[i]=select_school_sorted[i][1]
    if len(select_school_list)>=6:
        sql_insert="insert into 9__user_sim_zhiyuan values("+str(user_rank)+",'"+UserName[flag]+"',"+str(select_school_list[0])+",'"+SchoolName[select_school_list[0]]+"','science',"+str(select_school_list[1])+",'"+SchoolName[select_school_list[1]]+"',"+str(select_school_list[2])+",'"+SchoolName[select_school_list[2]]+"',"+str(select_school_list[3])+",'"+SchoolName[select_school_list[3]]+"',"+str(select_school_list[4])+",'"+SchoolName[select_school_list[4]]+"',"+str(select_school_list[5])+",'"+SchoolName[select_school_list[5]]+"')"
        cursor.execute(sql_insert)
        conn.commit()
    else:
        sql_insert="insert into 9__user_sim_zhiyuan values("+str(user_rank)+",'"+UserName[flag]+"',"+str(select_school_list[0])+",'"+SchoolName[select_school_list[0]]+"','science'"
        for m in range(1,len(select_school_list)):
            sql_insert=sql_insert+","+str(select_school_list[m])+",'"+SchoolName[select_school_list[m]]+"'"
        for n in range(6-len(select_school_list)):
            sql_insert=sql_insert+",null,null"
        sql_insert=sql_insert+")"
    flag=flag+1
conn.close()




