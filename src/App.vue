<template>
<!--    <el-container style="height: 100%">-->
<!--      <el-header class="header h-6 text-center">-->
<!--        <el-row>-->
<!--          <el-col :span="8">-->
<!--            <el-link :underline="false" href="/" class="el-icon-s-home h-6">首页</el-link>-->
<!--          </el-col>-->
<!--          <el-col :span="8">-->
<!--            <h1 class="h-6 m-auto">Newbee-English</h1>-->
<!--          </el-col>-->
<!--          <el-col :span="8">-->
<!--            <span v-if="name===undefined">-->
<!--              <el-link :underline="false" href="#/login">登录</el-link>-->
<!--            </span>-->
<!--            <span v-else>-->
<!--              <span v-text="name"></span>-->
<!--              <span>-->
<!--                <el-link :underline="false" icon="el-icon-thumb" @click="logout">退出登录</el-link>-->
<!--              </span>-->
<!--            </span>-->
<!--          </el-col>-->
<!--        </el-row>-->
<!--      </el-header>-->
<!--      <el-main class="text-center bcg">-->
        <router-view/>
<!--      </el-main>-->
<!--    </el-container>-->
</template>

<script>
export default {
  name: 'App',
  data(){
    return{
      name:undefined,
    }
  },

mounted () {
    // 检测浏览器路由改变页面不刷新问题,hash模式的工作原理是hashchange事件
    window.addEventListener('hashchange', () => {
      let currentPath = window.location.hash.slice(1)
      // if (this.$route.path !== currentPath) {
      //   this.$router.push(currentPath)
      // }
      console.log(currentPath)
    }, false)
  },
  methods: {
    // get_cookie() {
    //   this.$axios.post('/admin/api_get_cookie')
    //     .then(res => {
    //       if(res.data.info==='OK'){
    //         this.name=res.data.name
    //       }
    //     })
    // },
    logout(){
      this.$axios.get('/api/api_logout')
      .then(res=>{
        location.reload()
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


