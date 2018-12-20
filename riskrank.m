function [Risk] = riskrank(userrank,lineRank )
%TEST_RANK 此处显示有关此函数的摘要
%   此处显示详细说明
    N = 0;	%超过分数线排名年数
	%last1为最近一年，last2为last1前一年
    for i=1:5
        if userrank <= lineRank(i)
            N=N+1;
        end
    end
    if N < 2
        r = 500;
    else
        if (N == 5 && userrank <= min(lineRank))
            r = 25;
        else 
            r = 200;
        end
    end
    last1 =  userrank-lineRank(1);
    last2 =  userrank-lineRank(2);
    avg = userrank-sum(lineRank)/5;
    if (avg >= last2) && (last2 >= last1)	%若有下降趋势
        Risk = 0.03*(0.2 * last1 + 0.2 * last2 + 0.4 / 3 * avg) + r;
    else
            if (avg <= last2) && (last2 <= last1)
                Risk=0.03*(userrank-min(lineRank)) + r;
            else
                if std(lineRank)/(sum(lineRank)/5) <= 0.2
                    Risk = 0.03*avg + r;
                else
                    if std(lineRank)/(sum(lineRank)/5) >= 0.35
                        Risk = 0.03*(userrank-((sum(lineRank)-max(lineRank)-min(lineRank))/3)) + r;
                    else
                        Risk=0.03*(userrank-min(lineRank)) + r;
                    end
                end
            end
    end   
end
