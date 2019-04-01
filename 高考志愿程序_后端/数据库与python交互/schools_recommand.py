from getRisk import getRisk
from DB_handler import DB_handler
from DB_methods import DB_methods
import pymysql
import random
#加载本地
provinceID_dictionary={}
with open ('provinceid.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        line=line.strip('\n')
        provinceID_dictionary[line.split(',')[0]]=line.split(',')[1]
#数据库连接
conn = pymysql.connect()
cursor = conn.cursor()

class recommand():
    def __init__(self, user_ID):
        self.DBh = DB_handler()
        self.DBm = DB_methods()
        self.getRisk = getRisk(user_ID)
        self.user = user_ID
        self.score = str(self.DBh.select(['client'], ['score'], ['user_ID =' + user_ID]))
        self.year = str(self.DBh.select(['client'], ['year'], ['user_ID =' + user_ID]))
        self.rank = self.DBh.select(['client'], ['self_rank'], ['user_ID =' + user_ID])
        provinceID = str(self.DBh.select(['client'], ['province'], ['user_ID =' + user_ID]))
        self.province = str(provinceID_dictionary[provinceID])

        self.subject = self.DBh.select(['client'], ['subject'], ['user_ID =' + user_ID])


        pici = str(self.DBh.select(['client'], ['pici'], ['user_ID =' + user_ID]))



    def schools_recommand(self):
        # 对所有专业

        result_low_risk_school = []

        result_high_risk_school = []

        result_mid_risk_school = []

        school_list = []
        temp = []


        val = [self.province,self.subject,'sci-li']
        for year in range(int(self.year)-5,int(self.year)):
            val.append(year)
        db_school_list = "select schoolID, year, pici, lowest_score, avg_score, highest_score " \
                         "from school" + " where provinceID= %s"  + " and (subject=" + ' %s '+'or ' +'subject=%s )'+' and (year= %s or year=%s or year=%s or year=%s or year=%s)'
        print(db_school_list)
        print(val)
        cursor.execute(db_school_list,val)
        conn.commit()

        temp.append(cursor.fetchall()) #temp = [((schoolID,year,pici,ls,as,hs),()...)]
        #搜索分数线在考生附近的学校

        N = 1601
        avg_score_avg = [0 for i in range(N)]
        lowest_score_avg = [0 for i in range(N)]
        highest_score_avg = [0 for i in range(N)]
        n = 1  # 计数，学校
        j = 0  # 计数，最低分数据个数
        k = 0  # 计数，最高分数据个数
        m = 0  # 计数，平均分数据个数
        for i in range(len(temp[0])):
            # 因许多省份改革，只取2014以后数据
            if int(temp[0][i][1]) == int(self.year)-1 or int(temp[0][i][1]) == int(self.year)-2 or int(temp[0][i][1]) == int(self.year)-3 or \
                    int(temp[0][i][1]) == int(self.year)-4 or int(temp[0][i][1]) == int(self.year)-5:
                # 若是同一所学校
                if temp[0][i][0] == n:
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
                    n = temp[0][i][0]

        for i in range(len(lowest_score_avg)):  # 取上下十分
            if lowest_score_avg[i] and highest_score_avg[i]:
                if min(avg_score_avg[i], lowest_score_avg[i]) - 15 <= int(self.score) <= max(avg_score_avg[i],
                                                                                        highest_score_avg[i]) + 20:
                    school_list.append(i)
            else:
                if avg_score_avg[i] - 15 <= int(self.score) <= avg_score_avg[i] + 20:
                    school_list.append(i)
        print(school_list)
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
        '''
        # 已获得对应的学校列表，现在只需要对风险度进行排序即可。
        school_and_rank = []
        for school in school_list:
            line_rank = []
            avg_rank_store = []
            for year in range(int(self.year) - 5, int(self.year)):
                newconditionlist = ['schoolID=' + school,
                                 'provinceID= ' + self.province,
                                 'year=' + str(year)]
                store = self.DBh.select(['school'], ['avg_score'], newconditionlist, [['subject', self.subject, 'sci-li']])
                for avg_rank in store:
                    line_rank.append(avg_rank)
            school_and_rank.append(line_rank)

            if self.getRisk.risk_level(line_rank) == 0:
                low_risk_school.append(school)
            if self.getRisk.risk_level(line_rank) == 1:
                mid_risk_school.append(school)
            if self.getRisk.risk_level(line_rank) == 2:
                high_risk_school.append(school)
        '''
        #原方法
        high_risk_school = []
        normal_risk_school = []
        low_risk_school = []
        temp_list = []
        low_school_rank_list = []
        normal_school_rank_list = []
        high_school_rank_list = []

        for i in school_list:
            db_list = "select year, pici, lowest_score, avg_score, highest_score, avg_rank " \
                      "from school where schoolID= %s and provinceID= %s and (subject= %s or subject = %s)"
            val = [i,self.province,self.subject,'sci-li']
            cursor.execute(db_list,val)
            conn.commit()
            temp_list.append(cursor.fetchall())

        line_rank = [[] for i in range(len(school_list))]

        for i in range(len(school_list)):
            for j in range(len(temp_list[i])):
                if temp_list[i][j][5]:
                    line_rank[i].append(temp_list[i][j][5])
        print(line_rank)
        print(len(line_rank))

        for i in range(len(school_list)):
            if self.getRisk.risk_level(line_rank[i]) == 0:
                low_risk_school.append(school_list[i])
            if self.getRisk.risk_level( line_rank[i]) == 1:
                normal_risk_school.append(school_list[i])
            if self.getRisk.risk_level(line_rank[i]) == 2:
                high_risk_school.append(school_list[i])
        print('low:')
        print(low_risk_school)
        print('avg')
        print(normal_risk_school)
        print('high')
        print(high_risk_school)
        # 此处应排序，按学校排名学科排名和风险值综合考量对三个数组进行排序，只保留前几个结果
        for i in range(len(low_risk_school)):
            low_school_rank = self.DBh.select(['gaokaowang_schoolname'],['school_rank'],['ID='+str(low_risk_school[i])])
            #print(low_school_rank)

            low_school_rank_list.append(low_school_rank)
        print(low_school_rank_list)
        for i in range(len(normal_risk_school)):
            normal_school_rank = self.DBh.select(['gaokaowang_schoolname'],['school_rank'],['ID='+str(normal_risk_school[i])])

            normal_school_rank_list.append(normal_school_rank)
        for i in range(len(high_risk_school)):
            high_school_rank = self.DBh.select(['gaokaowang_schoolname'],['school_rank'],['ID='+str(high_risk_school[i])])

            high_school_rank_list.append(high_school_rank)

        #主义是从哪里读取的排名

        # 分三个表存储高中低风险。school_and_rank存储的是每个学校对应的近几年平均分数对应的排名。
        if len(low_risk_school) <= 3:
            for i in low_risk_school:
                result_low_risk_school.append(i)

        else:
            for i in range(3):
                best = 0
                for j in range(len(low_risk_school)):
                    t = school_list.index(low_risk_school[j])
                    r = self.getRisk.risk_rank(line_rank[t])  # school_list 中学校的序号和 school_and_list 中序号一致。
                    if int(low_school_rank_list[j]) > 0 and 0.1 * r + 10 * int(low_school_rank_list[j]) < \
                            0.1 * r + 10 * int(low_school_rank_list[best]) and random.random() >= 0.7:
                        best = j
                if int(low_school_rank_list[best]) != 10000 and int(low_school_rank_list[best]) != 0:
                    result_low_risk_school.append(low_risk_school[best])
                    low_school_rank_list[best] = 10000

        if len(normal_risk_school) <= 4:  # 中风险度
            for i in normal_risk_school:
                result_mid_risk_school.append(i)

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
                if int(normal_school_rank_list[best]) != 10000 and int(
                        normal_school_rank_list[best]) != 0:
                    result_mid_risk_school.append(normal_risk_school[best])
                    normal_school_rank_list[best] = 10000

        if len(high_risk_school) <= 3:
            for i in high_risk_school:
                result_high_risk_school.append(i)

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
                if int(high_school_rank_list[best]) != 10000 and int(
                        high_school_rank_list[best]) != 0:
                    result_high_risk_school.append(high_risk_school[best])
                    high_school_rank_list[best] = 10000
        return result_high_risk_school, result_mid_risk_school, result_low_risk_school
