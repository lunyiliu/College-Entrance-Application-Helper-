# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 19:48:23 2019

@author: zmxle
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:13:32 2019

@author: zmxle
"""

import requests
import json
import pymysql
conn = pymysql.connect(host='39.97.100.184', user='root', passwd='8612260', db='gaokao', charset='utf8')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

import requests

cookies = {
    'lastvisit': '1555156244397',
    'havecity': 'true',
    'tool_ipuse': '221.198.67.36',
    'tool_ipprovince': '12',
    'tool_iparea': '1',
    'eol_avd_got': '1555156244397',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'https://gkcx.eol.cn/linespecialty?luqutype=',
    'Content-Type': 'application/json;charset=utf-8',
    'Connection': 'keep-alive',
}

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://gkcx.eol.cn/api?uri=hxsjkqt/api/gk/score/special&province_id=&size=20&page=1&year=2017&type=&local_type_id=&f211=&f985=&dual_class=&is_dual_class=&department=&central=&admissions=&school_type=&local_batch_id=&keyword=', headers=headers, cookies=cookies)


for year in range(2014,2018):
    for page in range(1,22331):#22331
        params = (
            ('uri', 'hxsjkqt/api/gk/score/special'),
            ('province_id', ''),
            ('size', '20'),
            ('page', page),
            ('year', year),
            ('type', ''),
            ('local_type_id', ''),
            ('f211', ''),
            ('f985', ''),
            ('dual_class', ''),
            ('is_dual_class', ''),
            ('school_type', ''),
            ('local_batch_id', ''),
            ('department', ''),
            ('central', ''),
            ('admissions', ''),
            ('keyword', ''),
        )
        response = requests.get('https://gkcx.eol.cn/api', headers=headers, params=params, cookies=cookies)
        res = response.text
        infoes = json.loads(res)
        #专业名称 学校名称 avg low high 省份 科类 年份 批次 门类 一级学科 学科评级 flag_finish
        if infoes !=0 and len(infoes['data']) and len(infoes['data']['item']):
            for j in range(len(infoes['data']['item'])):
                l = ''
                info = infoes['data']['item'][j]
                major = info['all'][0]
                school = info['all'][1]
                major=major.replace('（','(')
                school=school.replace('（','(')
                major=major.replace('）',')')
                school=school.replace('）',')')
                l+="'"
                l+=major  # 存专业名字
                l+="','"
                l+=school  # 存学校名字
                l+="','"
                l+=str(info['average'])#平均分
                l+="','"
                l+=str(info['min']) #最低分
                l+="','"
                l+=str(info['max'])#最大录取分数
                l+="','"
                l+=info['local_province_name']#存省份
                l+="','"
                l+=info['local_type_name']  # 科类
                l+="','"
                l+=str(info['year'])#存年份
                l+="','"
                if info['local_batch_name']=='本科一批':
                    l+='第一批'#批次
                elif info['local_batch_name']=='本科二批':
                    l+='第二批'#批次
                elif info['local_batch_name']=='本科三批':
                    l+='第二批'#批次
                elif info['local_batch_name']=='本科提前批':
                    l+='提前批'#批次
                else:
                    l+='其他'#批次
                l+="','"
                if 'level2_name' in info:
                    l+=str(info['level2_name']) #门类
                else:
                    l+='--'
                l+="','"
                if 'level3_name' in info:
                    l+=str(info['level3_name']) #门类
                else:
                    l+='--'
                l+="','"
                l+='--' #门类
                l+="','"
                l+='--' #门类
                l+="'"
                l=l.replace("'--'",'NULL')
                print(l)
                
                sql="insert into ecol_majors values("+l+")"
                #print(sql)
                try:
                    cursor.execute(sql)
                    conn.commit()
                except Exception as e:
                    print(e)
                

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://gkcx.eol.cn/api?uri=hxsjkqt/api/gk/score/province&province_id=&size=20&page=1&year=2018&type=&local_type_id=2&f211=&f985=&dual_class=&is_dual_class=&school_type=&local_batch_id=&department=&central=&admissions=&keyword=', headers=headers, cookies=cookies)

