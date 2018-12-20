rankline=[2220,1903,2235,1891,2315;%HebeiNKU
    87,103,161,387,334;%HebeiFDU
    80,52,50,151,157;%HebeiTHU
    6041,6323,17242,11700,11097;%HebeiSCU
    2981,2788,2683,3907,4153;%HebeiTJU
    3673,2928,2235,3239,3443;%HebeiHIT
    29985,31037,32987,45034,41576;%Hebei四川农业大学
    74051,67656,73927,53650,67311;%Hebei广东海洋大学
    77802,70008,72321,71168,69971];%Hebei石河子大学

rank2017=[443,1331,2334;%HebeiNKU
   % 87,103,161,387,334;%HebeiFDU
    1,32,65;%HebeiTHU
    646,4399,5557;%HebeiSCU
    385,2234,3332;%HebeiTJU
    562,1921,4066;]%HebeiHIT
    %18708,26854,30485;%Hebei四川农业大学
    %74051,67656,73927,53650,67311;%Hebei广东海洋大学
    %77802,70008,72321,71168,69971];%Hebei石河子大学
    
risk=[];
for i =1:size(rankline,1)
    avg=sum(rankline(i,:))/size(rankline,2);
    series=round(0.3*avg):(round(2.5*avg)-round(0.3*avg))/200:round(2.5*avg);
   % series=0:(round(2.5*avg))/200:round(2.5*avg);
    for j=1:length(series)
       risk(i,j)= riskrank(series(j),rankline(i,:));
    end
    avgrisk=riskrank(avg,rankline(i,:));
    minrisk=riskrank(min(rankline(i,:)),rankline(i,:));
    maxrisk=riskrank(max(rankline(i,:)),rankline(i,:));
    plot(series,risk(i,:))
    hold on
    text(series(100),risk(i,100),int2str(i))
    
    %if i~=9
    %{
    plot(0:180000,ones(1,180001)*avgrisk,'color','y')
    plot(0:180000,ones(1,180001)*minrisk,'color','g')
    plot(0:180000,ones(1,180001)*maxrisk,'color','r')
    %}
   %{
    else
    plot(0:180000,ones(1,180001)*avgrisk,'color','y','marker','+')
    plot(0:180000,ones(1,180001)*minrisk,'color','g','marker','+')
    plot(0:180000,ones(1,180001)*maxrisk,'color','r','marker','+')  
    end
    %}
    
    %{
    plot(rank2017(i,2),riskrank(rank2017(i,2),rankline(i,:)),'color','y','marker','x','markersize',30)
    plot(rank2017(i,1),riskrank(rank2017(i,1),rankline(i,:)),'color','g','marker','x','markersize',30)
    plot(rank2017(i,3),riskrank(rank2017(i,3),rankline(i,:)),'color','r','marker','x','markersize',30)  
    xlabel('考生排名');
    ylabel('风险值');
    %}
    %预测
    
    rankline_5=[rankline(1,:);rankline(3:6,:)];
    for i =1:5
plot(rank2017(i,2),riskrank(rank2017(i,2),rankline_5(i,:)),'color','y','marker','+') 
   text(rank2017(i,2),riskrank(rank2017(i,2),rankline_5(i,:)),int2str(i))
hold on
plot(rank2017(i,1),riskrank(rank2017(i,1),rankline_5(i,:)),'color','g','marker','+')
    text(rank2017(i,1),riskrank(rank2017(i,1),rankline_5(i,:)),int2str(i))
plot(rank2017(i,3),riskrank(rank2017(i,3),rankline_5(i,:)),'color','r','marker','+') 
     text(rank2017(i,3),riskrank(rank2017(i,3),rankline_5(i,:)),int2str(i))
end
plot([1:6000],ones(1,6000)*117.35,'color','g')
 plot([1:6000],ones(1,6000)*350,'color','r')
    
end
    