load('Sum.mat')
 load('GaokaowangProvinceName.mat')
log=fopen('Workinglog.txt','w');
javaaddpath('D:\\mysql-connector-java-5.1.47.jar');
for i =[30,10]
    province=names{i};%ʡ��
  % province='Beijing';
    [~,provinceID]=ismember(province,GaokaowangProvinceName);
    for year=2012:2018
        for subject={'like','wenke'}
            DataName=[province,num2str(year),subject{1}];
            
            if ~exist(DataName,'var')
                fprintf(log,[DataName,'������\r\n']);
                [DataName,'������\r\n']
                continue
            else
                Data=eval(DataName);
                fprintf(log,['��ʼ',DataName,'\r\n']);
                ['��ʼ',DataName,'\r\n']
                if strcmp(subject{1},'like')
               Import(Data,DataName,year,'science',provinceID);
                else
                Import(Data,DataName,year,'literature',provinceID);
                end
            end
        end
    end
end
 fclose('all');               