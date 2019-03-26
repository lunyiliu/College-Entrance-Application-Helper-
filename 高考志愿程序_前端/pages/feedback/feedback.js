var app = getApp();
Page({
  data: {
    
  },

  /**
   * 生命周期函数--监听页面加载
   */
  exit: function (e) {
    wx.showModal({
      title: '提示',
      content: '是否提交意见？',
      success: function (res) {
        if (res.confirm) {
          // console.log('用户点击确定')
          wx.removeStorageSync('student');
          //页面跳转
          wx.switchTab({
            url: '../home/home',
          })
        } else if (res.cancel) {
          console.log('用户点击取消')
        }
      }
    })
  },
  
  
})