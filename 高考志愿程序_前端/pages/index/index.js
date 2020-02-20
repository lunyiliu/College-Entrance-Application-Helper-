var app = getApp();

Page({
  /** * 初始化数据 */
  data: {
    Province: 0,
    Kelei: 0,
    Grade: 0,
    Rank: 0,
    show: false, //控制下拉列表的显示隐藏，false隐藏、true显示
    selectData1: ['未选择省份', '北京', '天津', '河北', '山西', '山东', '河南', '内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '福建', '上海', '浙江', '安徽', '江西', '湖南', '湖北', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '陕西', '西藏', '甘肃', '青海', '宁夏', '新疆', '香港', '澳门', '台湾'],
    provinceid: [0, 1, 2, 19, 20, 11, 22, 21, 3, 4, 5, 7, 10, 6, 8, 9, 31, 13, 12, 14, 24, 23, 15, 16, 25, 26, 17, 27, 18, 28, 29, 30,33,38,39],
    area: ['未选择科类', '文史', '理工', '不分文理'], //下拉列表的数据
    index: 0, //选择的下拉列表下标
    areaIndex: 0,
    canIUse: wx.canIUse('button.open-type.getUserInfo')
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
  onLoad: function () {
    // 查看是否授权
    wx.getSetting({
      success: function (res) {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称
          wx.getUserInfo({
            success: function (res) {
              console.log(res.userInfo)
            }
          })
        }
      }
    })
  },
  Update: function () {
    wx.showLoading({
      title: '提交中...',
    });
    var that = this;
    var app = getApp();
    console.log('交换数据')
    //若有标记则缓存中有数据，数据库中有用户信息
    if (app.globalData.flag) {
      //update_data
      console.log('更新数据')
      wx.request({
        url: 'https://lunyiliu.eicp.vip/Interface.php',
        data: {
          sql:'update client set score=?, province=?,subject=?,self_rank=? where user_nickname=? and userID=?',
          //凡是涉及到具体的值的，一律以？代替
          format:'ississ',//有多少个？就有多少个字符
          mode:'update',
          //这后面的变量安排要按照？出现的顺序
          trans_grade: app.globalData.StudentGrade,
          trans_province: app.globalData.StudentProvince,
          trans_kelei: app.globalData.StudentKelei,
          trans_rank: app.globalData.StudentRank,
          user_nickname: app.globalData.nickName,
          userID: app.globalData.userID,
          command: 'handle_data'
        },
        method: 'GET',
        header: {
          'content-type': 'application/json'
        },
        success: function (res) {
          console.log(res)
          wx.hideLoading()
        },
        fail: function (error) {
          console.log(error);
        }
      }

      )

    } else {
      //insert_data
      //request是异步执行的
      wx.showLoading({
        title: '提交中...',
      });
      console.log('插入数据')
      wx.request({
        url: 'https://lunyiliu.eicp.vip/Interface.php',
        data: {
          
          table:'client',
          userID: app.globalData.userID,
          user_nickname: app.globalData.nickName,
          score: app.globalData.StudentGrade,
          province: app.globalData.StudentProvince,
          //subject: app.globalData.StudentKelei,
          subject: '啦啦啦',
          year:2019,
          pici:'null',
          choose_list:'null',
          focus:'null',
          rank: app.globalData.StudentRank,
          history:'null',
          command: 'insert_data',
          
          /*
          table: 'test1',
          userID: '啦啦啦',
          user_nickname: app.globalData.nickName,
          score: app.globalData.StudentGrade,
          province: app.globalData.StudentProvince,
          //subject: app.globalData.StudentKelei,
          subject1: '啦啦啦1',
          command: 'insert_data'
          */
        },
        method: 'GET',
        header: {
          'content-type': 'application/json'
        },
        success: function (res) {
          console.log(res.data)
          wx.hideLoading();
        },
        fail: function (error) {
          console.log(error);
        }
      }

      )
    }

  },

  bindGetUserInfo: function (e) {
    var app = getApp();
    if (app.globalData.nickName == ' ') {
      var that = this;
      //此处授权得到user NickName
      console.log(e.detail.userInfo);
      getApp().globalData.nickName = e.detail.userInfo.nickName;
      if (getApp().globalData.nickName.match(/\ud83c[\udf00-\udfff]|\ud83d[\udc00-\ude4f]|\ud83d[\ude80-\udeff]/g) != null) {
        getApp().globalData.nickName = 'vip用户';
      }
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

  listenerLogin: function() 
  {
    if (this.data.Province != 0 && this.data.Kelei != 0 && this.data.Grade != 0 && this.data.Grade <=750 && this.data.Rank > 0) 
    {
      var that = this;
      //更改变量
      app.globalData.StudentProvince = this.data.provinceid[parseInt(this.data.Province)];
      //app.globalData.StudentKelei = 'abcd';
      app.globalData.StudentKelei = this.data.area[parseInt(this.data.Kelei)];
      app.globalData.StudentGrade = this.data.Grade;
      app.globalData.StudentRank = this.data.Rank;
      

      wx.login({
        success: function (data) {
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
          else {
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
              success: function (res) { //回调处理 
                console.log(res);
                app.globalData.userID = res.data.openid;
                console.log(app.globalData.userID);
                wx.hideLoading();
                that.Update();

                //页面跳转
                wx.switchTab({
                  url: '../home/home'
                })

              },
              fail: function (error) {
                console.log(error);
              }
            })
          }
        },

        fail: function () {
          console('登录获取Code失败！');
        }
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
