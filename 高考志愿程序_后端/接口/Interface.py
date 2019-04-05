# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:14:15 2019

@author: lenovvo
"""
from getRisk import getRisk
from getRank import getRank
from schools_recommand import recommand
import sys
command=sys.argv[1]
userID=sys.argv[2]
user_nickname=sys.argv[3]
#返回的参数里有216个专业排名，36个专业成功率,6个学校成功率，36个学校排名，6个学校的近五年最低分，（所在省市一本线）
if command == 'intention_analyze' :
    obj_risk=getRisk(userID)
    obj_rank=getRank(userID)
    school_rank_36=obj_rank.get_rank_school()
    print('接下来是学校36排名')
    for i,school in enumerate(school_rank_36):
        print('接下来是第'+str(i)+'个学校')
        for rank in school:
            print(rank)
    print('接下来是专业216排名')
    major_rank_216=obj_rank.get_rank_profession()
    for i,school in enumerate(major_rank_216):
        print('接下来是第'+str(i)+'个学校')
        for i,major in enumerate(school):
            print('接下来是第'+str(i)+'个专业')
            for rank in major:
                print(rank)
    school_risk=obj_rank.get_success_school()
    major_risk=obj_rank.get_success_profession()
    print('接下来是成功率')
    for i,school in enumerate(major_risk):
        print('接下来是第'+str(i)+'个学校')
        print('学校成功率')
        print(school_risk[i])
        print('专业成功率')
        for risk in school:
            print(risk)
    # todo :近五年最低分 和一本线
	
if command == 'get_recommend_school_school_priority' :
    obj_recommand=recommand(userID)
    high,middle,low=obj_recommand.schools_recommand()
    print('接下来是高风险')
    for school in high:
        print(school)
    print('接下来是中风险')
    for school in middle:
        print(school)
    print('接下来是低风险')
    for school in low:
        print(school)

if command == 'get_recommend_school_major_priority' :
    obj_recommand=recommand(userID)
    high,middle,low=obj_recommand.majors_recommand()
    print('接下来是高风险')
    for school in high:
        print(school)
    print('接下来是中风险')
    for school in middle:
        print(school)
    print('接下来是低风险')
    for school in low:
        print(school)