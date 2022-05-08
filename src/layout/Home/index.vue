<template>
  <div>
    <div class="title1">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{path: '/home3' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="header1">
      <el-row class="home" :gutter="10">
        <!--span默认一共是24，这里占8 下面占16，所以这两个分隔栏所占的宽度 是1:2-->
        <el-col :span="8" style="margin-top: 20px">
          <!--shadow属性设置卡片阴影出现的时机-->
          <el-card shadow='hover' >
            <div class="user2">
              <img class='img2' src="../../assets/logo1.jpg" height="200" width="200"/>
              <div class="userinfo">
                <p class="name">Newbee-English</p>
                <p class="access">欢迎使用Newbee-English管理系统</p>
              </div>
            </div>
            <div class="login-info">
              <p>本次版本发布时间：<span>2022-5-11</span></p>
              <p>本次版本号：<span>v0.1</span></p>
            </div>
          </el-card>
          <el-card class="card1" shadow="hover" style=" margin-top: 20px" >
          </el-card>
        </el-col>
        <el-col :span="15" style="margin-top: 20px">
          <el-row :gutter="10" >
          <el-col class='col1' :span="8" >
          <div class="num">
            <el-card class="userico" shadow="hover" body-style="{ display: 'flex', padding: 0}">
              <div class="icon1">
                <i class="icon1_1 el-icon-user"></i>
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
        <el-col class='col1' :span="8" >
          <div class="num">
            <el-card class="userico" shadow="hover" body-style="{ display: 'flex', padding: 0}">
              <div class="icon2">
                <i class="icon1_1 el-icon-tickets"></i>
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
        <el-col class='col1' :span="8" >
          <div class="num">
            <el-card class="userico" shadow="hover" body-style="{ display: 'flex', padding: 0}">
              <div class="icon3">
                <i class="icon1_1 el-icon-warning-outline"></i>
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
          <el-row :gutter="10">
           <el-col :span="24" >
             <el-card class="card1" style=" margin-top: 20px ;height:480px" shadow="hover">
          </el-card>
           </el-col>
          </el-row>
        </el-col>

      </el-row>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
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
  methods: {
    getTableData() {
      // this.$http.get('/home/getData').then(res => {
      //     res = res.data
      //     this.tableData = res.data.tableData
      // })
    }
  },
  //一进组件就会去请求后端接口 获取首页数据
  created() {
    // this.getTableData()
  }
}
</script>
<style>
.header1 {
  box-sizing: border-box;
  padding-left: 3% /* 给gutter留padding */
}

.user2 {
  display: flex;
  align-items: center;
  padding-bottom: 20px;
  margin-bottom: 20px;
  border-bottom: 1px solid #ccc;
}

.img2 {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  margin-right: 40px;
}

.name {
  font-size: 32px;
  margin-bottom: 10px;
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
.miaoshu1{
  height: 85px;
  width: 60%;
  display: inline-block;
  text-align: center;
  vertical-align:center;
}
.biaoshi{
  font-size: 30px;
  color: #409EFF;
}
.biaoshi2{
  font-size: 30px;
  color: #67C23A;
}
.biaoshi3{
  font-size: 30px;
  color: #F56C6C;
}
.card1{
  height: 300px;
}
.miaoshu {
  font-size: 16px;
  display: inline-block;
}

.userico .el-card__body {
  padding: 0px !important;
}
</style>
