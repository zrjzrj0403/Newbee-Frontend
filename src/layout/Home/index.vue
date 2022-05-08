<template>
  <div class="top">
    <div class="header1">
      <div class="box3">
        <el-row class="home" :gutter="10">
          <!--span默认一共是24，这里占8 下面占16，所以这两个分隔栏所占的宽度 是1:2-->
          <el-col :span="8" style="margin-top: 10px;">
            <!--shadow属性设置卡片阴影出现的时机-->
            <el-card shadow='hover' :style="{height: scrollerHeight}">
              <div class="user2">
                <img class='img2' src="../../assets/logo1.jpg" :style="{height: scrollerHeight0,wight:scrollerHeight0}"/>
<!--                <div class="userinfo">-->
<!--                  <p class="name">Newbee-English</p>-->
<!--                  <p class="access">欢迎使用Newbee-English管理系统</p>-->
<!--                </div>-->
              </div>
<!--              <div style="height: 100%;" class="login-info">-->
<!--                <p>本次版本发布时间：<span>2022-5-11</span></p>-->
<!--                <p>本次版本号：<span>v0.1</span></p>-->
<!--              </div>-->
            </el-card>
            <el-card class="card1" shadow="hover" style=" margin-top: 10px" :style="{height: scrollerHeight2}">
            </el-card>
          </el-col>
          <el-col :span="15" style="margin-top: 10px">
            <el-row :gutter="10">
              <el-col class='col1' :span="8">
                <div class="num">
                  <el-card class="userico" shadow="hover" body-style="{ display: 'flex', padding: 0}">
                    <div class="icon1" style="text-align: center"
                         :style="{height: scrollerHeight4,wight:scrollerHeight4}">
                      <i class="icon1_1 el-icon-user" :style="{padding:scrollerpadding1}"></i>
                    </div>
                    <div class="miaoshu1">
                      <div class="miaoshu">
                        <p class="num biaoshi">1234</p>
                        <p class="txt">用户数量</p>
                      </div>
                    </div>
                  </el-card>
                </div>
              </el-col>
              <el-col class='col1' :span="8">
                <div class="num">
                  <el-card class="userico" shadow="hover" body-style="{ display: 'flex', padding: 0}">
                    <div class="icon2" style="text-align: center"
                         :style="{height: scrollerHeight4,wight:scrollerHeight4}">
                      <i style="margin: auto" class="icon1_1 el-icon-tickets " :style="{padding:scrollerpadding1}"></i>
                    </div>
                    <div class="miaoshu1">
                      <div class="miaoshu">
                        <p class="num biaoshi2">352</p>
                        <p class="txt">题目数量</p>
                      </div>
                    </div>
                  </el-card>
                </div>
              </el-col>
              <el-col class='col1' :span="8">
                <div class="num">
                  <el-card class="userico" shadow="hover" body-style="{ display: 'flex', padding: 0}">
                    <div class="icon3" style="text-align: center"
                         :style="{height: scrollerHeight4,wight:scrollerHeight4}">
                      <i class="icon1_1 el-icon-warning-outline" :style="{padding:scrollerpadding1}"></i>
                    </div>
                    <div class="miaoshu1">
                      <div class="miaoshu">
                        <p class="num biaoshi3">1234</p>
                        <p class="txt">待处理题解</p>
                      </div>
                    </div>
                  </el-card>
                </div>
              </el-col>
            </el-row>
            <el-row>
              <el-col :span="24">
                <el-card class="card1" style=" margin-top: 10px ;height:480px" shadow="hover"
                         :style="{height: scrollerHeight5}">
                </el-card>
              </el-col>
            </el-row>
          </el-col>
        </el-row>
      </div>

      <el-row class="el-row2" type="flex" :gutter="10">
        <el-col :span="12">
          <div>
            <el-card class="card1" style=" margin-top: 10px ;" shadow="hover" :style="{height: scrollerHeight3}">
            </el-card>
          </div>
        </el-col>
        <el-col :span="11">
          <div>
            <el-card class="card1" style=" margin-top: 10px ;" shadow="hover" :style="{height: scrollerHeight3}">
            </el-card>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      curheight: 0,
      padding1: 0,
      userImg: require('../../assets/logo.jpg'),
      countData: [],
      tableData: [],
      tableLabel: {
        name: '课程',
        todayBuy: '今日购买',
        monthBuy: '本月购买',
        totalBuy: '总购买'
      }
    }
  },
  computed: {
    // 滚动区高度
    // (业务需求：手机屏幕高度减去头部标题和底部tabbar的高度，当然这2个高度也是可以动态获取的)
    scrollerHeight: function () {
      return ((this.curheight - 60) * 0.3) + 'px';
    },
        scrollerHeight0: function () {
      return ((this.curheight - 60) * 0.1) + 'px';
    },
    scrollerHeight2: function () {
      return ((this.curheight - 60) * 0.3) - 10 + 'px';
    },
    scrollerHeight3: function () {
      return ((this.curheight - 60) * 0.4) - 20 + 'px';
    },
    scrollerHeight4: function () {
      this.padding1 = this.curheight * 0.09;
      return ((this.curheight - 60) * 0.1) + 'px';
    },
    scrollerHeight5: function () {
      return ((this.curheight - 60) * 0.5) - 10 + 'px';
    },
    scrollerpadding1: function () {
      return ((this.padding1 - 45) / 2 + 'px');
    }
  },
  methods: {
    setit() {
      this.curheight = document.documentElement.clientHeight || document.body.clientHeight;
      console.log(this.curheight);
    },
    getTableData() {
      // this.$http.get('/home/getData').then(res => {
      //     res = res.data
      //     this.tableData = res.data.tableData
      // })
    }
  },
  //一进组件就会去请求后端接口 获取首页数据
  created() {
    this.setit()
    // this.getTableData()
  }
}
</script>
<style>
.header1 {
  box-sizing: border-box;
  padding-left: 1% /* 给gutter留padding */
}

.user2 {
  display: flex;
  align-items: center;

  /*border-bottom: 1px solid #ccc;*/
}

.img2 {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}

.name {
  font-size: 32px;
  margin-bottom: 10px;
}


.el-row2 {
  margin-bottom: 20px;
  display: flex;
  flex-wrap: wrap
}

.access {
  color: #999999;
}

.col1 {
  /*margin-right: 3%;*/
}

.icon1 {
  background-color: #409EFF;
  height: 100%;
  display: inline-block
}

.icon2 {
  background-color: #67C23A;
  height: 100%;
  display: inline-block
}

.icon3 {
  background-color: #F56C6C;
  height: 100%;
  display: inline-block
}

.icon1_1 {
  padding: 20px;
  font-size: 45px;
}

.miaoshu1 {
  height: 85px;
  width: 60%;
  display: inline-block;
  text-align: center;
  vertical-align: center;
}

.biaoshi {
  font-size: 30px;
  color: #409EFF;
}

.biaoshi2 {
  font-size: 30px;
  color: #67C23A;
}

.biaoshi3 {
  font-size: 30px;
  color: #F56C6C;
}

.card1 {
  height: 300px;
}

.miaoshu {
  font-size: 16px;
  display: inline-block;
}

.login-info {
  height: 30%;
}

.userico .el-card__body {
  padding: 0px !important;
}
</style>
