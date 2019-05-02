from getRisk import getRisk
from DB_handler import DB_handler
from DB_methods import DB_methods
from get_dict_yifenyidang import get_dict_yifenyidang
import pymysql
import random
#导入学校id转化表
schoolID_dictionary={}
with open ('C:\\school2ID.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        line=line.strip('\n')
        schoolID_dictionary[line.split(',')[0]]=line.split(',')[1]
conn = pymysql.connect(host='39.97.100.184', user='root', passwd='8612260', db='gaokao', charset='utf8')
cursor = conn.cursor()

class recommand():
    def __init__(self,user_ID):
        self.DBh = DB_handler()
        self.DBm = DB_methods()
        store = self.DBh.select(['client'], ['score', 'year', 'self_rank', 'province', 'subject','pici','major'],
                                ['user_ID = ' + user_ID])
        self.getRisk = getRisk(user_ID)
        self.user = user_ID
        self.score = str(store[0])
        self.year = str(store[1])
        self.rank = store[2]
        self.province = str(store[3])
        self.subject = store[4]
        self.pici = store[5]
        self.majors = store[6].split(',')
        #print(self.major)
        #self.province = self.DBh.select(['provinceid'], ['省份'], ['ID = ' + provinceID])

        subject = store[4]
        if subject == 'science':
            self.subject = '理科'
        elif subject == 'literature':
            self.subject= '文科'
        elif subject == 'sci-li':
            self.subject = '综合'
        '''
        pici = str(self.DBh.select(['client'], ['pici'], ['user_ID =' + user_ID]))
        if pici == '0':
            self.pici = '提前批'
        elif pici == '1':
            self.pici = '第一批'
        elif pici == '2':
            self.pici = '第二批'
        else:
            self.pici = '第三批'
        '''

    def major_recommand(self,major):#一级学科
        #对所有专业

        result_low_risk_school = []

        result_high_risk_school = []

        result_mid_risk_school = []
        #majors_list = [] #记录推荐学校
        school_list = []

        #对单个专业

        lowest_score = []
        highest_score = []
        avg_score = []
        temp = []
        val = [self.province,self.pici,major, self.subject, '综合']
        for year in range(int(self.year)-5,int(self.year)):
            val.append(year)
        db_school_list = "select 学校名称, 年份, 批次, 录取最低分, 录取平均分, 录取最高分 " \
                         "from ecol_majors where 省份= %s and 批次 = %s and 一级学科=%s and (科类= %s or 科类=%s )  "+' and (年份= %s or 年份=%s or 年份=%s or 年份=%s or 年份=%s) order by 学校名称'
        #print(db_school_list)
        #print(val)
        cursor.execute(db_school_list, val)
        conn.commit()

        temp.append(cursor.fetchall())  # temp = [((schoolID,year,pici,ls,as,hs),()...)]
        print(temp)
        N = 2468
        avg_score_avg = [0 for i in range(N)]
        lowest_score_avg = [0 for i in range(N)]
        highest_score_avg = [0 for i in range(N)]
        n = 1  # 计数，学校
        j = 0  # 计数，最低分数据个数
        k = 0  # 计数，最高分数据个数
        m = 0  # 计数，平均分数据个数
        for i in range(len(temp[0])):
            # 因许多省份改革，只取2014以后数据
            if int(temp[0][i][1]) == int(self.year) - 1 or int(temp[0][i][1]) == int(self.year) - 2 or int(temp[0][i][1]) == int(
                    self.year) - 3 or \
                    int(temp[0][i][1]) == int(self.year) - 4 or int(temp[0][i][1]) == int(self.year) - 5:
                # 若是同一所学校
                #print('year ok')
                if int(schoolID_dictionary[schoolID_dictionary[temp[0][i][0]]]) == n:
                    #print('school ok')
                    if temp[0][i][3]:  # 若存在最低分数据
                        lowest_score_avg[n] += int(temp[0][i][3])  # 该学校最低分的平均分中加入此数据
                        j += 1  # 最低分数量加一
                    if temp[0][i][5]:  # 同上
                        highest_score_avg[n] += int(temp[0][i][5])
                        k += 1
                    if temp[0][i][4]:  # 同上
                        avg_score_avg[n] += int(temp[0][i][4])
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

                    n = int(schoolID_dictionary[schoolID_dictionary[temp[0][i][0]]])

                    if temp[0][i][3]:  # 若存在最低分数据
                        lowest_score_avg[n] += int(temp[0][i][3])  # 该学校最低分的平均分中加入此数据
                        j += 1  # 最低分数量加一
                    if temp[0][i][5]:  # 同上
                        highest_score_avg[n] += int(temp[0][i][5])
                        k += 1
                    if temp[0][i][4]:  # 同上
                        avg_score_avg[n] += int(temp[0][i][4])
                        m += 1

        #print(avg_score_avg)
        up_line = 10
        down_line = 20
        while (len(school_list) < 10):
            for i in range(len(lowest_score_avg)):  # 取上下十分
                if lowest_score_avg[i] and highest_score_avg[i]:
                    if min(avg_score_avg[i], lowest_score_avg[i]) - down_line <= int(self.score) <= max(
                            avg_score_avg[i],
                            highest_score_avg[i]) + up_line:
                        school_list.append(i)
                else:
                    if avg_score_avg[i] - 15 <= int(self.score) <= avg_score_avg[i] + 20:
                        school_list.append(i)
                if len(school_list) > 30:
                    break
            up_line += 5
            down_line += 20
        #****************************************************************************************************************
        #原方案：
        high_risk_school = []
        normal_risk_school = []
        low_risk_school = []
        temp_list = []
        low_school_rank_list = []
        normal_school_rank_list = []
        high_school_rank_list = []
        print('school_list:')
        print(school_list)
        #print(list(schoolID_dictionary.keys())[list(schoolID_dictionary.values()).index('51')])
        for i in school_list:
            db_list = "select 年份, 批次, 录取最低分, 录取平均分, 录取最高分 " \
                      "from major_copy where 学校名称= %s and 省份 = %s and (科类= %s or 科类 = %s) and 一级学科 = %s "
            #school = self.DBh.select(['gaokaowang_schoolname'],['学校名称'],['ID = '+str(i)])
            #print(list(schoolID_dictionary.keys())['51'])
            school = list(schoolID_dictionary.keys())[list(schoolID_dictionary.values()).index(str(i))] #反向查找keys
            val = [school, self.province, self.subject, '综合',major]
            cursor.execute(db_list, val)
            conn.commit()
            temp_list.append(cursor.fetchall()) #形式为[((年份,批次....),),] 第一个元祖是对应学校

        line_rank = [[] for i in range(len(school_list))]

        rank_dict = get_dict_yifenyidang(self.province, self.year, self.subject)
        for i in range(len(school_list)):
            for j in range(len(temp_list[i])):
                if temp_list[i][j][5]:
                    if temp_list[i][j][3]:
                        current_score = int(temp_list[i][j][3])
                        if current_score < list(rank_dict.keys())[-1]:
                            line_rank[i].append(list(rank_dict.values())[-1])
                        elif current_score > list(rank_dict.keys())[0]:
                            line_rank[i].append(list(rank_dict.values())[0])
                        else:
                            line_rank[i].append(rank_dict[current_score])
        #print(line_rank)
        #print(len(line_rank))
        for i in range(len(school_list)):
            if self.getRisk.risk_level(line_rank[i]) == 0:
                low_risk_school.append(school_list[i])
            if self.getRisk.risk_level(line_rank[i]) == 1:
                normal_risk_school.append(school_list[i])
            if self.getRisk.risk_level(line_rank[i]) == 2:
                high_risk_school.append(school_list[i])
        #print('low:')
        #print(low_risk_school)
        #print('avg')
        #print(normal_risk_school)
        #print('high')
        #print(high_risk_school)
        # 分三个表存储高中低风险。school_and_rank存储的是每个学校对应的近几年平均分数对应的排名。
        for i in range(len(low_risk_school)):
            school = list(schoolID_dictionary.keys())[list(schoolID_dictionary.values()).index(i)]
            low_school_rank = self.DBh.select(['majors_copy'],['rank'],['学校名称='+school,'一级学科='+major])
            #print(low_school_rank)

            low_school_rank_list.append(low_school_rank)
        #print(low_school_rank_list)
        for i in range(len(normal_risk_school)):


            school = list(schoolID_dictionary.keys())[list(schoolID_dictionary.values()).index(i)]
            normal_school_rank = self.DBh.select(['majors_copy'],['rank'],['学校名称='+school,'一级学科='+major])

            normal_school_rank_list.append(normal_school_rank)
        for i in range(len(high_risk_school)):
            school = list(schoolID_dictionary.keys())[list(schoolID_dictionary.values()).index(i)]
            high_school_rank = self.DBh.select(['majors_copy'],['rank'],['学校名称='+school,'一级学科='+major])

            high_school_rank_list.append(high_school_rank)

        #主义是从哪里读取的排名

        # 分三个表存储高中低风险。school_and_rank存储的是每个学校对应的近几年平均分数对应的排名。
        for i in range(len(low_risk_school)):
            low_school_rank = self.DBh.select(['gaokaowang_schoolname'],['school_rank'],['ID='+str(low_risk_school[i])])
            #print(low_school_rank)

            low_school_rank_list.append(low_school_rank)
        #print(low_school_rank_list)
        for i in range(len(normal_risk_school)):
            normal_school_rank = self.DBh.select(['gaokaowang_schoolname'],['school_rank'],['ID='+str(normal_risk_school[i])])

            normal_school_rank_list.append(normal_school_rank)
        for i in range(len(high_risk_school)):
            high_school_rank = self.DBh.select(['gaokaowang_schoolname'],['school_rank'],['ID='+str(high_risk_school[i])])

            high_school_rank_list.append(high_school_rank)

        #主义是从哪里读取的排名

        # 分三个表存储高中低风险。school_and_rank存储的是每个学校对应的近几年平均分数对应的排名。
        if len(low_risk_school) == 3:
            for i in range(len(low_risk_school)):
                if low_school_rank_list[i]!= 100000:
                    result_low_risk_school.append(low_risk_school[i])
                    low_school_rank_list[i] = 100000
        elif len(low_risk_school) < 3:
            N = 0
            for i in range(len(low_risk_school)):
                if low_school_rank_list[i] != 100000:
                    result_low_risk_school.append(low_risk_school[i])
                    low_school_rank_list[i] = 100000
                    N += 1
            if len(normal_risk_school) > 0:
                for i in range(3 - N):
                    best = 0
                    for j in range(len(normal_risk_school)):
                        t = school_list.index(normal_risk_school[j])
                        r = self.getRisk.risk_rank( line_rank[t])
                        best_rank = self.getRisk.risk_rank(line_rank[school_list.index(normal_risk_school[best])])
                        if int(normal_school_rank_list[j]) > 0 and 0.2 * r + 10 * int(
                                normal_school_rank_list[j]) < \
                                0.2 * best_rank + 10 * int(normal_school_rank_list[best]):
                            best = j
                        if int(normal_school_rank_list[j]) == 0 and r < best_rank:
                            best = j
                    if int(normal_school_rank_list[best]) != 100000:
                        result_low_risk_school.append(normal_risk_school[best])
                        normal_school_rank_list[best] = 100000
                        N += 1
            if N < 3 and len(high_risk_school) > 0:
                for i in range(3 - N):
                    best = 0
                    for j in range(len(high_risk_school)):
                        t = school_list.index(high_risk_school[j])
                        r = self.getRisk.risk_rank(line_rank[t])
                        best_rank = self.getRisk.risk_rank(line_rank[school_list.index(high_risk_school[best])])
                        if r < best_rank and int(high_school_rank_list[j]) != 100000:
                            best = j
                    result_low_risk_school.append(high_risk_school[best])
                    high_school_rank_list[best]= 100000
        else:
            for i in range(3):
                best = 0
                for j in range(len(low_risk_school)):
                    t = school_list.index(low_risk_school[j])
                    r = self.getRisk.risk_rank(line_rank[t])  # school_list 中学校的序号和 school_and_list 中序号一致。
                    if int(low_school_rank_list[j]) > 0 and 0.1 * r + 10 * int(low_school_rank_list[j]) < \
                            0.1 * r + 10 * int(low_school_rank_list[best]) and random.random() >= 0.7:
                        best = j
                if int(low_school_rank_list[best]) != 100000 and int(low_school_rank_list[best]) != 0:
                    result_low_risk_school.append(low_risk_school[best])
                    low_school_rank_list[best] = 100000


        #中等风险学校
        if len(normal_risk_school) == 4:  # 中风险度
            for i in range(len(normal_risk_school)):
                if normal_school_rank_list[i] != 100000:
                    result_mid_risk_school.append(normal_risk_school[i])
                    normal_school_rank_list[i] = 100000
        elif len(normal_risk_school) < 4:
            N = 0
            for i in range(len(normal_risk_school)):
                if normal_school_rank_list[i]!= 100000:
                    select_school_list.append(normal_risk_school[i])
                    normal_school_rank_list[i] = 100000
                    N += 1
            if len(high_risk_school) > 0:
                for i in range(4 - N):
                    best = 0
                    for j in range(len(high_risk_school)):
                        t = school_list.index(high_risk_school[j])
                        r = self.getRisk.risk_rank(line_rank[t])
                        best_rank = self.getRisk.risk_rank(line_rank[school_list.index(high_risk_school[best])])
                        if r < best_rank and int(high_school_rank_list[j]) != 100000:
                            best = j
                    result_mid_risk_school.append(high_risk_school[best])
                    high_school_rank_list[best] = 100000
                    N += 1
            if N < 4 and len(low_risk_school) > 0:
                for i in range(4 - N):
                    best = 0
                    for j in range(len(low_risk_school)):
                        t = school_list.index(low_risk_school[j])
                        r = self.getRisk.risk_rank(line_rank[t])
                        best_rank = self.getRisk.risk_rank( line_rank[school_list.index(low_risk_school[best])])
                        if 0 < int(low_school_rank_list[j]) < int(
                                low_school_rank_list[best]):
                            best = j
                        if int(low_school_rank_list[j]) == 0 and r < best_rank:
                            best = j
                    if int(low_school_rank_list[best]) != 100000:
                        result_mid_risk_school.append(low_risk_school[best])
                        low_school_rank_list[best] = 100000
        else:
            for i in range(4):
                best = 0
                for j in range(len(normal_risk_school)):
                    t = school_list.index(normal_risk_school[j])
                    r = self.getRisk.risk_rank( line_rank[
                        t])  # school_list 中学校的序号和 school_and_list 中序号一致。
                    if int(normal_school_rank_list[j]) > 0 and 0.1 * r + 10 * int(
                            normal_school_rank_list[j]) \
                            < 0.1 * r + 10 * int(
                        normal_school_rank_list[best]) and random.random() >= 0.7:
                        best = j
                if int(normal_school_rank_list[best]) != 100000 and int(
                        normal_school_rank_list[best]) != 0:
                    result_mid_risk_school.append(normal_risk_school[best])
                    normal_school_rank_list[best] = 100000

        if len(high_risk_school) == 3:
            for i in range(len(high_risk_school)):
                if high_school_rank_list[i] != 100000:
                    result_high_risk_school.append(high_risk_school[i])
                    high_school_rank_list[i] = 100000
        elif len(high_risk_school) < 3:
            N = 0
            for i in range(len(high_risk_school)):
                if high_school_rank_list[i] != 100000:
                    result_high_risk_school.append(high_risk_school[i])
                    high_school_rank_list[i] = 100000
                    N += 1
            if len(normal_risk_school) > 0:
                for i in range(3 - N):
                    best = 0
                    for j in range(len(normal_risk_school)):
                        t = school_list.index(normal_risk_school[j])
                        r = self.getRisk.risk_rank(line_rank[t])
                        best_rank = self.getRisk.risk_rank( line_rank[school_list.index(normal_risk_school[best])])
                        if int(normal_school_rank_list[j]) > 0 and 0.2 * r + 10 * int(
                                normal_school_rank_list[j]) < \
                                0.2 * best_rank + 10 * int(normal_school_rank_list[best]):
                            best = j
                        if int(normal_school_rank_list[j]) == 0 and r < best_rank:
                            best = j
                    if int(normal_school_rank_list[best]) != 100000:
                        result_high_risk_school.append(normal_risk_school[best])
                        normal_school_rank_list[best] = 100000
                        N += 1
            if N < 3 and len(low_risk_school) > 0:
                for i in range(3 - N):
                    best = 0
                    for j in range(len(low_risk_school)):
                        t = school_list.index(low_risk_school[j])
                        r = self.getRisk.risk_rank( line_rank[t])
                        best_rank = self.getRisk.risk_rank( line_rank[school_list.index(low_risk_school[best])])
                        if 0 < int(low_school_rank_list[j]) < int(
                                low_school_rank_list[best]):
                            best = j
                        if int(low_school_rank_list[j]) == 0 and r < best_rank:
                            best = j
                    if int(low_school_rank_list[best]) != 100000:
                        result_high_risk_school.append(low_risk_school[best])
                        low_school_rank_list[best] = 100000
        else:
            for i in range(3):
                best = 0
                for j in range(len(high_risk_school)):
                    t = school_list.index(high_risk_school[j])
                    r = self.getRisk.risk_rank(line_rank[
                        t])  # school_list 中学校的序号和 school_and_list 中序号一致。
                    if int(high_school_rank_list[j]) > 0 and 0.1 * r + 10 * int(
                            high_school_rank_list[j]) \
                            < 0.1 * r + 10 * int(
                        high_school_rank_list[best]) and random.random() >= 0.7:
                        best = j
                if int(high_school_rank_list[best]) != 100000 and int(
                        high_school_rank_list[best]) != 0:
                    result_high_risk_school.append(high_risk_school[best])
                    high_school_rank_list[best] = 100000


        #e5 = time.clock()



        return result_high_risk_school, result_mid_risk_school, result_low_risk_school

    def majors_recommand(self):
        store_low_school_all = []
        store_mid_school_all = []
        store_high_school_all = []
        #把每个学校的顺序排入
        for i in range(len(self.majors)):
            print('majors')
            print(i)
            store_high_school,store_mid_school,store_low_school = self.major_recommand(self.majors[i])
            store_high_school_all +=store_high_school
            store_low_school_all += store_low_school
            store_mid_school_all += store_mid_school
        #返回出现频率最高的学校
        high_school_dict = {}
        mid_school_dict = {}
        low_school_dict ={}

        result_high_school = []
        result_mid_school = []
        result_low_school = []
        for school in store_high_school_all:
            high_school_dict[school] = store_high_school_all.count(school)
        high_school_dict = sorted(high_school_dict.items(),key = lambda item:item[0])
        '''
        for i in range(3):
            result_high_school.append(list(high_school_dict.keys())[i])
        '''
        for school in store_mid_school_all:
            mid_school_dict[school] = store_mid_school_all.count(school)
        mid_school_dict = sorted(mid_school_dict.items(),key = lambda item:item[0])
        '''
        for i in range(3):
            result_mid_school.append(list(mid_school_dict.keys())[i])
        '''
        for school in store_low_school_all:
            low_school_dict[school] = store_low_school_all.count(school)
        low_school_dict = sorted(low_school_dict.items(),key = lambda item:item[0])
        '''
        for i in range(3):
            result_low_school.append(list(low_school_dict.keys())[i])
        '''

        return result_high_school,result_mid_school,result_low_school
