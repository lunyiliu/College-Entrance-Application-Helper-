function [ a ] = Import( Data,RankList,year,subject,provinceID)
%IMPORT 此处显示有关此函数的摘要
%   此处显示详细说明
%Data=eval(['evalin(''base'',',RankList,')']);
eval([RankList,'=Data;']);
conn = database('gaokao', 'root', '123456', 'com.mysql.jdbc.Driver', 'jdbc:mysql://39.96.168.183:3306/gaokao');
sql=['select avg_score from school where provinceID=',num2str(provinceID),' and year=',num2str(year),' and subject=''',subject,''''];
cursor1 = fetch(exec(conn ,sql));
score=(cursor1.data)';%注意读取的数据是元胞->字符串的形式
flag=0;


for s=score
    if strcmp(s{1},'null')
        continue;
    end
    if ~isconnection(conn)
        conn = database('gaokao', 'root', '123456', 'com.mysql.jdbc.Driver', 'jdbc:mysql://39.96.168.183:3306/gaokao');
    end
    flag=flag+1;
    if eval(['ismember(str2num(s{1}),',RankList,'(:,1))'])
    Rank=eval([RankList,'(',RankList,'(:,1)==str2num(s{1}),2)']);
    else
        log=fopen('Workinglog.txt','w');
        fprintf(log,['错误',str2num(s{1}),'不在一分一档表中\r\n']);
        fclose(log);
        continue
    end
    update(conn,'school',{'avg_rank'},{Rank},['where provinceID=',num2str(provinceID),' and year=',num2str(year),' and subject=''',subject,''' and avg_score=',s{1}]);
     ['ProvinceID',num2str(provinceID),'第',num2str(year),' ',num2str(subject),'更新进度',num2str(flag),'/',num2str(length(score))]
end
end

