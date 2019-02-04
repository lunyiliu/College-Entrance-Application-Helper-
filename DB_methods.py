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
    def GetDict(self,FormList:"list，从哪几个表中选，如果只有一个元素也要记得加[]哦",ResultList:"只接受元素数大于等于二的列表，第一个元素是key，之后的元素都是value",ConditionList:"列表，查询的条件，元素格式：XX=XX",para_logic:"哪些条件需要或逻辑"=[],para_repeated:"这个参数为true意味着字典的key和value是一对多映射，value将是列表"=False,para_Order:"只在一对多映射字典中使用，将每个key中的value按ResultList中最后一个字段的大小排序（该字段不输出且必须与value字段不同），该参数默认为0，为1表示升序排列，为-1表示降序排列"=0)->"返回字典":
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