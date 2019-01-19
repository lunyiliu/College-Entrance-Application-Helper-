var app = getApp();

Page({
  /** * 初始化数据 */
  data: {
    Province: 0,
    Kelei: 0,
    Grade: 0,
    Rank: 0,
    show: false, //控制下拉列表的显示隐藏，false隐藏、true显示
    selectData1: ['未选择省份', '北京', '天津', '河北', '山西', '山东', '河南', '内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '福建', '上海', '浙江', '安徽', '江西', '湖南', '湖北', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '陕西', '西藏', '甘肃', '青海', '宁夏', '新疆'],
    area: ['未选择科类', '文史', '理工', '不分文理'], //下拉列表的数据
    index: 0, //选择的下拉列表下标
    areaIndex: 0,
  },

  /** * 监听成绩输入 */
  listenerGradeInput: function(e) {
    this.data.Grade = e.detail.value;
  },
  /** * 监听排名输入 */
  listenerRankInput: function(e) {
    this.data.Rank = e.detail.value;
  },
  /** * 监听登录按钮 */
  listenertestInput: function(e) {
    this.data.result = e.detail.value;
  },
  listenerLogin: function() {
    if (this.data.Province != 0 && this.data.Kelei != 0 && this.data.Grade != 0 && this.data.Grade <= 750 && this.data.Rank > 0) {
      //更改变量
      app.globalData.StudentProvince = this.data.selectData1[parseInt(this.data.Province)];
      app.globalData.StudentKelei = this.data.area[parseInt(this.data.Kelei)];
      app.globalData.StudentGrade = this.data.Grade;
      app.globalData.StudentRank = this.data.Rank;
      //打印信息 
      console.log('所在省份: ', app.globalData.StudentProvince);
      console.log('科类为: ', app.globalData.StudentKelei);
      console.log('成绩为: ', app.globalData.StudentGrade);
      console.log('排名为: ', app.globalData.StudentRank);
      //页面跳转
      wx.navigateTo({
        url: '../list/list'
      })
    }
     else {
      if (this.data.Province == 0) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确选择省份!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      } else if (this.data.Kelei == 0) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确选择科类!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      } else if (this.data.Grade == 0 || parseInt(this.data.Grade) > 750) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确填写分数!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      } else if (this.data.Rank == 0 || parseInt(this.data.Rank) <= 0) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确填写名次!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      }
    }
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