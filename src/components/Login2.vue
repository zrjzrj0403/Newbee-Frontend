<template>
  <div>
    <div class="loginbg">
      <img :src="imgUrl" ref="img">
    </div>
      <el-container >
    <el-header class="header h-6 text-center">
      <el-row>
        <el-col :span="8">
          <el-link :underline="false"></el-link>
        </el-col>
        <el-col :span="8">
          <h1 class="h-6 m-auto">Newbee-English</h1>
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
    <el-main class="text-center  transparent" >
      <div class="login_box">
        <el-row :gutter="20">
          <el-col :span="8" :offset="8">
            <div class="setHeight"></div>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="8" :offset="8">
            <el-card class="test" shodow="always">
              <h1>登录</h1>
              <el-divider></el-divider>
              <el-form ref="loginForm" :model="loginForm" label-width="10px" :rules="rule">
                <el-form-item prop="name">
                  <el-input class="input" v-model="loginForm.name" prefix-icon="el-icon-user-solid" placeholder="请输入用户名"
                            clearable></el-input>
                </el-form-item>
                <el-form-item prop="password">
                  <el-input class="input" v-model="loginForm.password" prefix-icon="el-icon-lock" placeholder="请输入密码"
                            clearable
                            show-password></el-input>
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
  </div>

</template>

<script>
export default {
  data() {
    return {
      name: undefined,
      imgUrl: require('../assets/1.jpeg'),
      index: 1,
      timer2:null,
      loginForm: {
        name: '',
        password: ''
      },
      rule: {
        name: [
          {required: true, message: '用户名不能为空', tigger: 'blur'},
          {min: 2, max: 20, message: '用户名长度在2-20之间', tigger: 'blur'}
        ],
        password: [
          {required: true, message: '密码不能为空', tigger: 'blur'}
        ]
      }
    }
  },
  created() {
    this.imgUrl = require('../assets/1.jpeg');
    this.index = 1;
  },
  mounted() {
    this.setTimer();
  },
   beforeDestroy() {//页面关闭前关闭定时器 （这个才有用）
    clearInterval(this.timer);
    clearTimeout(this.timer1);
     clearTimeout(this.timer2);
  },
  methods: {
    setTimer() {
      this.$nextTick(() => {
      this.timer = setInterval(() => {
        console.log(this.$refs.img.style.opacity)
        this.$refs.img.style.opacity = 1.0;
        this.index = this.index < 10 ? this.index + 1 : 1;
        this.imgUrl = require('../assets/' + this.index + '.jpeg');
        this.timer1=setTimeout(() => {
          this.$refs.img.style.opacity = 0.5;
        }, 4000);
      }, 5000);
      this.timer2=setTimeout(() => {
        this.$refs.img.style.opacity = 0.5;
      }, 4000);
    })

    },
    login() {
      this.$refs.loginForm.validate(valid => {
        if (valid) {
          // console.log(valid)
          let datas = {name: this.loginForm.name, pwd: this.loginForm.password}
//           console.log(typeof(data))
// var jsons={
//     arr:["123"],
//     str:'123'
// }
//    console.log(typeof(jsons))
          this.$axios({
            url: 'api/admin/login', data: datas,
            method: "post",
            headers: {
              'Content-Type': 'application/json'
            }
          })
            .then(res => {
              console.log(res);
              if (res.data.ret === 0) {
                this.$router.push('/home3')
                // console.log(res)
              } else {
                this.$alert('用户名或密码不正确，请重新输入')
              }
            })
        } else {
          return false
        }
      })
    }
  }
}
</script>

<style scoped>
.test {
  opacity: 0.8;
}

.test .input {
  color: black !important;
}

.setHeight {
  height: 210px;
}

/deep/ .el-input__inner::placeholder {
  color: black;
}

.bcg {
  background-position: center;
  height: 100%;
  width: 100%;
  background-size: cover;

}
.loginbg {
  width: 100%;
  height: 100%;
  overflow: hidden;
  position: absolute;
  /*  size:contain|cover;*/
  /*width:100%;*/
  /*height: auto;*/
  top: 0;
}
.loginbg img {
  width: 100%;
  /*height: 100%;*/
        overflow: hidden;
    position: absolute;
        /*position: center;*/
  transition: 1.5s all;
}
/deep/ .el-input__inner {
  color: black;
}
.header{
  background-color: #f5f5f5;
}
</style>
