# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 17:44:02 2018

@author: lenovvo
"""
from DB_handler import DB_handler
from DB_methods import DB_methods
import numpy as np
def auto_generate(rank_level:"rank_level应该是指今年的一分一档表里的排名档位",year:"year是当年年份",kelei,provinceID):
    #(1)得出去年平均该排名段左右的学校

    DBm=DB_methods()
    DBh=DB_handler()
    #I.生成学校ID-录取平均排名字典
    DictRankToId=DBm.GetDict(["school"],["avg_rank","schoolID"],["provinceID=%d"%provinceID,"year=%d"%(year-1),"subject='%s'"%kelei],para_repeated=True)
    #II.找到去年该省份所有学校在该科目里收人的平均排名，去重倒序排，并按最近取出基准档位
    SchoolRankLastYear=DBh.select(["school"],["avg_rank"],["provinceID=%d"%provinceID,"year=%d"%(year-1),"subject='%s'"%kelei],para_OrderBy=["avg_rank",True],para_distinct=True)
        #去掉空元素 
    while None in SchoolRankLastYear:
        SchoolRankLastYear.remove(None)
        #得到今年排名在去年的基准排名
    RelatedRankSet=np.transpose(np.asarray(SchoolRankLastYear))-int(rank_level)*np.ones((1,len(SchoolRankLastYear)))
    RelatedRankSet=RelatedRankSet[RelatedRankSet<=0]
        #边界情况：rank_level已经比最高排名还高了
    if not RelatedRankSet==[]:
        BaseRank=RelatedRankSet[0]+rank_level
        IndexBaseRank=SchoolRankLastYear.index(BaseRank)
        RankPool=[]
        #取基准排名在去年的平均排名表中上下三档
        for i in range(IndexBaseRank-3,IndexBaseRank+4):
            RankPool.append(SchoolRankLastYear[i])
    else:
        BaseRank=SchoolRankLastYear[-1]+rank_level
        RankPool=[]
        for i in range(IndexBaseRank-3,IndexBaseRank+1):
            RankPool.append(SchoolRankLastYear[i])
        #III.计入以基准排名为一个范围内的学校
    auto_school_set_1=[]
    for Rank in RankPool:
        SchoolList1=DictRankToId[Rank]
        for SchoolId in SchoolList1:
            auto_school_set_1.append(SchoolId)
    #(2)（在模拟志愿表里）找到今年该排名上下考生所填报的学校和该排名挡其它考生填报的学校
        #I.确定该排名挡上下现有最近的两档排名（注意，模拟志愿表有考生排名和考生所填学校ID
            #获得模拟表内现有的排名列表，降序去重
    UserRankSet=DBh.select(["%s__user_sim_zhiyuan"%(provinceID)],["user_rank"],[],para_OrderBy=["user_rank",True],para_distinct=True)
            #取得相对排名列表
    RelatedUserRankSet=np.transpose(np.asarray(UserRankSet))-int(rank_level)*np.ones((1,len(UserRankSet)))
    UserRankPool=[]
            #如果rank_level比排名表里第一个排名还靠前
    if RelatedUserRankSet[RelatedUserRankSet<=0]==[]:
        UserRankPool.append(UserRankSet[-1])
            #如果rank_level已经存在于模拟表中了
    if RelatedUserRankSet[RelatedUserRankSet<=0][0]==0:
        BaseRankIndex=np.argwhere(RelatedUserRankSet==0)[0][1]
        UserRankPool.append(UserRankSet[BaseRankIndex])
            #考虑一些边界情况，并把上下两档的排名和自己的排名加进去
        if len(UserRankSet)!=BaseRankIndex+1:
            UserRankPool.append(UserRankSet[BaseRankIndex+1])
        if BaseRankIndex!=0:
            UserRankPool.append(UserRankSet[BaseRankIndex-1])
            #如果rank_level还不在模拟表中
    else:
        BaseRankIndex=np.argwhere(RelatedUserRankSet<=0)[0][1]
        UserRankPool.append(UserRankSet[BaseRankIndex])
        if BaseRankIndex!=0:
            UserRankPool.append(UserRankSet[BaseRankIndex-1])
        #II.得到这几档排名其它所有考生的志愿（从模拟志愿表里获取）
        #生成今年模拟志愿表里的考生的排名与所有志愿学校ID的字典
        #每一个排名段内的学校是去重了，但是排名段之间的学校没有去重
    DictUserRankToId=DBm.GetDict(["%s__user_sim_zhiyuan"%(provinceID)],["user_rank","school_ID1","school_ID2","school_ID3","school_ID4","school_ID5","school_ID6"],[],para_repeated=True)
    auto_school_set_2=[]
    for Rank in UserRankPool:
        SchoolList=list(set(DictUserRankToId[Rank]))
        for School in SchoolList:
            if School!=None:
                auto_school_set_2.append(School)
    auto_school_set=auto_school_set_1+auto_school_set_2#总学校池
    #3、根据专业推荐风险筛选出学校
        #（1）获得学校池中所有学校的前五年平均录取排名 line_rank列表（按year从大到小排列）
        #批次的问题，统一批次否（我认为应当去掉提前批，一来提前批的数量过少
    DictIDToLineRank=DBm.GetDict(["school"],["schoolID","avg_rank","year"],["provinceID=9","subject='science'","year>=2014"],para_repeated=True,para_Order=-1)    
    #需要各省2012-2017一分一档表
#为了求出某个用户所填志愿中某个学校的成功率，需要知道：
#（1）排名较该用户靠前且已经提交模拟志愿表且填的志愿里有这个学校的用户数a
#（2）排名较该用户靠前的模拟用户也有一定的概率填报该志愿，这样的用户有b个（暴力方法：蒙特卡罗法求概率）
#（3）该学校该年计划招生人数c
#在简单的单志愿的情况下，该用户被该学校的录取概率p满足，
    #p=(Σ（bi*pi))/(c-a) pi是每个模拟用户填报该学校的概率
    #如果使用蒙特卡洛法，进行n次试验，每次进行试验，b个用户该志愿的填报总人数如果大小于c-a则认为用户被学校录取
    #如果成功了m次，那么p=m/n
#如果有n个平行志愿，假设志愿录取是依次按第一、第二、第三走。
#设若增加条件：知道每个学校在该年的招生人数gi，
#进行模拟填报，
#情况一：使用蒙特卡洛法。那么每次都会以随机模拟用户补齐缺失的用户
    #设该用户前有j人，对这j人进行模拟录取，并对用户志愿里的每一个学校进行追踪，如在录取完成后，
    #某个学校仍然未招满，那么认为该学校成功录取用户。多次重复这一过程，得到成功率。
    #（这样思路简单，但计算量极大）
    


    