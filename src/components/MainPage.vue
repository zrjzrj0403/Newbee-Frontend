<template>
    <el-container style="height: 100%">
      <el-header class="header h-6 text-center">
        <el-row>
          <el-col :span="8">
            <el-link :underline="false" href="/" class="el-icon-s-home h-6">公告编辑</el-link>
          </el-col>
          <el-col :span="8">
            <h1 class="h-6 m-auto">newbee英语</h1>
          </el-col>
          <el-col :span="8">
            <span v-if="name===undefined">
              <el-link :underline="false" href="#/login">登录</el-link>
            </span>
            <span v-else>
              <span v-text="name"></span>
              <span>
                <el-link :underline="false" icon="el-icon-thumb" @click="logout">退出登录</el-link>
              </span>
            </span>
          </el-col>
        </el-row>
      </el-header>
        <el-main class="text-center bcg">

      </el-main>
    </el-container>
</template>

<script>
export default {
  name: 'App',
  data(){
    return{
      name:undefined,
    }
  },
  methods: {
    get_cookie() {
      this.$axios.post('/api/api_get_cookie')
        .then(res => {
          if(res.data.info==='OK'){
            this.name=res.data.name
          }
        })
    },
    logout(){
      this.$axios.get('/api/api_logout')
      .then(res=>{
        location.reload()
        }
      )
       this.$router.push('/login')
    }
  },
    created() {
      this.get_cookie()
    },
    beforeUpdate() {
      this.get_cookie()
    }
}
</script>

<style scoped>
.background{
  background: url("../../bcg.jpg");
  background-position: center;
    height: 100%;
    width: 100%;
    background-size: cover;
    position: fixed;
}
</style>
