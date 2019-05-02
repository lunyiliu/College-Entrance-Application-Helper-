from getRisk_for_test import risk_rank,risk_level
from DB_handler import DB_handler
from DB_methods import DB_methods
import pymysql
import random
import time
from get_dict_yifenyidang import get_dict_yifenyidang
import random

# 加载本地
pici_dict = {'提前批': 'tiqianpi', '第一批': 'diyipi', '第二批': 'dierpi', '其他': 'other'}
provinceID_dictionary = {}
with open('provinceid.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        provinceID_dictionary[line.split(',')[0]] = line.split(',')[1]

schoolID_dictionary = {}
with open('school2ID.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        schoolID_dictionary[line.split(',')[0]] = line.split(',')[1]
# 数据库连接
conn = pymysql.connect(host='39.97.100.184', user='root', passwd='8612260', db='gaokao', charset='utf8')
cursor = conn.cursor()


class recommand():
    def __init__(self,user_ID):
        self.DBh = DB_handler()
        self.DBm = DB_methods()

        self.user = user_ID
        store = self.DBh.select(['client'], ['score', 'year', 'self_rank', 'province', 'subject', 'pici'],
                                ['user_ID =' + user_ID])
        self.score = str(store[0])
        self.year = str(store[1])
        self.rank = store[2]
        self.subject = store[4]

        if self.rank is None or self.rank == 0:
            rank_dict = get_dict_yifenyidang('天津', '2018',self.subject)
            if self.score < list(rank_dict.keys())[-1]:
                # print("year1")
                # print()
                self.rank = list(rank_dict.values())[-1]
            elif self.score > list(rank_dict.keys())[0]:
                self.rank = list(rank_dict.values())[0]
            else:
                self.rank = rank_dict[self.score]
        self.province = str(store[3])
        # self.province = str(provinceID_dictionary[province]) #实际存的是id



        self.pici = str(store[5])
        self.pici = pici_dict[self.pici]

        '''
        self.DBh = DB_handler()
        self.DBm = DB_methods()



        self.score = str(score)
        self.year = str(2019)
        self.rank = rank
        self.province = '天津'
        # self.province = str(provinceID_dictionary[province]) #实际存的是id

        self.subject = subject

        self.pici = pici
        self.pici = pici_dict[self.pici]
        # self.pici = 'diyipi'
        '''
    def schools_recommand(self):
        # 对所有专业
        s = time.clock()
        result_low_risk_school = []

        result_high_risk_school = []

        result_mid_risk_school = []

        school_list = []
        temp = []
        if self.pici == 'tiqianpi':
            #print('tiqianpi')
            val = [self.province, self.pici, self.subject, 'sci-li']
            for year in range(int(self.year) - 5, int(self.year)):
                val.append(year)
            #print(val)
            db_school_list = "select schoolName, year, pici, lowest_score, avg_score, highest_score " \
                             "from ecol_school" + " where provinceName= %s and pici =%s  and (subject=" + ' %s ' + 'or ' + 'subject=%s )' + ' and (year= %s or year=%s or year=%s or year=%s or year=%s) order by schoolName'
        else :
            val = [self.province, self.pici, 'other', self.subject, 'sci-li']
            for year in range(int(self.year) - 5, int(self.year)):
                val.append(year)
            '''
            db_school_list = "select schoolID, year, pici, lowest_score, avg_score, highest_score " \
                             "from school" + " where provinceID= %sand pici =%s and (subject=" + ' %s '+'or ' +'subject=%s )'+' and (year= %s or year=%s or year=%s or year=%s or year=%s) order by schoolID'
            #print(db_school_list)
            '''
            db_school_list = "select schoolName, year, pici, lowest_score, avg_score, highest_score " \
                             "from ecol_school" + " where provinceName= %s and (pici =%s or pici = %s) and (subject=" + ' %s ' + 'or ' + 'subject=%s )' + ' and (year= %s or year=%s or year=%s or year=%s or year=%s) order by schoolName'

        # print(val)
        cursor.execute(db_school_list, val)
        conn.commit()

        temp.append(cursor.fetchall())  # temp = [((schoolID,year,pici,ls,as,hs),()...)]
        # 搜索分数线在考生附近的学校
        # print(temp)
        # print(temp[0][0])
        # print(len(temp))

        e1 = time.clock()

        N = 2468
        avg_score_avg = [0 for i in range(N)]
        lowest_score_avg = [0 for i in range(N)]
        highest_score_avg \
            = [0 for i in range(N)]
        n = int(schoolID_dictionary[temp[0][0][0]])  # 计数，学校
        j = 0  # 计数，最低分数据个数
        k = 0  # 计数，最高分数据个数
        m = 0  # 计数，平均分数据个数
        for i in range(len(temp[0])):  # 同一个i代表一个年份
            # 因许多省份改革，只取2014以后数据
            if int(temp[0][i][1]) == int(self.year) - 1 or int(temp[0][i][1]) == int(self.year) - 2 or int(
                    temp[0][i][1]) == int(self.year) - 3 :#\
                    #or \int(temp[0][i][1]) == int(self.year) - 4 or int(temp[0][i][1]) == int(self.year) - 5:
                # 若是同一所学校
                if int(schoolID_dictionary[temp[0][i][0]]) == n:

                    if temp[0][i][3]:  # 若存在最低分数据
                        score_all = int(float(lowest_score_avg[n])) + int(float(temp[0][i][3]))  # 该学校最低分的平均分中加入此数据
                        lowest_score_avg[n] = score_all
                        j += 1  # 最低分数量加一
                    if temp[0][i][5]:  # 同上
                        # print(temp[0][i][5])
                        score_all = int(float(highest_score_avg[n])) + int(float(temp[0][i][5]))
                        highest_score_avg[n] = score_all
                        k += 1
                    if temp[0][i][4]:  # 同上
                        score_all = int(float(avg_score_avg[n])) + int(float(temp[0][i][4]))
                        avg_score_avg[n] = score_all
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
                    # print(temp[0][i][0])
                    n = int(schoolID_dictionary[temp[0][i][0]])
                    if temp[0][i][3]:  # 若存在最低分数据
                        score_all = int(float(lowest_score_avg[n])) + int(float(temp[0][i][3]))  # 该学校最低分的平均分中加入此数据
                        lowest_score_avg[n] = score_all
                        j += 1  # 最低分数量加一
                    if temp[0][i][5]:  # 同上
                        # print(temp[0][i][5])
                        score_all = int(float(highest_score_avg[n])) + int(float(temp[0][i][5]))
                        highest_score_avg[n] = score_all
                        k += 1
                    if temp[0][i][4]:  # 同上
                        score_all = int(float(avg_score_avg[n])) + int(float(temp[0][i][4]))
                        avg_score_avg[n] = score_all
                        m += 1
        # print(highest_score_avg)
        # print(avg_score_avg)
        # print(avg_score_avg)
        temp_dict = {}
        for i in range(len(lowest_score_avg)):
            if avg_score_avg[i]:
                value = int(avg_score_avg[i])
            elif lowest_score_avg[i] and highest_score_avg[i]:
                value = int((int(lowest_score_avg[i]) + int(highest_score_avg[i]))/2)
            else:
                value = 0
            if value != 0:
                temp_dict[i] = value
        #print(temp_dict)
        sorted_temp_dict = sorted(temp_dict.items(), key=lambda e:e[1], reverse=True)
        #print(len(sorted_temp_dict))
        for i in range(len(sorted_temp_dict)):
            if  int(self.score) >= int(sorted_temp_dict[i][1]):
                index = i
                break
            if i == len(sorted_temp_dict) -1:
                index = len(sorted_temp_dict) -1
        #print(type(index))

        if index == 0:
            pass

        elif index <10 :
            #print('yes1')
            for i in range(0,index):
                school_list.append(sorted_temp_dict[i][0])

        else:
            if int(sorted_temp_dict[index-10][1]) >= int(self.score) + 20:
                #print('yes')
                for i in range(index-10,index):
                    school_list.append(sorted_temp_dict[i][0])
            else:
                #print('yes2')
                for i in range(index-10,index):
                    school_list.append(sorted_temp_dict[i][0])

                up_line = 15
                down_line = 5
                for i in range(len(sorted_temp_dict)):
                    if  int(sorted_temp_dict[index][1]) +down_line <= sorted_temp_dict[i][1] <= int(sorted_temp_dict[index][1]) + up_line :
                        school_list.append(sorted_temp_dict[i][0])



        if index == len(sorted_temp_dict) -1:
            pass
        elif index > len(sorted_temp_dict) -7:
            for i in range(index,len(sorted_temp_dict)):
                school_list.append(sorted_temp_dict[i][0])
        else:
            #print('yes')
            for i in range(index,index + 7):
                school_list.append(sorted_temp_dict[i][0])

            up_line = -5
            down_line = -10
            for i in range(len(sorted_temp_dict)):
                if int(sorted_temp_dict[index][1]) +down_line <= sorted_temp_dict[i][1] <= int(
                        sorted_temp_dict[index][1]) + up_line:
                    school_list.append(sorted_temp_dict[i][0])
        school_list = list(set(school_list))
        #print(school_list)

        '''
        up_line = 10
        down_line = 10
        while (len(school_list) < 10):
            school_list = []
            for i in range(len(lowest_score_avg)):  # 取上下十分

                if lowest_score_avg[i] or highest_score_avg[i]:
                    if min(avg_score_avg[i], lowest_score_avg[i]) - down_line <=  int(self.score) <= max(avg_score_avg[i],highest_score_avg[i]) + up_line:
                        school_list.append(i)
                else:
                    if avg_score_avg[i] - down_line <= int(self.score) <= avg_score_avg[i] + up_line:
                        school_list.append(i)
                #if len(school_list) > 30:
                #    break

            up_line += 15
            down_line += 10
            #print(down_line)
        '''
        '''
        if len(school_list) < 10:
            print('used1')
            school_list = []
            for i in range(len(lowest_score_avg)):  # 取上下十分
                if lowest_score_avg[i] and highest_score_avg[i]:
                    if min(avg_score_avg[i], lowest_score_avg[i]) - 40 <= int(self.score) <= max(avg_score_avg[i],
                                                                                                 highest_score_avg[
                                                                                                     i]) + 40:
                        school_list.append(i)
                else:
                    if avg_score_avg[i] - 40 <= int(self.score) <= avg_score_avg[i] + 40:
                        school_list.append(i)
                if len(school_list) > 30:
                    break
            print(school_list)

        if len(school_list) < 10:
            print('used2')
            school_list = []
            for i in range(len(lowest_score_avg)):  # 取上下十分
                if lowest_score_avg[i] and highest_score_avg[i]:
                    if min(avg_score_avg[i], lowest_score_avg[i]) - 120 <= int(self.score) <= max(avg_score_avg[i],
                                                                                                 highest_score_avg[
                                                                                                     i]) + 40:
                        school_list.append(i)
                else:
                    if avg_score_avg[i] - 150 <= int(self.score) <= avg_score_avg[i] + 40:
                        school_list.append(i)
                if len(school_list) > 30:
                    break
            print(school_list)
        '''
        # print('school_list:')
        #print(school_list)
        e2 = time.clock()

        #print(school_list)
        '''
        #原来的方案，发现效率实在太低了
        schools = self.DBh.select(['gaokaowang_schoolname'], ['ID'],[])
        for i in range(len(schools)):
            sum_avg_score = 0
            sum_lowest_score = 0
            sum_highest_score = 0
            school = schools[i]
            lowest_score = []
            highest_score = []
            avg_score = []
            for year in range(int(self.year) - 5, int(self.year)):
                conditionlist = ['schoolID=' + str(school),
                                 'provinceID= ' + self.province,
                                 'year=' + str(year)]
                lowest_score_store = self.DBh.select(['school'], ['lowest_score'], conditionlist,
                                                     [['subject', self.subject, 'sci-li']],para_debug=True)
                highest_score_store = self.DBh.select(['school'], ['highest_score'], conditionlist,
                                                     [['subject', self.subject, 'sci-li']])
                avg_score_store = self.DBh.select(['school'], ['avg_score'], conditionlist,
                                                     [['subject', self.subject, 'sci-li']])
                #print(lowest_score_store)
                #print(type(lowest_score_store))

                if type(lowest_score_store) is str:
                    lowest_score.append(lowest_score_store)
                    sum_lowest_score += int(lowest_score_store)
                elif lowest_score_store is not None:
                    for score in lowest_score_store:
                        if score is not None and score != 0:
                            lowest_score.append(score)
                            print('low='+score)
                            print(score is not None)
                            sum_lowest_score += int(score)

                if type(highest_score_store) is str:
                    highest_score.append(highest_score_store)
                    sum_highest_score += int(highest_score_store)
                elif highest_score_store is not None:

                    for score in highest_score_store:
                        if score is not None and score != 0:
                            print('high=' + score)
                            print(score is not None)
                            highest_score.append(score)
                            sum_highest_score += int(score)
                if type(avg_score_store) is str:
                    avg_score.append(avg_score_store)
                    sum_avg_score += int(avg_score_store)
                elif avg_score_store is not None:
                    for score in avg_score_store:
                        if score is not None and score != 0:
                            print('avg=' + score)
                            print(score is not None)
                            avg_score.append(score)
                            sum_avg_score += int(score)

            print('end')
            if lowest_score != [] and highest_score != []:
                if min(sum_avg_score / len(avg_score), sum_lowest_score / len(lowest_score)) - 15 <= int(
                        self.score) <= max(sum_avg_score / len(avg_score), sum_lowest_score / len(lowest_score)) + 20:
                    school_list.append(school)
            else:
                if sum_avg_score / len(avg_score) - 15 <= int(self.score) <= sum_avg_score / len(avg_score) + 20:
                    school_list.append(school)
        '''

        # 原方法
        high_risk_school = []
        normal_risk_school = []
        low_risk_school = []
        temp_list = []
        low_school_rank_list = []
        normal_school_rank_list = []
        high_school_rank_list = []

        for i in school_list:
            db_list = "select year, pici, lowest_score, avg_score, highest_score " \
                      "from ecol_school where schoolName= %s and provinceName= %s and (subject= %s or subject = %s) and (pici = %s or pici = %s)"
            school_name = list(schoolID_dictionary.keys())[list(schoolID_dictionary.values()).index(str(i))]
            val = [school_name, self.province, self.subject, 'sci-li', self.pici, 'other']
            cursor.execute(db_list, val)
            conn.commit()
            temp_list.append(cursor.fetchall())

        # print(temp_list)

        rank_dict_1 = get_dict_yifenyidang(self.province, int(self.year) - 1, self.subject)
        rank_dict_2 = get_dict_yifenyidang(self.province, int(self.year) - 2, self.subject)
        rank_dict_3 = get_dict_yifenyidang(self.province, int(self.year) - 3, self.subject)
        rank_dict_4 = get_dict_yifenyidang(self.province, int(self.year) - 4, self.subject)
        rank_dict_5 = get_dict_yifenyidang(self.province, int(self.year) - 5, self.subject)
        # print(rank_dict_2)
        line_rank = [[] for i in range(len(school_list))]
        e3 = time.clock()
        # print(school_list)
        for i in range(len(school_list)):
            # print(len(temp_list[i]))
            for j in range(len(temp_list[i])):
                # print(j)
                # print(temp_list[i][j][3])
                if temp_list[i][j][2]:

                    n = int(self.year) - int(temp_list[i][j][0])
                    # print('n:')
                    # print(n)
                    if n == 1:
                        # print(temp_list[i][j][3])
                        # print(type(temp_list[i][j][3]))

                        current_score = int(float(temp_list[i][j][2]))

                        # print(list(rank_dict_1.keys())[-1])
                        # print(list(rank_dict_1.keys())[0])
                        if current_score < list(rank_dict_1.keys())[-1]:
                            # print("year1")
                            # print()
                            line_rank[i].append(list(rank_dict_1.values())[-1])
                        elif current_score > list(rank_dict_1.keys())[0]:
                            line_rank[i].append(list(rank_dict_1.values())[0])
                        else:
                            line_rank[i].append(rank_dict_1[current_score])
                    if n == 2:
                        current_score = int(float(temp_list[i][j][2]))
                        if current_score < list(rank_dict_2.keys())[-1]:

                            line_rank[i].append(list(rank_dict_2.values())[-1])
                        elif current_score > list(rank_dict_2.keys())[0]:
                            line_rank[i].append(list(rank_dict_2.values())[0])
                        else:
                            line_rank[i].append(rank_dict_2[current_score])
                    if n == 3:
                        current_score = int(float(temp_list[i][j][2]))
                        if current_score < list(rank_dict_3.keys())[-1]:

                            line_rank[i].append(list(rank_dict_3.values())[-1])
                        elif current_score > list(rank_dict_3.keys())[0]:
                            line_rank[i].append(list(rank_dict_3.values())[0])
                        else:
                            line_rank[i].append(rank_dict_3[current_score])
                    if n == 4:
                        current_score = int(float(temp_list[i][j][2]))
                        if current_score < list(rank_dict_4.keys())[-1]:

                            line_rank[i].append(list(rank_dict_4.values())[-1])
                        elif current_score > list(rank_dict_4.keys())[0]:
                            line_rank[i].append(list(rank_dict_4.values())[0])
                        else:
                            line_rank[i].append(rank_dict_4[current_score])
                    if n == 5:
                        current_score = int(float(temp_list[i][j][2]))
                        if current_score < list(rank_dict_5.keys())[-1]:

                            line_rank[i].append(list(rank_dict_5.values())[-1])
                        elif current_score > list(rank_dict_5.keys())[0]:
                            line_rank[i].append(list(rank_dict_5.values())[0])
                        else:
                            line_rank[i].append(rank_dict_5[current_score])

                elif temp_list[i][j][3]:

                    n = int(self.year) - int(temp_list[i][j][0])
                    # print('n:')
                    # print(n)
                    if n == 1:
                        # print(temp_list[i][j][3])
                        # print(type(temp_list[i][j][3]))

                        current_score = int(float(temp_list[i][j][3]))

                        # print(list(rank_dict_1.keys())[-1])
                        # print(list(rank_dict_1.keys())[0])
                        if current_score < list(rank_dict_1.keys())[-1]:
                            # print("year1")
                            # print()
                            line_rank[i].append(list(rank_dict_1.values())[-1])
                        elif current_score > list(rank_dict_1.keys())[0]:
                            line_rank[i].append(list(rank_dict_1.values())[0])
                        else:
                            line_rank[i].append(rank_dict_1[current_score])
                    if n == 2:
                        current_score = int(float(temp_list[i][j][3]))
                        if current_score < list(rank_dict_2.keys())[-1]:

                            line_rank[i].append(list(rank_dict_2.values())[-1])
                        elif current_score > list(rank_dict_2.keys())[0]:
                            line_rank[i].append(list(rank_dict_2.values())[0])
                        else:
                            line_rank[i].append(rank_dict_2[current_score])
                    if n == 3:
                        current_score = int(float(temp_list[i][j][3]))
                        if current_score < list(rank_dict_3.keys())[-1]:

                            line_rank[i].append(list(rank_dict_3.values())[-1])
                        elif current_score > list(rank_dict_3.keys())[0]:
                            line_rank[i].append(list(rank_dict_3.values())[0])
                        else:
                            line_rank[i].append(rank_dict_3[current_score])
                    if n == 4:
                        current_score = int(float(temp_list[i][j][3]))
                        if current_score < list(rank_dict_4.keys())[-1]:

                            line_rank[i].append(list(rank_dict_4.values())[-1])
                        elif current_score > list(rank_dict_4.keys())[0]:
                            line_rank[i].append(list(rank_dict_4.values())[0])
                        else:
                            line_rank[i].append(rank_dict_4[current_score])
                    if n == 5:
                        current_score = int(float(temp_list[i][j][3]))
                        if current_score < list(rank_dict_5.keys())[-1]:

                            line_rank[i].append(list(rank_dict_5.values())[-1])
                        elif current_score > list(rank_dict_5.keys())[0]:
                            line_rank[i].append(list(rank_dict_5.values())[0])
                        else:
                            line_rank[i].append(rank_dict_5[current_score])
        #print(line_rank)
        # print(len(line_rank))

        for i in range(len(school_list)):
            if risk_level(self.rank,line_rank[i]) == 0:
                low_risk_school.append(school_list[i])
            if risk_level(self.rank,line_rank[i]) == 1:
                normal_risk_school.append(school_list[i])
            if risk_level(self.rank,line_rank[i]) == 2:
                high_risk_school.append(school_list[i])
        #print('low:')
        #print(low_risk_school)
        #print('avg')
        #print(normal_risk_school)
        #print('high')
        #print(high_risk_school)
        # 此处应排序，按学校排名学科排名和风险值综合考量对三个数组进行排序，只保留前几个结果
        e4 = time.clock()
        # print(low_risk_school)
        for i in range(len(low_risk_school)):
            low_school_rank = self.DBh.select(['ecol_schoolnames'], ['school_rank'], ['ID=' + str(low_risk_school[i])])
            # print(low_school_rank)

            low_school_rank_list.append(low_school_rank)
        #print(low_school_rank_list)
        for i in range(len(normal_risk_school)):
            normal_school_rank = self.DBh.select(['ecol_schoolnames'], ['school_rank'],
                                                 ['ID=' + str(normal_risk_school[i])])

            normal_school_rank_list.append(normal_school_rank)
        for i in range(len(high_risk_school)):
            high_school_rank = self.DBh.select(['ecol_schoolnames'], ['school_rank'],
                                               ['ID=' + str(high_risk_school[i])])

            high_school_rank_list.append(high_school_rank)

        # 主义是从哪里读取的排名

        # 分三个表存储高中低风险。school_and_rank存储的是每个学校对应的近几年平均分数对应的排名。

        #print(len(low_risk_school))
        #('select')
        #print(low_risk_school)
        #print(normal_risk_school)
        #print(high_risk_school)
        if len(high_risk_school) == 3:
            for i in range(len(high_risk_school)):
                if high_school_rank_list[i] != 100000:
                    result_high_risk_school.append(high_risk_school[i])
                    high_school_rank_list[i] = 100000
            if len(result_high_risk_school) < 3:
                N = len(result_high_risk_school)
                if len(normal_risk_school) > 0:
                    for i in range(3 - N):
                        best = 0

                        for j in range(len(normal_risk_school)):
                            if int(normal_school_rank_list[j]) != 100000:
                                best = j
                                break
                        # 如果都被使用了，则换下一个
                        if best == 0 and int(normal_school_rank_list[best]) == 100000:
                            break

                        for j in range(len(normal_risk_school)):
                            if int(normal_school_rank_list[j]) != 100000:
                                t = school_list.index(normal_risk_school[j])
                                r = risk_rank(self.rank,line_rank[t])
                                best_rank = risk_rank(self.rank,line_rank[school_list.index(normal_risk_school[best])])
                                if int(normal_school_rank_list[j]) > 0 and 0.2 * r + 10 * int(
                                        normal_school_rank_list[j]) > \
                                        0.2 * best_rank + 10 * int(normal_school_rank_list[best]) and random.random()>0.3:
                                    best = j
                                if int(normal_school_rank_list[j]) == 0 and r > best_rank and random.random() > 0.5:
                                    best = j
                        if int(normal_school_rank_list[best]) != 100000:
                            result_high_risk_school.append(normal_risk_school[best])
                            normal_school_rank_list[best] = 100000
                            N += 1
                if N < 3 and len(low_risk_school) > 0:
                    for i in range(3 - N):
                        best = 0

                        for j in range(len(low_risk_school)):
                            if int(low_school_rank_list[j]) != 100000:
                                best = j
                                break

                        for j in range(len(low_risk_school)):
                            if int(low_school_rank_list[j]) != 100000:
                                t = school_list.index(low_risk_school[j])
                                r = risk_rank(self.rank,line_rank[t])
                                best_rank = risk_rank(self.rank,line_rank[school_list.index(low_risk_school[best])])
                                if  int(low_school_rank_list[j]) > int(
                                        low_school_rank_list[best]) and random.random() > 0.3:
                                    best = j
                                if int(low_school_rank_list[j]) == 0 and r > best_rank and random.random() > 0.5:
                                    best = j
                        if int(low_school_rank_list[best]) != 100000:
                            result_high_risk_school.append(low_risk_school[best])
                            low_school_rank_list[best] = 100000

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
                        if int(normal_school_rank_list[j]) != 100000:
                            best = j
                            break
                    # 如果都被使用了，则换下一个
                    if best == 0 and int(normal_school_rank_list[best]) == 100000:
                        break

                    for j in range(len(normal_risk_school)):
                        if int(normal_school_rank_list[j]) != 100000:
                            t = school_list.index(normal_risk_school[j])
                            r = risk_rank(self.rank, line_rank[t])
                            best_rank = risk_rank(self.rank, line_rank[school_list.index(normal_risk_school[best])])
                            if int(normal_school_rank_list[j]) > 0 and 0.2 * r + 10 * int(
                                    normal_school_rank_list[j]) > \
                                    0.2 * best_rank + 10 * int(normal_school_rank_list[best]) and random.random() > 0.3:
                                best = j
                            if int(normal_school_rank_list[j]) == 0 and r > best_rank and random.random() > 0.5:
                                best = j
                    if int(normal_school_rank_list[best]) != 100000:
                        result_high_risk_school.append(normal_risk_school[best])
                        normal_school_rank_list[best] = 100000
                        N += 1
            if N < 3 and len(low_risk_school) > 0:
                for i in range(3 - N):
                    best = 0

                    for j in range(len(low_risk_school)):
                        if int(low_school_rank_list[j]) != 100000:
                            best = j
                            break

                    for j in range(len(low_risk_school)):
                        if int(low_school_rank_list[j]) != 100000:
                            t = school_list.index(low_risk_school[j])
                            r = risk_rank(self.rank, line_rank[t])
                            best_rank = risk_rank(self.rank, line_rank[school_list.index(low_risk_school[best])])
                            if    int(low_school_rank_list[j]) > int(
                                    low_school_rank_list[best]) >= 0 and random.random() >0.3:
                                best = j
                            if int(low_school_rank_list[j]) == 0 and r > best_rank and random.random() > 0.5:
                                best = j
                    if int(low_school_rank_list[best]) != 100000:
                        result_high_risk_school.append(low_risk_school[best])
                        low_school_rank_list[best] = 100000
            '''
            if len(normal_risk_school) > 0:
                for i in range(3 - N):
                    best = 0
                    for j in range(len(normal_risk_school)):
                        t = school_list.index(normal_risk_school[j])
                        r = risk_rank(self.rank,line_rank[t])
                        best_rank = risk_rank(self.rank,line_rank[school_list.index(normal_risk_school[best])])
                        if int(normal_school_rank_list[j]) > 0 and 0.2 * r + 10 * int(
                                normal_school_rank_list[j]) < \
                                0.2 * best_rank + 10 * int(normal_school_rank_list[best]):
                            best = j
                        #print(type(r))
                        #print(type(best_rank))
                        if int(normal_school_rank_list[j]) == 0 and (r < best_rank) or random.random() > 0.7:
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
                        r = risk_rank(self.rank,line_rank[t])
                        best_rank = risk_rank(self.rank,line_rank[school_list.index(low_risk_school[best])])
                        if 0 < int(low_school_rank_list[j]) < int(
                                low_school_rank_list[best]):
                            best = j
                        if int(low_school_rank_list[j]) == 0 and r < best_rank:
                            best = j
                    if int(low_school_rank_list[best]) != 100000:
                        result_high_risk_school.append(low_risk_school[best])
                        low_school_rank_list[best] = 100000
                        '''
        else:
            # for i in range(3):
            a = 0 #记录有几个学校没被用到
            for i in range(len(high_school_rank_list)):
                if high_school_rank_list[i] != 100000:
                    a += 1
            if  a >=3:
                while len(result_high_risk_school) < 3:
                    best = 0
                    #print(high_school_rank_list)
                    for j in range(len(high_risk_school)):
                        if int(high_school_rank_list[j]) != 100000:
                            best = j
                            break
                    for j in range(len(high_risk_school)):
                        if int(high_school_rank_list[j]) != 100000:
                            t = school_list.index(high_risk_school[j])
                            r = risk_rank(self.rank, line_rank[t])
                            if r > risk_rank(self.rank, line_rank[school_list.index(high_risk_school[best])]) and random.random()>0.3:
                                best = j
                    result_high_risk_school.append(high_risk_school[best])
                    high_school_rank_list[best] = 100000
            else:
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
                            if int(normal_school_rank_list[j]) != 100000:
                                best = j
                                break
                        # 如果都被使用了，则换下一个
                        if best == 0 and int(normal_school_rank_list[best]) == 100000:
                            break

                        for j in range(len(normal_risk_school)):
                            if int(normal_school_rank_list[j]) != 100000:
                                t = school_list.index(normal_risk_school[j])
                                r = risk_rank(self.rank, line_rank[t])
                                best_rank = risk_rank(self.rank, line_rank[school_list.index(normal_risk_school[best])])
                                if int(normal_school_rank_list[j]) > 0 and 0.2 * r + 10 * int(
                                        normal_school_rank_list[j]) > \
                                        0.2 * best_rank + 10 * int(normal_school_rank_list[best]) and random.random() > 0.3:
                                    best = j
                                if int(normal_school_rank_list[j]) == 0 and r > best_rank and random.random() > 0.5:
                                    best = j
                        if int(normal_school_rank_list[best]) != 100000:
                            result_high_risk_school.append(normal_risk_school[best])
                            normal_school_rank_list[best] = 100000
                            N += 1
                if N < 3 and len(low_risk_school) > 0:
                    for i in range(3 - N):
                        best = 0

                        for j in range(len(low_risk_school)):
                            if int(low_school_rank_list[j]) != 100000:
                                best = j
                                break

                        for j in range(len(low_risk_school)):
                            if int(low_school_rank_list[j]) != 100000:
                                t = school_list.index(low_risk_school[j])
                                r = risk_rank(self.rank, line_rank[t])
                                best_rank = risk_rank(self.rank, line_rank[school_list.index(low_risk_school[best])])
                                if int(low_school_rank_list[j]) > int(
                                        low_school_rank_list[best]) >= 0 and random.random() > 0.4:
                                    best = j
                                if int(low_school_rank_list[j]) == 0 and r > best_rank and random.random() > 0.5:
                                    best = j
                        if int(low_school_rank_list[best]) != 100000:
                            result_high_risk_school.append(low_risk_school[best])
                            low_school_rank_list[best] = 100000



        if len(low_risk_school) == 3:
            for i in range(len(low_risk_school)):
                if low_school_rank_list[i] != 100000:
                    result_low_risk_school.append(low_risk_school[i])
                    low_school_rank_list[i] = 100000

            if len(result_low_risk_school) < 3:
                N = len(result_low_risk_school)
                if len(normal_risk_school) > 0:
                    for i in range(3 - N):
                        best = 0
                        #先取一个没有被选中的作为起始best
                        for j in range(len(normal_risk_school)):
                            if int(normal_school_rank_list[j]) != 100000:
                                best = j
                                break
                        #如果都被使用了，则换下一个
                        if best == 0 and int(normal_school_rank_list[best]) == 100000:
                            break
                        #筛选最佳
                        for j in range(len(normal_risk_school)):
                            if int(normal_school_rank_list[j]) != 100000:
                                t = school_list.index(normal_risk_school[j])
                                r = risk_rank(self.rank,line_rank[t])
                                best_rank = risk_rank(self.rank,line_rank[school_list.index(normal_risk_school[best])])
                                if int(normal_school_rank_list[j]) > 0 and 0.2 * r + 10 * int(
                                        normal_school_rank_list[j]) < \
                                        0.2 * best_rank + 10 * int(normal_school_rank_list[best]) and random.random() > 0.3:
                                    best = j
                                if int(normal_school_rank_list[j]) == 0 and r < best_rank and random.random() > 0.5:
                                    best = j

                        if int(normal_school_rank_list[best]) != 100000:
                            result_low_risk_school.append(normal_risk_school[best])
                            normal_school_rank_list[best] = 100000
                            N += 1

                if N < 3 and len(high_risk_school) > 0:
                    for i in range(3 - N):
                        best = 0

                        for j in range(len(high_risk_school)):
                            if int(high_school_rank_list[j]) != 100000:
                                best = j
                                break

                        for j in range(len(high_risk_school)):
                            if int(high_school_rank_list[j]) != 100000:
                                t = school_list.index(high_risk_school[j])
                                r = risk_rank(self.rank,line_rank[t])
                                best_rank = risk_rank(self.rank,line_rank[school_list.index(high_risk_school[best])])
                                if r < best_rank and int(high_school_rank_list[j]) != 100000 and random.random() > 0.5:
                                    best = j
                        result_low_risk_school.append(high_risk_school[best])
                        high_school_rank_list[best] = 100000

        elif len(low_risk_school) < 3:

            N = 0
            for i in range(len(low_risk_school)):
                if low_school_rank_list[i] != 100000:
                    result_low_risk_school.append(low_risk_school[i])
                    low_school_rank_list[i] = 100000
                    N += 1

            #print(N)

            if len(normal_risk_school) > 0:
                for i in range(3 - N):

                    #print(normal_school_rank_list)

                    best = 0
                    # 先取一个没有被选中的作为起始best
                    for j in range(len(normal_risk_school)):
                        if int(normal_school_rank_list[j]) != 100000:
                            best = j
                            break
                    # 如果都被使用了，则换下一个
                    if best == 0 and int(normal_school_rank_list[best]) == 100000:
                        break
                    # 筛选最佳
                    for j in range(len(normal_risk_school)):
                        if int(normal_school_rank_list[j]) != 100000:
                            t = school_list.index(normal_risk_school[j])
                            r = risk_rank(self.rank, line_rank[t])
                            best_rank = risk_rank(self.rank, line_rank[school_list.index(normal_risk_school[best])])
                            if int(normal_school_rank_list[j]) > 0 and 0.2 * r + 10 * int(
                                    normal_school_rank_list[j]) < \
                                    0.2 * best_rank + 10 * int(normal_school_rank_list[best]) and random.random() > 0.2:
                                best = j
                            if int(normal_school_rank_list[j]) == 0 and r < best_rank and random.random() > 0.4:
                                best = j

                    if int(normal_school_rank_list[best]) != 100000:
                        result_low_risk_school.append(normal_risk_school[best])
                        normal_school_rank_list[best] = 100000
                        N += 1
                    #print(normal_school_rank_list)

            if N < 3 and len(high_risk_school) > 0:
                for i in range(3 - N):
                    best = 0

                    for j in range(len(high_risk_school)):
                        if int(high_school_rank_list[j]) != 100000:
                            best = j
                            break

                    for j in range(len(high_risk_school)):
                        if int(high_school_rank_list[j]) != 100000:
                            t = school_list.index(high_risk_school[j])
                            r = risk_rank(self.rank, line_rank[t])
                            best_rank = risk_rank(self.rank, line_rank[school_list.index(high_risk_school[best])])
                            if r < best_rank and int(high_school_rank_list[j]) != 100000 and random.random() > 0.2:
                                best = j
                    result_low_risk_school.append(high_risk_school[best])
                    high_school_rank_list[best] = 100000
            '''
            if len(normal_risk_school) > 0:
                for i in range(3 - N):
                    best = 0
                    for j in range(len(normal_risk_school)):
                        t = school_list.index(normal_risk_school[j])
                        r = risk_rank(self.rank,line_rank[t])
                        best_rank = risk_rank(self.rank,line_rank[school_list.index(normal_risk_school[best])])
                        if int(normal_school_rank_list[j]) != 100000 and int(normal_school_rank_list[j]) > 0 and 0.2 * r + 10 * int(
                                normal_school_rank_list[j]) < \
                                0.2 * best_rank + 10 * int(normal_school_rank_list[best]) or random.random()>0.7:
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
                        r = risk_rank(self.rank,line_rank[t])
                        best_rank =risk_rank(self.rank,line_rank[school_list.index(high_risk_school[best])])
                        if r < best_rank and int(high_school_rank_list[j]) != 100000:
                            best = j
                    result_low_risk_school.append(high_risk_school[best])
                    high_school_rank_list[best] = 100000
                    '''
        else:
            #print('yes')
            # for i in range(3):
            a = 0
            for i in range(len(low_risk_school)):
                if low_school_rank_list[i] != 100000:
                    a+=1
            if a >= 3:
                while len(result_low_risk_school) < 3:
                    best = 0
                    for j in range(len(low_risk_school)):
                        if int(low_school_rank_list[j]) != 100000:
                            best = j
                            break
                    #print(best)
                    for j in range(len(low_risk_school)):
                        if int(low_school_rank_list[j]) != 100000:
                            t = school_list.index(low_risk_school[j])
                            r = risk_rank(self.rank, line_rank[t])
                            if r > risk_rank(self.rank, line_rank[school_list.index(low_risk_school[best])]) and random.random() > 0.4:
                                best = j
                    if int(low_school_rank_list[best]) != 100000:
                        result_low_risk_school.append(low_risk_school[best])
                        low_school_rank_list[best] = 100000
            else:
                N = 0
                for i in range(len(low_risk_school)):
                    if low_school_rank_list[i] != 100000:
                        result_low_risk_school.append(low_risk_school[i])
                        low_school_rank_list[i] = 100000
                        N += 1

                # print(N)

                if len(normal_risk_school) > 0:
                    for i in range(3 - N):

                        # print(normal_school_rank_list)

                        best = 0
                        # 先取一个没有被选中的作为起始best
                        for j in range(len(normal_risk_school)):
                            if int(normal_school_rank_list[j]) != 100000:
                                best = j
                                break
                        # 如果都被使用了，则换下一个
                        if best == 0 and int(normal_school_rank_list[best]) == 100000:
                            break
                        # 筛选最佳
                        for j in range(len(normal_risk_school)):
                            if int(normal_school_rank_list[j]) != 100000:
                                t = school_list.index(normal_risk_school[j])
                                r = risk_rank(self.rank, line_rank[t])
                                best_rank = risk_rank(self.rank, line_rank[school_list.index(normal_risk_school[best])])
                                if int(normal_school_rank_list[j]) > 0 and 0.2 * r + 10 * int(
                                        normal_school_rank_list[j]) < \
                                        0.2 * best_rank + 10 * int(normal_school_rank_list[best]) and random.random() > 0.2:
                                    best = j
                                if int(normal_school_rank_list[j]) == 0 and r < best_rank and random.random()>0.5:
                                    best = j

                        if int(normal_school_rank_list[best]) != 100000:
                            result_low_risk_school.append(normal_risk_school[best])
                            normal_school_rank_list[best] = 100000
                            N += 1
                        # print(normal_school_rank_list)

                if N < 3 and len(high_risk_school) > 0:
                    for i in range(3 - N):
                        best = 0

                        for j in range(len(high_risk_school)):
                            if int(high_school_rank_list[j]) != 100000:
                                best = j
                                break

                        for j in range(len(high_risk_school)):
                            if int(high_school_rank_list[j]) != 100000:
                                t = school_list.index(high_risk_school[j])
                                r = risk_rank(self.rank, line_rank[t])
                                best_rank = risk_rank(self.rank, line_rank[school_list.index(high_risk_school[best])])
                                if r < best_rank and int(high_school_rank_list[j]) != 100000 and random.random() > 0.2:
                                    best = j
                        result_low_risk_school.append(high_risk_school[best])
                        high_school_rank_list[best] = 100000

        #print(result_low_risk_school)
        # 中等风险学校
        if len(normal_risk_school) == 4:  # 中风险度
            for i in range(len(normal_risk_school)):
                if normal_school_rank_list[i] != 100000:
                    result_mid_risk_school.append(normal_risk_school[i])
                    normal_school_rank_list[i] = 100000

            if len(result_mid_risk_school) < 4:
                N = len(result_mid_risk_school)
                if len(high_risk_school) > 0:
                    for i in range(4 - N):
                        best = 0

                        for j in range(len(high_risk_school)):
                            if int(high_school_rank_list[j]) != 100000:
                                best = j
                                break
                        # 如果都被使用了，则换下一个
                        if best == 0 and int(high_school_rank_list[best]) == 100000:
                            break

                        for j in range(len(high_risk_school)):
                            if int(high_school_rank_list[j]) != 100000:
                                t = school_list.index(high_risk_school[j])
                                r = risk_rank(self.rank,line_rank[t])
                                best_rank = risk_rank(self.rank,line_rank[school_list.index(high_risk_school[best])])
                                if r > best_rank and int(high_school_rank_list[j]) != 100000 and random.random() > 0.2:
                                    best = j
                        result_mid_risk_school.append(high_risk_school[best])
                        high_school_rank_list[best] = 100000
                        N += 1

                if N < 4 and len(low_risk_school) > 0:
                    for i in range(4 - N):
                        best = 0

                        for j in range(len(low_risk_school)):
                            if int(low_school_rank_list[j]) != 100000:
                                best = j
                                break

                        for j in range(len(low_risk_school)):
                            if int(low_school_rank_list[j]) !=100000:
                                t = school_list.index(low_risk_school[j])
                                r = risk_rank(self.rank,line_rank[t])
                                best_rank = risk_rank(self.rank,line_rank[school_list.index(low_risk_school[best])])
                                if 0 < int(low_school_rank_list[j]) < int(
                                        low_school_rank_list[best]):
                                    best = j
                                if int(low_school_rank_list[j]) == 0 and r > best_rank and random.random() > 0.3:
                                    best = j

                        if int(low_school_rank_list[best]) != 100000:
                            result_mid_risk_school.append(low_risk_school[best])
                            low_school_rank_list[best] = 100000

        elif len(normal_risk_school) < 4:
            #print('yes')
            N = 0
            for i in range(len(normal_risk_school)):
                if normal_school_rank_list[i] != 100000:
                    result_mid_risk_school.append(normal_risk_school[i])
                    normal_school_rank_list[i] = 100000
                    N += 1

            if len(high_risk_school) > 0:
                for i in range(4 - N):
                    best = 0

                    for j in range(len(high_risk_school)):
                        if int(high_school_rank_list[j]) != 100000:
                            best = j
                            break
                    # 如果都被使用了，则换下一个
                    if best == 0 and int(high_school_rank_list[best]) == 100000:
                        break

                    for j in range(len(high_risk_school)):
                        if int(high_school_rank_list[j]) != 100000:
                            t = school_list.index(high_risk_school[j])
                            r = risk_rank(self.rank, line_rank[t])
                            best_rank = risk_rank(self.rank, line_rank[school_list.index(high_risk_school[best])])
                            if r < best_rank and int(high_school_rank_list[j]) != 100000 and random.random() > 0.2:
                                best = j
                    result_mid_risk_school.append(high_risk_school[best])
                    high_school_rank_list[best] = 100000
                    N += 1

            if N < 4 and len(low_risk_school) > 0:
                for i in range(4 - N):
                    best = 0

                    for j in range(len(low_risk_school)):
                        if int(low_school_rank_list[j]) != 100000:
                            best = j
                            break

                    for j in range(len(low_risk_school)):
                        if int(low_school_rank_list[j]) != 100000:
                            t = school_list.index(low_risk_school[j])
                            r = risk_rank(self.rank, line_rank[t])
                            best_rank = risk_rank(self.rank, line_rank[school_list.index(low_risk_school[best])])
                            if 0 < int(low_school_rank_list[j]) < int(
                                    low_school_rank_list[best]) and random.random() > 0.2:
                                best = j
                            if int(low_school_rank_list[j]) == 0 and r > best_rank and random.random() > 0.3:
                                best = j

                    if int(low_school_rank_list[best]) != 100000:
                        result_mid_risk_school.append(low_risk_school[best])
                        low_school_rank_list[best] = 100000

            '''
            if len(high_risk_school) > 0:
                for i in range(4 - N):
                    best = 0
                    for j in range(len(high_risk_school)):
                        t = school_list.index(high_risk_school[j])
                        r = risk_rank(self.rank,line_rank[t])
                        best_rank = risk_rank(self.rank,line_rank[school_list.index(high_risk_school[best])])
                        if (r < best_rank or random.random() > 0.7) and int(high_school_rank_list[j]) != 100000  :
                            best = j
                    result_mid_risk_school.append(high_risk_school[best])
                    high_school_rank_list[best] = 100000
                    N += 1
            if N < 4 and len(low_risk_school) > 0:
                for i in range(4 - N):
                    best = 0
                    for j in range(len(low_risk_school)):
                        t = school_list.index(low_risk_school[j])
                        r = risk_rank(self.rank,line_rank[t])
                        best_rank = risk_rank(self.rank,line_rank[school_list.index(low_risk_school[best])])
                        if 0 < int(low_school_rank_list[j]) < int(
                                low_school_rank_list[best]):
                            best = j
                        if int(low_school_rank_list[j]) == 0 and r < best_rank or random.random() >0.7:
                            best = j
                    if int(low_school_rank_list[best]) != 100000:
                        result_mid_risk_school.append(low_risk_school[best])
                        low_school_rank_list[best] = 100000
                        '''
        else:
            #print(normal_school_rank_list)
            #print('yes')
            # for i in range(3):
            a = 0
            for i in range(len(normal_school_rank_list)):
                if normal_school_rank_list[i] != 100000:
                    a += 1
            if a >= 4:
                while len(result_mid_risk_school) < 4:
                    #print(normal_school_rank_list)
                    best = 0
                    for j in range(len(normal_risk_school)):
                        if int(normal_school_rank_list[j]) != 100000:
                            best = j
                            break
                    #print(best)


                    for j in range(len(normal_risk_school)):
                        if int(normal_school_rank_list[j]) != 100000:
                            t = school_list.index(normal_risk_school[j])
                            r = risk_rank(self.rank, line_rank[t])
                            if r > risk_rank(self.rank, line_rank[school_list.index(normal_risk_school[best])]) and random.random() > 0.2:
                                best = j
                    if int(normal_school_rank_list[best]) != 100000:
                        result_mid_risk_school.append(normal_risk_school[best])
                        normal_school_rank_list[best] = 100000
            else:
                N = 0
                for i in range(len(normal_risk_school)):
                    if normal_school_rank_list[i] != 100000:
                        result_mid_risk_school.append(normal_risk_school[i])
                        normal_school_rank_list[i] = 100000
                        N += 1

                if len(high_risk_school) > 0:
                    for i in range(4 - N):
                        best = 0

                        for j in range(len(high_risk_school)):
                            if int(high_school_rank_list[j]) != 100000:
                                best = j
                                break
                        # 如果都被使用了，则换下一个
                        if best == 0 and int(high_school_rank_list[best]) == 100000:
                            break

                        for j in range(len(high_risk_school)):
                            if int(high_school_rank_list[j]) != 100000:
                                t = school_list.index(high_risk_school[j])
                                r = risk_rank(self.rank, line_rank[t])
                                best_rank = risk_rank(self.rank, line_rank[school_list.index(high_risk_school[best])])
                                if r < best_rank and int(high_school_rank_list[j]) != 100000:
                                    best = j
                        result_mid_risk_school.append(high_risk_school[best])
                        high_school_rank_list[best] = 100000
                        N += 1

                if N < 4 and len(low_risk_school) > 0:
                    for i in range(4 - N):
                        best = 0

                        for j in range(len(low_risk_school)):
                            if int(low_school_rank_list[j]) != 100000:
                                best = j
                                break

                        for j in range(len(low_risk_school)):
                            if int(low_school_rank_list[j]) != 100000:
                                t = school_list.index(low_risk_school[j])
                                r = risk_rank(self.rank, line_rank[t])
                                best_rank = risk_rank(self.rank, line_rank[school_list.index(low_risk_school[best])])
                                if 0 < int(low_school_rank_list[j]) < int(
                                        low_school_rank_list[best]):
                                    best = j
                                if int(low_school_rank_list[j]) == 0 and r > best_rank:
                                    best = j

                        if int(low_school_rank_list[best]) != 100000:
                            result_mid_risk_school.append(low_risk_school[best])
                            low_school_rank_list[best] = 100000

        list_add = result_high_risk_school + result_mid_risk_school + result_low_risk_school
        school_score = []

        dict_score = {}
        current_value = 0
        #对list_add排序
        for i in list_add:
            #print(i)
            current = temp_list[school_list.index(i)]
            #print(current)
            n=0 #记录有几年数据
            for year in range(int(self.year) - 5, int(self.year)):

                # print(year)
                year_store = 0
                for j in current:
                    if int(j[0]) == year:
                        # print(year)
                        if j[2] is None or j[2] == 0:
                            year_store =  0
                        else:
                            year_store = int(float(j[2]))
                            n += 1
                            #print(n)
                current_value += year_store
                #print(current_value)

                if year == int(self.year) -1 and n != 0:
                    current_value = current_value/n
                elif year == int(self.year) -1 and n == 0:
                    current_value = 0
                #print(current_value)

            dict_score[i] = current_value
            current_value = 0
        new_dict_score = sorted(dict_score.items(), key=lambda e:e[1], reverse=True)
        #print(new_dict_score)
        #print(list_add)
        new_list_score = []
        for i in range(len(new_dict_score)):
            new_list_score.append(new_dict_score[i][0])
        #print(new_list_score)

        result_high_risk_school =new_list_score[0:3]
        result_mid_risk_school = new_list_score[3:7]
        result_low_risk_school = new_list_score[7:10]

        if new_list_score is not None or list_add != []:

            for i in new_list_score:
                a = []  # 记录该学校的近三年平均分
                current = temp_list[school_list.index(i)]
                # print(current)
                for year in range(int(self.year) - 3, int(self.year)):
                    # print(year)
                    year_store = [year, None]
                    for j in current:
                        if int(j[0]) == year:
                            # print(year)
                            if j[2] is None or j[2] == 0:
                                year_store = [year, None]
                            else:
                                year_store = [year, int(float(j[2]))]
                    a.append(year_store)
                school_score.append(a)
        else:
            school_score = []
        e5 = time.clock()

        # print(e5-e4)#
        # print(e4-e3)
        # print(e3-e2)
        # print(e2-e1)
        # print(e1-s)

        return result_high_risk_school, result_mid_risk_school, result_low_risk_school, school_score
