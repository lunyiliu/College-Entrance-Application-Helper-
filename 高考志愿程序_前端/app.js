   //app.js
App({
  globalData: {
    //以下是从后端接收到的考生选填的学校的全部专业
    School1: ['未选择省份', '北京', '天津', '河北', '山西', '山东', '河南', '内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '福建', '上海', '浙江', '安徽', '江西', '湖南', '湖北', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '陕西', '西藏', '甘肃', '青海', '宁夏', '新疆'],
    School2: ['未选择省份', '北京', '天津', '河北', '山西', '山东', '河南', '内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '福建', '上海', '浙江', '安徽', '江西', '湖南', '湖北', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '陕西', '西藏', '甘肃', '青海', '宁夏', '新疆'],
    School3: ['未选择省份', '北京', '天津', '河北', '山西', '山东', '河南', '内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '福建', '上海', '浙江', '安徽', '江西', '湖南', '湖北', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '陕西', '西藏', '甘肃', '青海', '宁夏', '新疆'],
    School4: ['未选择省份', '北京', '天津', '河北', '山西', '山东', '河南', '内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '福建', '上海', '浙江', '安徽', '江西', '湖南', '湖北', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '陕西', '西藏', '甘肃', '青海', '宁夏', '新疆'],
    School5: ['未选择省份', '北京', '天津', '河北', '山西', '山东', '河南', '内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '福建', '上海', '浙江', '安徽', '江西', '湖南', '湖北', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '陕西', '西藏', '甘肃', '青海', '宁夏', '新疆'],
    School6: ['未选择省份', '北京', '天津', '河北', '山西', '山东', '河南', '内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '福建', '上海', '浙江', '安徽', '江西', '湖南', '湖北', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '陕西', '西藏', '甘肃', '青海', '宁夏', '新疆'],
    //以下是考生填报的专业志愿
    School1Major: [0, 0, 0, 0, 0, 0],
    School2Major: [0, 0, 0, 0, 0, 0],
    School3Major: [0, 0, 0, 0, 0, 0],
    School4Major: [0, 0, 0, 0, 0, 0],
    School5Major: [0, 0, 0, 0, 0, 0],
    School6Major: [0, 0, 0, 0, 0, 0],
    nickName: ' ',
    flag:0,
    userID: '',
    StudentProvince: 0,
    StudentKelei: 0,
    StudentGrade: 0,
    StudentRank: 0,
    multiindex1:[0,0],
    multiindex2: [0, 0],
    multiindex3: [0, 0],
    multiindex4: [0, 0],
    multiindex5: [0, 0],
    AllSchool: ['北京工业大学', '北京大学', '内蒙古大学', '西北大学', '北京交通大学', '哈尔滨工业大学', '大连海事大学', '北京外国语大学', '云南大学', '长安大学'],
    //SelectedSchool为考生填报的学校
    SelectedSchool:[],
    SelectedSchoolID: [],
    //FocusSchool为考生关注的学校
    FocusSchool: ['学校名称'],
    FocusSchoolID:['id'],
    SchoolName: ['北京工业大学', '北京大学', '内蒙古大学', '西北大学', '北京交通大学', '哈尔滨工业大学', '大连海事大学', '北京外国语大学', '云南大学', '长安大学'],
    SchoolID: [44, 1, 61, 101, 43, 14, 63, 51, 99, 113],
    SchoolScore: [
      [
        ['2017', '580'],
        ['2016', '--'],
        ['2015', '--']
      ],
      [
        ['2017', '660'],
        ['2016', '673'],
        ['2015', '--']
      ],
      [
        ['2017', '556'],
        ['2016', '--'],
        ['2015', '--']
      ],
      [
        ['2017', '595'],
        ['2016', '605'],
        ['2015', '--']
      ],
      [
        ['2017', '608'],
        ['2016', '640'],
        ['2015', '--']
      ],
      [
        ['2017', '609'],
        ['2016', '632'],
        ['2015', '628']
      ],
      [
        ['2017', '566'],
        ['2016', '589'],
        ['2015', '--']
      ],
      [
        ['2017', '637'],
        ['2016', '650'],
        ['2015', '--']
      ],
      [
        ['2017', '--'],
        ['2016', '--'],
        ['2015', '--']
      ],
      [
        ['2017', '--'],
        ['2016', '--'],
        ['2015', '--']
      ]
    ]
  },
  onLaunch: function() {
    console.log('App Launch')
  },
  onShow: function() {
    console.log('App Show')
  },
  onHide: function() {
    console.log('App Hide')
  }
})