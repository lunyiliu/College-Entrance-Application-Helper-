# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 10:17:59 2018

@author: lenovvo
"""
import numpy as np
def riskRank(userrank,lineRank):
    N = 0	#超过分数线排名年数
	#last1为最近一年，last2为last1前一年
    for i in range(5):
        if userrank <= lineRank[i]:
            N=N+1
    if N <= 2 :
        r = 500
    if N == 5:
        r = 50
    else :
        r = 200
    last1 =  userrank-lineRank[0]
    last2 =  userrank-lineRank[1]
    avg = userrank-sum(lineRank)/5
    if (avg >= last2) and (last2 >= last1):	#若有下降趋势
        Risk = 0.3*(0.3 * last1 + 0.3 * last2 + 0.4 * avg) + r
    else:
        if np.std(np.array(lineRank))/sum(lineRank)/5 <= 0.2:	#若浮动在50名内则视为较稳定
            Risk = 0.3*avg + r
        else:
            Risk=0.3*max(avg, last1, last2) + r
    return Risk

lineRank=[2220,1903,2235,1891,2315]
userrank_set=[4066,2913,2334,1723,1031]
for i in userrank_set:
    print(str(riskRank(i,lineRank)))
