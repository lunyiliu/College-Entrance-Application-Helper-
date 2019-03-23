var app = getApp();
Page({
  data: {
    selectData1: app.globalData.School1,
    selectData2: app.globalData.School2,
    selectData3: app.globalData.School3,
    selectData4: app.globalData.School4,
    selectData5: app.globalData.School5,
    selectData6: app.globalData.School6,
    index1_1: 0, index1_2: 0, index1_3: 0, index1_4: 0, index1_5: 0, index1_6: 0,
    index2_1: 0, index2_2: 0, index2_3: 0, index2_4: 0, index2_5: 0, index2_6: 0,
    index3_1: 0, index3_2: 0, index3_3: 0, index3_4: 0, index3_5: 0, index3_6: 0,
    index4_1: 0, index4_2: 0, index4_3: 0, index4_4: 0, index4_5: 0, index4_6: 0,
    index5_1: 0, index5_2: 0, index5_3: 0, index5_4: 0, index5_5: 0, index5_6: 0,
    index6_1: 0, index6_2: 0, index6_3: 0, index6_4: 0, index6_5: 0, index6_6: 0,

    zhiyuan1: [0, 0, 0, 0, 0, 0],
    zhiyuan2: [0, 0, 0, 0, 0, 0],
    zhiyuan3: [0, 0, 0, 0, 0, 0],
    zhiyuan4: [0, 0, 0, 0, 0, 0],
    zhiyuan5: [0, 0, 0, 0, 0, 0],
    zhiyuan6: [0, 0, 0, 0, 0, 0],

    isShowFrom1: false,
    isShowFrom2: false,
    isShowFrom3: false,
    isShowFrom4: false,
    isShowFrom5: false,
    isShowFrom6: false,
    indicatorDots: true,
    vertical: false,
    autoplay: true,
    interval: 3000,
    duration: 800,
    selected_school: app.globalData.SelectedSchool,
    img: app.globalData.SelectedSchoolID,

  },
  showFrom(e) {
    var param = e.target.dataset.param;
    this.setData({
      isShowFrom1: param == 1 ? (!this.data.isShowFrom1) : false,
      isShowFrom2: param == 2 ? (!this.data.isShowFrom2) : false,
      isShowFrom3: param == 3 ? (!this.data.isShowFrom3) : false,
      isShowFrom4: param == 4 ? (!this.data.isShowFrom4) : false,
      isShowFrom5: param == 5 ? (!this.data.isShowFrom5) : false,
      isShowFrom6: param == 6 ? (!this.data.isShowFrom6) : false
    });

  },

  sum: function (arr) {
    var s = 1;
    for (var i = arr.length - 1; i >= 0; i--) {
      s *= arr[i];
    }
    return s;
  },

  ToRecommend: function () {
    // if (this.sum(this.data.zhiyuan1) && this.sum(this.data.zhiyuan2) && this.sum(this.data.zhiyuan3) && this.sum(this.data.zhiyuan4) && this.sum(this.data.zhiyuan5) && this.sum(this.data.zhiyuan6)){
      for (var i = 0; i < 6; i++){
        app.globalData.School1Major[i] = this.data.selectData1[this.data.zhiyuan1[i]];
      }
      for (var i = 0; i < 6; i++) {
        app.globalData.School2Major[i] = this.data.selectData2[this.data.zhiyuan2[i]];
      }
      for (var i = 0; i < 6; i++) {
        app.globalData.School3Major[i] = this.data.selectData3[this.data.zhiyuan3[i]];
      }
      for (var i = 0; i < 6; i++) {
        app.globalData.School4Major[i] = this.data.selectData4[this.data.zhiyuan4[i]];
      }
      for (var i = 0; i < 6; i++) {
        app.globalData.School5Major[i] = this.data.selectData5[this.data.zhiyuan5[i]];
      }
      for (var i = 0; i < 6; i++) {
        app.globalData.School6Major[i] = this.data.selectData6[this.data.zhiyuan6[i]];
      }
      
      console.log(app.globalData.School1Major)
      console.log(app.globalData.School2Major)
      console.log(app.globalData.School3Major)
      console.log(app.globalData.School4Major)
      console.log(app.globalData.School5Major)
      console.log(app.globalData.School6Major)
    //页面跳转
    wx.navigateTo({
      url: '../recommend/recommend'
    })
    //}
    // else {
    //   console.log(this.data.zhiyuan1)
    //   console.log(this.sum(this.data.zhiyuan1))
    //   if (this.sum(this.data.zhiyuan1) == 0) {
    //     console.log(this.data.zhiyuan1)
    //     console.log(this.sum(this.data.zhiyuan1))
    //     wx.showModal({
    //       title: '提示',
    //       showCancel: false,
    //       content: '请填写所有一志愿学校专业!',
    //       success: function (res) {
    //         console.log('用户点击确定')
    //       }
    //     })
    //   } else if (this.sum(this.data.zhiyuan2) == 0) {
    //     wx.showModal({
    //       title: '提示',
    //       showCancel: false,
    //       content: '请填写所有二志愿学校专业!',
    //       success: function (res) {
    //         console.log('用户点击确定')
    //       }
    //     })
    //   } else if (this.sum(this.data.zhiyuan3) == 0) {
    //     wx.showModal({
    //       title: '提示',
    //       showCancel: false,
    //       content: '请填写所有三志愿学校专业!',
    //       success: function (res) {
    //         console.log('用户点击确定')
    //       }
    //     })
    //   } else if (this.sum(this.data.zhiyuan4) == 0) {
    //     wx.showModal({
    //       title: '提示',
    //       showCancel: false,
    //       content: '请填写所有四志愿学校专业!',
    //       success: function (res) {
    //         console.log('用户点击确定')
    //       }
    //     })
    //   } else if (this.sum(this.data.zhiyuan5) == 0) {
    //     wx.showModal({
    //       title: '提示',
    //       showCancel: false,
    //       content: '请填写所有五志愿学校专业!',
    //       success: function (res) {
    //         console.log('用户点击确定')
    //       }
    //     })
    //   } else if (this.sum(this.data.zhiyuan6) == 0) {
    //     wx.showModal({
    //       title: '提示',
    //       showCancel: false,
    //       content: '请填写所有六志愿学校专业!',
    //       success: function (res) {
    //         console.log('用户点击确定')
    //       }
    //     })
    //   }
    // }

  },
  bindPickerChange1_1: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan1[" + 0 + "]";
    that.setData({ [zhiyuan]: e.detail.value})
    this.setData({index1_1:e.detail.value})
  },
  bindPickerChange1_2: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan1[" + 1 + "]";
    that.setData({ [zhiyuan]: e.detail.value })    
    this.setData({ index1_2: e.detail.value })
  },
  bindPickerChange1_3: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan1[" + 2 + "]";
    var S_Data = "selectData1[e.detail.value]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index1_3: e.detail.value })
  },
  bindPickerChange1_4: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan1[" + 3 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index1_4: e.detail.value })
  },
  bindPickerChange1_5: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan1[" + 4 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index1_5: e.detail.value })
  },
  bindPickerChange1_6: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan1[" + 5 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index1_6: e.detail.value })
  },

  bindPickerChange2_1: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan2[" + 0 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index2_1: e.detail.value })
  },
  bindPickerChange2_2: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan2[" + 1 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index2_2: e.detail.value })
  },
  bindPickerChange2_3: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan2[" + 2 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index2_3: e.detail.value })
  },
  bindPickerChange2_4: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan2[" + 3 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index2_4: e.detail.value })
  },
  bindPickerChange2_5: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan2[" + 4 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index2_5: e.detail.value })
  },
  bindPickerChange2_6: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan2[" + 5 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index2_6: e.detail.value })
  },

  bindPickerChange3_1: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan3[" + 0 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index3_1: e.detail.value })
  },
  bindPickerChange3_2: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan3[" + 1 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index3_2: e.detail.value })
  },
  bindPickerChange3_3: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan3[" + 2 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index3_3: e.detail.value })
  },
  bindPickerChange3_4: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan3[" + 3 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index3_4: e.detail.value })
  },
  bindPickerChange3_5: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan3[" + 4 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index3_5: e.detail.value })
  },
  bindPickerChange3_6: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan3[" + 5 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index3_6: e.detail.value })
  },

  bindPickerChange4_1: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan4[" + 0 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index4_1: e.detail.value })
  },
  bindPickerChange4_2: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan4[" + 1 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index4_2: e.detail.value })
  },
  bindPickerChange4_3: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan4[" + 2 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index4_3: e.detail.value })
  },
  bindPickerChange4_4: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan4[" + 3 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index4_4: e.detail.value })
  },
  bindPickerChange4_5: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan4[" + 4 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index4_5: e.detail.value })
  },
  bindPickerChange4_6: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan4[" + 5 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index4_6: e.detail.value })
  },

  bindPickerChange5_1: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan5[" + 0 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index5_1: e.detail.value })
  },
  bindPickerChange5_2: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan5[" + 1 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index5_2: e.detail.value })
  },
  bindPickerChange5_3: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan5[" + 2 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index5_3: e.detail.value })
  },
  bindPickerChange5_4: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan5[" + 3 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index5_4: e.detail.value })
  },
  bindPickerChange5_5: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan5[" + 4 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index5_5: e.detail.value })
  },
  bindPickerChange5_6: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan5[" + 5 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index5_6: e.detail.value })
  },

  bindPickerChange6_1: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan6[" + 0 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index6_1: e.detail.value })
  },
  bindPickerChange6_2: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan6[" + 1 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index6_2: e.detail.value })
  },
  bindPickerChange6_3: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan6[" + 2 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index6_3: e.detail.value })
  },
  bindPickerChange6_4: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan6[" + 3 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index6_4: e.detail.value })
  },
  bindPickerChange6_5: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan6[" + 4 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index6_5: e.detail.value })
  },
  bindPickerChange6_6: function (e) {
    var that = this;
    var zhiyuan = "zhiyuan6[" + 5 + "]";
    that.setData({ [zhiyuan]: e.detail.value })
    this.setData({ index6_6: e.detail.value })
  },
})