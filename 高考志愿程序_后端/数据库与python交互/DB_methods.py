# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 22:23:42 2018
@author: lenovvo
"""
from collections import defaultdict
from DB_handler import DB_handler
class DB_methods:
    def __init__(self):
      self.DB=DB_handler()
    #查询几个参数，并以字典返回（第一个参数是key）
    #关于一对多映射字典，其指的是一个key可能有多个value，而且这些value可能是来自数据库里一栏，也可能是多栏
    def GetDict(self,
                FormList:"list，从哪几个表中选，如果只有一个元素也要记得加[]哦",
                ResultList:"只接受元素数大于等于二的列表，第一个元素是key，之后的元素都是value",
                ConditionList:"列表，查询的条件，元素格式：XX=XX",
                para_logic:"哪些条件需要或逻辑"=[],
                para_repeated:"这个参数为true意味着字典的key和value是一对多映射，value将是列表"=False,
                para_Order:"只在一对多映射字典中使用，将每个key中的value按ResultList中最后一个字段的大小排序（该字段不输出且必须与value字段不同），该参数默认为0，为1表示升序排列，为-1表示降序排列"=0)->"返回字典":
        if not para_repeated:
            List=self.DB.select(FormList,ResultList,ConditionList,para_logic)
            return dict(zip(List[0],List[1]))
        else:
            r_=self.DB.select(FormList,ResultList,ConditionList,para_logic,para_dict=True)
            r=defaultdict(list)
            for element in r_:
                if para_Order==0:
                    for i in range(1,len(ResultList)):
                        r[element[ResultList[0]]].append(element[ResultList[i]])
                else:
                        r[element[ResultList[0]]].append([[element[ResultList[i]] for i in range(1,len(ResultList)-1)],element[ResultList[-1]]])
            if para_Order!=0:
                for dic in r:
                    if para_Order==1:#升序
                        r[dic]=sorted(r[dic],key=lambda element:element[-1])
                    if para_Order==-1:#降序
                        r[dic]=sorted(r[dic],key=lambda element:element[-1],reverse=True)
                    for i in range(len(r[dic])):
                        element=r[dic][i]
                        r[dic][i]=element[0]
                        if len(r[dic][i])==1:
                            r[dic][i]=r[dic][i][0]
            return dict(r)

#"""
    #def getRank(self,FormList:'选取表',schoolID:"关注学校id", provinceID:'用户所在省份',score:"用户成绩",year:'当年年份',subject:'文理分类'):#给用户成绩排序。返回rank值。
    def getRank(self,
                FormList: '选取表',
                conditionList:'格式同前，选取条件',
                score:'学生分数'):
        rank = 0
        count = 0
        storeScore = self.DB.select([FormList],['store_rank_all'],conditionList)
        #ranklist = storeScore[0]
        score = score
        str = ''
        if storeScore[0] is None or storeScore[0] is '':
            #print('first')
            rank = 1
            count = 1
            print(score)
            str = score+'.'
            #print(str)
            self.DB.update(FormList,['store_rank_all ='+'\"'+ str+'\"' ],conditionList)
        else:
            #print(storeScore[0])
            str = ''
            ranklist = storeScore[0][:-1].split('.')
            count = len(ranklist)
            if int(ranklist[-1]) <= int(score):
                for i in range(count):#从大到小
                    if int(ranklist[i]) <= int(score):
                        rank = i+1
                        ranklist.insert(i,score)
                        count = count+1
                        break
            else:
                ranklist.append(score)
                rank = count+1
                count = count+1

            for element in ranklist:
                str = str + element +'.'
                #print(element)
            #print(str)
            self.DB.update(FormList, ['store_rank_all =' +'\"'+ str+'\"'], conditionList)
        return rank,count
#"""
    def deleteRecords(self,user_ID):
        #获得user的基本信息 chooselist 里 形式如'schoolID1.schoolID2'
        store_pre = self.DB.select(['client'],['choose_list'],['user_ID ='+user_ID])[0]
        score = str(self.DB.select(['client'], ['score'], ['user_ID =' + user_ID])[0])
        provinceID = str(self.DB.select(['client'], ['provinceID'], ['user_ID =' + user_ID])[0])
        subject = self.DB.select(['client'], ['subject'], ['user_ID =' + user_ID])[0]
        year = str(self.DB.select(['client'], ['year'], ['user_ID =' + user_ID])[0])
        if store_pre is None or store_pre is '':
            return 0 #其实什么都不执行就行
        else:
            store = self.DB.select(['client'],['choose_list'],['user_ID ='+user_ID])[0][:-1].split('.')
            for element in store:
                list2str = ''
                list1 = self.DB.select(['test'],
                                       ['store_rank_chosen'],
                                       ['schoolID ='+element,
                                        'year ='+year,
                                        'provinceID ='+provinceID,
                                        'subject ='+'\"'+subject+'\"'])[0][:-1].split('.') #分数排名
                '''
                for i in range(len(list1)):
                    if score == list1[i]:
                        list1 = list1.remove(list1[i])
                        break
                '''
                list1.remove(score)
                print(list1)
                if list1 is None:
                    list2str = ''
                else:
                    for j in range(len(list1)):
                        list2str = list2str + list1[j] +'.'
                self.DB.update('test',
                               ['store_rank_chosen ='+'\"'+list2str+'\"'],
                               ['schoolID ='+element,
                                'year ='+year,
                                'provinceID ='+provinceID,
                                'subject ='+'\"'+subject+'\"'])
            self.DB.update('client',['choose_list ='+'\"'+''+'\"'],['user_ID =' + user_ID])#可能存在问题 这个清除

    def setRecords(self,user_ID,referenceList):#referenceList为志愿学校形式为list，里面有学校id  输入志愿学校 存储 返回各校排名2
        score = str(self.DB.select(['client'], ['score'], ['user_ID=' + user_ID])[0])
        provinceID = str(self.DB.select(['client'], ['provinceID'], ['user_ID=' + user_ID])[0])
        subject = self.DB.select(['client'], ['subject'], ['user_ID=' + user_ID])[0]
        year = self.DB.select(['client'], ['year'], ['user_ID=' + user_ID])[0]
        year = str(year)
        ranklist = []
        str1 = '' #记录到choose_list
        for element in referenceList:
            liststr = ''  # 记录到client-choose_list
            str1 = str1 + element +'.'
            list2 = self.DB.select(['test'],
                                   ['store_rank_chosen'],
                                   ['schoolID =' + element,
                                   'year =' + year,
                                   'provinceID =' + provinceID,
                                   'subject =' + '\"' + subject + '\"'])[0] #代表choose——list

            if list2 is None or list2 is '':
                ranklist.append(1)
                list1 = [score]

            else:
                list1 =self.DB.select(['test'], ['store_rank_chosen'],
                                  ['schoolID =' + element,
                                   'year =' + year,
                                   'provinceID =' + provinceID,
                                   'subject =' + '\"' + subject + '\"'])[0][:-1].split('.')
                if int(list1[-1]) > int(score):
                    ranklist.append(len(list1)+1)
                    list1.append(score)
                else:
                    for i in range(len(list1)):
                        if int(list1[i]) <= int(score):
                            ranklist.append(i+1)
                            list1.insert(i,score)
                            break
            for j in list1:
                liststr = liststr + j + '.'
            self.DB.update('test',['store_rank_chosen = '+'\"'+liststr+'\"'],
                           ['schoolID =' + element,
                            'year =' + year,
                            'provinceID =' + provinceID,
                            'subject =' + '\"' + subject + '\"'])
        self.DB.update('client',['choose_list ='+'\"'+str1+'\"'],['user_ID = '+user_ID])
        return ranklist

