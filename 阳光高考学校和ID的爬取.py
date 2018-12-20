# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 09:36:10 2018

@author: lenovvo
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
school_set=range(1,10)
school_name=[]
for school in school_set:
    url_school="https://gaokao.chsi.com.cn/sch/schoolInfoMain--schId-"+str(school)+".dhtml"
    html1 = urlopen(url_school)
    bs = BeautifulSoup(html1)
    info = bs.findAll("a", {"href" : "/sch/schoolInfoMain--schId-"+str(school)+".dhtml"})
    if info!=[]:
        info_name=info[0].get_text()
        school_name.append(info_name[:-1])
    