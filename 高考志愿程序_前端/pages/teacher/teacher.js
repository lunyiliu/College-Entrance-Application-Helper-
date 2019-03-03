var app = getApp();
Page({
  data: {
    Name: 0,
    Work: 0,
    Invitation: 0,
    canIUse: wx.canIUse('button.open-type.getUserInfo')
  },
  jumptohome: function(e) {
    wx.redirectTo({
      url: '../home/home',
    })
  },
  /** * 监听姓名输入 */
  listenerNameInput: function(e) {
    this.data.Name = e.detail.value;
  },
  /** * 监听工作单位输入 */
  listenerWorkInput: function(e) {
    this.data.Work = e.detail.value;
  },
  /** * 监听邀请码输入 */
  listenerInvitationInput: function(e) {
    this.data.Invitation = e.detail.value;
  },
  /** * 监听登录按钮 */
  listenertestInput: function(e) {
    this.data.result = e.detail.value;
  },
  onLoad: function() {
    // 查看是否授权
    wx.getSetting({
      success: function(res) {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称
          wx.getUserInfo({
            success: function(res) {
              console.log(res.userInfo)
            }
          })
        }
      }
    })
  },
  listenerLogin: function() {

    //更改变量
    //app.globalData.StudentProvince = this.data.selectData1[parseInt(this.data.Province)];
    //app.globalData.StudentKelei = this.data.area[parseInt(this.data.Kelei)];
    //app.globalData.StudentGrade = this.data.Grade;
    //app.globalData.StudentRank = this.data.Rank;


    //页面跳转
    wx.switchTab({
      url: '../home/home'
    })
  },
  bindPickerChange: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      Kelei: e.detail.value,
      areaIndex: e.detail.value
    })
  },
  bindPickerChange1: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      Province: e.detail.value,
      index: e.detail.value
    })
  },
  onReady: function() {

    // 页面渲染完成 
  },
  onShow: function() {
    // 页面显示 
  },
  onHide: function() {
    // 页面隐藏 
  },
  onUnload: function() {
    // 页面关闭 
  }
})