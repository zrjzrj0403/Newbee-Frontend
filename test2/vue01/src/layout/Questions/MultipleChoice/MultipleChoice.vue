<template>
  <div class="total">
  <div class="title1">
    <h4>首页/题库管理/单项选择</h4>
  </div>
<div class="user">
    <!--    搜索区域-->
    <div class="userheader">
      <el-input v-model="input" placeholder="请输入内容"></el-input>
      <el-button type="primary">查询</el-button>
      <el-button type="primary">添加</el-button>
    </div>
    <!--  2.表格区域 展示视图数据-->
    <div class="wrapper">
      <el-table border :data="tableData" style="width: 100%">
        <el-table-column type="selection" width="55"></el-table-column>
        <el-table-column prop="question_title" label="题目名称" width="900"></el-table-column>
        <el-table-column prop="question_number" label="所含小题数量" width="180"></el-table-column>
        <el-table-column prop="operate" label="操作">
          <template slot-scope="scope">
            <el-button size="mini" @click="handleEdit(scope.$index, scope.row)"
            >编辑</el-button>
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)"
            >删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div>
        <Mypagination :total='total' :pageSize='pageSize'/>
    </div>
  </div>
  </div>
</template>

<script>
import Mypagination from "../../../components/Mypagination";
export default {
  components:{
    Mypagination
  },
  name: "cloze",
   data() {
    return {
      input:'',
        total:2   ,
      pageSize:1,
      tableData: [{
        question_title:'I always remember waking up to the smell of the breakfast my mother was cooking. What a wonderful smell! I used to _______ ,wash quickly and run downstairs. My breakfast would be waiting for me on the table.',
        question_number:'20',
      }],
    }},
   methods:{
    // 编辑操作
    handleEdit(){},
    // 删除操作
    handleDelete(){}}
}
</script>

<style scoped>
.user {
  margin: 20px;
}

.userheader {
  display: flex;
}

.userheader button {
  margin-left: 20px;
}

.wrapper {
  margin: 20px 0;
}
</style>

