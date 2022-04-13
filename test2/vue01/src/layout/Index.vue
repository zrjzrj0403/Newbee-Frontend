import Menu from './Menu'
<template>
  <div class="common-layout">
    <el-container >
      <el-aside width="200px">
        <Menu />
      </el-aside>
      <el-container>
        <el-header>Header</el-header>
        <el-main>Main</el-main>
      </el-container>
    </el-container>
  </div>
</template>


<script>
export default {
  name: "Index"
}
</script>

<style scoped>

</style>
