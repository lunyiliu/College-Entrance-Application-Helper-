from DB_handler import DB_handler
from DB_methods import DB_methods
import numpy
import pymysql
import random
from getRank import getRank
provinceID_dictionary={}
with open ('provinceid.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        line=line.strip('\n')
        provinceID_dictionary[line.split(',')[0]]=line.split(',')[1]

class getRisk():

    def __init__(self,user_ID):
        self.DBh = DB_handler()
        self.DBm = DB_methods()
        self.user = user_ID
        store = self.score = str(self.DBh.select(['client'], ['score','province','subject','year','pici','choose_list',], ['user_ID =' + user_ID]))

        self.score = str(self.DBh.select(['client'], ['score'], ['user_ID =' + user_ID]))
        province = str(self.DBh.select(['client'], ['province'], ['user_ID =' + user_ID]))
        self.provinceID = str(provinceID_dictionary[province])
        self.subject = self.DBh.select(['client'], ['subject'], ['user_ID =' + user_ID])
        self.year = str(self.DBh.select(['client'], ['year'], ['user_ID =' + user_ID]))
        self.pici = str(self.DBh.select(['client'], ['pici'], ['user_ID =' + user_ID]))
        self.intension_list = []
        self.mid_list = self.DBh.select(['client'], ['choose_list'], ['user_ID =' + user_ID])[:-1].split(',')
        for element in self.mid_list:
            self.intension_list.append(element[:-1].split('.'))
        self.rank = self.DBh.select(['client'], ['self_rank'], ['user_ID =' + user_ID])
        self.getRank = getRank(user_ID)

    def risk_rank_school(self,i):#i代表第几个志愿
        school = self.intension_list[i][0]
        current_year = int(self.year)
        line_rank = []
        for year in range(current_year-5,current_year):
            conditionlist = ['schoolID='+school,
                             'provinceID='+self.provinceID,
                             'year='+str(year),
                             'subject ='+self.subject,
                             'pici='+self.pici]
            avgrank = self.DBh.select(['school'],['lowest_rank'],conditionlist,para_debug=True)
            print(avgrank)
            if avgrank is not None:
                if type(avgrank) is list:
                    for avg in avgrank:
                        line_rank.append(avg)
                else:
                    line_rank.append(avgrank)
        N = 0  # 超过分数线排名年数
        # last1为最近一年，last2为last1前一年
        for i in range(len(line_rank)):
            if self.rank <= line_rank[i]:
                N = N + 1
        if N <= 2/5 * len(line_rank):
            r = 500
        else:
            if N > 4/5 *len(line_rank):
                r = 0
            else:
                r = 100
        print(line_rank)
        last1 = self.rank - line_rank[-1]
        last2 = self.rank - line_rank[-2]
        avg = self.rank - sum(line_rank) / len(line_rank)
        if (line_rank[-1] >= line_rank[-2]) and (line_rank[-2] >= sum(line_rank) / len(line_rank)):  # 若有下降趋势
            Risk = 0.3 * (0.2 * last1 + 0.2 * last2 + 0.4 / 3 * avg) + r  # 近两年各占0.3权值，其余年份共占0.4
        else:
            if (numpy.std(line_rank) / (sum(line_rank) / len(line_rank))) <= 0.2:  # 以差异系数来确定稳定程度
                Risk = 0.3 * avg + r
            else:
                Risk = 0.3 * max(avg, last1, last2) + r
        return Risk

    def get_success_school(self):
        success_result = []

        rank_list,count_of_users = self.getRank.get_rank_school()

        for i in range(len(self.intension_list)):
            N = self.get_risk_level_school(i) #N代表风险数
            rank = rank_list[i]#对一个学校的6个排名
            count = count_of_users[i]#一个学校6个总人数
            success = 0
            for j in range(len(rank)):
                if j <2:#前1,2个
                    success += 0.1*(1-rank[j]/count[j])
                elif j>4:#第6个
                    success += 0.1*(1-rank[j]/count[j])
                else:
                    success += 0.3*(1-rank[j]/count[j])
            # 人数影响权重
            if sum(count) >200:
                beta = 0.3
            else:
                beta = 1-0.3*(200-sum(count))
            success += beta*N
            success_result.append(success)
        return success_result

    def get_success_profession(self):
        success_result = []

        rank_list, count_of_users = self.getRank.get_rank_profession()
        for i in range(len(rank_list)):#学校
            success_of_profession = []#学校里的专业排名
            for j in range(len(rank_list[i])-1):#专业
                serial = j + 1
                N = self.get_risk_level_profession(i,serial)

                rank = rank_list[i][serial]
                count = count_of_users[i][serial]
                success = 0
                for k in range(len(rank)):
                    if k < 2:  # 前1,2个
                        success += 0.1 * (1 - rank[k] / count[k])
                    elif k > 4:  # 第6个
                        success += 0.3 * (1 - rank[k] / count[k])
                    else:
                        success += 0.1 * (1 - rank[k] / count[k])
                # 人数影响权重
                if sum(count) > 200:
                    beta = 0.3
                else:
                    beta = 1 - 0.3 * (200 - sum(count))
                success += beta * N
                success_of_profession.append(success)
            success_result.append(success_of_profession)
        return success_result

    def risk_rank_profession(self,i,j):#i代表学校，j代表专业
        profession_ID = self.intension_list[i][j]
        current_year = int(self.year)
        line_rank = []
        majors_province = self.DBh.select(['provinceid'],['省份'],['ID = '+self.provinceID])
        if self.pici == '0':
            pici = '提前批'
        elif self.pici == '1':
            pici = '第一批'
        elif self.pici == '2':
            pici = '第二批'
        else:
            pici = '第三批'
        school,profession = self.DBh.select(['majors_ID'],['学校名称','专业名称'],['id='+profession_ID])

        if self.subject == 'science':
            subject = '理科'
        elif self.subject == 'literature':
            subject= '文科'
        elif self.subject == 'sci-li':
            subject = '文理不分'


        for year in range(current_year - 5, current_year):
            conditionlist = ['专业名称 ='+profession,
                             '学校名称=' + school,
                             '省份=' + majors_province,
                             '年份=' + str(year),
                             '批次=' + pici] #
            avgrank = self.DBh.select(['majors_copy'], ['rank'], conditionlist,[['科类','文理不分',subject]],para_debug=True) #修改这里。主要是要 majors里有rank栏
            print(avgrank)
            if avgrank is not None:
                if type(avgrank) is list:
                    for avg in avgrank:
                        line_rank.append(avg)
                else:
                    line_rank.append(avgrank)
        N = 0  # 超过分数线排名年数
        # last1为最近一年，last2为last1前一年
        for i in range(len(line_rank)):
            if self.rank <= line_rank[i]:
                N = N + 1
        if N <= 2/5 * len(line_rank):
            r = 500
        else:
            if N >4/5 * len(line_rank):
                r = 0
            else:
                r = 100
        last1 = self.rank - line_rank[-1]
        last2 = self.rank - line_rank[-2]
        avg = self.rank - sum(line_rank) / len(line_rank)
        if (line_rank[-1] >= line_rank[-2]) and (line_rank[-2] >= sum(line_rank) / len(line_rank)):  # 若有下降趋势
            Risk = 0.3 * (0.2 * last1 + 0.2 * last2 + 0.4 / 3 * avg) + r  # 近两年各占0.3权值，其余年份共占0.4
        else:
            if (numpy.std(line_rank) / (sum(line_rank) / len(line_rank))) <= 0.2:  # 以差异系数来确定稳定程度
                Risk = 0.3 * avg + r
            else:
                Risk = 0.3 * max(avg, last1, last2) + r
        return Risk

    def get_risk_level_school(self,i):
        r = self.risk_rank_school(i)
        if r >= 500:
            return 2
        else:
            if r <= -200:
                return 0
            else:
                return 1

    def get_risk_level_profession(self,i,j):
        r = self.risk_rank_profession(i,j)
        if r >= 500:
            return 2
        else:
            if r <= -200:
                return 0
            else:
                return 1

    def risk_rank(self, line_rank):
        N = 0  # 超过分数线排名年数
        # last1为最近一年，last2为last1前一年
        for i in range(len(line_rank)):
            if self.rank <= line_rank[i]:
                N = N + 1
        if N <= 2:
            r = 500
        else:
            if N == len(line_rank):
                r = 0
            else:
                r = 100

        last1 = self.rank - line_rank[0]
        if len(line_rank) == 1:
            last2 = last1
        else:
            last2 = self.rank - line_rank[1]
        avg = self.rank - sum(line_rank) / len(line_rank)
        if len(line_rank)==1 or ((line_rank[0] >= line_rank[1]) and (line_rank[1] >= sum(line_rank) / len(line_rank))):  # 若有下降趋势
            Risk = 0.3 * (0.2 * last1 + 0.2 * last2 + 0.4 / 3 * avg) + r  # 近两年各占0.3权值，其余年份共占0.4
        else:
            if (numpy.std(line_rank) / (sum(line_rank) / len(line_rank))) <= 0.2:  # 以差异系数来确定稳定程度
                Risk = 0.3 * avg + r
            else:
                Risk = 0.3 * max(avg, last1, last2) + r
        return Risk

    def risk_level(self, line_rank):
        r = self.risk_rank(line_rank)
        if r >= 500:
            return 2
        else:
            if r <= -200:
                return 0
            else:
                return 1

