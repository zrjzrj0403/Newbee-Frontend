<template>
<div>
  <div class="contentheader">
    <i v-if='!isCollapse' @click="changeMenu" class="iconfont el-icon-s-fold"></i>
    <i v-else  @click="changeMenu" class="iconfont el-icon-s-unfold"></i>
    顶部区域
    <span class='dengchu' @click="logout">
      <i class="iconfont el-icon-switch-button"></i>
    </span>
     <span class='loginname' v-text="'欢迎:'+name"></span>
  </div>
<!-- 内容区域,路由出口-->
  <div class="content">
    <router-view>

    </router-view>
  </div>
</div>
</template>

<script>
export default {
  props:['isCollapse'],
   data(){
    return{
      name:undefined,
    }
  },
  methods:{
    changeMenu(){
      //点击切换按钮修改父组件数据 isCollapse
      this.$emit('changeCollapse')
    },
    //  get_cookie() {
    //   this.$axios.post('/api/api_get_cookie')
    //     .then(res => {
    //       if(res.data.info==='OK'){
    //         this.name=res.data.name
    //       }
    //     })
    // },
    logout(){
      this.$axios.delete('/api/admin/logout/')
      .then(res=>{
        if(res.data.ret===0)
        {
             this.$router.push('/login/');
        }
        else
        {
           this.$message({
                type: 'error',
                message: '登录已过期，请重新登录'
              })
          this.$router.push('/login/');
        }
        }
      )
    }
  },
   created() {
      // this.get_cookie()
    },
    beforeUpdate() {
      // this.get_cookie()
    }
}
</script>

<style scoped>
.contentheader {
  height: 50px;
  line-height: 50px;
  background-color: #314158;
  color: #fff;
}
  .iconfont{
    font-size: 30px;
    line-height: 50px;
  }
.dengchu{
  float: right;
    margin-right: 20px;
}
.loginname{
  margin-left: 10px;
  margin-right: 20px;
  float: right;
}
</style>
