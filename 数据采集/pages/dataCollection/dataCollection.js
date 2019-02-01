var app = getApp(); //其后可通过app变量获取全局变量（存于globalData）
Page({
  data: {
    Clear: null, //用于清空输入框，每次提交后将所有输入框内容置为null
    School: app.globalData.School, //从全局变量中获取学校名
    Kelei: 0, //文、理、不分文理
    keleiIndex: 0, //用于记录所选科类为第几项
    Province: 0,
    Year: '',
    Major: '', //从全局变量获取专业，若有预置专业则显示并存储，若无预置专业则为0等待输入
    Pici: 0,
    PiciIndex: 0,
    pici: ['未选择批次', '第一批', '第二批', '第三批', '提前批', '专科'],
    Lowest: 0,
    Avg: '',
    Highest: '',
    Rank: 0, //学科评估结果
    kelei: ['未选择科类', '文科', '理科', '不分文理'],
    area: ['未选择省份', '北京', '天津', '河北', '山西', '山东', '河南', '内蒙古', '辽宁', '吉林', '黑龙江', '江苏', '福建', '上海', '浙江', '安徽', '江西', '湖南', '湖北', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '陕西', '西藏', '甘肃', '青海', '宁夏', '新疆'],
    areaIndex: 0, //用于记录所选省份为第几项
    selectData1: ['学科评估结果', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-'],
    index: 0, //用于记录所选评级为第几项
    multiArray: [
      ['门类','人文社科类', '理学', '工学', '农学', '医学', '管理学', '艺术学'],
      ['一级学科',
        '0101 哲学',

        '0201 理论经济学',

        '0202 应用经济学',

        '0301 法学',

        '0302 政治学',

        '0303 社会学',

        '0304 民族学',

        '0305 马克思主义理论',

        '0401 教育学',

        '0402 心理学',

        '0403 体育学',

        '0501 中国语言文学',

        '0502 外国语言文学',

        '0503 新闻传播学',

        '0601 考古学',

        '0602 中国史',

        '0603 世界史'
      ]
    ],
    objectMultiArray: [
      [{
        id: 0,
        name: '门类'
      },{
        id: 1,
        name: '人文社科类'
      }, {
        id: 2,
        name: '理学'
      }, {
        id: 3,
        name: '工学'
      }, {
        id: 4,
        name: '农学'
      }, {
        id: 5,
        name: '医学'
      }, {
        id: 6,
        name: '管理学'
      }, {
        id: 7,
        name: '艺术学'
      }],
      [{
        id: 0,
        name: '一级学科'
      },
        {
        id: 1,
        name: '0101 哲学'
      }, {
        id: 2,
        name: '0201 理论经济学'
      }, {
        id: 3,
        name: '0202 应用经济学'
      }, {
        id: 4,
        name: '0301 法学'
      }, {
        id: 5,
        name: '0302 政治学'
      }, {
        id: 6,
        name: '0303 社会学'
      }, {
        id: 7,
        name: '0304 民族学'
      }, {
        id: 8,
        name: '0305 马克思主义理论'
      }, {
        id: 9,
        name: '0401 教育学'
      }, {
        id: 10,
        name: '0402 心理学'
      }, {
        id: 11,
        name: '0403 体育学'
      }, {
        id: 12,
        name: '0501 中国语言文学'
      }, {
        id: 13,
        name: '0502 外国语言文学'
      }, {
        id: 14,
        name: '0503 新闻传播学'
      }, {
        id: 15,
        name: '0601 考古学'
      }, {
        id: 16,
        name: '0602 中国史'
      }, {
        id: 17,
        name: '0603 世界史'
      }]
    ],
    multiIndex: [0, 0], //表示多列选择器中两列所选项位置（门类，一级学科）
  },

  listenerYearInput: function(e) {
    //获取年份输入
    this.data.Year = e.detail.value;
  },
  listenerProvinceInput: function(e) {
    //获取省份输入
    this.data.Province = e.detail.value;
  },
  listenerMajorInput: function(e) {
    //获取专业输入
    this.data.Major = e.detail.value;
  },
  listenerLowestInput: function(e) {
    this.data.Lowest = e.detail.value;
  },
  listenerAvgInput: function(e) {
    this.data.Avg = e.detail.value;
  },
  listenerHighestInput: function(e) {
    this.data.Highest = e.detail.value;
  },

  ReadNext: function() {
    wx.showLoading({
      title: '查询中...',
    });
    var app = getApp();
    var that=this;
    console.log('下一所学校')
    //将this.globalData.School存入已填完的历史学校
    //将新的学校返回给this.globalData.School
    //this.globalData.School = next_school
    //this.globalData.Major = get_major
    wx.request({
      url: 'https://lunyiliu.eicp.vip/DataInsert.php',
      data: {
        command: 'next_school',
        userID: app.globalData.userID,
        current_school: app.globalData.School
      },
      method: 'GET',
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        wx.hideLoading();
        if (res.data.length>1){
          var major = res.data[0];
          wx.showModal({
            title: '警告',
            showCancel: false,
            content: major+'还没有填写',
          })
        }
        else{
          app.globalData.School = res.data[0];
          that.setData({
            'School': app.globalData.School
          });
          that.get_major();
        }
       
      },
      fail: function (error) {
        console.log(error);
      }
    }

    )
  },
  NextSchool: function() {
    var dataCollection = this;
    wx.showModal({
      title: '警告',
      showCancel: true,
      content: '是否要填写下一所学校？',
      success: function(res) {
        if (res.confirm) {
          console.log('用户点击确定');
          dataCollection.ReadNext();
        }
      }
    })

  },

  onLoad: function() {
    var that = this;
    console.log('返回初始的学校和专业')
    wx.showLoading({
      title: '获取学校...',
    }),
    wx.request({
      url: 'https://lunyiliu.eicp.vip/DataInsert.php',
      data: {
        command: 'get_school',
        userID: app.globalData.userID,
        user_nickname:'轮'
        //user_nickname: app.globalData.nickName
      },
      method: 'GET',
      header: {
        'content-type': 'application/json'
      },
      success: function(res) {
        console.log(res);
        app.globalData.School = res.data[0];
        that.setData({
          'School': app.globalData.School
        })
        console.log(that.data.School);
        wx.hideLoading();
        that.get_major();
      }
    });
    /*
    wx.request({
      url: 'http://localhost/DataInsert.php',
      data: {
        command: 'get_major',
        userID: app.globalData.userID,
      },
      method: 'GET',
      header: {
        'content-type': 'application/json'
      },
      success: function(res) {
        
        let areaindex, piciindex, keleiindex;
        if (res.data[0] != 0) {
          app.globalData.Major = res.data[0];
          app.globalData.Avg = res.data[2];
          app.globalData.Highest = res.data[3];
          app.globalData.Province = res.data[4];
          app.globalData.kelei = res.data[5];
          app.globalData.Year = res.data[6];
          app.globalData.Pici = res.data[7];
          for (let i = 0; i < 32; i++) {
            if (that.data.area[i] == app.globalData.Province) {
              areaindex = i;
            }
          }
          for (let i = 0; i < 6; i++) {
            if (that.data.pici[i] == app.globalData.Pici) {
              piciindex = i;
            }
          }
          for (let i = 0; i < 4; i++) {
            if (that.data.kelei[i] == app.globalData.kelei) {
              keleiindex = i;
            }
          }
          that.setData({
            'areaIndex': areaindex,
            'Year': app.globalData.Year,
            'Avg': app.globalData.Avg,
            'Highest': app.globalData.Highest,
            'Major': app.globalData.Major,
            'PiciIndex': piciindex,
            'keleiIndex': keleiindex
          })
        }
      }

    })
    */
  },
  get_major: function () {
    var that = this;
    var app = getApp();
    wx.showLoading({
      title: '获取专业...',
    });
    wx.request({
      url: 'https://lunyiliu.eicp.vip/DataInsert.php',
      data: {
        command: 'get_major',
        userID: app.globalData.userID,
      },
      method: 'GET',
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        console.log(res)
        if (res.data[0] != 0) {
          app.globalData.Major = res.data[0];
          app.globalData.Avg = res.data[2];
          app.globalData.Highest = res.data[3];
          app.globalData.Province = res.data[4];
          app.globalData.Kelei = res.data[5];
          app.globalData.Year = res.data[6];
          app.globalData.Pici = res.data[7];
          for (let i = 0; i < 32; i++) {
            if (app.globalData.area[i] == app.globalData.Province) {
              app.globalData.areaindex = i;
              break;
            }
          }
          for (let i = 0; i < 6; i++) {
            if (app.globalData.pici[i] == app.globalData.Pici) {
              app.globalData.piciindex = i;
              break;
            }
          } 

          for (let i = 0; i < 4; i++) {
            if (that.data.kelei[i] == app.globalData.Kelei) {
              app.globalData.keleiindex = i;
              
              break;
            }
          }
         
        }
        else {
          app.globalData.Major = 0;
        }
        
        console.log('到了这一步')
        if (app.globalData.Major != 0) {
          that.setData({
            'areaIndex': app.globalData.areaindex,
            'Year': app.globalData.Year,
            'Avg': app.globalData.Avg,
            'Highest': app.globalData.Highest,
            'Major': app.globalData.Major,
            'PiciIndex': app.globalData.piciindex,
            'keleiIndex': app.globalData.keleiindex
          })
        }
        /*
        console.log(res.data[0])
        console.log(res.data[1])
        console.log(res.data[2])
        console.log(res.data[3])
        console.log(res.data[4])
        console.log(res.data[5])
        console.log(res.data[6])
        console.log(res.data[7])
        console.log(res.data[8])
*/

        setTimeout(function () {
          //要延时执行的代码
          wx.hideLoading()
        }, 400)
         
      }
    })
  },
  Update: function() {
    wx.showLoading({
      title: '提交中...',
    });
    var that =this;
    var app = getApp();
    console.log('交换数据')
    if (app.globalData.ifMajor) {
      //update_data
      console.log('更新数据')
      wx.request({
        url: 'https://lunyiliu.eicp.vip/DataInsert.php',
        data: {
          command: 'update_data',
          user_nickname: app.globalData.nickName,
          userID: app.globalData.userID,
          trans_major: app.globalData.Major,
          trans_school: app.globalData.School,
          trans_avg: app.globalData.Avg,
          trans_highest: app.globalData.Highest,
          trans_province: app.globalData.Province,
          trans_subject: app.globalData.Kelei,
          trans_year: app.globalData.Year,
          trans_pici: app.globalData.Pici,
          trans_category: app.globalData.Class,
          trans_upper_major: app.globalData.Subject,
          trans_major_rank: app.globalData.Rank,
          trans_lowest: app.globalData.Lowest
        },
        method: 'GET',
        header: {
          'content-type': 'application/json'
        },
        success: function (res) {
          console.log(res)
          wx.hideLoading()
          that.get_major();
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
        url: 'https://lunyiliu.eicp.vip/DataInsert.php',
        data: {
          command: 'insert_data',
          user_nickname: app.globalData.nickName,
          userID: app.globalData.userID,
          trans_major: app.globalData.Major,
          trans_school: app.globalData.School,
          trans_avg: app.globalData.Avg,
          trans_highest: app.globalData.Highest,
          trans_province: app.globalData.Province,
          trans_subject: app.globalData.Kelei,
          trans_year: app.globalData.Year,
          trans_pici: app.globalData.Pici,
          trans_category: app.globalData.Class,
          trans_upper_major: app.globalData.Subject,
          trans_major_rank: app.globalData.Rank,
          trans_lowest: app.globalData.Lowest
        },
        method: 'GET',
        header: {
          'content-type': 'application/json'
        },
        success: function (res) {
          wx.hideLoading();
          that.get_major();
        },
        fail: function (error) {
          console.log(error);
        }
      }

      )
    }

  },
  listenerLogin: function() {
    //点击提交时判断各项输入是否合法
    //确认年份、专业名称已输入，科类、省份、学科门类等已选择，分数输入合法
    if (this.data.PiciIndex && this.data.areaIndex && this.data.School && this.data.Year && this.data.Major && this.data.Lowest < 750 && this.data.Avg < 750 && this.data.Highest < 750 && this.data.keleiIndex && this.data.Lowest < this.data.Avg && this.data.Lowest < this.data.Highest && this.data.Avg < this.data.Highest && this.data.multiIndex[0] !=0) {
      //将所有结果返回全局变量
      app.globalData.Province = this.data.area[parseInt(this.data.areaIndex)];
      app.globalData.Rank = this.data.selectData1[parseInt(this.data.Rank)];
      app.globalData.Year = this.data.Year;
      if (app.globalData.Major) {
        app.globalData.ifMajor = 1
      } else {
        app.globalData.ifMajor = 0
      }
      app.globalData.Major = this.data.Major;
      app.globalData.Kelei = this.data.kelei[parseInt(this.data.keleiIndex)];
      app.globalData.Class = this.data.multiArray[0][parseInt(this.data.multiIndex[0])];
      app.globalData.Subject = this.data.multiArray[1][parseInt(this.data.multiIndex[1])];
      app.globalData.Lowest = this.data.Lowest;
      app.globalData.Avg = this.data.Avg;
      app.globalData.Highest = this.data.Highest;
      app.globalData.Pici = this.data.pici[this.data.PiciIndex];
      //打印信息 
      console.log('学校: ', app.globalData.School);
      console.log('年份: ', app.globalData.Year);
      console.log('科类: ', app.globalData.Kelei);
      console.log('省份: ', app.globalData.Province);
      console.log('批次: ', app.globalData.Pici);
      console.log('门类: ', app.globalData.Class);
      console.log('一级学科: ', app.globalData.Subject);
      console.log('专业名称: ', app.globalData.Major);
      console.log('最低分: ', app.globalData.Lowest);
      console.log('平均分: ', app.globalData.Avg);
      console.log('最高分: ', app.globalData.Highest);
      console.log('评级: ', app.globalData.Rank);
      wx.showToast({
        title: '提交成功！',
        icon: 'succes',
        duration: 1000,
        mask: true
      })
      this.ClearInput();
      this.Update();
      //成功提交后显示提交成功，清空输入，重置this中所有变量（应在此处重置的同时读出全局变量）

    }
    //有非法输入时显示错误信息
    else {
      if (this.data.areaIndex == 0) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确选择省份!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      } else if (this.data.keleiIndex == 0) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确选择科类!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      } else if (this.data.PiciIndex == 0) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确选择批次!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      } else if (this.data.Lowest > 750 || this.data.Avg > 750 || this.data.Highest > 750 || this.data.Lowest > this.data.Avg || this.data.Lowest > this.data.Highest || this.data.Avg > this.data.Highest) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确填写分数!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      } else if (this.data.index == 0) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确填写学科评级!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      } else if (this.data.Year == 0) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确填写年份!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      } else if (this.data.Major == 0) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确填写专业名称!',
          success: function(res) {
            console.log('用户点击确定')
          }
        })
      }
      else if (this.data.multiIndex[0]==0) {
        wx.showModal({
          title: '提示',
          showCancel: false,
          content: '请正确选择门类及一级学科!',
          success: function (res) {
            console.log('用户点击确定')
          }
        })
      }
    }
  },
  bindPickerChange: function(e) {
    //监听省份栏输入
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      Province: e.detail.value,
      areaIndex: e.detail.value
    })
  },
  bindPickerChange1: function(e) {
    //监听评级输入
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      Rank: e.detail.value,
      index: e.detail.value
    })
  },
  bindPickerChange2: function(e) {
    //监听科类输入
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      Kelei: e.detail.value,
      keleiIndex: e.detail.value
    })
  },
  bindPickerChange3: function(e) {
    //监听批次输入
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      Pici: e.detail.value,
      PiciIndex: e.detail.value
    })
  },
  bindMultiPickerChange: function(e) {
    //监听多列选择器输入（门类，一级学科）
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      multiIndex: e.detail.value
    })
  },
  bindMultiPickerColumnChange: function(e) {
    console.log('修改的列为', e.detail.column, '，值为', e.detail.value);
    var data = {
      multiArray: this.data.multiArray,
      multiIndex: this.data.multiIndex
    };
    data.multiIndex[e.detail.column] = e.detail.value;
    switch (e.detail.column) {
      case 0:
        switch (data.multiIndex[0]) {
          case 0:
            data.multiArray[1] = ['一级学科'
            ];
            break;
          case 1:
            data.multiArray[1] = ['0101 哲学',

              '0201 理论经济学',

              '0202 应用经济学',

              '0301 法学',

              '0302 政治学',

              '0303 社会学',

              '0304 民族学',

              '0305 马克思主义理论',

              '0401 教育学',

              '0402 心理学',

              '0403 体育学',

              '0501 中国语言文学',

              '0502 外国语言文学',

              '0503 新闻传播学',

              '0601 考古学',

              '0602 中国史',

              '0603 世界史'
            ];
            break;
          case 2:
            data.multiArray[1] = ['0701 数学',

              '0702 物理学',

              '0703 化学',

              '0704 天文学',

              '0705 地理学',

              '0706 大气科学',

              '0707 海洋科学',

              '0708 地球物理学',

              '0709 地质学',

              '0710 生物学',

              '0711 系统科学',

              '0712 科学技术史',

              '0713 生态学',

              '0714 统计学'
            ];
            break;
          case 3:
            data.multiArray[1] = ['0801 力学',

              '0802 机械工程',

              '0803 光学工程',

              '0804 仪器科学与技术',

              '0805 材料科学与工程',

              '0806 冶金工程',

              '0807 动力工程及工程热物理',

              '0808 电气工程',

              '0809 电子科学与技术',

              '0810 信息与通信工程',

              '0811 控制科学与工程',

              '0812 计算机科学与技术',

              '0813 建筑学',

              '0814 土木工程',

              '0815 水利工程',

              '0816 测绘科学与技术',

              '0817 化学工程与技术',

              '0818 地质资源与地质工程',

              '0819 矿业工程',

              '0820 石油与天然气工程',

              '0821 纺织科学与工程',

              '0822 轻工技术与工程',

              '0823 交通运输工程',

              '0824 船舶与海洋工程',

              '0825 航空宇航科学与技术',

              '0826 兵器科学与技术',

              '0827 核科学与技术',

              '0828 农业工程',

              '0829 林业工程',

              '0830 环境科学与工程',

              '0831 生物医学工程',

              '0832 食品科学与工程',

              '0833 城乡规划学',

              '0834 风景园林学',

              '0835 软件工程',

              '0837 安全科学与工程'
            ];
            break;
          case 4:
            data.multiArray[1] = ['0901 作物学',

              '0902 园艺学',

              '0903 农业资源与环境',

              '0904 植物保护',

              '0905 畜牧学',

              '0906 兽医学',

              '0907 林学',

              '0908 水产',

              '0909 草学'
            ];
            break;
          case 5:
            data.multiArray[1] = ['1001 基础医学',

              '1002 临床医学',

              '1003 口腔医学',

              '1004 公共卫生与预防医学',

              '1005 中医学',

              '1006 中西医结合',

              '1007 药学',

              '1008 中药学',

              '1011 护理学'
            ];
            break;
          case 6:
            data.multiArray[1] = ['1201 管理科学与工程',

              '1202 工商管理',

              '1203 农林经济管理',

              '1204 公共管理',

              '1205 图书情报与档案管理'
            ];
            break;
          case 7:
            data.multiArray[1] = ['1301 艺术学理论',

              '1302 音乐与舞蹈学',

              '1303 戏剧与影视学',

              '1304 美术学',

              '1305 设计学'
            ];
            break;
        }
        data.multiIndex[1] = 0;
        break;


        console.log(data.multiIndex);
        break;
    }
    this.setData(data);
  },
  ClearInput: function(options) {
    //提交后重置数据及清空输入框
    this.setData({
      Kelei: '',
      keleiIndex: '',
      Pici: '',
      PiciIndex: 0,
      Province: '',
      Clear: null,
      Year: '',
      Major: '', //重新获取专业
      Lowest: '',
      Avg: '',
      Highest: '',
      Rank: '',
      areaIndex: 0,
      index: 0,
      multiIndex: [0, 0]
    });
  },
})