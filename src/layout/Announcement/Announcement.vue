<template>
  <div class="box">
    <div class="title1">
      <h4>首页/公告管理</h4>
    </div>
    <div style="width:50%;margin:auto">
      <div style="width:50%;margin:auto">
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <img src="../../../公告管理.jpg" style="margin:auto">
      </div>
      <el-input class="shuru"
                rows="25"
                width="50%"
                vertical-align="middle"
                border-radius:="20px"
                maxlength="200"
                show-word-limit
                box-shadow=" 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)"
                type="textarea"
                placeholder="请输入内容"
                v-model="textarea">
      </el-input>
      <div style="float:right">
        <div class="block">
          <span class="demonstration">请选择发布时间</span>
          <el-date-picker
            v-model="value2"
            align="right"
            type="date"
            placeholder="选择日期"
            :picker-options="pickerOptions1">
          </el-date-picker>
          <el-time-picker
            v-model="value1"
            placeholder="请选择一小时之后的日期">
          </el-time-picker>
        </div>
        <div style="float:right">
          <br><br>
          <el-row>
            <el-button type="primary" icon="el-icon-edit" circle @click="test1()"></el-button>
            <el-popconfirm
              confirm-button-text='好的'
              cancel-button-text='不用了'
              icon="el-icon-info"
              icon-color="red"
              title="确定要删除上述公告吗？"
              @confirm="test()"
            >
              <el-button slot="reference" type="danger" icon="el-icon-delete">删除</el-button>
            </el-popconfirm>
            <el-button type="success" round>提交</el-button>
          </el-row>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // var qingkong=1;
      textarea: '',
      value1: new Date(2021, 4, 6, 18, 40),
      pickerOptions1: {
        disabledDate(time) {
          return time.getTime() < (Date.now() - 3600 * 1000 * 24);
        },
        shortcuts: [{
          text: '今天',
          onClick(picker) {
            picker.$emit('pick', new Date());
          }
        }, {
          text: '明天',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() + 3600 * 1000 * 24);
            picker.$emit('pick', date);
          }
        }, {
          text: '后天',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() + 3600 * 1000 * 24 * 2);
            picker.$emit('pick', date);
          }
        }]
      },
      value2: '',
      // if(qingkong=0)
      // {
      //   textarea=''
      //   qingkong=1
      // }
    }
  },
  methods: {
    test() {
      // qingkong=0
      this.textarea = ''
    },
    test1() {
      // qingkong=0
      this.textarea = 'Welcome To NewBee English!!!'
    },
  }

}
</script>

<style scoped>
.title1{
  margin-bottom: 20px;
}
</style>
