<template>
  <div class="total">
    <div class="title1">
      <el-breadcrumb style="margin-left: 1%" separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{path: '/home3' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="user">
      <!--    搜索区域-->
      <div class="userheader">
        <el-input @keyup.enter.native="searchinput(input,num)" v-model="input" placeholder="请输入内容"></el-input>
        <el-button @click="searchinput(input,num)" type="primary">查询</el-button>
        <el-button type="primary" @click="batchDelete(tableChecked)">批量删除</el-button>
      </div>
      <!--  2.表格区域 展示视图数据-->
      <div class="wrapper">
        <el-table border :data="tableData" @sort-change="sortChange" style="width: 100%"
                  @selection-change="handleSelectionChange">
          <el-table-column type="selection" width="55"></el-table-column>
          <el-table-column prop="name" label="用户名称" width="180"></el-table-column>
          <el-table-column prop="id" label="用户id" width="180"></el-table-column>
          <el-table-column prop="numm" sortable="custom" label="单选数量" width="180"></el-table-column>
          <el-table-column prop="numc" label="完型数量" sortable="custom" width="180"></el-table-column>
          <el-table-column prop="numr" label="阅读数量" sortable="custom" width="180"></el-table-column>
          <el-table-column prop="operate" label="操作">
            <template slot-scope="scope">
              <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)"
              >删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <!--  3.分页-->
      <div>
        <Mypagination :total='total' :pageSize='pageSize' @changePage='changePage'/>
      </div>
    </div>
  </div>
</template>

<script>
import Mypagination from "../../components/Mypagination";

export default {
  components: {
    Mypagination
  },
  data() {
    return {
      tabSort: 0, //该字段代表升序还是降序 假设：0正序 1倒序
      tabProp: '',//prop绑定的字段名
      input: '',
      tableData: [],
      tableChecked: [],
      ids: [],
      total: 10,
      pageSize: 12,
      page: 1,
      type: 1,
      num: 1,
      val: '',
      column2:''
    }
  },
  created() {
    this.get_information(this.tabSort,this.tabProp,1);//需要触发的函数
  },
  methods: {
    sortChange(column,num) {

      if (column.order === "ascending") {
        this.tabSort = 1
      } else if (column.order === "descending") {
        this.tabSort = 0
      } else {
        this.tabSort = 0
      }
      this.tabProp = column.prop
      this.get_information(this.tabSort,this.tabProp ,1)
    },

    // 搜索查询数据
    searchinput(val, num) {
      console.log(val)
      if (!val) {
        this.$router.go(0);
        type = 1;
        return;
      } else {
        console.log('搜索', num);
        this.val = val;
        // let  data=this.$qs.stringify({name:val})
        //     this.$axios.post('/api/api_search',data)
        this.$axios.get('/api/admin/designated_user', {params: {name: val, pagesize: 12, pagenumber: num}})
          .then(res => {
            if (res.data.ret === 0) {
              console.log(this.num);
              // this.tableData=[{name:res.data.num.name,numm:res.data.num.numm}]
              this.tableData = res.data.list;
              this.type = 2;
              this.total = res.data.total;
            } else {
              this.type = 2;
              this.total = res.data.total;
            }
          })
      }
    },
    handleSelectionChange(val) {
      let id = val.map(item => item.id);
      this.tableChecked = id;
    },
    // 编辑操作
    handleEdit() {
    },
    //批量删除
    batchDelete(rows) {
      if (rows.length <= 0) {//选中0条数据时
        this.$message.info("未选中数据");
      } else {
        this.$confirm('此操作将永久删除用户, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$axios.delete('/api/admin/list_user', {
            params: {userid: rows},
            paramsSerializer: params => {
              return this.$qs.stringify(params, {indices: false})
            }
          })
            .then(res => {
              if (res.data.ret === 0) {
                this.$message({
                  type: 'success',
                  message: '删除成功!'
                });
                this.$router.go(0);
              } else {
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
    // 单个删除
    handleDelete(index, row) {
      this.$confirm('此操作将永久删除该用户, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        // let  data=this.$qs.stringify({rows:row.id})
        this.$axios.delete('/api/admin/list_user', {params: {userid: row.id}})
          .then(res => {
            if (res.data.ret === 0) {
              this.$message({
                type: 'success',
                message: '删除成功!'
              });
              this.$router.go(0);
            } else {
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
    get_information(tabSort,tabProp,pagenumber) {
      console.log(tabSort);
      console.log(tabProp);
      this.$axios.get('/api/admin/list_user', {params: {pagenumber: pagenumber, pagesize: 12}})
        .then(res => {
          console.log(res)
          if (res.data.ret === 0) {
            // this.tableData=[{name:res.data.num.name,numm:res.data.num.numm}]
            // console.log(res.data)
            this.tableData = res.data.list;
            this.total = res.data.total;
            // console.log(res)
          }
        })
    },
    // 分页页码
    changePage(num) {
      if (this.type === 1) {
        this.get_information(this.tabSort,this.tabProp,num)
      } else {

        this.searchinput(this.val, num)
      }

    }
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

.wrapper {
  margin: 20px 0;
}
</style>
