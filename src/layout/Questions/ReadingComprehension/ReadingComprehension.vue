<template>
  <div>
    <test/>
  </div>
</template>
<script>
import test from "../Templates/test";
export default {
  components: {
    test
  },
  data() {
    return {
    }},
  created(){
      this.localStorage();//需要触发的函数
    },
  methods: {
    // 编辑操作
    localStorage(){
        window.localStorage.setItem('type','reading_question');
    },
  }
  /*
  本地存储
  存window.localStorage.setItem('键‘,值)
  取window.localStorage.getItem('键‘)
   */
}
</script>

<style scoped>

</style>
