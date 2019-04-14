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
cookies = {
    'lastvisit': '1555146771318',
    'havecity': 'true',
    'tool_ipuse': '221.198.67.36',
    'tool_ipprovince': '12',
    'tool_iparea': '1',
    'eol_avd_got': '1555146771318',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'https://gkcx.eol.cn/lineschool?luqutype=%E6%96%87%E7%A7%91',
    'Content-Type': 'application/json;charset=utf-8',
    'Connection': 'keep-alive',
}




for year in range(2014,2019):
    for page in range(1,3603):
        params = (
            ('uri', 'hxsjkqt/api/gk/score/province'),
            ('province_id', ''),
            ('size', '20'),
            ('page', page),
            ('year', year),
            ('type', ''),
            ('local_type_id', '2'),
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
		while 1:
            try:
                response = requests.get('https://gkcx.eol.cn/api', headers=headers, params=params, cookies=cookies,timeout=5)
                break
			except Exception as e:
                print(e)			
        res = response.text
        infoes = json.loads(res)
        if infoes !=0 and len(infoes['data']) and len(infoes['data']['item']):
            for j in range(len(infoes['data']['item'])):
                l = ''
                info = infoes['data']['item'][j]
                name = info['all'][0]
                name=name.replace('（','(')
                name=name.replace('）',')')
                l+="'"
                l+=name  # 存学校名字
                l+="','"
                l+=info['local_province_name']#存省份
                l+="','"
                l+=str(info['year'])#存年份
                l+="','"
                if info['local_type_name'] == '理科':
                    l+='science'  # 科类
                elif info['local_type_name'] == '文科':
                    l+='literature'
                else:
                    l+='sci-li'
                l+="','"
                if info['local_batch_name']=='本科一批':
                    l+='diyipi'#批次
                elif info['local_batch_name']=='本科二批':
                    l+='dierpi'#批次
                elif info['local_batch_name']=='本科提前批':
                    l+='tiqianpi'#批次
                else:
                    l+='other'#批次
                l+="','"
                l+=str(info['min']) #最低分
                l+="','"
                l+=str(info['max'])#最大录取分数
                l+="','"
                l+=str(info['average'])#平均分
                l+="'"
                l=l.replace("'--'",'NULL')
                #print(l)
                
                sql="insert into ecol_school values("+l+")"
                print('年份：'+str(year)+',页数：'+str(page)+','+name+',省份:'+info['local_province_name']+'，科类：'+info['local_type_name']+',批次:'+info['local_batch_name'])
                try:
                    cursor.execute(sql)
                    conn.commit()
                except Exception as e:
                    print(e)
                

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://gkcx.eol.cn/api?uri=hxsjkqt/api/gk/score/province&province_id=&size=20&page=1&year=2018&type=&local_type_id=2&f211=&f985=&dual_class=&is_dual_class=&school_type=&local_batch_id=&department=&central=&admissions=&keyword=', headers=headers, cookies=cookies)
