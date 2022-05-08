<template>
  <div class="total">
  <div class="title1">
      <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home3' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: this.$route.path}">题目管理</el-breadcrumb-item>
      <el-breadcrumb-item>{{item}}</el-breadcrumb-item>
</el-breadcrumb>
  </div>
<div class="user">
    <!--    搜索区域-->
    <div class="userheader">
      <el-input  @keyup.enter.native="get_information(1,input)" v-model="input" placeholder="请输入内容"></el-input>
      <el-button type="primary">查询</el-button>
      <el-button type="primary" @click="batchDelete(tableChecked)">批量删除</el-button>
    </div>
    <!--  2.表格区域 展示视图数据-->
    <div class="wrapper">
      <el-table border  :data="tableData" style="width: 100%" @selection-change="handleSelectionChange" @cell-click="handle" :row-class-name="tableRowClassName">
        <el-table-column type="selection" width="55" class='no'></el-table-column>
        <el-table-column prop="title" label="题目名称" width="900" @click="test"></el-table-column>
         <el-table-column prop="id" label="题目id" width="180"></el-table-column>
        <el-table-column prop="sub_que_num" label="所含小题数量" width="180"></el-table-column>
         <el-table-column prop="has_bad_solution" label="是否存在有问题的题解" width="180" :formatter="FunctionStatus"></el-table-column>
        <el-table-column prop="operate" class='no' label="操作">
          <template slot-scope="scope">
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)"
            >删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div>
        <Mypagination :total='total' :pageSize='pageSize'@changePage='changePage'/>
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
   data() {
    return {
      input:'',
        total:2   ,
      pageSize:13,
      tableData: [],
      tableChecked: [],
      type:'',
      str:'',
      item:'单选'
    }},
   created(){
      this.get_information(1,this.str);//需要触发的函数
    },
   methods: {
     tableRowClassName({row, rowIndex}) {
        if (row.has_bad_solution === 1) {
          return 'warning-row';
        }
        else
        {
          return '';
        }
      },
    FunctionStatus(row, column){
       return row.has_bad_solution== '1' ? "有" : row.has_bad_solution== '0' ? "无" : "暂无";
    },
    handle(row,column,cell,event) {
	    // console.log(row)
	    // console.log(column)
	    // console.log(cell)
	    // console.log(event)
      if(column.label === '题目名称')
      {
        console.log(row.id);
        this.$router.push({name:'details',query: {type:this.type,id:row.id}})
      }
    },
    test(){
      console.log("ok")
    },
    handleSelectionChange(val) {
       let id =val.map(item=>item.id);
        this.tableChecked = id;
      },
     // 编辑操作
     handleEdit() {
     },
       //批量删除
    batchDelete(rows) {
      console.log(rows)
      if (rows.length <= 0) {//选中0条数据时
	    	this.$message.info("未选中数据");
	}
      else
      {``
        this.$confirm('此操作将永久删除题目, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
                this.$axios.delete('/api/admin/list_question', {params: {question:rows},
          paramsSerializer: params => {
            return this.$qs.stringify(params, { indices: false })
        }})
         .then(res=>{
           if(res.data.ret===0)
           {
                this.$message({
                type: 'success',
                message: '删除成功!'
              });
                this.$router.go (0);
           }
           else{
                     this.$message({
                type: 'info',
                message: '删除失败'
              });
           }
         })
        })
         .catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
      }
       },
     // 删除操作
     handleDelete(index,row){
       this.$confirm('此操作将永久删除该题目, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          // let  data=this.$qs.stringify({rows:row.id})
         console.log(row.id);
          this.$axios.delete('/api/admin/list_question',{params: {question:row.id}})
         .then(res=>{
           if(res.data.ret===0)
           {
                this.$message({
                type: 'success',
                message: '删除成功!'
              });
                this.$router.go (0);
           }
           else{
                     this.$message({
                type: 'info',
                message: '删除失败'
              });
           }
         })
        })
         .catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
    },
     get_information(pagenumber,str) {
       // console.log(str)
       this.type=window.localStorage.getItem('type')
       if(this.type==='choice_question')
       {
        this.item='单项选择';
       }
       else if(this.type==='cloze_question')
       {
        this.item='完型填空';
       }
       else
       {
         this.item='阅读理解';
       }
       this.$axios.get('/api/admin/list_question', {params: {pagenumber: pagenumber, pagesize: 13,type:this.type,title:str}})
         .then(res => {
           // console.log(res)
           if (res.data.ret === 0) {
             console.log(res);
             this.tableData = res.data.list;
             this.total =res.data.total;
             // console.log(res)
           }
         })
     },
     // 分页页码
     changePage(num) {
         this.get_information(num,this.str)
     },
   }
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
  /deep/.el-table .warning-row {
    background:#ffb3a7;
  }
/deep/.no{
    background:white;
  }
/deep/  .el-table .success-row {
    background: #f0f9eb;
  }
/*/deep/ .el-table_1_column_1.el-table-column--selection.el-table__cell{*/
/*  background: white;*/
/*}*/
.wrapper {
  margin: 20px 0;
}
</style>

