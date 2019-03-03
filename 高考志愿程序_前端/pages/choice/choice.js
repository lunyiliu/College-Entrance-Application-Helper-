var app = getApp();
Page({
  data: {
  },

  jumptoteacher: function (e) {
    wx.showModal({
      title: '提示',
      content: '你当前选择的身份为教师',
      success: function (res) {
        if (res.confirm) {
          // console.log('用户点击确定')
          wx.removeStorageSync('student');
          //页面跳转
          wx.redirectTo({
            url: '../teacher/teacher',
          })
        } else if (res.cancel) {
          console.log('用户点击取消')
        }
      }
    })
  },
  jumptostudent: function (e) {
    wx.showModal({
      title: '提示',
      content: '您当前选择的身份是学生',
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
})
