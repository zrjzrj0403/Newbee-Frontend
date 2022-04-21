<template>
 <div class="total">
  <div class="title1">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home3' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>题目上传</el-breadcrumb-item>
      </el-breadcrumb>
  </div>
   <div class="box">
      <el-steps :space="400" align-center :active="step" finish-status="success" >
      <el-step title="题目类型选择 题目标题上传"></el-step>
      <el-step title="题目内容上传"></el-step>
      <el-step title="上传者登记"></el-step>
        <el-step title="上传完成"></el-step>
</el-steps>
   </div>
      <el-button class='button' type="success" icon="el-icon-check" circle @click="changeStrp"></el-button>

</div>
</template>

<script>
export default {
  data(){
    return{
       step:0
    }
  },
  methods:{
    changeStrp(){
      if(this.step<=3){
        this.step=this.step+1;
      }
      else{
        this.step=0;
      }
    }
  }
}
</script>

<style scoped>
.box{
  margin:80px auto;
}
.button{
  position: fixed;
  right: 100px;
}
</style>
