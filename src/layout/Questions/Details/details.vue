<template>
  <div>
    <div class="title1">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home3' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: this.$route.path}">题目管理</el-breadcrumb-item>
        <el-breadcrumb-item :to="{path:paths}">{{ item }}</el-breadcrumb-item>
        <el-breadcrumb-item>题目详情</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div>
      <router-view/>
    </div>
    <div>
      <h1 style="text-align: center;">题目详情</h1>
    </div>
    <el-button type="primary" @click="edit = !edit">编辑</el-button>
    <div>
      <div v-show="!edit" style="white-space: pre-wrap;" class="text textbox">
        <h1 style="text-align: center">{{ description_title }}</h1>
      </div>
      <el-input v-show="edit" v-model="description_title" type="textarea" autosize></el-input>
      <br>
      <div v-show="!edit" style="white-space: pre-wrap;" class="text textbox">{{ description }}</div>
      <el-input v-show="edit" v-model="description" type="textarea" autosize></el-input>
      <br>
      <div v-for="(item, index) in dynamicForm.counter">
        <div v-show="!edit" v-model="item.description_1" style="white-space: pre-wrap;" class="text textbox sub_title">
          {{ index + 1 }}.{{ item.description_1 }}
        </div>
        <el-input v-show="edit" v-model="item.description_1" type="textarea" autosize></el-input>
        <div v-show="!edit" style="white-space: pre-wrap;" v-model="item.description_A" class="text textbox">
          A.{{ item.description_A }}
        </div>
        <el-input v-show="edit" v-model="item.description_A" type="textarea" autosize></el-input>
        <div v-show="!edit" style="white-space: pre-wrap;" v-model="item.description_B" class="text textbox">
          B.{{ item.description_B }}
        </div>
        <el-input v-show="edit" v-model="item.description_B" type="textarea" autosize></el-input>
        <div v-show="!edit" style="white-space: pre-wrap;" v-model="item.description_C" class="text textbox">
          C.{{ item.description_C }}
        </div>
        <el-input v-show="edit" v-model="item.description_C" type="textarea" autosize></el-input>
        <div v-show="!edit" style="white-space: pre-wrap;" v-model="item.description_D" class="text textbox">
          D.{{ item.description_D }}
        </div>
        <el-input v-show="edit" v-model="item.description_D" type="textarea" autosize></el-input>
        <!--            radioSelect[index]-->
      </div>
      <i
        :class="{'el-icon-edit': !edit, 'el-icon-check': edit}"
        @click="edit = !edit"
      ></i>
    </div>
    <div>

    </div>
    <div>

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      edit: false,
      description_title: "我是题目",
      description: "我是文章",
      description_1: '',
      description_A: '',
      description_B: '',
      description_C: '',
      description_D: '',
      item2: '11',
      paths: '',
      item: '',
      textarea: 666,
      times: 0,
      id: 0,
      sub_que_num: 0,
      sub_que_t: [],
      dynamicForm: {
        counter: []
      },
      radioSelect: [{name: 'description_1'}, {name: 'description_2'}, {name: 'description_3'}],
    }
  },
  created() {
    this.get();//需要触发的函数
    this.get_details();
    // this.addInput();
  },
  methods: {
    get() {
      // console.log('1')
      this.id = this.$route.query.id;
      this.type = this.$route.query.type;
      if (this.type === 'choice_question') {
        this.item = '单项选择';
        this.paths = '/question/multiplechoice';
      } else if (this.type === 'cloze_question') {
        this.item = '完型填空';
        this.paths = '/question/cloze';
      } else {
        this.item = '阅读理解';
        this.paths = '/question/readingcomprehension';
      }
    },
    get_details() {
      this.$axios.get('/api/admin/designated_question/', {params: {id: this.id}})
        .then(res => {
          // console.log(res);
          this.description_title = res.data.title;
          this.description = res.data.text;
          this.sub_que_num = res.data.sub_que_num;
          // console.log(this.sub_que_num)
          // this.description_1 = res.data.sub_que[this.times].stem;
          // this.description_A = res.data.sub_que[this.times].options[0];
          // this.description_B = res.data.sub_que[this.times].options[1];
          // this.description_C = res.data.sub_que[this.times].options[2];
          // this.description_D = res.data.sub_que[this.times].options[3];
          this.sub_que_t = res.data.sub_que;
          this.addInput();
          this.times = this.times + 1;
        })
    },
    addInput() {
      var i;
      var j = 0;
      // console.log(this.sub_que_num)
      // console.log('3')
      console.log(this.sub_que_t);
      for (i = 0; i < this.sub_que_num; i++) {
        // this.radioSelect.forEach(item => {
        //   console.log(j)
        //   if (j === i) {
        //    console.log(this.sub_que_t[1])
        this.dynamicForm.counter.push({
          description_1: this.sub_que_t[i].stem,
          description_A: this.sub_que_t[i].options[0],
          description_B: this.sub_que_t[i].options[1],
          description_C: this.sub_que_t[i].options[2],
          description_D: this.sub_que_t[i].options[3],
          // 'description_C': 'description_D'
        })
        // q=item.name;
        // console.log(this.q)
        // console.log(this)
        // this.item.name = this.sub_que_t[i].stem;
        //  console.log(this.sub_que_t[i].stem)
      }
      //     j = j + 1;
      // })
      // j = 0;
      //     // }
      console.log(this)
    }
  }
  // }
}
</script>

<style scoped>
.text {
  font-size: 14px;
}

.sub_title {
  font-size: 16px;
}

.textbox {
  margin: 0 50px;
}
</style>
