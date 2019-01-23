Page({
  onLoad: function() {
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
    wx.login({
      success: function(data) {
        console.log('获取登录 Code：' + data.code)
        var postData = {
          code: data.code

        };
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
            console.log('getOpenID-OK!');
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
      },
      
      fail: function() {
        console('登录获取Code失败！');
      }
    })
  },
})