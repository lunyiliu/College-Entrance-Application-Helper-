load('Sum.mat')
 load('GaokaowangProvinceName.mat')
log=fopen('Workinglog.txt','w');
javaaddpath('D:\\mysql-connector-java-5.1.47.jar');
for i =[30,10]
    province=names{i};%省份
  % province='Beijing';
    [~,provinceID]=ismember(province,GaokaowangProvinceName);
    for year=2012:2018
        for subject={'like','wenke'}
            DataName=[province,num2str(year),subject{1}];
            
            if ~exist(DataName,'var')
                fprintf(log,[DataName,'不存在\r\n']);
                [DataName,'不存在\r\n']
                continue
            else
                Data=eval(DataName);
                fprintf(log,['开始',DataName,'\r\n']);
                ['开始',DataName,'\r\n']
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