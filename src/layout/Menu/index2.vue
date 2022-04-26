<template>
  <el-container>
    <el-aside :width=test>
      <Mymenu class="menu" :isCollapse='isCollapse'/>
    </el-aside>
    <el-container>
      <el-header>
        <Content class="content" :class="{isActive:isCollapse}" @changeCollapse='changeCollapse' :isCollapse='isCollapse'/>
      </el-header>
      <el-main>Main</el-main>
    </el-container>
  </el-container>
</template>

<script>
import Mymenu from "./Mymenu";
import Content from "./Content";
  export default {
       components:{
         Mymenu,
         Content
       },
    data(){
         return{
           isCollapse:false,
           test:"10",
         }
    },
    methods:{
         changeCollapse(){
           this.isCollapse=!this.isCollapse;
           if(this.isCollapse)
           {
             this.test="3%";
           }
           else{
             this.test="10%";
           }
         }
    }
  }
</script>

<style scoped>
.menu{
  min-height: 100%;

}
/deep/ .el-header {
  padding: 0;
}
</style>
