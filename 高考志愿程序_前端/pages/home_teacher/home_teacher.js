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
    this.setData({
      Province:app.globalData.StudentProvince,
      Kelei: app.globalData.StudentKelei,
      Grade: app.globalData.StudentGrade,
      Rank: app.globalData.StudentRank,
    })
  },
  jumptohistroy:function(e)
  {
    console.log('执行')
    wx.redirectTo({
      url: '../histroy/histroy',
    })
  },
  jumptofocus: function (e) {
    console.log('执行')
    wx.redirectTo({
      url: '../showfocusteacher/showfocusteacher',
    })
  },
  jumptomessage: function (e) {
    console.log('执行')
    wx.redirectTo({
      url: '../message/message',
    })
  },
  jumptohelp: function (e) {
    console.log('执行')
    wx.redirectTo({
      url: '../help/help',
    })
  },
  jumptofeedback: function (e) {
    console.log('执行')
    wx.redirectTo({
      url: '../feedback/feedback',
    })
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