function [Risk] = riskrank(userrank,lineRank )
%TEST_RANK �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
    N = 0;	%������������������
	%last1Ϊ���һ�꣬last2Ϊlast1ǰһ��
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
    if (avg >= last2) && (last2 >= last1)	%�����½�����
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
