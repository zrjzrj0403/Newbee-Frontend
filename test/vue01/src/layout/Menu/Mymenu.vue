<template>
  <div>
    <el-menu
      default-active="/home3"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose"
      background-color="#314158"
      text-color="#fff"
      active-text-color="#ffd04b"
       :collapse-transition="false"
      router
      :collapse="isCollapse">
     <el-menu-item >
        <span class="title" slot="title">newbee英语</span>
      </el-menu-item>
      <el-menu-item index="/home3">
        <i class="el-icon-menu"></i>
        <span slot="title">首页</span>
      </el-menu-item>
      <el-menu-item index="/user">
        <i class="el-icon-document"></i>
        <span slot="title">用户管理</span>
      </el-menu-item>
      <el-submenu index="/question">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>题目管理</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="/question/multiplechoice">单项选择</el-menu-item>
          <el-menu-item index="/question/readingcomprehension">阅读理解</el-menu-item>
          <el-menu-item index="/question/cloze">完形填空</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
       <el-menu-item index="/upload">
        <i class="el-icon-setting"></i>
        <span slot="title">题目上传</span>
      </el-menu-item>
      <el-menu-item index="/announcement">
        <i class="el-icon-setting"></i>
        <span slot="title">公告管理</span>
      </el-menu-item>

    </el-menu>
</div>
</template>

<script>
export default {
  props:['isCollapse'],//接收的数据
  name: "Mymenu",
  // data(){
  //   return{
  //     isCollapse:false
  //   }
  // }
  methods:{
    handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
  }
}
</script>

<style scoped>
.el-menu {
	border-right:0!important;
}
.el-menu-vertical-demo:not(.el-menu--collapse){
  width: 200px;
  min-height: 400px;
}
.title{
  font-size: 20px;
  color: #fff;
}
</style>
