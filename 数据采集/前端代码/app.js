App({
  globalData:{
    //初始（第一轮信息）直接写入下面School和Major
    //get_school
    //get_major
    //除School与Major项外其余项在每次提交后存入数据库,School与major为应读取的项
    nickName :' ',
    areaindex:0, 
    piciindex:0,
     keleiindex:0,
    finish: 0,
    School: ' ',     //在此预置学校名
    Pici: '',
    Province: '',
    Rank: '',
    Year: '',
    Major: '',     //在此预置专业，若无预置为0
    Kelei: '',
    Class: '',
    Subject: '',
    Lowest: '',
    Avg: '',
    Highest: '',
    pici: ['未选择批次', '第一批', '第二批', '第三批', '提前批', '专科'],
    kelei: ['未选择科类', '文科', '理科', '不分文理'],
    area: ['未选择省份', '北京', '天津', '河北', '山西', '山东', '河南', '内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '福建', '上海', '浙江', '安徽', '江西', '湖南', '湖北', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '陕西', '西藏', '甘肃', '青海', '宁夏', '新疆'],
    userID:'啦啦啦',
    ifMajor: 0,     //是否预置专业，是则1
  },



   
  
})