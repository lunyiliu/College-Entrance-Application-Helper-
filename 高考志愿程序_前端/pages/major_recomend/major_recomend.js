var app = getApp();
Page({
  data: {
    start: ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    SchoolName: app.globalData.SchoolName,
    SchoolID: app.globalData.SchoolID,
    Score: app.globalData.SchoolScore,
    SchoolList: app.globalData.AllSchool,
  },

  listenerLogin: function() {
    //页面跳转
    wx.navigateTo({
      url: '../tianbao/tianbao'
    })
  },

  addfocus: function(e) {
    //添加、取消关注
    var i = parseInt(e.currentTarget.dataset.id)
    console.log(e)
    if (e.currentTarget.dataset.click == 'start') {
      var up = "start[" + i + "]";
      this.setData({
        [up]: '0'
      })
      app.globalData.FocusSchool.push(this.data.SchoolName[i])
      app.globalData.FocusSchoolID.push(this.data.SchoolID[i])
      console.log(app.globalData.FocusSchool)
      console.log(app.globalData.FocusSchoolID)
    } else {
      var up = "start[" + i + "]";
      this.setData({
        [up]: '1'
      })
      for (var index in app.globalData.FocusSchool) {
        if (this.data.SchoolName[i] == app.globalData.FocusSchool[index]) {
          app.globalData.FocusSchool.splice(index, 1)
          app.globalData.FocusSchoolID.splice(index, 1)
          console.log(app.globalData.FocusSchool)
          console.log(app.globalData.FocusSchoolID)
        }
      }
    }
  }
})