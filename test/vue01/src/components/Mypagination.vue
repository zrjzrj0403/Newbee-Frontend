<template>
  <div style="text-align: center;margin: 20px;">
      <el-pagination
  background
  layout=" total,jumper,prev, pager, next"
  :total="total" :page-size="pageSize" @current-change="changePage">
</el-pagination>
  </div>
</template>

<script>
export default {
    props:{
      total:{
        type:Number,
        default:100
      },
      pageSize:{
        type:Number,
        default:10
      }
    },
  methods:{
      changePage(page){
        this.$emit('changePage',page)
      }
  }
}
</script>

<style scoped>

</style>
