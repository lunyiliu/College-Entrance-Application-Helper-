function [ a ] = Import( Data,RankList,year,subject,provinceID)
%IMPORT �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
%Data=eval(['evalin(''base'',',RankList,')']);
eval([RankList,'=Data;']);
conn = database('gaokao', 'root', '123456', 'com.mysql.jdbc.Driver', 'jdbc:mysql://39.96.168.183:3306/gaokao');
sql=['select avg_score from school where provinceID=',num2str(provinceID),' and year=',num2str(year),' and subject=''',subject,''''];
cursor1 = fetch(exec(conn ,sql));
score=(cursor1.data)';%ע���ȡ��������Ԫ��->�ַ�������ʽ
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
        fprintf(log,['����',str2num(s{1}),'����һ��һ������\r\n']);
        fclose(log);
        continue
    end
    update(conn,'school',{'avg_rank'},{Rank},['where provinceID=',num2str(provinceID),' and year=',num2str(year),' and subject=''',subject,''' and avg_score=',s{1}]);
     ['ProvinceID',num2str(provinceID),'��',num2str(year),' ',num2str(subject),'���½���',num2str(flag),'/',num2str(length(score))]
end
end

