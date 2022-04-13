<template>
    <div  class="login_container w-25 m-auto">
      <h1>登录</h1>
      <el-form ref="loginForm" :model="loginForm" label-width="80px" :rules="rule">
        <el-form-item label="用户名:" prop="name">
          <el-input v-model="loginForm.name" placeholder="请输入用户名" clearable></el-input>
        </el-form-item>
        <el-form-item label="密码:" prop="password">
          <el-input v-model="loginForm.password" placeholder="请输入密码" clearable show-password></el-input>
        </el-form-item>
        <div class="m-auto">
            <el-button type="primary" @click="login">登录</el-button>
             <el-button type="danger" native-type="reset">重置</el-button>
        </div>
      </el-form>
    </div>

</template>


<script>
// export default {
//   name: "Login",
//   data() {
//     return {
//       loginForm: {
//         name: '',
//         password: ''
//       },
//       rule:{
//         name:[
//           {required:true,message:'用户名不能为空',tigger:'blur'},
//           {min:2,max:20,message: '用户名长度在2-20之间',tigger: 'blur'}
//         ],
//         password:[
//           {required:true,message:'密码不能为空',tigger:'blur'}
//         ]
//       }
//     }
//   },
//   methods:{
//     login(){
//       this.$refs.loginForm.validate(valid=>{
//         console.log(valid)
//         if(valid){
//           let data=this.$qs.stringify({name:this.loginForm.name,pwd:this.loginForm.password})
//           this.$axios.post('/api/api_login',data)
//             .then(res=>{
//               if(res.data.info ==='OK'){
//                 this.$router.go(-1)
//               }else{
//                 this.$alert('用户名或密码不正确，请重新输入')
//               }
//             })
//         }else{
//           return false
//         }
//         })
//     }
//   }
// }
</script>

<style scoped>
.login_container {
  background-color: #2b4b6b;
}

</style>
