<template>
  <div id="main">
  </div>
</template>

<script>
import E from 'wangeditor'
export default {
  data(){
    return{
      editor:'',
    }
  },
  mounted() {
    // 创建示例
    this.editor=new E('#main')
    this.editor.create();
  }
}
</script>

<style scoped>

</style>
