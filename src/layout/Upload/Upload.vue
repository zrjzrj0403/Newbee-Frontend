<template>
  <div class="total">
    <div class="title1">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/home3' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>题目上传</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="box">
      <el-steps :space="600" align-center :active="step" finish-status="success">
        <el-step title="题目类型选择 题目标题上传"></el-step>
        <el-step title="题目内容上传"></el-step>
        <el-step title="内容阅览"></el-step>
      </el-steps>
    </div>
    <div class="form" v-if="step === 0">
      <el-form ref="question" :model="question" label-width="80px" size="mini" :rules="rule" prop="question">
        <el-form-item label="题目标题" prop="title">
          <el-input v-model="question.title" type="textarea" rows="2"></el-input>
        </el-form-item>
        <el-form-item label="题目类别" prop="type">
          <el-select v-model="question.type" placeholder="请选择题目类别">
            <el-option label="选择" value="choice_question"></el-option>
            <el-option label="完型" value="cloze_question"></el-option>
            <el-option label="阅读" value="reading_question"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="小题数量" prop="sub_que_num">
          <el-input-number v-model="question.sub_que_num" @change="handleChange" :min="1" :max="10"
                           label="描述文字"></el-input-number>
        </el-form-item>
        <el-form-item v-if="question.type!== 'choice_question'" label="题目内容" prop="text">
          <el-input v-model="question.text" type="textarea" rows="8"></el-input>
        </el-form-item>
        <!--        <el-form-item size="large">-->
        <!--         <el-button class='button'  type="primary"    @click="changeStrp">下一步</el-button>-->
        <!--        </el-form-item>-->
        <el-button class='button' type="success" @click="changeStrp">下一步</el-button>
      </el-form>
    </div>
    <div v-if="step === 1">
      <el-form ref="dynamicForm" :model="dynamicForm" label-width="80px" size="mini" prop="dynamicForm">
        <div class="form" v-for="(item, index) in dynamicForm.counter">
          <el-form-item label="子题目标题" v-if="question.type!== 'cloze_question'" :prop="'counter.' + index + '.stem'"
                        :rules="rules2.stem">
            <el-input v-model="item.stem" type="textarea" rows="2"></el-input>
          </el-form-item>
          <el-form-item label="子题目选项" :prop="'counter.' + index + '.option'" :rules="rules2.option">
            <el-input v-model="item.option" type="textarea" rows="8" @change="changeit($event,index)"></el-input>
          </el-form-item>
          <el-form-item label="子题目答案" :prop="'counter.' + index + '.answer'" :rules="rules2.answer">
            <el-select v-model="item.answer" placeholder="请选择子题目答案">
              <el-option label="A" value="A"></el-option>
              <el-option label="B" value="B"></el-option>
              <el-option label="C" value="C"></el-option>
              <el-option label="D" value="D"></el-option>
            </el-select>
          </el-form-item>
        </div>
      </el-form>
      <el-button class='button' type="primary" @click="upStep">上一步</el-button>
      <el-button class='button' type="success" @click="changeStrp">下一步</el-button>
    </div>
    <div>
      <div v-if="step === 2">
        <div v-show="!edit" style="white-space: pre-wrap;" class="text textbox">
          <h1 style="text-align: center">{{ question.title }}</h1>
        </div>
        <el-input v-show="edit" v-model="question.title" type="textarea" autosize>></el-input>
        <br>
        <div v-show="!edit" style="white-space: pre-wrap;" class="text2 textbox"
             v-if="question.type==='reading_question'">该题目的类型为：阅读
        </div>
        <div v-show="!edit" style="white-space: pre-wrap;" class="text2 textbox"
             v-if="question.type==='cloze_question'">该题目的类型为：完型
        </div>
        <div v-show="!edit" style="white-space: pre-wrap;" class="text2 textbox"
             v-if="question.type==='choice_question'">该题目的类型为：选择
        </div>
        <el-select v-show="edit" v-model="question.type" placeholder="请选择子题目答案">
          <el-option label="选择" value="choice_question"></el-option>
          <el-option label="完型" value="cloze_question"></el-option>
          <el-option label="阅读" value="reading_question"></el-option>
        </el-select>
        <br>
        <el-input v-show="edit" v-model="question.text" type="textarea" autosize></el-input>
        <div v-show="!edit" style="white-space: pre-wrap;" class="text textbox">{{ question.text }}</div>
        <br>
        <div v-for="(item, index) in subque">
          <div v-show="!edit" v-model="item.stem" style="white-space: pre-wrap;" class="text textbox sub_title">
            {{ index + 1 }}.{{ item.stem }}
          </div>
          <div v-show="!edit" style="white-space: pre-wrap;" v-model="item.options[0]" class="text textbox">
            A.{{ item.options[0] }}
          </div>
          <el-input v-show="edit" v-model="item.options[0]" type="textarea" autosize
                    @change="onChange(4+(index)*5,$event)"></el-input>
          <div v-show="!edit" style="white-space: pre-wrap;" v-model="item.options[1]" class="text textbox">
            B.{{ item.options[1] }}
          </div>
          <el-input v-show="edit" v-model="item.options[1]" type="textarea" autosize
                    @change="onChange(5+(index)*5,$event)"></el-input>
          <div v-show="!edit" style="white-space: pre-wrap;" v-model="item.options[2]" class="text textbox">
            C.{{ item.options[2] }}
          </div>
          <el-input v-show="edit" v-model="item.options[2]" type="textarea" autosize
                    @change="onChange(6+(index)*5,$event)"></el-input>
          <div v-show="!edit" style="white-space: pre-wrap;" v-model="item.options[3]" class="text textbox">
            D.{{ item.options[3] }}
          </div>
          <el-input v-show="edit" v-model="item.options[3]" type="textarea" autosize
                    @change="onChange(7+(index)*5,$event)"></el-input>
          <div v-show="!edit" style="white-space: pre-wrap;" v-model="item.answer" class="text textbox">
            答案为：{{ item.answer }}
          </div>
          <el-select v-show="edit" v-model="item.answer" placeholder="请选择子题目答案">
            <el-option label="A" value="A"></el-option>
            <el-option label="B" value="B"></el-option>
            <el-option label="C" value="C"></el-option>
            <el-option label="D" value="D"></el-option>
          </el-select>
        </div>
        <el-button class='button' type="primary" @click="upStep">上一步</el-button>
        <el-button class='button' type="success" @click="changeStrp2">确定提交</el-button>
        <el-button class='button' type="primary" @click="edit = !edit">编辑</el-button>
        <i
          :class="{'el-icon-edit': !edit, 'el-icon-check': edit}"
          @click="edit = !edit"
        ></i>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      subque: [],
      edit: false,
      option: [
        {value: "reading_question"},
      ],
      question: {
        title: '',
        type: '',
        sub_que_num: '',
        text: '',
        answer: ''
      },
      rule: {
        title: [{required: true, message: '题目不能为空', tigger: 'change'}],
        type: [{required: true, message: '类型不能为空', trigger: ["blur", 'change']}],
        text: [{required: true, message: '题目不能为空', tigger: 'blur'}],
        sub_que_num: [{required: true}],
      },
      num: '',
      step: 0,
      nextstep: 0,
      dynamicForm: {
        counter: [],
      },
      rules2: {
        stem: [{required: true, message: '子题目不能为空', tigger: 'blur'}],
        option: [{required: true, message: '选项不能为空', tigger: 'blur'}],
        answer: [{required: true, message: '答案不能为空', trigger: ["blur", 'change']}],
      },
      str: [],
      savestr: [],
    }
  },
  created() {
    // this.test();
    //   this.question.type=this.option[0].value;
    this.step = 0;
  },
  methods: {
    changeit(e, a) {
      // str="A.the average sur-vival tim_e of condor's is satisfactory.\n" +
      //   "B.Rideouts research interest lies in electric engineering\n" +
      //   "C.the efforts to protect condors have brought good results\n" +
      //   "D.researchers have found the final answers to the problem";
      this.str = e.split(/A\.\s*((?:[a-zA-Z0-9-_'’.?!]+\x20?)+)\s*\r*\n*B\.\s*((?:[a-zA-Z0-9-_'’.?!]+\x20?)+)\w*\s*\r*\n*C\.\s*((?:[a-zA-Z0-9-_'’.!?]+\x20?)+)\w*\s*\r*\n*D\.\s*((?:[a-zA-Z0-9-_'’.!?]+\x20?)+)\s*\r*\n*/);//使用，作为分隔符，输出：["Hello","can I help you?"]
      this.savestr[a] = this.str;
      // console.log(this.savestr)
      // console.log(e)
    },
    handleChange(value) {
      // console.log(value);
    },
    upStep() {
      if (this.step >= 0) {
        if (this.nextstep < this.step) {
          this.nextstep = this.step;
        }
        this.step = this.step - 1;
      } else {
        this.step = 0;
      }
    },
    changeStrp() {
      if (this.step === 0) {
        this.$refs.question.validate(valid => {
          if (valid) {
            var sub_que_num, title, text, type;
            title = this.question.title
            sub_que_num = this.question.sub_que_num;
            type = this.question.type;
            text = this.question.text;
            var i;
            if (this.nextstep === 0) {
              this.num = this.question.sub_que_num;
              for (i = 0; i < sub_que_num; i++) {
                // // console.log(i)
                this.dynamicForm.counter.push({
                  stem: "",
                  option: "",
                  answer: "",
                })
              }
            }
            if (this.num !== sub_que_num) {
              this.num = sub_que_num;
              this.dynamicForm.counter = [];
              for (i = 0; i < sub_que_num; i++) {
                // console.log(i)
                this.dynamicForm.counter.push({
                  stem: "",
                  option: "",
                })
              }
            }
            this.step = 1;
          }
        })
      } else if (this.step === 1) {
        this.$refs.dynamicForm.validate(valid => {
          if (valid) {
            var i;
            console.log(this.dynamicForm.counter)
            this.subque.length = 0;
            console.log(this.subque)
            for (i = 0; i < this.question.sub_que_num; i++) {
              this.subque.push(
                {
                  stem: this.dynamicForm.counter[i].stem,
                  options: this.savestr[i].slice(1, 5),
                  answer: this.dynamicForm.counter[i].answer,
                  number: i + 1,
                }
              )
              // this.subque[i].stem=this.dynamicForm.counter[i].stem;
              // this.subque[i].options=this.savestr[i].slice(1,5);
              // this.subque[i].answer=this.dynamicForm.counter[i].answer;
            }
            console.log(this.subque)
            // this.subque=this.subque.slice(0,0)
            // console.log(this.subque)
            this.step = 2;
          }
        })
      } else if (this.step === 2) {
        this.$router.go(0);
      }
    },
    changeStrp2() {
      console.log(this.subque);
      console.log(this.question.sub_que_num);
      console.log(this.question.text);
      console.log(this.question.type);
      let datas = {
        type: this.question.type,
        text: this.question.text,
        title: this.question.title,
        sub_que_num: this.question.sub_que_num,
        sub_que: this.subque
      }
      this.$axios({
        url: '/api/admin/designated_question', data: datas,
        method: "post",
        headers: {
          'Content-Type': 'application/json'
        }
      })
      this.$router.go(0);
    },
    onSubmit() {
      console.log('submit!');
    }
  }
}
</script>

<style scoped>
.box {
  margin: 60px auto;
}

.button {
  right: 100px;
  /*margin:80px 0;*/
  margin-left: 80px;
}

.form {
  margin: 0 100px;
  font-size: 13px;
}

.form .el-form-item__label {
  font-size: 13px;
}

.text {
  font-size: 14px;
}

.sub_title {
  font-size: 16px;
}

.textbox {
  margin: 0 50px;
}

.text2 {
  font-size: 16px;
}
</style>
