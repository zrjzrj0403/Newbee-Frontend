<template>
  <div>
          <div>
              <el-input style="width:230px" placeholder="请输入学校" autocomplete="off"></el-input>
              <el-input style="width:180px" placeholder="请输入专业" autocomplete="off"></el-input>
              <el-input style="width:150px" placeholder="请输入安置人数" autocomplete="off"></el-input>
              <el-date-picker type="month" placeholder="选择安置日期" format="yyyy 年 MM 月" value-format="yyyy-MM-dd"></el-date-picker>
              <el-button type="success" @click="addInput" icon="el-icon-plus"></el-button>
          </div>
          <div v-for="(item, index) in dynamicForm.counter">
              <el-input style="width:230px" v-model="item.xxName" placeholder="请输入学校" autocomplete="off"></el-input>
              <el-input style="width:180px" v-model="item.zyName" placeholder="请输入专业" autocomplete="off"></el-input>
              <el-input style="width:150px" v-model="item.azCount" placeholder="请输入安置人数" autocomplete="off"></el-input>
              <el-date-picker v-model="item.azDate" type="month" placeholder="选择安置日期" format="yyyy 年 MM 月" value-format="yyyy-MM-dd"></el-date-picker>
              <el-button type="danger" @click="delInput(item, index)" icon="el-icon-minus"></el-button>
          </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        dynamicFormVisible: true,
        dynamicForm: {
          counter: []
        }
      }
    },
    created() {
      this.addInput();
    },
    methods: {
      addInput() {
        var i;
        for (i = 0; i < 4; i++)
        {
         this.dynamicForm.counter.push({xxName: i, zyName: '', azCount: '', azDate: '' })
        }
      },
      delInput(index) {
        this.dynamicForm.counter.splice(index, 1)
      },
    }
  }
</script>

<style scoped>

</style>
