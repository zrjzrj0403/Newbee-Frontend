<template>
   <el-container style="height: 100%">
      <el-header class="header h-6 text-center">
          <el-row>
              <el-col :span="8">
                  <el-link :underline="false" href="/" class="el-icon-s-home h-6">首页</el-link>
              </el-col>
              <el-col :span="8">
                   <h1 class="h-6 m-auto">newbee英语</h1>
              </el-col>
              <el-col :span="8">
                  <span v-if="name===undefined">
                    <el-link :underline="false" href="#/login"></el-link>
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
      <el-main class="text-center bcg transparent">
          <div class="login_box">
            <el-row :gutter="20">
                <el-col :span="8" :offset="8">
                   <div class="setHeight"></div>
                </el-col>
            </el-row>
            <el-row :gutter="20">
                <el-col :span="8" :offset="8">
                  <el-card  shodow="always">
                    <h1>登录</h1>
                    <el-divider></el-divider>
                    <el-form ref="loginForm" :model="loginForm" label-width="10px" :rules="rule">
                    <el-form-item   prop="name">
                      <el-input v-model="loginForm.name"  prefix-icon="el-icon-user-solid" placeholder="请输入用户名" clearable></el-input>
                    </el-form-item>
                    <el-form-item  prop="password">
                      <el-input v-model="loginForm.password" prefix-icon="el-icon-lock" placeholder="请输入密码" clearable show-password></el-input>
                    </el-form-item>
                    <div class="m-auto">
                        <el-button type="primary" @click="login">登录</el-button>
                         <el-button type="danger" native-type="reset">重置</el-button>
                    </div>
                  </el-form>
                  </el-card>
                </el-col>
              </el-row>
          </div>
    </el-main>
   </el-container>
</template>

<script>
export default {
  data() {
    return {
      name:undefined,
      loginForm: {
        name: '',
        password: ''
      },
      rule:{
        name:[
          {required:true,message:'用户名不能为空',tigger:'blur'},
          {min:2,max:20,message: '用户名长度在2-20之间',tigger: 'blur'}
        ],
        password:[
          {required:true,message:'密码不能为空',tigger:'blur'}
        ]
      }
    }
  },
  methods:{
    login(){
      this.$refs.loginForm.validate(valid=>{
        console.log(valid)
        if(valid){
          let data=this.$qs.stringify({name:this.loginForm.name,pwd:this.loginForm.password})
          this.$axios.post('/api/admin_login',data)
            .then(res=>{
              if(res.data.info ==='OK'){
                this.$router.push('/home3')
                // console.log(res)
              }else{
                this.$alert('用户名或密码不正确，请重新输入')
              }
            })
        }else{
          return false
        }
        })
    }
  }
}
</script>

<style scoped>
.setHeight{
  height: 210px;
}
</style>
