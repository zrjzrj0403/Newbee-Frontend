<template>
  <div>
    <el-menu
      :default-active=act
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
        <span class="title" slot="title">Newbee-English</span>
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
  data(){
    return{
      act:'',
      path:''
    };
  },
  created() {
    //  this.path=this.$route.path.split('?')[0].replace(/(#|\/)/g,'')
    //    if(this.path==='details')
    // {
    //   this.type=this.$route.query.type;
    //   console.log(this.type);
    //   if(this.type==='choice_question')
    //    {
    //     this.act='/question/multiplechoice';
    //    }
    //    else if(this.type==='cloze_question')
    //    {
    //     this.act='/question/cloze';
    //    }
    //    else
    //    {
    //      this.act='/question/readingcomprehension';
    //    }
    // }
    // else
    // {
    //     this.act = this.$route.path;
    // }
  },
   // watch: {
   //   $route(to, from) {
   //     //监听路由变化
   //     this.path=this.$route.path.split('?')[0].replace(/(#|\/)/g,'')
   //     console.log(this.path)
   //      if(this.path==='details')
   //  {
   //    this.type=this.$route.query.type;
   //    console.log(this.type);
   //    if(this.type==='choice_question')
   //     {
   //      this.act='/question/multiplechoice';
   //     }
   //     else if(this.type==='cloze_question')
   //     {
   //      this.act='/question/cloze';
   //     }
   //     else
   //     {
   //       this.act='/question/readingcomprehension';
   //     }
   //  }
   //  else
   //  {
   //      this.act = this.$route.path;
   //  }
   //   },
   // },
  // mounted() {
    // if(this.$route.path==='/details')
    // {
    //   this.type=window.localStorage.getItem('type')
    //   if(this.type==='choice_question')
    //    {
    //     this.act='/question/multiplechoice';
    //    }
    //    else if(this.type==='cloze_question')
    //    {
    //     this.act='/question/cloze';
    //    }
    //    else
    //    {
    //      this.act='/question/readingcomprehension';
    //    }
    // }
    // else
    // {
    //     this.act = this.$route.path;
    // }
    // window.addEventListener('hashchange', () => {
    //   let currentPath = window.location.hash.slice(1)
    //   this.act=currentPath;
    // }, false)
     // console.log(this.act);
  // },
  methods:{
    handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },
    getBreadcrumb(){
      console.log('1');
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
