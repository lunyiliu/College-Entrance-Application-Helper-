Page({
bindGetUserInfo:  function(e) {
  var  that  =  this;
  //此处授权得到user NickName
  console.log(e.detail.userInfo);
  getApp().globalData.nickName = e.detail.userInfo.nickName;
  wx.setStorage({
    key: '123456',
    data: getApp().globalData.nickName

  })
  //最后，记得返回刚才的页面
  wx.navigateBack({
    delta:  1
  })


}
})