var app = getApp();
let Charts = require('../../wx-charts-master/dist/wxcharts.js');

Page({
  data: {
    focusschool:app.globalData.FocusSchool,
    focusschoolID:app.globalData.FocusSchoolID,
    isShowFrom1: false,
    isShowFrom2: false,
    isShowFrom3: false,
    isShowFrom4: false,
    isShowFrom5: false,
    indicatorDots: true,
    vertical: false,
    autoplay: true,
    interval: 3000,
    duration: 800,
    //以下应全部改为FocusSchool
    /*
    AccomandSchool: app.globalData.AccomandSchool,
    AccomandSchoolID: app.globalData.AccomandSchoolID,
    banner_url1: ['../../SchoolPic/' + app.globalData.AccomandSchool[0] + '/1.jpg', '../../SchoolPic/' + app.globalData.AccomandSchool[0] + '/2.jpg', '../../SchoolPic/' + app.globalData.AccomandSchool[0] + '/3.jpg', '../../SchoolPic/' + app.globalData.AccomandSchool[0] + '/4.jpg'],
    banner_url2: ['../../SchoolPic/' + app.globalData.AccomandSchool[1] + '/1.jpg', '../../SchoolPic/' + app.globalData.AccomandSchool[1] + '/2.jpg', '../../SchoolPic/' + app.globalData.AccomandSchool[1] + '/3.jpg', '../../SchoolPic/' + app.globalData.AccomandSchool[1] + '/4.jpg'],
    banner_url3: ['../../SchoolPic/' + app.globalData.AccomandSchool[2] + '/1.jpg', '../../SchoolPic/' + app.globalData.AccomandSchool[2] + '/2.jpg', '../../SchoolPic/' + app.globalData.AccomandSchool[2] + '/3.jpg', '../../SchoolPic/' + app.globalData.AccomandSchool[2] + '/4.jpg'],
    banner_url4: ['../../SchoolPic/' + app.globalData.AccomandSchool[3] + '/1.jpg', '../../SchoolPic/' + app.globalData.AccomandSchool[3] + '/2.jpg', '../../SchoolPic/' + app.globalData.AccomandSchool[3] + '/3.jpg', '../../SchoolPic/' + app.globalData.AccomandSchool[3] + '/4.jpg'],
    banner_url5: ['../../SchoolPic/' + app.globalData.AccomandSchool[4] + '/1.jpg', '../../SchoolPic/' + app.globalData.AccomandSchool[4] + '/2.jpg', '../../SchoolPic/' + app.globalData.AccomandSchool[4] + '/3.jpg', '../../SchoolPic/' + app.globalData.AccomandSchool[4] + '/4.jpg'],
  },
  onLoad: function () {
    new Charts({
      canvasId: 'Canvas1',
      type: 'line',
      categories: ['2012', '2013', '2014', '2015', '2016'],
      series: [{
        name: '校线',
        data: [625, 666, 683, 0, 678],
      }, {
        name: '省市分数线',
        data: [477, 550, 543, 548, 548],
      }],
      yAxis: {
        title: '历年分数线',
        min: 0
      },
      width: 330,
      height: 200
    });
    new Charts({
      canvasId: 'Canvas2',
      type: 'line',
      categories: ['2013', '2014', '2015', '2016', '2017'],
      series: [{
        name: '校线',
        data: [634, 656, 0, 670, 649],
      }, {
        name: '省市分数线',
        data: [550, 543, 548, 548, 537],
      }],
      yAxis: {
        title: '历年分数线',
        min: 0
      },
      width: 330,
      height: 200
    });
    new Charts({
      canvasId: 'Canvas3',
      type: 'line',
      categories: ['2013', '2014', '2015', '2016', '2017'],
      series: [{
        name: '校线',
        data: [671, 682, 694, 680, 671],
      }, {
        name: '省市分数线',
        data: [550, 543, 548, 548, 537],
      }],
      yAxis: {
        title: '历年分数线',
        min: 0
      },
      width: 330,
      height: 200
    });
    new Charts({
      canvasId: 'Canvas4',
      type: 'line',
      categories: ['2013', '2014', '2015', '2016', '2017'],
      series: [{
        name: '校线',
        data: [640, 645, 673, 659, 650],
      }, {
        name: '省市分数线',
        data: [550, 543, 548, 548, 537],
      }],
      yAxis: {
        title: '历年分数线',
        min: 0
      },
      width: 330,
      height: 200
    });
    new Charts({
      canvasId: 'Canvas5',
      type: 'line',
      categories: ['2013', '2014', '2015', '2016', '2017'],
      series: [{
        name: '校线',
        data: [627, 640, 0, 605, 643],
      }, {
        name: '省市分数线',
        data: [550, 543, 548, 548, 537],
      }],
      yAxis: {
        title: '历年分数线',
        min: 0
      },
      width: 330,
      height: 200
    });
  },
  showFrom(e) {
    var param = e.target.dataset.param;
    this.setData({
      isShowFrom1: param == 1 ? (!this.data.isShowFrom1) : false,
      isShowFrom2: param == 2 ? (!this.data.isShowFrom2) : false,
      isShowFrom3: param == 3 ? (!this.data.isShowFrom3) : false,
      isShowFrom4: param == 4 ? (!this.data.isShowFrom4) : false,
      isShowFrom5: param == 5 ? (!this.data.isShowFrom5) : false
    });
*/
  },
  


})