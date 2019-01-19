var app = getApp();


Page({
  data: {
    index1: 0,
    index2: 0,
    index3: 0,
    index4: 0,
    index5: 0,
    focusSchool: app.globalData.FocusSchool,
    focusSchoolid: app.globalData.FocusSchoolID,
  },
  listenerLogin: function() {
    if (this.data.index1 != 0 && this.data.index2 != 0 && this.data.index3 != 0 && this.data.index4 != 0 && this.data.index5 != 0 && this.data.index1 != this.data.index2 && this.data.index1 != this.data.index3 && this.data.index1 != this.data.index4 && this.data.index1 != this.data.index5 && this.data.index2 != this.data.index3 && this.data.index2 != this.data.index4 && this.data.index2 != this.data.index5 && this.data.index3 != this.data.index4 && this.data.index3 != this.data.index5 && this.data.index4 != this.data.index5) {
      app.globalData.SelectedSchool.push(this.data.focusSchool[this.data.index1]);
      app.globalData.SelectedSchoolID.push(this.data.focusSchoolid[this.data.index1]);
      app.globalData.SelectedSchool.push(this.data.focusSchool[this.data.index2]);
      app.globalData.SelectedSchoolID.push(this.data.focusSchoolid[this.data.index2]);
      app.globalData.SelectedSchool.push(this.data.focusSchool[this.data.index3]);
      app.globalData.SelectedSchoolID.push(this.data.focusSchoolid[this.data.index3]);
      app.globalData.SelectedSchool.push(this.data.focusSchool[this.data.index4]);
      app.globalData.SelectedSchoolID.push(this.data.focusSchoolid[this.data.index4]);
      app.globalData.SelectedSchool.push(this.data.focusSchool[this.data.index5]);
      app.globalData.SelectedSchoolID.push(this.data.focusSchoolid[this.data.index5]);
      console.log('一志愿学校为', app.globalData.SelectedSchool[0]);
      console.log('二志愿学校为', app.globalData.SelectedSchool[1]);
      console.log('三志愿学校为', app.globalData.SelectedSchool[2]);
      console.log('四志愿学校为', app.globalData.SelectedSchool[3]);
      console.log('五志愿学校为', app.globalData.SelectedSchool[4]);
      //页面跳转
      wx.navigateTo({
        url: '../result/result'
      })
    } else {
      if (this.data.index1 == 0) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确填写一志愿!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      } else if (this.data.index2 == 0 || this.data.index2 == this.data.index1) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确填写二志愿!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      } else if (this.data.index3 == 0 || this.data.index3 == this.data.index2 || this.data.index3 == this.data.index1) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确填写三志愿!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      } else if (this.data.index4 == 0 || this.data.index4 == this.data.index3 || this.data.index4 == this.data.index2 || this.data.index4 == this.data.index1) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确填写四志愿!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      } else if (this.data.index5 == 0 || this.data.index5 == this.data.index4 || this.data.index5 == this.data.index3 || this.data.index5 == this.data.index2 || this.data.index5 == this.data.index1) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确填写五志愿!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      }
    }
  },
  bindPickerChange: function(e) {
    var i = e.currentTarget.dataset.id
    var up = "index" + i;
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      [up]: e.detail.value
    })
  },
})