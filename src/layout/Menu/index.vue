<template>
  <div class="layout">
<!--    左侧导航区域-->
    <Mymenu class="menu" :isCollapse='isCollapse'/>
<!--    右侧内容区域-->
    <Content class="content" :class="{isActive:isCollapse}" @changeCollapse='changeCollapse' :isCollapse='isCollapse'/>
  </div>
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
         }
    },
    methods:{
         changeCollapse(){
           this.isCollapse=!this.isCollapse;
         }
    }
  }
</script>

<style  scoped>
  .menu{
    /*width: 200px;*/
    /*min-height: 500px;*/
    /*background-color: #314158;*/
    background-image: linear-gradient(-20deg, #2b5876 0%, #4e4376 100%)!important;
    position: fixed;
    top:0;
    bottom: 0;
    margin-right: 0;

  }
  .content{
    margin-left: 200px;
  }
  .isActive{
    margin-left: 64px;
  }

</style>
