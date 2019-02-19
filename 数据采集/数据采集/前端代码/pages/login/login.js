Page({
  onLoad: function() {
    //wx.clearStorageSync()
    wx.loadFontFace({
      family: 'webfont',
      source: 'url("//at.alicdn.com/t/webfont_1f7b3qbimiv.eot")',
      success: function(res) {
        console.log(res.status) // loaded 
      },
      fail: function(res) {
        console.log(res.status) // error 
      },
      complete: function(res) {
        console.log(res.status);
      }
    });
  },
  bingGetOpenID: function() {
    var app = getApp();
    wx.login({
      success: function(data) {
        console.log('获取登录 Code：' + data.code)
        var postData = {
          code: data.code

        };
          /**
           * 获取用户信息
           */
      //console.log(app.globalData.nickName)
          const value = wx.getStorageSync('123456')
          if (value) {
            app.globalData.nickName = value
            console.log(value)
          }
          else{
            app.globalData.nickName == ' '
          }
          /*
        if (app.globalData.nickName == ' ') {

          
            wx.showModal({
              title:  '警告',
              content:  '尚未进行授权，请点击确定跳转到授权页面进行授权。',
              success:  function  (res)  {
                if  (res.confirm)  {
                  console.log('用户同意授权')
                  wx.navigateTo({
                    url:  '../authorization/authorization',
    
                  })
                }
              }
            })
            
        }
      */    
        if (app.globalData.nickName != ' ') {
        wx.showLoading({
          title: '登录中...',
        });
        wx.request({
          url: 'https://lunyiliu.eicp.vip/login.php', //注意改成自己的服务器请求地址哦！ 
          data: postData,
          method: 'POST', // OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, CONNECT 
          header: {
            'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
          },
          success: function(res) { //回调处理 
            console.log(res);
            getApp().globalData.userID = res.data.openid;
            console.log(getApp().globalData.userID);
            wx.hideLoading();
            wx.navigateTo({
              url: '../dataCollection/dataCollection'
            })
          },
          fail: function(error) {
            console.log(error);
          }
        })
      }
      },
      
      fail: function() {
        console('登录获取Code失败！');
      }
    })
  },
  bindGetUserInfo: function (e) {
    var app = getApp();
    if (app.globalData.nickName == ' ') {
    var that = this;
    //此处授权得到user NickName
    console.log(e.detail.userInfo);
    getApp().globalData.nickName = e.detail.userInfo.nickName;
    wx.setStorage({
      key: '123456',
      data: getApp().globalData.nickName
    })
    wx.setStorage({
        key: 'IsFirstTime',
        data: 1
      })
    }
  },
})