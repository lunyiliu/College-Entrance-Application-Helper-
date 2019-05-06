from DB_handler import DB_handler
from DB_methods import DB_methods
#读取省份对应表
provinceID_dictionary={}
with open ('provinceid.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        line=line.strip('\n')
        provinceID_dictionary[line.split(',')[0]]=line.split(',')[1]

class getRank():

    def __init__(self,user_ID):
        self.DBh = DB_handler()
        self.DBm = DB_methods()
        self.user = user_ID
        self.score = str(self.DBh.select(['client'], ['score'], ['user_ID =' + user_ID]))
        provinceID = str(self.DBh.select(['client'], ['province'], ['user_ID =' + user_ID]))
        self.provinceID = str(provinceID_dictionary[provinceID])
        self.subject = self.DBh.select(['client'], ['subject'], ['user_ID =' + user_ID])
        self.year = str(self.DBh.select(['client'], ['year'], ['user_ID =' + user_ID]))
        self.pici = str(self.DBh.select(['client'], ['pici'], ['user_ID =' + user_ID]))
        self.intension_list =[]
        #print(self.DBh.select(['client'],['choose_list'],['user_ID ='+user_ID]))
        if self.DBh.select(['client'],['choose_list'],['user_ID ='+user_ID]) is not None and self.DBh.select(['client'],['choose_list'],['user_ID ='+user_ID]) != '':
            self.mid_list = self.DBh.select(['client'],['choose_list'],['user_ID ='+user_ID])[:-1].split(',')
            for element in self.mid_list:
                self.intension_list.append(element[:-1].split('.'))
        self.rank_school = 0
        self.rank_profession = 0
        self.rank_school_list = []
        self.rank_profession_list = []

    def get_rank_school(self):#获取学校排名。对每个学校有6个排名，一个二维数组返回.分一档 430-，510-，5901，670-，750- 存储的时候从高到低
        #对每个学校 对每个志愿序列
        #print(self.mid_list)
        #print(self.intension_list)
        school_list = []
        school_rank_list = [] #一个学校的6个排名
        school_count_result = [] #选择学校人数
        result = []#用于返回结果
        for i in range(len(self.intension_list)):
            school_list.append(self.intension_list[i][0])
        #print(school_list)

        for school in school_list:
            school_rank_list = []
            school_count = []
            for number in range(6):#一所学校的对某一支援序列计算排名
                self.rank_school = 0  # 一次学校的排名 1/36
                new_store = []
                school_str = str(school)
                serial = str(number+1)
                Conditionlist = ['schoolID ='+school_str,
                                 'provinceID ='+self.provinceID,
                                 'subject =' +self.subject,
                                 'pici =' + self.pici,
                                 'serialnumber ='+serial]
                #print(Conditionlist)

                #print(self.DBh.select(['intension_school_table'], ['block1'], Conditionlist))

                store_all = self.DBh.select(['intention_school_table'],
                                            ['block1', 'block2', 'block3', 'block4', 'block5'], Conditionlist)
                #print(store_all)
                store1 = store_all[0]
                store2 = store_all[1]
                store3 = store_all[2]
                store4 = store_all[3]
                store5 = store_all[4]
                #获取每一block内存的人数

                if  store1 is None or store1 =='' or store1 == []:
                    count1 = 0
                else:
                    #print(store1)
                    count1 = int(store1.split(',',1)[0])

                if  store2 == None or store2 ==''or store2 ==[]:
                    count2 = 0
                else:
                    count2 = int(store2.split(',',1)[0])

                if  store3 == None or store3 ==''or store3 ==[]:
                    count3 = 0
                else:
                    count3 = int(store3.split(',',1)[0])

                if  store4 == None or store4 ==''or store4 ==[]:
                    count4 = 0
                else:
                    count4 = int(store4.split(',',1)[0])

                if  store5 == None or store5 ==''or store5 ==[]:
                    count5= 0
                else:
                    count5 = int(store5.split(',',1)[0])

                count = count1+count2+count3+count4+count5

                if count == 0:
                    count = 1
                school_count.append(count)#某个学校第i个志愿选择某学校的人数

                if int(self.score) < 430:#block1内查询 block内包含以逗号隔开的第一位人数，后面用点隔开的分数排行。
                    store_pre = store1
                    if store_pre == None or store_pre == ''or store_pre ==[]:
                        rank_current = 1
                    else:
                        new_store = store1.split(',')[1][:-1].split('.')
                        if int(self.score) < int(new_store[-1]):
                            rank_current = count1 +1
                        else:
                            for j in range(len(new_store)):
                                if self.score >=new_store[j]:
                                    rank_current = j+1
                                    break
                    self.rank_school = rank_current + count2 + count3 + count4 + count5


                elif int(self.score)< 510:#block1内查询 block内包含以逗号隔开的第一位人数，后面用点隔开的分数排行。
                    store_pre = store2
                    if store_pre == None or store_pre == '' or store_pre ==[]:
                        rank_current = 1
                    else:
                        new_store = store2.split(',')[1][:-1].split('.')
                        if int(self.score) < int(new_store[-1]):
                            rank_current = count2 +1
                        else:
                            for j in range(len(new_store)):
                                if self.score >=new_store[j]:
                                    rank_current = j+1
                                    break
                    self.rank_school = rank_current  + count3 + count4 + count5


                elif int(self.score) < 590:#block1内查询 block内包含以逗号隔开的第一位人数，后面用点隔开的分数排行。
                    store_pre = store3
                    if store_pre == None or store_pre == ''or store_pre ==[]:
                        rank_current = 1
                    else:
                        new_store = store3.split(',')[1][:-1].split('.')
                        if int(self.score) < int(new_store[-1]):
                            rank_current = count3 +1
                        else:
                            for j in range(len(new_store)):
                                if self.score >=new_store[j]:
                                    rank_current = j+1
                                    break
                    self.rank_school = rank_current  + count4 + count5


                elif int(self.score) < 670:#block1内查询 block内包含以逗号隔开的第一位人数，后面用点隔开的分数排行。
                    store_pre = store4
                    if store_pre == None or store_pre == ''or store_pre ==[]:
                        rank_current = 1
                    else:
                        new_store = store4.split(',')[1][:-1].split('.')
                        if int(self.score) < int(new_store[-1]):
                            rank_current = count4 +1
                        else:
                            for j in range(len(new_store)):
                                if self.score >=new_store[j]:
                                    rank_current = j+1
                                    break
                    self.rank_school = rank_current   + count5


                elif int(self.score) < 750:#block1内查询 block内包含以逗号隔开的第一位人数，后面用点隔开的分数排行。
                    store_pre = store5
                    if store_pre == None or store_pre == ''or store_pre ==[]:
                        rank_current = 1
                    else:
                        new_store = store5.split(',')[1][:-1].split('.')
                        if int(self.score) < int(new_store[-1]):
                            rank_current = count5 +1
                        else:
                            for j in range(len(new_store)):
                                if self.score >=new_store[j]:
                                    rank_current = j+1
                                    break
                    self.rank_school = rank_current  + count5
                    
                school_rank_list.append(self.rank_school)
            result.append(school_rank_list)
            school_count_result.append(school_count)
        return result,school_count_result #形式为[[,,,,,],[],[],[],[],[]]

    def get_rank_profession(self):
        #6个学校，6个专业，6个排名，流程类似上面一个
        #print(self.intension_list)
        school_list = []
        profession_count_result = []
        result = []  # 用于记录六个学校，36个专业，256个排名
        for i in range(len(self.intension_list)):
            school_list.append(self.intension_list[i][0])
        #print(school_list)

        for i in range(len(school_list)):#对每个学校
            #store_profession = [] #在每个志愿学校里学生填写的专业名称
            school = school_list[i]
            store_profession = self.intension_list[i][1:] #去除学校项,某个学校内按顺序选择的专业
            #print(store_profession)
            store_profession_rank = []
            profession_count = []#记录人数

            for profession in store_profession:#对每个专业
                profession_rank_list = [] #记录某一个学校里的某一个专业的六个排名情况
                profession_count_one = [] #同上，人数
                zhuanye = profession
                for i in range(len(store_profession)):#确定专业是第几志愿


                    #zhuanye = store_profession[i]
                    serial = str(i+1)
                    self.rank_profession = 0
                    new_store = []

                    Conditionlist = ['schoolID =' + school, 'provinceID =' + self.provinceID,
                                     'subject ='  + self.subject , 'pici =' + self.pici,
                                     'serialnumber =' + serial,'zhuanye ='+zhuanye]

                    #print(Conditionlist)
                    store_all = self.DBh.select(['intension_zhuanye_table'], ['block1','block2','block3','block4','block5'], Conditionlist)

                    store1 = store_all[0]
                    store2 = store_all[1]
                    store3 = store_all[2]
                    store4 = store_all[3]
                    store5 = store_all[4]
                    # 获取每一block内存的人数

                    if store1 == None or store1 == ''or store1 ==[]:
                        count1 = 0
                    else:
                        count1 = int(store1.split(',', 1)[0])

                    if store2 == None or store2 == ''or store2 ==[]:
                        count2 = 0
                    else:
                        count2 = int(store2.split(',', 1)[0])

                    if store3 == None or store3 == ''or store3 ==[]:
                        count3 = 0
                    else:
                        count3 = int(store3.split(',', 1)[0])

                    if store4 == None or store4 == ''or store4==[]:
                        count4 = 0
                    else:
                        count4 = int(store4.split(',', 1)[0])

                    if store5 == None or store5 == ''or store5 ==[]:
                        count5 = 0
                    else:
                        count5 = int(store5.split(',', 1)[0])

                    count=count1+count2+count3+count4+count5
                    if count == 0:
                        count = 1
                    profession_count_one.append(count)

                    #print(count4)

                    if int(self.score) < 430:
                        #print(Conditionlist)
                        store_pre = store1
                        if store_pre == None or store_pre == ''or store_pre ==[]:
                            rank_current = 1
                        else:
                            new_store = store1.split(',')[1][:-1].split('.')
                            if int(self.score) < int(new_store[-1]):
                                rank_current = count1 + 1
                            else:
                                for j in range(len(new_store)):
                                    if self.score >= new_store[j]:
                                        rank_current = j + 1
                                        break


                        self.rank_profession = rank_current + count2 + count3 + count4 + count5


                    elif int(self.score) < 510:
                        store_pre = store2
                        if store_pre == None or store_pre == ''or store_pre ==[]:
                            rank_current = 1
                        else:
                            new_store = store2.split(',')[1][:-1].split('.')
                            if int(self.score) < int(new_store[-1]):
                                rank_current = count2 + 1
                            else:
                                for j in range(len(new_store)):
                                    if self.score >= new_store[j]:
                                        rank_current = j + 1
                                        break
                        self.rank_profession = rank_current + count3 + count4 + count5


                    elif int(self.score) < 590:
                        store_pre =store3
                        if store_pre == None or store_pre == ''or store_pre ==[]:
                            rank_current = 1
                        else:
                            new_store = store3.split(',')[1][:-1].split('.')
                            if int(self.score) < int(new_store[-1]):
                                rank_current = count3 + 1
                            else:
                                for j in range(len(new_store)):
                                    if self.score >= new_store[j]:
                                        rank_current = j + 1
                                        break
                        self.rank_profession = rank_current + count4 + count5


                    elif int(self.score) < 670:
                        store_pre = store4
                        if store_pre == None or store_pre == ''or store_pre ==[]:
                            rank_current = 1
                        else:
                            new_store = store4.split(',')[1][:-1].split('.')
                            if int(self.score) < int(new_store[-1]):
                                rank_current = count4 + 1
                            else:
                                for j in range(len(new_store)):
                                    if self.score >= new_store[j]:
                                        rank_current = j + 1
                                        break
                        self.rank_profession = rank_current + count5


                    elif int(self.score) < 750:
                        store_pre = store5
                        if store_pre == None or store_pre == ''or store_pre ==[]:
                            rank_current = 1
                        else:
                            new_store = store5.split(',')[1][:-1].split('.')
                            if int(self.score) < int(new_store[-1]):
                                rank_current = count5 + 1
                            else:
                                for j in range(len(new_store)):
                                    if self.score >= new_store[j]:
                                        rank_current = j + 1
                                        break
                        self.rank_profession = rank_current + count5

                    profession_rank_list.append(self.rank_profession)

                store_profession_rank.append(profession_rank_list)
                profession_count.append(profession_count_one)

            result.append(store_profession_rank)
            profession_count_result.append(profession_count)

        return result,profession_count_result

#todolist:返回志愿学校的近五年最低分。
