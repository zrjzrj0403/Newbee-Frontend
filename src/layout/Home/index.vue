<template>
  <div class="top">
    <div class="header1">
      <div class="box3">
        <el-row class="home" :gutter="10">
          <!--span默认一共是24，这里占8 下面占16，所以这两个分隔栏所占的宽度 是1:2-->
          <el-col :span="21" style="margin-top: 5px">

            <div class="box" :style="{height: scrollerHeight0}">
              <div class="box" :style="{height: scrollerHeight0}">
                <e-charts
                  class="chart" :option="optionbiaoti" :style="{height: scrollerHeight0}"/>
              </div>
            </div>

          </el-col>
          <el-col :span="1" :offset="2">
            <!--shadow属性设置卡片阴影出现的时机-->
            <img class='img2' src="../../assets/logo1.jpg" :style="{height: scrollerHeight0,wight:scrollerHeight0}"/>
          </el-col>
        </el-row>
      </div>

      <el-row :gutter="10">
        <el-col class='col1' :span="8">
          <el-row :gutter="10">
            <div class="num">
              <el-card class="userico" shadow="hover" body-style="{ display: 'flex', padding: 0}">
                <div class="icon1" style="text-align: center"
                     :style="{height: scrollerHeight4,width:scrollerHeight4}">
                  <i class="icon1_1 el-icon-user" :style="{padding:scrollerpadding1}"></i>
                </div>
                <div class="miaoshu1">
                  <div class="miaoshu">
                    <p class="num biaoshi">{{ usernumber }}</p>
                    <p class="txt">用户数量</p>
                  </div>
                </div>
              </el-card>
            </div>
          </el-row>
          <el-row :gutter="10">
            <div class="num">
              <el-card class="userico" shadow="hover" body-style="{ display: 'flex', padding: 0}">
                <div class="icon2" style="text-align: center"
                     :style="{height: scrollerHeight4,width:scrollerHeight4}">
                  <i style="margin: auto" class="icon1_1 el-icon-tickets " :style="{padding:scrollerpadding1}"></i>
                </div>
                <div class="miaoshu1">
                  <div class="miaoshu">
                    <p class="num biaoshi2">{{ questionnumber }}</p>
                    <p class="txt">题目数量</p>
                  </div>
                </div>
              </el-card>
            </div>
          </el-row>
          <el-row :gutter="10">
            <div class="num">
              <el-card class="userico" shadow="hover" body-style="{ display: 'flex', padding: 0}">
                <div class="icon3" style="text-align: center"
                     :style="{height: scrollerHeight4,width:scrollerHeight4}">
                  <i class="icon1_1 el-icon-warning-outline" :style="{padding:scrollerpadding1}"></i>
                </div>
                <div class="miaoshu1">
                  <div class="miaoshu">
                    <p class="num biaoshi3">{{ bad_solution_number }}</p>
                    <p class="txt">待处理题解</p>
                  </div>
                </div>
              </el-card>
            </div>
          </el-row>
        </el-col>
        <el-col :span="16">
          <el-card class="card1" style=" height:480px" shadow="hover"
                   :style="{height: scrollerHeight5}">
            <h1>管理员操作列表</h1>
            <el-table
              :data="tableData"
              style="width: 100%;padding-top: 10px">
              <el-table-column
                prop="name"
                label="管理员名称"
                width="200">
              </el-table-column>
              <el-table-column
                prop="op_type"
                label="操作"
                width="200">
              </el-table-column>
              <el-table-column
                prop="description"
                label="操作对象">
              </el-table-column>
            </el-table>
            <div>
              <Mypagination :total='total' :pageSize='pageSize' @changePage='changePage'/>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <el-row class="el-row2" type="flex" :gutter="10">
        <el-col :span="14">
          <div>
            <el-card class="card1" style=" margin-top: 10px ;" shadow="hover" :style="{height: scrollerHeight3}">
              <div>
                <e-charts
                  class="chart" :option="option" :style="{height:scrollerHeight3}"/>
              </div>
            </el-card>
          </div>
        </el-col>
        <el-col :span="10">
          <div class="card3">
            <el-card class="card1" style=" margin-top: 10px ;" shadow="hover" :style="{height: scrollerHeight3}">
              <div>
                <e-charts
                  className="chart3 " :option="optiontu" :style="{height:scrollerHeight6}"/>
              </div>
            </el-card>
          </div>
        </el-col>
      </el-row>
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
      total: 10,
      bad_solution_number: 554,
      pageSize: 4,
      tableData: [],
      usernumber: 123,
      questionnumber: 222,
      optiontu: {
        title: {
          text: '各类题型数量',
          subtext: '请大家多传传体量较小的题！！',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        series: [
          {
            center: ["50%", "60%"],
            name: '题目数量:',
            type: 'pie',
            radius: '70%',
            labelLine: {
              normal: {
                length: 10,     // 指示线宽度
                lineStyle: {
                  color: "#135ae7",  // 指示线颜色
                  width: 5,
                }
              },
            },
            label: {
              normal: {
                formatter: function (params) {
                  return params.name + ':' + params.value + "\n\n" + params.percent + "%";
                },
                textStyle: {            // 提示文字的样式
                  color: '#482828',
                  fontSize: 15,
                }
              }
            },
            data: [],
            itemStyle: {
              color: {
                image: require('../../assets/logo最终版1.jpg'),
                wight: '100px',
                repeat: 'repeat'
              },
              borderWidth: 3,
              borderColor: '#3a5bde'
            },
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 1)'
              }
            }
          }
        ],
      },
      option: {
        title: {
          text: "特此表彰，选择题做对数量前五名",
          subtext: "请在每周日发送表彰公告\n"
        },
        legend: {
          x: "40%",

          data: ['单项选择', '完形填空', '阅读理解'],
          selectedMode: false, //取消图例上的点击事件
        },
        grid: {
          top: '25%',
          bottom: '7%',
          right: '7%',
          left: '7%',
          containLabel: true,
        },
        toolbox: { //可视化的工具箱
          show: true,
          feature: {
            dataView: { //数据视图
              show: true
            },
            saveAsImage: {//保存图片
              show: true
            },
            magicType: {//动态类型切换
              type: ['bar', 'line']
            }
          }
        },
        tooltip: {
          trigger: 'axis',
          borderColor: '#333',
          formatter: function (params) {
            var dotHtml = '<span style="display:inline-block;margin-right:3px;border-radius:5px;width:15px;height:15px;background-color:#5B76C8"></span>'
            var dotHtml2 = '<span style="display:inline-block;margin-right:3px;border-radius:5px;width:15px;height:15px;background-color:#B0D7A5"></span>'
            var dotHtml3 = '<span style="display:inline-block;margin-right:3px;border-radius:5px;width:15px;height:15px;background-color:#FADC58"></span>'
            return (
              dotHtml + '单项选择:' + '<br>' + (params[0].name ? params[0].name : "") + ':' + (params[0].data.code ? params[0].data.code : "") +
              '<br/>' +
              '答对数量: ' +
              (params[0].value ? params[0].value : "") + '<br>' + dotHtml2 + '完形填空:' + '<br>' +
              (params[1].name ? params[1].name : "") + ':' + (params[1].data.code ? params[1].data.code : "") +
              '<br/>' +
              '答对数量: ' +
              (params[1].value ? params[1].value : "") + '<br>' + dotHtml3 + '阅读理解:' + '<br>' +
              (params[2].name ? params[2].name : "") + ':' + (params[2].data.code ? params[2].data.code : "") +
              '<br/>' +
              '答对数量: ' +
              (params[2].value ? params[2].value : "")
            );
          },
          axisPointer: {
            type: 'shadow'
          }
        },
        xAxis: [
          {
            type: 'category',
            axisTick: {show: false},
            data: ['First', 'Second', 'Third', 'Fourth', 'Fifth']
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: '单项选择',
            type: 'bar',
            barGap: 0,
            emphasis: {
              focus: 'series'
            },
            label: {
              show: true,
              color: '#5B76C8',
              fontWeight: 'bold',
              fontSize: '20',
              position: 'top'
            },
            data: [{value: '220', code: '小赵'}, {value: '191', code: '小李'}, {value: '182', code: '小姜'}, {
              value: '172',
              code: '小徐'
            }, {value: '160', code: '小LD'}]
          },
          {
            name: '完形填空',
            type: 'bar',
            emphasis: {
              focus: 'series'
            },
            label: {
              show: true,
              color: '#B0D7A5',
              fontWeight: 'bold',
              fontSize: '20',
              position: 'top'
            },
            data: [{value: '320', code: '小李'}, {value: '300', code: '小赵'}, {value: '250', code: '小姜'}, {
              value: '201',
              code: '小徐'
            }, {value: '150', code: '小LD'}]
          },
          {
            name: '阅读理解',
            type: 'bar',
            emphasis: {
              focus: 'series'
            },
            label: {
              show: true,
              color: '#FADC58',
              fontWeight: 'bold',
              fontSize: '20',
              position: 'top'
            },
            data: [{value: '234', code: '小姜'}, {value: '231', code: '小徐'}, {value: '180', code: '小LD'}, {
              value: '177',
              code: '小赵'
            }, {value: '165', code: '小李'}]
          },
        ]
      },
      optionbiaoti: {
        graphic: {
          elements: [
            {
              type: 'text',
              left: '1%',
              top: '3%',
              style: {
                text: 'Welcome To New Bee English',
                fontSize: 70,
                fontWeight: 'bold',
                lineDash: [0, 200],
                lineDashOffset: 0,
                fill: 'transparent',
                stroke: '#000',
                lineWidth: 1
              },
              keyframeAnimation: {
                duration: 6000,
                loop: true,
                keyframes: [
                  {
                    percent: 0.25,
                    style: {
                      fill: 'transparent',
                      lineDashOffset: 200,
                      lineDash: [100, 0]
                    }
                  },
                  {
                    // Stop for a while.
                    percent: 0.25,
                    style: {
                      fill: 'transparent'
                    }
                  },
                  {
                    percent: 0.30,
                    style: {
                      fill: "black"
                    }
                  }
                ]
              }
            }
          ]
        }
      },
      curheight: 0,
      padding1: 0,
      userImg: require('../../assets/logo.jpg'),
      countData: [],
      tableLabel: {
        name: '课程',
        todayBuy: '今日购买',
        monthBuy: '本月购买',
        totalBuy: '总购买'
      }
    }
  },
  computed: {
    // 滚动区高度
    // (业务需求：手机屏幕高度减去头部标题和底部tabbar的高度，当然这2个高度也是可以动态获取的)
    scrollerHeight: function () {
      return ((this.curheight - 60) * 0.3) + 'px';
    },
    scrollerHeight0: function () {
      return ((this.curheight - 60) * 0.09) + 5 + 'px';
    },
    scrollerHeight1: function () {
      return ((this.curheight - 60) * 0.09) - 5 + 'px';
    },
    scrollerHeight2: function () {
      return ((this.curheight - 60) * 0.5) - 10 + 'px';
    },
    scrollerHeight3: function () {
      return ((this.curheight - 60) * 0.4) - 30 + 'px';
    },
    scrollerHeight4: function () {
      this.padding1 = (((this.curheight - 60) * 0.5)) / 3;
      return (((this.curheight - 60) * 0.5) - 10) / 3 + 'px';
    },
    scrollerHeight5: function () {
      return ((this.curheight - 60) * 0.5 - 10) + 'px';
    },
    scrollerHeight6: function () {
      return ((this.curheight - 60) * 0.3) + 'px';
    },
    scrollerpadding1: function () {
      return ((this.padding1 - 50) / 2 + 'px');
    }
  },
  methods: {
    getit() {
      this.$axios.get('/api/admin/has_bad_solution')
        .then(res => {
          this.has_bad_solution = res.data.has_bad_solution;
          this.open2();
        })
    },
    open2() {
      // this.$notify({
      //   title: '警告',
      //   message: '您有新的判了么订单待处理',
      //   duration: 0,
      //
      // });
      // el-icon-warning
      if (this.has_bad_solution === 1) {
        this.$alert('有未完成的题解审核，请前往处理', '警告', {
          confirmButtonText: '确定',
          type: 'warning'
          // dangerouslyUseHTMLString: true,
          // callback: action => {
          //   this.$message({
          //     type: 'info',
          //     message: `action: ${ action }`
          //   });
          // }
        });
      }
    },
    get_op_record(num) {
      this.$axios.get('/api/admin/op_record', {params: {pagenumber: num, pagesize: 4}})
        .then(res => {
          if (res.data.ret === 0) {
            this.tableData = res.data.records;
            this.total = res.data.total;
          }
        })
    },
    changePage(num) {
      this.get_op_record(num)
    },
    setit() {
      this.curheight = document.documentElement.clientHeight || document.body.clientHeight;
      console.log(this.curheight);
    },
    getTableData() {
      // this.$http.get('/home/getData').then(res => {
      //     res = res.data
      //     this.tableData = res.data.tableData
      // })
    },
    fuzhi() {
      this.optiontu.series[0].data = [{value: 1048, name: '单项选择'},
        {value: 735, name: '完形填空'},
        {value: 580, name: '阅读理解'},]
    }
  },
  //一进组件就会去请求后端接口 获取首页数据
  created() {
    this.get_op_record(1);
    this.setit();
    this.getit();
    this.fuzhi();
    // this.getTableData()
  }
}
</script>
<style>
.header1 {
  box-sizing: border-box;
  padding: 0 2% /* 给gutter留padding */
}

.user2 {
  display: flex;
  align-items: center;

  /*border-bottom: 1px solid #ccc;*/
}


.name {
  font-size: 32px;
  margin-bottom: 10px;
}


.el-row2 {
  margin-bottom: 20px;
  display: flex;
  flex-wrap: wrap
}

.access {
  color: #999999;
}

.col1 {
  /*margin-right: 3%;*/
}

.icon1 {
  background-color: #409EFF;
  height: 100%;
  display: inline-block
}

.icon2 {
  background-color: #67C23A;
  height: 100%;
  display: inline-block
}

.icon3 {
  background-color: #F56C6C;
  height: 100%;
  display: inline-block
}

.icon1_1 {
  padding: 20px;
  font-size: 50px;
}

.miaoshu1 {
  height: 85px;
  width: 60%;
  display: inline-block;
  text-align: center;
  vertical-align: center;
}

.biaoshi {
  font-size: 30px;
  color: #409EFF;
}

.biaoshi2 {
  font-size: 30px;
  color: #67C23A;
}

.biaoshi3 {
  font-size: 30px;
  color: #F56C6C;
}

.card1 {
  height: 300px;
}

.miaoshu {
  font-size: 16px;
  display: inline-block;
}

.login-info {
  height: 30%;
}

.box {
  height: 100px;
  width: 100%;
  display: inline-block
}

.userico .el-card__body {
  padding: 0px !important;
}

.card3 .el-card__body {
  padding: 5px !important;
}
</style>
