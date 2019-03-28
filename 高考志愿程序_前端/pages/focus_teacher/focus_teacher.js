var app = getApp();
Page({
  data: {
    start1: ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    start2: ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    start3: ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    start4: ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    start5: ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    SchoolName: app.globalData.SchoolName,
    SchoolID: app.globalData.SchoolID,
    Score: app.globalData.SchoolScore,
    SchoolList: app.globalData.AllSchool,
    focus: false,
    inputValue: '',
    multiArray1:
     [
      ['省份', '北京', '上海', '天津', '重庆', '河北', '山东', '辽宁', '黑龙江', '甘肃', '吉林', '青海', '河南', '江苏', '湖北', '湖南', '浙江', '江西', '广东', '云南', '福建', '台湾', '海南', '山西', '四川', '陕西', '贵州', '安徽', '内蒙古', '广西', '西藏', '新疆', '宁夏'],
      ['', ]
    ],
    multiArray2:
      [
        ['省份', '北京', '上海', '天津', '重庆', '河北', '山东', '辽宁', '黑龙江', '甘肃', '吉林', '青海', '河南', '江苏', '湖北', '湖南', '浙江', '江西', '广东', '云南', '福建', '台湾', '海南', '山西', '四川', '陕西', '贵州', '安徽', '内蒙古', '广西', '西藏', '新疆', '宁夏'],
        ['',]
      ],
    multiArray3:
      [
        ['省份', '北京', '上海', '天津', '重庆', '河北', '山东', '辽宁', '黑龙江', '甘肃', '吉林', '青海', '河南', '江苏', '湖北', '湖南', '浙江', '江西', '广东', '云南', '福建', '台湾', '海南', '山西', '四川', '陕西', '贵州', '安徽', '内蒙古', '广西', '西藏', '新疆', '宁夏'],
        ['',]
      ],
    multiArray4:
      [
        ['省份', '北京', '上海', '天津', '重庆', '河北', '山东', '辽宁', '黑龙江', '甘肃', '吉林', '青海', '河南', '江苏', '湖北', '湖南', '浙江', '江西', '广东', '云南', '福建', '台湾', '海南', '山西', '四川', '陕西', '贵州', '安徽', '内蒙古', '广西', '西藏', '新疆', '宁夏'],
        ['',]
      ],
    multiArray5:
      [
        ['省份', '北京', '上海', '天津', '重庆', '河北', '山东', '辽宁', '黑龙江', '甘肃', '吉林', '青海', '河南', '江苏', '湖北', '湖南', '浙江', '江西', '广东', '云南', '福建', '台湾', '海南', '山西', '四川', '陕西', '贵州', '安徽', '内蒙古', '广西', '西藏', '新疆', '宁夏'],
        ['',]
      ],
    objectmultiArray1: [
    ],
    
    multiIndex1: [0,0],
    multiIndex2: [0,0],
    multiIndex3: app.globalData.multiindex3,
    multiIndex4: app.globalData.multiindex4,
    multiIndex5: app.globalData.multiindex5,
},
  bindMultiPickerChange1: function (e) {
    //监听多列选择器输入（门类，一级学科）
    console.log('picker发送选择改变，携带值为', e.detail.value)
    var app = getApp();
    this.setData({
      multiIndex1:e.detail.value,
      
    })
  },
  bindMultiPickerColumnChange1: function (e) {
    console.log('修改的列为', e.detail.column, '，值为', e.detail.value);
    var data = {
      multiArray1: this.data.multiArray1,
      multiIndex1: this.data.multiIndex1,
      
    };
    data.multiIndex1[e.detail.column] = e.detail.value;
    switch (e.detail.column) {
      case 0:
        switch (data.multiIndex1[0]) {
          case 0:
            data.multiArray1[1] = [''
            ];
            break;
          case 1:
            data.multiArray1[1] = ['北京大学',

              '清华大学',
              '北京理工大学',
              '北京航空航天大学',
              '中国人民大学',
              '北京师范大学',
              '中国农业大学',
              '北京交通大学',
              '北京科技大学',
              '北京协和医学院'
            ];
            break;
          case 2:
            data.multiArray1[1] = [
              '复旦大学',

              '上海交通大学',

              '同济大学',

              '华东师范大学',

              '上海大学',

              '东华大学',

              '上海财经大学',

              '上海理工大学',

              '上海师范大学'

            ];
            break;
          case 3:
            data.multiArray1[1] = [
              '南开大学',

              '天津大学'

             
            ];
            break;
          case 4:
            data.multiArray1[1] = [
              '重庆大学',

              '西南大学',

              '解放军第三军医大学'
            ];
            break;
          case 5:
            data.multiArray1[1] = [
              '河北师范大学'
            ];
            break;
          case 6:
            data.multiArray1[1] = [
              '山东大学',
              '中国海洋大学'
            ];
            break;
          case 7:
            data.multiArray1[1] = [
              '大连理工大学',

              '东北大学',

              '辽宁大学',

              '东北财经大学',

              '大连海事大学'
            ];
            break;
          case 8:
            data.multiArray1[1] = [
              '哈尔滨工业大学',

              '哈尔滨工程大学',

              '东北林业大学',

              '黑龙江大学'


            ];
            break;
          case 9:
            data.multiArray1[1] = [
              '兰州大学',

              '西北师范大学',

              '兰州交通大学',

              '兰州理工大学',

              '西北民族大学'
            ];
            break;
          case 10:
            data.multiArray1[1] = [
              '吉林大学',

              '东北师范大学',

              '长春理工大学',

              '延边大学',

              '东北电力大学'
            ];
            break;
          case 11:
            data.multiArray1[1] = [
              '青海大学',

              '青海师范大学',

              '青海民族大学'

             
            ];
            break;
          case 12:
            data.multiArray1[1] = [
              '郑州大学',

              '解放军信息工程大学',

              '河南大学',

              '河南科技大学',

              '河南农业大学'
            ];
            break;
          case 13:
            data.multiArray1[1] = [
              '南京大学',

              '东南大学',

              '河海大学',

              '南京农业大学',

              '南京理工大学'
            ];
            break;
          case 14:
            data.multiArray1[1] = [
              '武汉大学',

              '华中科技大学',

              '武汉理工大学',

              '华中师范大学',

              '华中农业大学'
            ];
            break;
          case 15:
            data.multiArray1[1] = [
              '解放军国防科学技术大学',

              '中南大学',

              '湖南大学',

              '湖南师范大学',

              '湘潭大学'
            ];
            break;
          case 16:
            data.multiArray1[1] = [
              '浙江大学',

              '宁波大学',

              '浙江工业大学',

              '浙江师范大学',

              '杭州电子科技大学'
            ];
            break;
          case 17:
            data.multiArray1[1] = [
              '南昌大学',

              '江西师范大学',

              '江西财经大学',

              '江西理工大学',

              '江西农业大学'
            ];
            break;
          case 18:
            data.multiArray1[1] = [
              '中山大学',

              '华南理工大学',

              '深圳大学',

              '暨南大学',

              '华南师范大学'
            ];
            break;
          case 19:
            data.multiArray1[1] = [
              '云南大学',

              '昆明理工大学',

              '云南师范大学',

              '云南民族大学',

              '云南农业大学'
            ];
            break;
          case 20:
            data.multiArray1[1] = [
              '厦门大学',

              '福建师范大学',

              '福州大学',

              '福建农林大学',

              '华侨大学'
            ];
            break;
          case 21:
            data.multiArray1[1] = [
              '',
            ];
            break;
          case 22:
            data.multiArray1[1] = [
              '海南大学',
            ];
            break;
          case 23:
            data.multiArray1[1] = [
              '山西大学',

              '太原理工大学',

              '中北大学',

              '山西师范大学',

              '山西财经大学'
            ];
            break;
          case 24:
            data.multiArray1[1] = [
              '四川大学',

              '电子科技大学',

              '西南交通大学',

              '西南财经大学',

              '四川农业大学'
            ];
            break;
          case 25:
            data.multiArray1[1] = [
              '西安交通大学',

              '西安工业大学',

              '西安电子科技大学',

              '西北大学',

              '西北农村科技大学'
            ];
            break;
          case 26:
            data.multiArray1[1] = [
              '贵州大学',

              '贵州师范大学',

              '贵州民族大学',

              '贵州财经大学',

              '贵州医科大学'
            ];
            break;
          case 27:
            data.multiArray1[1] = [
              '中国科学技术大学',

              '合肥工业大学',

              '安徽大学',

              '安徽师范大学',

              '安徽农业大学'
            ];
            break;
          case 28:
            data.multiArray1[1] = [
              '内蒙古大学',

              '内蒙古农业大学',

              '内蒙古师范大学',

            
            ];
            break;
          case 29:
            data.multiArray1[1] = [
              '广西大学',

              '广西师范大学',

              '桂林电子科技大学',

          
            ];
            break;
          case 30:
            data.multiArray1[1] = [
              '西藏大学',

              '西藏民族大学',

              '西藏藏医学院',

            ];
            break;
          case 31:
            data.multiArray1[1] = [
              '新疆大学',

              '石河子大学',

              '新疆师范大学',

            ];
          case 32:
            data.multiArray1[1] = [
              '宁夏大学',

              '宁夏医科大学',

              '北方民族大学',

            ];
            break;
        }
        data.multiIndex1[1] = 0;
        break;


        console.log(data.multiIndex1);
        break;
    }
    this.setData(data);
  },

  bindMultiPickerChange2: function (e) {
    //监听多列选择器输入（门类，一级学科）
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      multiIndex2: e.detail.value
    })
  },
  bindMultiPickerColumnChange2: function (e) {
    console.log('修改的列为', e.detail.column, '，值为', e.detail.value);
    var data = {
      multiArray2: this.data.multiArray2,
      multiIndex2: this.data.multiIndex2
    };
    data.multiIndex2[e.detail.column] = e.detail.value;
    switch (e.detail.column) {
      case 0:
        switch (data.multiIndex2[0]) {
          case 0:
            data.multiArray2[1] = [''
            ];
            break;
          case 1:
            data.multiArray2[1] = ['北京大学',

              '清华大学',
              '北京理工大学',
              '北京航空航天大学',
              '中国人民大学',
              '北京师范大学',
              '中国农业大学',
              '北京交通大学',
              '北京科技大学',
              '北京协和医学院'
            ];
            break;
          case 2:
            data.multiArray2[1] = [
              '复旦大学',

              '上海交通大学',

              '同济大学',

              '华东师范大学',

              '上海大学',

              '东华大学',

              '上海财经大学',

              '上海理工大学',

              '上海师范大学'

            ];
            break;
          case 3:
            data.multiArray2[1] = [
              '南开大学',

              '天津大学'

            ];
            break;
          case 4:
            data.multiArray2[1] = [
              '重庆大学',

              '西南大学',

              '解放军第三军医大学'
            ];
            break;
          case 5:
            data.multiArray2[1] = [
              '河北师范大学'
            ];
            break;
          case 6:
            data.multiArray2[1] = [
              '山东大学',
              '中国海洋大学'
            ];
            break;
          case 7:
            data.multiArray2[1] = [
              '大连理工大学',

              '东北大学',

              '辽宁大学',

              '东北财经大学',

              '大连海事大学'
            ];
            break;
          case 8:
            data.multiArray2[1] = [
              '哈尔滨工业大学',

              '哈尔滨工程大学',

              '东北林业大学',

              '黑龙江大学'

            ];
            break;
          case 9:
            data.multiArray2[1] = [
              '兰州大学',

              '西北师范大学',

              '兰州交通大学',

              '兰州理工大学',

              '西北民族大学'
            ];
            break;
          case 10:
            data.multiArray2[1] = [
              '吉林大学',

              '东北师范大学',

              '长春理工大学',

              '延边大学',

              '东北电力大学'
            ];
            break;
          case 11:
            data.multiArray2[1] = [
              '青海大学',

              '青海师范大学',

              '青海民族大学'

            ];
            break;
          case 12:
            data.multiArray2[1] = [
              '郑州大学',

              '解放军信息工程大学',

              '河南大学',

              '河南科技大学',

              '河南农业大学'
            ];
            break;
          case 13:
            data.multiArray2[1] = [
              '南京大学',

              '东南大学',

              '河海大学',

              '南京农业大学',

              '南京理工大学'
            ];
            break;
          case 14:
            data.multiArray2[1] = [
              '武汉大学',

              '华中科技大学',

              '武汉理工大学',

              '华中师范大学',

              '华中农业大学'
            ];
            break;
          case 15:
            data.multiArray2[1] = [
              '解放军国防科学技术大学',

              '中南大学',

              '湖南大学',

              '湖南师范大学',

              '湘潭大学'
            ];
            break;
          case 16:
            data.multiArray2[1] = [
              '浙江大学',

              '宁波大学',

              '浙江工业大学',

              '浙江师范大学',

              '杭州电子科技大学'
            ];
            break;
          case 17:
            data.multiArray2[1] = [
              '南昌大学',

              '江西师范大学',

              '江西财经大学',

              '江西理工大学',

              '江西农业大学'
            ];
            break;
          case 18:
            data.multiArray2[1] = [
              '中山大学',

              '华南理工大学',

              '深圳大学',

              '暨南大学',

              '华南师范大学'
            ];
            break;
          case 19:
            data.multiArray2[1] = [
              '云南大学',

              '昆明理工大学',

              '云南师范大学',

              '云南民族大学',

              '云南农业大学'
            ];
            break;
          case 20:
            data.multiArray2[1] = [
              '厦门大学',

              '福建师范大学',

              '福州大学',

              '福建农林大学',

              '华侨大学'
            ];
            break;
          case 21:
            data.multiArray2[1] = [
              '',
            ];
            break;
          case 22:
            data.multiArray2[1] = [
              '海南大学',
            ];
            break;
          case 23:
            data.multiArray2[1] = [
              '山西大学',

              '太原理工大学',

              '中北大学',

              '山西师范大学',

              '山西财经大学'
            ];
            break;
          case 24:
            data.multiArray2[1] = [
              '四川大学',

              '电子科技大学',

              '西南交通大学',

              '西南财经大学',

              '四川农业大学'
            ];
            break;
          case 25:
            data.multiArray2[1] = [
              '西安交通大学',

              '西安工业大学',

              '西安电子科技大学',

              '西北大学',

              '西北农村科技大学'
            ];
            break;
          case 26:
            data.multiArray2[1] = [
              '贵州大学',

              '贵州师范大学',

              '贵州民族大学',

              '贵州财经大学',

              '贵州医科大学'
            ];
            break;
          case 27:
            data.multiArray2[1] = [
              '中国科学技术大学',

              '合肥工业大学',

              '安徽大学',

              '安徽师范大学',

              '安徽农业大学'
            ];
            break;
          case 28:
            data.multiArray2[1] = [
              '内蒙古大学',

              '内蒙古农业大学',

              '内蒙古师范大学',

            ];
            break;
          case 29:
            data.multiArray2[1] = [
              '广西大学',

              '广西师范大学',

              '桂林电子科技大学',

            ];
            break;
          case 30:
            data.multiArray2[1] = [
              '西藏大学',

              '西藏民族大学',

              '西藏藏医学院',

            ];
            break;
          case 31:
            data.multiArray2[1] = [
              '新疆大学',

              '石河子大学',

              '新疆师范大学',

            ];
          case 32:
            data.multiArray2[1] = [
              '宁夏大学',

              '宁夏医科大学',

              '北方民族大学',

            ];
            break;
        }
        data.multiIndex2[1] = 0;
        break;

        console.log(data.multiIndex2);
        break;
    }
    this.setData(data);
  },


  bindMultiPickerChange3: function (e) {
    //监听多列选择器输入（门类，一级学科）
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      multiIndex3: e.detail.value
    })
  },
  bindMultiPickerColumnChange3: function (e) {
    console.log('修改的列为', e.detail.column, '，值为', e.detail.value);
    var data = {
      multiArray3: this.data.multiArray3,
      multiIndex3: this.data.multiIndex3
    };
    data.multiIndex3[e.detail.column] = e.detail.value;
    switch (e.detail.column) {
      case 0:
        switch (data.multiIndex3[0]) {
          case 0:
            data.multiArray3[1] = [''
            ];
            break;
          case 1:
            data.multiArray3[1] = ['北京大学',

              '清华大学',
              '北京理工大学',
              '北京航空航天大学',
              '中国人民大学',
              '北京师范大学',
              '中国农业大学',
              '北京交通大学',
              '北京科技大学',
              '北京协和医学院'
            ];
            break;
          case 2:
            data.multiArray3[1] = [
              '复旦大学',

              '上海交通大学',

              '同济大学',

              '华东师范大学',

              '上海大学',

              '东华大学',

              '上海财经大学',

              '上海理工大学',

              '上海师范大学'

            ];
            break;
          case 3:
            data.multiArray3[1] = [
              '南开大学',

              '天津大学'

            ];
            break;
          case 4:
            data.multiArray3[1] = [
              '重庆大学',

              '西南大学',

              '解放军第三军医大学'
            ];
            break;
          case 5:
            data.multiArray3[1] = [
              '河北师范大学'
            ];
            break;
          case 6:
            data.multiArray3[1] = [
              '山东大学',
              '中国海洋大学'
            ];
            break;
          case 7:
            data.multiArray3[1] = [
              '大连理工大学',

              '东北大学',

              '辽宁大学',

              '东北财经大学',

              '大连海事大学'
            ];
            break;
          case 8:
            data.multiArray3[1] = [
              '哈尔滨工业大学',

              '哈尔滨工程大学',

              '东北林业大学',

              '黑龙江大学'

            ];
            break;
          case 9:
            data.multiArray3[1] = [
              '兰州大学',

              '西北师范大学',

              '兰州交通大学',

              '兰州理工大学',

              '西北民族大学'
            ];
            break;
          case 10:
            data.multiArray3[1] = [
              '吉林大学',

              '东北师范大学',

              '长春理工大学',

              '延边大学',

              '东北电力大学'
            ];
            break;
          case 11:
            data.multiArray3[1] = [
              '青海大学',

              '青海师范大学',

              '青海民族大学'

            ];
            break;
          case 12:
            data.multiArray3[1] = [
              '郑州大学',

              '解放军信息工程大学',

              '河南大学',

              '河南科技大学',

              '河南农业大学'
            ];
            break;
          case 13:
            data.multiArray3[1] = [
              '南京大学',

              '东南大学',

              '河海大学',

              '南京农业大学',

              '南京理工大学'
            ];
            break;
          case 14:
            data.multiArray3[1] = [
              '武汉大学',

              '华中科技大学',

              '武汉理工大学',

              '华中师范大学',

              '华中农业大学'
            ];
            break;
          case 15:
            data.multiArray3[1] = [
              '解放军国防科学技术大学',

              '中南大学',

              '湖南大学',

              '湖南师范大学',

              '湘潭大学'
            ];
            break;
          case 16:
            data.multiArray3[1] = [
              '浙江大学',

              '宁波大学',

              '浙江工业大学',

              '浙江师范大学',

              '杭州电子科技大学'
            ];
            break;
          case 17:
            data.multiArray3[1] = [
              '南昌大学',

              '江西师范大学',

              '江西财经大学',

              '江西理工大学',

              '江西农业大学'
            ];
            break;
          case 18:
            data.multiArray3[1] = [
              '中山大学',

              '华南理工大学',

              '深圳大学',

              '暨南大学',

              '华南师范大学'
            ];
            break;
          case 19:
            data.multiArray3[1] = [
              '云南大学',

              '昆明理工大学',

              '云南师范大学',

              '云南民族大学',

              '云南农业大学'
            ];
            break;
          case 20:
            data.multiArray3[1] = [
              '厦门大学',

              '福建师范大学',

              '福州大学',

              '福建农林大学',

              '华侨大学'
            ];
            break;
          case 21:
            data.multiArray3[1] = [
              '',
            ];
            break;
          case 22:
            data.multiArray3[1] = [
              '海南大学',
            ];
            break;
          case 23:
            data.multiArray3[1] = [
              '山西大学',

              '太原理工大学',

              '中北大学',

              '山西师范大学',

              '山西财经大学'
            ];
            break;
          case 24:
            data.multiArray3[1] = [
              '四川大学',

              '电子科技大学',

              '西南交通大学',

              '西南财经大学',

              '四川农业大学'
            ];
            break;
          case 25:
            data.multiArray3[1] = [
              '西安交通大学',

              '西安工业大学',

              '西安电子科技大学',

              '西北大学',

              '西北农村科技大学'
            ];
            break;
          case 26:
            data.multiArray3[1] = [
              '贵州大学',

              '贵州师范大学',

              '贵州民族大学',

              '贵州财经大学',

              '贵州医科大学'
            ];
            break;
          case 27:
            data.multiArray3[1] = [
              '中国科学技术大学',

              '合肥工业大学',

              '安徽大学',

              '安徽师范大学',

              '安徽农业大学'
            ];
            break;
          case 28:
            data.multiArray3[1] = [
              '内蒙古大学',

              '内蒙古农业大学',

              '内蒙古师范大学',

            ];
            break;
          case 29:
            data.multiArray3[1] = [
              '广西大学',

              '广西师范大学',

              '桂林电子科技大学',

            ];
            break;
          case 30:
            data.multiArray3[1] = [
              '西藏大学',

              '西藏民族大学',

              '西藏藏医学院',

            ];
            break;
          case 31:
            data.multiArray3[1] = [
              '新疆大学',

              '石河子大学',

              '新疆师范大学',

            ];
          case 32:
            data.multiArray3[1] = [
              '宁夏大学',

              '宁夏医科大学',

              '北方民族大学',

            ];
            break;
        }
        data.multiIndex3[1] = 0;
        break;

        console.log(data.multiIndex3);
        break;
    }
    this.setData(data);
  },

  bindMultiPickerChange4: function (e) {
    //监听多列选择器输入（门类，一级学科）
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      multiIndex4: e.detail.value
    })
  },
  bindMultiPickerColumnChange4: function (e) {
    console.log('修改的列为', e.detail.column, '，值为', e.detail.value);
    var data = {
      multiArray4: this.data.multiArray4,
      multiIndex4: this.data.multiIndex4
    };
    data.multiIndex4[e.detail.column] = e.detail.value;
    switch (e.detail.column) {
      case 0:
        switch (data.multiIndex4[0]) {
          case 0:
            data.multiArray4[1] = [''
            ];
            break;
          case 1:
            data.multiArray4[1] = ['北京大学',

              '清华大学',
              '北京理工大学',
              '北京航空航天大学',
              '中国人民大学',
              '北京师范大学',
              '中国农业大学',
              '北京交通大学',
              '北京科技大学',
              '北京协和医学院'
            ];
            break;
          case 2:
            data.multiArray4[1] = [
              '复旦大学',

              '上海交通大学',

              '同济大学',

              '华东师范大学',

              '上海大学',

              '东华大学',

              '上海财经大学',

              '上海理工大学',

              '上海师范大学'

            ];
            break;
          case 3:
            data.multiArray4[1] = [
              '南开大学',

              '天津大学'

            ];
            break;
          case 4:
            data.multiArray4[1] = [
              '重庆大学',

              '西南大学',

              '解放军第三军医大学'
            ];
            break;
          case 5:
            data.multiArray4[1] = [
              '河北师范大学'
            ];
            break;
          case 6:
            data.multiArray4[1] = [
              '山东大学',
              '中国海洋大学'
            ];
            break;
          case 7:
            data.multiArray4[1] = [
              '大连理工大学',

              '东北大学',

              '辽宁大学',

              '东北财经大学',

              '大连海事大学'
            ];
            break;
          case 8:
            data.multiArray4[1] = [
              '哈尔滨工业大学',

              '哈尔滨工程大学',

              '东北林业大学',

              '黑龙江大学'

            ];
            break;
          case 9:
            data.multiArray4[1] = [
              '兰州大学',

              '西北师范大学',

              '兰州交通大学',

              '兰州理工大学',

              '西北民族大学'
            ];
            break;
          case 10:
            data.multiArray4[1] = [
              '吉林大学',

              '东北师范大学',

              '长春理工大学',

              '延边大学',

              '东北电力大学'
            ];
            break;
          case 11:
            data.multiArray4[1] = [
              '青海大学',

              '青海师范大学',

              '青海民族大学'

            ];
            break;
          case 12:
            data.multiArray4[1] = [
              '郑州大学',

              '解放军信息工程大学',

              '河南大学',

              '河南科技大学',

              '河南农业大学'
            ];
            break;
          case 13:
            data.multiArray4[1] = [
              '南京大学',

              '东南大学',

              '河海大学',

              '南京农业大学',

              '南京理工大学'
            ];
            break;
          case 14:
            data.multiArray4[1] = [
              '武汉大学',

              '华中科技大学',

              '武汉理工大学',

              '华中师范大学',

              '华中农业大学'
            ];
            break;
          case 15:
            data.multiArray4[1] = [
              '解放军国防科学技术大学',

              '中南大学',

              '湖南大学',

              '湖南师范大学',

              '湘潭大学'
            ];
            break;
          case 16:
            data.multiArray4[1] = [
              '浙江大学',

              '宁波大学',

              '浙江工业大学',

              '浙江师范大学',

              '杭州电子科技大学'
            ];
            break;
          case 17:
            data.multiArray4[1] = [
              '南昌大学',

              '江西师范大学',

              '江西财经大学',

              '江西理工大学',

              '江西农业大学'
            ];
            break;
          case 18:
            data.multiArray4[1] = [
              '中山大学',

              '华南理工大学',

              '深圳大学',

              '暨南大学',

              '华南师范大学'
            ];
            break;
          case 19:
            data.multiArray4[1] = [
              '云南大学',

              '昆明理工大学',

              '云南师范大学',

              '云南民族大学',

              '云南农业大学'
            ];
            break;
          case 20:
            data.multiArray4[1] = [
              '厦门大学',

              '福建师范大学',

              '福州大学',

              '福建农林大学',

              '华侨大学'
            ];
            break;
          case 21:
            data.multiArray4[1] = [
              '',
            ];
            break;
          case 22:
            data.multiArray4[1] = [
              '海南大学',
            ];
            break;
          case 23:
            data.multiArray4[1] = [
              '山西大学',

              '太原理工大学',

              '中北大学',

              '山西师范大学',

              '山西财经大学'
            ];
            break;
          case 24:
            data.multiArray4[1] = [
              '四川大学',

              '电子科技大学',

              '西南交通大学',

              '西南财经大学',

              '四川农业大学'
            ];
            break;
          case 25:
            data.multiArray4[1] = [
              '西安交通大学',

              '西安工业大学',

              '西安电子科技大学',

              '西北大学',

              '西北农村科技大学'
            ];
            break;
          case 26:
            data.multiArray4[1] = [
              '贵州大学',

              '贵州师范大学',

              '贵州民族大学',

              '贵州财经大学',

              '贵州医科大学'
            ];
            break;
          case 27:
            data.multiArray4[1] = [
              '中国科学技术大学',

              '合肥工业大学',

              '安徽大学',

              '安徽师范大学',

              '安徽农业大学'
            ];
            break;
          case 28:
            data.multiArray4[1] = [
              '内蒙古大学',

              '内蒙古农业大学',

              '内蒙古师范大学',

            ];
            break;
          case 29:
            data.multiArray4[1] = [
              '广西大学',

              '广西师范大学',

              '桂林电子科技大学',

            ];
            break;
          case 30:
            data.multiArray4[1] = [
              '西藏大学',

              '西藏民族大学',

              '西藏藏医学院',

            ];
            break;
          case 31:
            data.multiArray4[1] = [
              '新疆大学',

              '石河子大学',

              '新疆师范大学',

            ];
          case 32:
            data.multiArray4[1] = [
              '宁夏大学',

              '宁夏医科大学',

              '北方民族大学',

            ];
            break;
        }
        data.multiIndex4[1] = 0;
        break;

        console.log(data.multiIndex4);
        break;
    }
    this.setData(data);
  },



  bindMultiPickerChange5: function (e) {
    //监听多列选择器输入（门类，一级学科）
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      multiIndex5: e.detail.value
    })
  },
  bindMultiPickerColumnChange5: function (e) {
    console.log('修改的列为', e.detail.column, '，值为', e.detail.value);
    var data = {
      multiArray5: this.data.multiArray5,
      multiIndex5: this.data.multiIndex5
    };
    data.multiIndex5[e.detail.column] = e.detail.value;
    switch (e.detail.column) {
      case 0:
        switch (data.multiIndex5[0]) {
          case 0:
            data.multiArray5[1] = [''
            ];
            break;
          case 1:
            data.multiArray5[1] = ['北京大学',

              '清华大学',
              '北京理工大学',
              '北京航空航天大学',
              '中国人民大学',
              '北京师范大学',
              '中国农业大学',
              '北京交通大学',
              '北京科技大学',
              '北京协和医学院'
            ];
            break;
          case 2:
            data.multiArray5[1] = [
              '复旦大学',

              '上海交通大学',

              '同济大学',

              '华东师范大学',

              '上海大学',

              '东华大学',

              '上海财经大学',

              '上海理工大学',

              '上海师范大学'

            ];
            break;
          case 3:
            data.multiArray5[1] = [
              '南开大学',

              '天津大学'

            ];
            break;
          case 4:
            data.multiArray5[1] = [
              '重庆大学',

              '西南大学',

              '解放军第三军医大学'
            ];
            break;
          case 5:
            data.multiArray5[1] = [
              '河北师范大学'
            ];
            break;
          case 6:
            data.multiArray5[1] = [
              '山东大学',
              '中国海洋大学'
            ];
            break;
          case 7:
            data.multiArray5[1] = [
              '大连理工大学',

              '东北大学',

              '辽宁大学',

              '东北财经大学',

              '大连海事大学'
            ];
            break;
          case 8:
            data.multiArray5[1] = [
              '哈尔滨工业大学',

              '哈尔滨工程大学',

              '东北林业大学',

              '黑龙江大学'

            ];
            break;
          case 9:
            data.multiArray5[1] = [
              '兰州大学',

              '西北师范大学',

              '兰州交通大学',

              '兰州理工大学',

              '西北民族大学'
            ];
            break;
          case 10:
            data.multiArray5[1] = [
              '吉林大学',

              '东北师范大学',

              '长春理工大学',

              '延边大学',

              '东北电力大学'
            ];
            break;
          case 11:
            data.multiArray5[1] = [
              '青海大学',

              '青海师范大学',

              '青海民族大学'

            ];
            break;
          case 12:
            data.multiArray5[1] = [
              '郑州大学',

              '解放军信息工程大学',

              '河南大学',

              '河南科技大学',

              '河南农业大学'
            ];
            break;
          case 13:
            data.multiArray5[1] = [
              '南京大学',

              '东南大学',

              '河海大学',

              '南京农业大学',

              '南京理工大学'
            ];
            break;
          case 14:
            data.multiArray5[1] = [
              '武汉大学',

              '华中科技大学',

              '武汉理工大学',

              '华中师范大学',

              '华中农业大学'
            ];
            break;
          case 15:
            data.multiArray5[1] = [
              '解放军国防科学技术大学',

              '中南大学',

              '湖南大学',

              '湖南师范大学',

              '湘潭大学'
            ];
            break;
          case 16:
            data.multiArray5[1] = [
              '浙江大学',

              '宁波大学',

              '浙江工业大学',

              '浙江师范大学',

              '杭州电子科技大学'
            ];
            break;
          case 17:
            data.multiArray5[1] = [
              '南昌大学',

              '江西师范大学',

              '江西财经大学',

              '江西理工大学',

              '江西农业大学'
            ];
            break;
          case 18:
            data.multiArray5[1] = [
              '中山大学',

              '华南理工大学',

              '深圳大学',

              '暨南大学',

              '华南师范大学'
            ];
            break;
          case 19:
            data.multiArray5[1] = [
              '云南大学',

              '昆明理工大学',

              '云南师范大学',

              '云南民族大学',

              '云南农业大学'
            ];
            break;
          case 20:
            data.multiArray5[1] = [
              '厦门大学',

              '福建师范大学',

              '福州大学',

              '福建农林大学',

              '华侨大学'
            ];
            break;
          case 21:
            data.multiArray5[1] = [
              '',
            ];
            break;
          case 22:
            data.multiArray5[1] = [
              '海南大学',
            ];
            break;
          case 23:
            data.multiArray5[1] = [
              '山西大学',

              '太原理工大学',

              '中北大学',

              '山西师范大学',

              '山西财经大学'
            ];
            break;
          case 24:
            data.multiArray5[1] = [
              '四川大学',

              '电子科技大学',

              '西南交通大学',

              '西南财经大学',

              '四川农业大学'
            ];
            break;
          case 25:
            data.multiArray5[1] = [
              '西安交通大学',

              '西安工业大学',

              '西安电子科技大学',

              '西北大学',

              '西北农村科技大学'
            ];
            break;
          case 26:
            data.multiArray5[1] = [
              '贵州大学',

              '贵州师范大学',

              '贵州民族大学',

              '贵州财经大学',

              '贵州医科大学'
            ];
            break;
          case 27:
            data.multiArray5[1] = [
              '中国科学技术大学',

              '合肥工业大学',

              '安徽大学',

              '安徽师范大学',

              '安徽农业大学'
            ];
            break;
          case 28:
            data.multiArray5[1] = [
              '内蒙古大学',

              '内蒙古农业大学',

              '内蒙古师范大学',

            ];
            break;
          case 29:
            data.multiArray5[1] = [
              '广西大学',

              '广西师范大学',

              '桂林电子科技大学',

            ];
            break;
          case 30:
            data.multiArray5[1] = [
              '西藏大学',

              '西藏民族大学',

              '西藏藏医学院',

            ];
            break;
          case 31:
            data.multiArray5[1] = [
              '新疆大学',

              '石河子大学',

              '新疆师范大学',

            ];
          case 32:
            data.multiArray5[1] = [
              '宁夏大学',

              '宁夏医科大学',

              '北方民族大学',

            ];
            break;
        }
        data.multiIndex5[1] = 0;
        break;

        console.log(data.multiIndex5);
        break;
    }
    this.setData(data);
  },

  listenerLogin: function () {
    //页面跳转
    wx.navigateTo({
      url: '../home_teacher/home_teacher'
    })
  },

  addfocus1: function (e) 
  {
    //添加、取消关注
    var i = parseInt(e.currentTarget.dataset.id)
    console.log(this.data.multiIndex1)
    if (this.data.multiIndex1[0]==0)
    {
      wx.showModal({
        title: '提示',
        showCancel: false,
        content: '请选择关注院校!',
        success: function (res) {
          console.log('用户点击确定')
        }
      })
    }
    else
    {
      if (e.currentTarget.dataset.click == 'start1') {
        var up = "start1[" + i + "]";
        this.setData
          ({
            [up]: '0'
          })
        app.globalData.FocusSchool.push(this.data.multiArray1[1][this.data.multiIndex1[1]])
        app.globalData.multiindex1.push(this.data.multiIndex1[0])
        app.globalData.multiindex1.push(this.data.multiIndex1[1])
        console.log(this.data.multiArray1[1], app.globalData.multiindex1[2])
        //   console.log(app.globalData.FocusSchoolID)
      }
      else {
        var up = "start1[" + i + "]";
        this.setData({
          [up]: '1'
        })
        for (var index in app.globalData.FocusSchool) {
          if (this.data.SchoolName[i] == app.globalData.FocusSchool[index]) {
            app.globalData.FocusSchool.splice(index, 1)
            app.globalData.FocusSchoolID.splice(index, 1)
            console.log(app.globalData.FocusSchool)
            console.log(app.globalData.FocusSchoolID)
          }
        }
      }
    }
     
  },


   addfocus2: function (e) {
    //添加、取消关注
    var i = parseInt(e.currentTarget.dataset.id)
    console.log(this.data.multiIndex2)
     if (this.data.multiIndex2[0] == 0) {
       wx.showModal({
         title: '提示',
         showCancel: false,
         content: '请选择关注院校!',
         success: function (res) {
           console.log('用户点击确定')
         }
       })
     }
     else
    {if (e.currentTarget.dataset.click == 'start2') {
      var up = "start2[" + i + "]";
      this.setData({
        [up]: '0'
      })
      app.globalData.FocusSchool.push(this.data.multiArray2[1][this.data.multiIndex2[1]])
      app.globalData.multiindex2.push(this.data.multiIndex2[0])
      app.globalData.multiindex2.push(this.data.multiIndex2[1])
      console.log(this.data.multiArray2[1][this.data.multiIndex2[1]])
      // console.log(app.globalData.FocusSchoolID)
    } else {
      var up = "start2[" + i + "]";
      this.setData({
        [up]: '1'
      })
      for (var index in app.globalData.FocusSchool) {
        if (this.data.SchoolName[i] == app.globalData.FocusSchool[index]) {
          app.globalData.FocusSchool.splice(index, 1)
          app.globalData.FocusSchoolID.splice(index, 1)
          console.log(app.globalData.FocusSchool)
          console.log(app.globalData.FocusSchoolID)
        }
      }
    }}
  },
 
  addfocus3: function (e) {
    //添加、取消关注
    var i = parseInt(e.currentTarget.dataset.id)
    console.log(this.data.multiIndex3)
    if (this.data.multiIndex3[0] == 0) {
      wx.showModal({
        title: '提示',
        showCancel: false,
        content: '请选择关注院校!',
        success: function (res) {
          console.log('用户点击确定')
        }
      })
    }
    else
    {if (e.currentTarget.dataset.click == 'start3') {
      var up = "start3[" + i + "]";
      this.setData({
        [up]: '0'
      })
      app.globalData.FocusSchool.push(this.data.multiArray3[1][this.data.multiIndex3[1]])
      app.globalData.multiindex3.push(this.data.multiIndex3[0])
      app.globalData.multiindex3.push(this.data.multiIndex3[1])
      console.log(this.data.multiArray3[1][this.data.multiIndex3[1]])
      // console.log(app.globalData.FocusSchoolID)
    } else {
      var up = "start3[" + i + "]";
      this.setData({
        [up]: '1'
      })
      for (var index in app.globalData.FocusSchool) {
        if (this.data.SchoolName[i] == app.globalData.FocusSchool[index]) {
          app.globalData.FocusSchool.splice(index, 1)
          app.globalData.FocusSchoolID.splice(index, 1)
          console.log(app.globalData.FocusSchool)
          console.log(app.globalData.FocusSchoolID)
        }
      }}
    }
  },

  addfocus4: function (e) {
    //添加、取消关注
    var i = parseInt(e.currentTarget.dataset.id)
    console.log(this.data.multiIndex4)
    if (this.data.multiIndex4[0] == 0) {
      wx.showModal({
        title: '提示',
        showCancel: false,
        content: '请选择关注院校!',
        success: function (res) {
          console.log('用户点击确定')
        }
      })
    }
    else
    {if (e.currentTarget.dataset.click == 'start4') {
      var up = "start4[" + i + "]";
      this.setData({
        [up]: '0'
      })
      app.globalData.FocusSchool.push(this.data.multiArray4[1][this.data.multiIndex4[1]])
      app.globalData.multiindex4.push(this.data.multiIndex4[0])
      app.globalData.multiindex4.push(this.data.multiIndex4[1])
      console.log(this.data.multiArray4[1][this.data.multiIndex4[1]])
      // console.log(app.globalData.FocusSchoolID)
    } else {
      var up = "start4[" + i + "]";
      this.setData({
        [up]: '1'
      })
      for (var index in app.globalData.FocusSchool) {
        if (this.data.SchoolName[i] == app.globalData.FocusSchool[index]) {
          app.globalData.FocusSchool.splice(index, 1)
          app.globalData.FocusSchoolID.splice(index, 1)
          console.log(app.globalData.FocusSchool)
          console.log(app.globalData.FocusSchoolID)
        }
      }
    }}
  },

  addfocus5: function (e) {
    //添加、取消关注
    var i = parseInt(e.currentTarget.dataset.id)
    console.log(this.data.multiIndex5)
    if (this.data.multiIndex5[0] == 0) {
      wx.showModal({
        title: '提示',
        showCancel: false,
        content: '请选择关注院校!',
        success: function (res) {
          console.log('用户点击确定')
        }
      })
    }
    else
    {if (e.currentTarget.dataset.click == 'start5') {
      var up = "start5[" + i + "]";
      this.setData({
        [up]: '0'
      })
      app.globalData.FocusSchool.push(this.data.multiArray5[1][this.data.multiIndex5[1]])
      app.globalData.multiindex5.push(this.data.multiIndex5[0])
      app.globalData.multiindex5.push(this.data.multiIndex5[1])
      console.log(this.data.multiArray5[1][this.data.multiIndex5[1]])
      // console.log(app.globalData.FocusSchoolID)
    } else {
      var up = "start5[" + i + "]";
      this.setData({
        [up]: '1'
      })
      for (var index in app.globalData.FocusSchool) {
        if (this.data.SchoolName[i] == app.globalData.FocusSchool[index]) {
          app.globalData.FocusSchool.splice(index, 1)
          app.globalData.FocusSchoolID.splice(index, 1)
          console.log(app.globalData.FocusSchool)
          console.log(app.globalData.FocusSchoolID)
        }
      }
    }}
  },
  jumptohome_tea:function()
  {
    if (this.data.multiIndex5[0] == 0 && this.data.multiIndex4[0] == 0 && this.data.multiIndex3[0] == 0 && this.data.multiIndex2[0] == 0 && this.data.multiIndex1[0] == 0)
    {
      wx.showModal({
        title: '提示',
        showCancel: false,
        content: '您尚未选择关注院校!',
        success: function (res) {
          console.log('用户点击确定')
        }
      })
    } else
     {
      wx.redirectTo({
        url: '../home_teacher/home_teacher',
      })}
    
  }
})