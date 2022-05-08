<template>
  <div>
    <div style="height:100px;">
      <div class="box">
        <e-charts
          class="chart" :option="optionbiaoti"/>
      </div>
      <img class='img' src="../../assets/logo1.jpg" >
      <!--      style="display:inline-block"-->
    </div>
        <e-charts
          class="chart" :option="optionxuanze"/>
        <e-charts
          class="chart" :option="optionwanxing"/>
        <e-charts
          class="chart" :option="optionyuedu"/>

  </div>
</template>

<script>
export default {
  name: "index",
  data() {
    return {
      // 'Welcome To Wew Bee English'
      // data: this.getRandomData(),
      optionbiaoti: {
        graphic: {
          elements: [
            {
              type: 'text',
              left: '1%',
              top: '3%',
              style: {
                text: 'Welcome To New Bee English',
                fontSize: 80,
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
                      fill:"black"
                    }
                  }
                ]
              }
            }
          ]
        }
      },
      optionxuanze: {
        title: {
          text: '特此表彰，选择题做对数量前七名',
          subtext: '请在每周日发送表彰公告'
        },
        tooltip: {
          trigger: 'axis',
          // formatter: '{a} <br/>{b}: {c} ({d}%)'
          formatter: function (params) {
            return (
              (params[0].name ? params[0].name : "") + ':' + (params[0].data.code ? params[0].data.code : "") +
              '<br/>' +
              '答对数量: ' +
              (params[0].value ? params[0].value : "")
            );
          },
          axisPointer: {
            type: 'shadow'
          }
        },
        xAxis: {
          type: 'category',
          data: ['First', 'Second', 'Third', 'Fourth', 'Fiftn', 'Sixth', 'Seventh', 'eighth', 'ninth', 'tenth']
        },
        yAxis: {
          type: 'value',
        },
        series: [
          {
            data: [
              {
                value: 300,
                code: '小赵',
                itemStyle: {
                  color: '#a90000'
                },
              },
              {
                value: 200,
                code: '还是小赵',
                itemStyle: {
                  color: '#a90000'
                },
              },
              {
                value: 150,
                code: '又是小赵',
                itemStyle: {
                  color: '#a90000'
                },
              },
              {
                value: 110,
                code: '小李',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 100,
                code: '又是小李',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 80,
                code: '还是小李',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 70,
                code: '小豪',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 60,
                code: '小徐',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 50,
                code: '小ld',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 40,
                code: '小姜',
                itemStyle: {
                  color: 'skyblue'
                },
              },
            ],
            type: 'bar',
            label: {
              show: true,
              position: 'top'
            },
          },
        ],
      },
      optionwanxing: {
        title: {
          text: '特此表彰，完型做对数量前七名',
        },
        tooltip: {
          trigger: 'axis',
          // formatter: '{a} <br/>{b}: {c} ({d}%)'
          formatter: function (params) {
            return (
              (params[0].name ? params[0].name : "") + ':' + (params[0].data.code ? params[0].data.code : "") +
              '<br/>' +
              '答对数量: ' +
              (params[0].value ? params[0].value : "")
            );
          },
          axisPointer: {
            type: 'shadow'
          }
        },
        xAxis: {
          type: 'category',
          data: ['First', 'Second', 'Third', 'Fourth', 'Fiftn', 'Sixth', 'Seventh', 'eighth', 'ninth', 'tenth']
        },
        yAxis: {
          type: 'value',
        },
        series: [
          {
            data: [
              {
                value: 300,
                code: '小赵',
                itemStyle: {
                  color: '#a90000'
                },
              },
              {
                value: 200,
                code: '还是小赵',
                itemStyle: {
                  color: '#a90000'
                },
              },
              {
                value: 150,
                code: '又是小赵',
                itemStyle: {
                  color: '#a90000'
                },
              },
              {
                value: 110,
                code: '小李',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 100,
                code: '又是小李',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 80,
                code: '还是小李',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 70,
                code: '小豪',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 60,
                code: '小徐',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 50,
                code: '小ld',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 40,
                code: '小姜',
                itemStyle: {
                  color: 'skyblue'
                },
              },
            ],
            type: 'bar',
            label: {
              show: true,
              position: 'top'
            },
          },
        ],
      },
      optionyuedu: {
        title: {
          text: '特此表彰，阅读数量前七名',
        },
        tooltip: {
          trigger: 'axis',
          // formatter: '{a} <br/>{b}: {c} ({d}%)'
          formatter: function (params) {
            return (
              (params[0].name ? params[0].name : "") + ':' + (params[0].data.code ? params[0].data.code : "") +
              '<br/>' +
              '答对数量: ' +
              (params[0].value ? params[0].value : "")
            );
          },
          axisPointer: {
            type: 'shadow'
          }
        },
        xAxis: {
          type: 'category',
          data: ['First', 'Second', 'Third', 'Fourth', 'Fiftn', 'Sixth', 'Seventh', 'eighth', 'ninth', 'tenth']
        },
        yAxis: {
          type: 'value',
        },
        series: [
          {
            data: [
              {
                value: 300,
                code: '小赵',
                itemStyle: {
                  color: '#a90000'
                },
              },
              {
                value: 200,
                code: '还是小赵',
                itemStyle: {
                  color: '#a90000'
                },
              },
              {
                value: 150,
                code: '又是小赵',
                itemStyle: {
                  color: '#a90000'
                },
              },
              {
                value: 110,
                code: '小李',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 100,
                code: '又是小李',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 80,
                code: '还是小李',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 70,
                code: '小豪',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 60,
                code: '小徐',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 50,
                code: '小ld',
                itemStyle: {
                  color: 'skyblue'
                },
              },
              {
                value: 40,
                code: '小姜',
                itemStyle: {
                  color: 'skyblue'
                },
              },
            ],
            type: 'bar',
            label: {
              show: true,
              position: 'top'
            },
          },
        ],
      },
    };
    // return {
    //   data: this.getRandomData(),
    // };
  },
  computed: {
    // option1() {
    //   return {
    //     xAxis: {
    //       type: 'category',
    //       data: this.data.map(d => d.time),
    //     },
    //     yAxis: {
    //       type: 'value'
    //     },
    //     series: [
    //       {
    //         data: this.data.map(d => d.value),
    //         type: 'line'
    //       }
    //     ],
    //   };
    // },
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
    }
    // getRandomData() {
    //   return [
    //     {
    //       time: '2021-01-01',
    //       value: Math.random() * 100,
    //     },
    //     {
    //       time: '2021-01-01',
    //       value: Math.random() * 100,
    //     },
    //     {
    //       time: '2021-01-01',
    //       value: Math.random() * 100,
    //     },
    //     {
    //       time: '2021-01-01',
    //       value: Math.random() * 100,
    //     },
    //     {
    //       time: '2021-01-01',
    //       value: Math.random() * 100,
    //     },
    //   ];
    // },
  },
  created() {
     this.getit();
    // setInterval(() => {
    //   this.data = this.getRandomData();
    // }, 1000);
  },
};
</script>

<style scoped>
.chart {
  height: 350px;
}
.box {
  position: absolute;
  right: 8%;
  height: 100px;
  width: 80%;
  display: inline-block
}
.img{
   position: absolute;
  right: 0px;
  height:15%;
  width: auto;
  /*background-color: #fffff;*/
}
</style>
