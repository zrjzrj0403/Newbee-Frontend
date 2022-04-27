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
    <div class="button">
      <el-button class="edit" type="primary" @click="changeit">编辑</el-button>
      <el-button class="confirm" type="primary" @click="confirmit">确认提交</el-button>
    </div>
    <div>
      <div class="display" v-show="!edit">
        <div v-show="!edit" style="white-space: pre-wrap;" class="text textbox title">
          <h1 style="text-align: center">{{ dynamicForm.title }}</h1>
        </div>
        <div class="information">
          <el-collapse v-model="activeNames">
            <el-collapse-item name="1" v-show="type!=='choice_question'">
              <span class="collapse-title" slot="title">题目正文</span>
              <div v-show="!edit" style="white-space: pre-wrap;" class="text textbox">
                <p>{{ dynamicForm.text }}</p>
              </div>
            </el-collapse-item>
            <div v-for="(item, index) in dynamicForm.counter">
              <el-collapse-item :name="''+(index+2)">
                <span class="collapse-title" slot="title">第{{ index + 1 }}小题信息</span>
                <div>
                  <el-button class="button2" type="primary" round @click="changed(index,item.id)"
                             style="margin-left: 16px;">
                    查看题解
                  </el-button>
                </div>
                <div v-show="!edit&&type!=='cloze_question'" v-model="item.stem" style="white-space: pre-wrap;"
                     class="text textbox sub_title">
                  {{ index + 1 }}.{{ item.stem }}
                </div>
                <div v-show="!edit" style="white-space: pre-wrap;" v-model="item.optionA" class="text textbox">
                  A.{{ item.optionA }}
                </div>
                <div v-show="!edit" style="white-space: pre-wrap;" v-model="item.optionB" class="text textbox">
                  B.{{ item.optionB }}
                </div>
                <div v-show="!edit" style="white-space: pre-wrap;" v-model="item.optionC" class="text textbox">
                  C.{{ item.optionC }}
                </div>
                <div v-show="!edit" style="white-space: pre-wrap;" v-model="item.optionD" class="text textbox">
                  D.{{ item.optionD }}
                </div>
                <div v-show="!edit" style="white-space: pre-wrap;" v-model="item.answer" class="text">
                  答案为：{{ item.answer }}
                </div>
              </el-collapse-item>
            </div>
          </el-collapse>
        </div>
      </div>
      <el-form :model="dynamicForm" ref="dynamicForm" label-width="120px" class="form" :rules="rule">
        <el-form-item v-show="edit" prop="title" label="题目标题">
          <el-input v-show="edit" v-model="dynamicForm.title" type="textarea" autosize @focus="getfocus">></el-input>
        </el-form-item>
        <el-form-item v-show="edit&&type!=='choice_question'" prop="text" label="题目正文">
          <el-input v-show="edit" v-model="dynamicForm.text" type="textarea" autosize
                    @change="onChange(2,$event)"></el-input>
        </el-form-item>
        <div v-for="(item, index) in dynamicForm.counter">
          <el-form-item v-show="edit&&type!=='cloze_question'" :label="'第'+(index+1)+'小题标题'"
                        :prop="'counter.' + index + '.stem'"
                        :rules="rule.stem">
            <el-input v-show="edit" v-model="item.stem" type="textarea" autosize
                      @change="onChange(3+(index)*5,$event)"></el-input>
          </el-form-item>
          <el-form-item v-show="edit" :label="'第'+(index+1)+'小题A选项'" :prop="'counter.' + index + '.optionA'"
                        :rules="rule.optionA">
            <el-input v-show="edit" v-model="item.optionA" type="textarea" autosize
                      @change="onChange(4+(index)*5,$event)"></el-input>
          </el-form-item>
          <el-form-item v-show="edit" :label="'第'+(index+1)+'小题B选项'" :prop="'counter.' + index + '.optionB'"
                        :rules="rule.optionB">
            <el-input v-show="edit" v-model="item.optionB" type="textarea" autosize
                      @change="onChange(5+(index)*5,$event)"></el-input>
          </el-form-item>
          <el-form-item v-show="edit" :label="'第'+(index+1)+'小题C选项'" :prop="'counter.' + index + '.optionC'"
                        :rules="rule.optionC">
            <el-input v-show="edit" v-model="item.optionC" type="textarea" autosize
                      @change="onChange(6+(index)*5,$event)"></el-input>
          </el-form-item>
          <el-form-item v-show="edit" :label="'第'+(index+1)+'小题D选项'" :prop="'counter.' + index + '.optionD'"
                        :rules="rule.optionD">
            <el-input v-show="edit" v-model="item.optionD" type="textarea" autosize
                      @change="onChange(7+(index)*5,$event)"></el-input>
          </el-form-item>
          <el-form-item v-show="edit" :label="'第'+(index+1)+'小题答案'" :prop="'counter.' + index + '.answer'"
                        :rules="rule.answer">
            <el-select v-model="item.answer" placeholder="请选择子题目答案">
              <el-option label="A" value="A"></el-option>
              <el-option label="B" value="B"></el-option>
              <el-option label="C" value="C"></el-option>
              <el-option label="D" value="D"></el-option>
            </el-select>
          </el-form-item>
        </div>
        <!--        <i-->
        <!--          :class="{'el-icon-edit': !edit, 'el-icon-check': edit}"-->
        <!--          @click="edit = !edit"-->
        <!--        ></i>-->
      </el-form>
      <br><br>
    </div>
    <el-drawer
      :visible.sync="drawer"
      :direction="direction"
      :before-close="handleClose">
      <div class="sublote">
        <h1>第{{ this.soluteid }}小题题解</h1>
        <el-table :data="gridData">
          <el-table-column property="date" label="日期" width="150"></el-table-column>
          <el-table-column property="name" label="姓名" width="200"></el-table-column>
          <el-table-column property="address" label="地址"></el-table-column>
        </el-table>
      </div>
    </el-drawer>
  </div>
</template>

<script>
import Wangeditor from "./Wangeditor";

export default {
  components: {
    Wangeditor,
  },
  data() {
    return {
      drawer: false,
      direction: 'ltr',
      change: false,
      edit: false,
      activeNames: ['1', '2', '3', '4', '5'],
      item2: '11',
      paths: '',
       gridData: [],
      judge: 0,
      item: '',
      textarea: 666,
      times: 0,
      type: '',
      id: 0,
      soluteid: 0,
      sub_que_num: 0,
      sub_que_t: [],
      dynamicForm: {
        title: '',
        text: '',
        counter: [],
        sub_que: [],
      },
      rule: {
        title: [{required: true, message: '标题不能为空', tigger: 'blur'}],
        text: [{required: true, message: '正文不能为空', tigger: 'blur'}],
        stem: [{required: true, message: '子题目不能为空', tigger: 'blur'}],
        optionA: [{required: true, message: 'A选择不能为空', tigger: 'blur'}],
        optionB: [{required: true, message: 'B选项不能为空', tigger: 'blur'}],
        optionC: [{required: true, message: 'C选择不能为空', tigger: 'blur'}],
        optionD: [{required: true, message: 'D选项不能为空', tigger: 'blur'}],
        answer: [{required: true, message: '答案不能为空', trigger: ["blur", 'change']}],
      },
      thistext: '',
    }
  },
  created() {
    this.get();//需要触发的函数
    this.get_details();
    // this.addInput();
  },
  methods: {
    changed(index, thisid) {
      this.drawer = true;
      this.soluteid = index + 1;
      this.$axios.get('/api/admin/solution', {params: {sub_question_id: thisid}})
    },
    handleClose(done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done();
        })
        .catch(_ => {
        });
    },
    this1() {
      console.log('yes')
    },
    changeit() {
      this.edit = !this.edit;
      this.judge = 1;
    },
    confirmit() {
      if (this.judge === 1) {
        console.log(this.dynamicForm.title);
        console.log(this.dynamicForm.text);
        console.log(this.dynamicForm.counter);
        console.log(this.type);
        // console.log()
        var i;
        for (i = 0; i < this.dynamicForm.counter.length; i++) {
          this.dynamicForm.sub_que.push({
            answer: this.dynamicForm.counter[i].answer,
            stem: this.dynamicForm.counter[i].stem,
            id: this.dynamicForm.counter[i].id,
            number: this.dynamicForm.counter[i].number,
            options: [this.dynamicForm.counter[i].optionA, this.dynamicForm.counter[i].optionB, this.dynamicForm.counter[i].optionC, this.dynamicForm.counter[i].optionD],
          })
        }
        let datas = {
          problemid: this.id,
          type: this.type,
          text: this.dynamicForm.text,
          title: this.dynamicForm.title,
          sub_que_num: this.sub_que_num,
          sub_que: this.dynamicForm.sub_que,
        }
        this.$axios({
          url: '/api/admin/designated_question', data: datas,
          method: "put",
          headers: {
            'Content-Type': 'application/json'
          }
        })
        this.judge = 0;
        this.$router.go(0);
      }
    },
    getfocus() {
      this.thistext = this.dynamicForm.title;
      console.log(this.thistext)
    },
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
      this.$axios.get('/api/admin/designated_question', {params: {id: this.id}})
        .then(res => {
          // console.log(res);
          this.dynamicForm.title = res.data.title;
          this.dynamicForm.text = res.data.text;
          this.sub_que_num = res.data.sub_que_num;
          // console.log(this.sub_que_num)
          // this.description_1 = res.data.sub_que[this.times].stem;
          // this.description_A = res.data.sub_que[this.times].options[0];
          // this.description_B = res.data.sub_que[this.times].options[1];
          // this.description_C = res.data.sub_que[this.times].options[2];
          // this.description_D = res.data.sub_que[this.times].options[3];
          this.sub_que_t = res.data.sub_que;
          console.log('tuins', res.data.sub_que)
          this.addInput();
          this.times = this.times + 1;
        })
    },
    onChange(a, e) {
      console.log(a)
      console.log(e)
      // const { value } = e.target;
      // console.log(e.target);
    },
    addInput() {
      var i;
      var j = 0;
      // console.log(this.sub_que_num)
      // console.log('3')
      console.log(this.sub_que_t);
      // this.sub_que_t.sort(function(a,b){return a.number-b.number});
      for (i = 0; i < this.sub_que_num; i++) {
        // this.radioSelect.forEach(item => {
        //   console.log(j)
        //   if (j === i) {
        //    console.log(this.sub_que_t[1])
        // for(j=0;j<this.sub_que_num;j++)
        // {
        // if(i==this.sub_que_t[j].number)
        // {
        // console.log(this.sub_que_t)
        this.dynamicForm.counter.push({
          id: this.sub_que_t[i].id,
          number: this.sub_que_t[i].number,
          'answer': this.sub_que_t[i].answer,
          stem: this.sub_que_t[i].stem,
          optionA: this.sub_que_t[i].options[0],
          optionB: this.sub_que_t[i].options[1],
          optionC: this.sub_que_t[i].options[2],
          optionD: this.sub_que_t[i].options[3],
          // 'description_C': 'description_D'
        })
        // }
        // }
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

.confirm {
  position: absolute;
  right: 5%;
}

.button {
  margin-left: 3%;
}

.form {
}

.collapse-title {
  flex: 1 0 90%;
  order: 1;
}

.information {
  margin: 1% 2%;
}

.display {
  margin-bottom: 2%;
}

.button2 {
  position: absolute;
  right: 5%;
}

.sublote {
  margin: 5%;
}
</style>
