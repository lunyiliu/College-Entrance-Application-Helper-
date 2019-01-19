var app = getApp();
Page({
  data: {
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
    selected_school: app.globalData.SelectedSchool,
    success_ratio: app.globalData.success_ratio,
    img: app.globalData.SelectedSchoolID,
    banner_url1: ['../../SchoolPic/' + app.globalData.SelectedSchool[0] + '/1.jpg', '../../SchoolPic/' + app.globalData.SelectedSchool[0] + '/2.jpg', '../../SchoolPic/' + app.globalData.SelectedSchool[0] + '/3.jpg', '../../SchoolPic/' + app.globalData.SelectedSchool[0] + '/4.jpg'],
    banner_url2: ['../../SchoolPic/' + app.globalData.SelectedSchool[1] + '/1.jpg', '../../SchoolPic/' + app.globalData.SelectedSchool[1] + '/2.jpg', '../../SchoolPic/' + app.globalData.SelectedSchool[1] + '/3.jpg', '../../SchoolPic/' + app.globalData.SelectedSchool[1] + '/4.jpg'],
    banner_url3: ['../../SchoolPic/' + app.globalData.SelectedSchool[2] + '/1.jpg', '../../SchoolPic/' + app.globalData.SelectedSchool[2] + '/2.jpg', '../../SchoolPic/' + app.globalData.SelectedSchool[2] + '/3.jpg', '../../SchoolPic/' + app.globalData.SelectedSchool[2] + '/4.jpg'],
    banner_url4: ['../../SchoolPic/' + app.globalData.SelectedSchool[3] + '/1.jpg', '../../SchoolPic/' + app.globalData.SelectedSchool[3] + '/2.jpg', '../../SchoolPic/' + app.globalData.SelectedSchool[3] + '/3.jpg', '../../SchoolPic/' + app.globalData.SelectedSchool[3] + '/4.jpg'],
    banner_url5: ['../../SchoolPic/' + app.globalData.SelectedSchool[4] + '/1.jpg', '../../SchoolPic/' + app.globalData.SelectedSchool[4] + '/2.jpg', '../../SchoolPic/' + app.globalData.SelectedSchool[4] + '/3.jpg', '../../SchoolPic/' + app.globalData.SelectedSchool[4] + '/4.jpg'],

  },
  listenerLogin: function () {
    console.log('2',this.banner_url1);
    //页面跳转
    wx.navigateTo({
      url: '../list/list'
    })  
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

  },
  ToRecommend: function () {
    //页面跳转
    wx.navigateTo({
      url: '../recommend/recommend'
    })

  },
  bindPickerChange: function (e) {
    var i = e.currentTarget.dataset.id
    var up = "index" + i;
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      [up]: e.detail.value
    })
  },
})