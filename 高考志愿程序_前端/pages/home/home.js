var app = getApp();
Page({
  data: {
    Province: app.globalData.StudentProvince,
    Kelei: app.globalData.StudentKelei,
    Grade: app.globalData.StudentGrade,
    Rank: app.globalData.StudentRank,
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
    var stu = wx.getStorageSync('student');
    // console.log(this.data.myinfo);
    this.Province=app.globalData.StudentProvince,
    this.Kelei=app.globalData.StudentKelei,
    this.Grade=app.globalData.StudentGrade,
    this.Rank=app.globalData.StudentRank,
    console.log('所在省份: ', this.Province);
    console.log('科类为: ', this.Kelei);
    console.log('成绩为: ', this.Grade);
    console.log('排名为: ', this.Rank);
  },
  exit: function (e) {
    wx.showModal({
      title: '提示',
      content: '是否修改信息？',
      success: function (res) {
        if (res.confirm) {
          // console.log('用户点击确定')
          wx.removeStorageSync('student');
          //页面跳转
          wx.redirectTo({
            url: '../index/index',
          })
        } else if (res.cancel) {
          console.log('用户点击取消')
        }
      }
    })
  },
  resetpwd: function (e) {
    var no = this.data.myinfo.no;
    wx.navigateTo({
      url: '../password/password?no=' + no,
    })
  },
  setemail: function (e) {
    var no = this.data.myinfo.no;
    wx.navigateTo({
      url: '../email/email?no=' + no,
    })
  }
})