<template>
  <div>
     <div class="title1">
      <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home3' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: this.$route.path}">题目管理</el-breadcrumb-item>
      <el-breadcrumb-item :to="{path:paths}">{{item}}</el-breadcrumb-item>
        <el-breadcrumb-item>题目详情</el-breadcrumb-item>
</el-breadcrumb>
  </div>
    <div>
      <router-view/>
    </div>
      <div>
        <h1 style="text-align: center;">题目详情</h1>
      </div>
        <el-button type="primary"  @click="edit = !edit">编辑</el-button>
        <div>
            <div v-show="!edit" style="white-space: pre-wrap;" class="text textbox">
              <h1 style="text-align: center">{{ description_title}}</h1>
            </div>
           <el-input v-show="edit" v-model="description_title" type="textarea" autosize></el-input>
            <div v-show="!edit" style="white-space: pre-wrap;" class="text textbox">{{ description }}</div>
          <el-input v-show="edit" v-model="description" type="textarea" autosize></el-input>
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
   data(){
     return {
                 edit: false,
       description_title:"California Condor’s Shocking Recovery\n",
      description:  "\n" +
        "　　California condors are North America’s largest birds, with wind-length of up to 3 meters. In the 1980s, electrical lines and lead poisoning(铅中毒) nearly drove them to dying out. Now, electric shock training and medical treatment are helping to rescue these big birds.\n" +
        "\n" +
        "　　In the late 1980s, the last few condors were taken from the wild to be bred(繁殖).Since 1992,there have been multiple reintroductions to the wild, and there are now more than 150 flying over California and nearby Arizona, Utah and Baja in Mexico.\n" +
        "\n" +
        "　　Electrical lines have been killing them off. “As they go in to rest for the night, they just don’t see the power lines,” says Bruce Rideout of San Diego Zoo. Their wings can bridge the gap between lines, resulting in electrocution(电死) if they touch two lines at once.\n" +
        "\n" +
        "　　So scientists have come up with a shocking idea. Tall poles, placed in large training areas, teach the birds to stay clear of electrical lines by giving them a painful but undeadly electric shock. Before the training was introduced, 66% of set-free birds died of electrocution. This has now dropped to 18%.\n" +
        "\n" +
        "　　Lead poisoning has proved more difficult to deal with. When condors eat dead bodies of other animals containing lead, they absorb large quantities of lead. This affects their nervous systems and ability to produce baby birds, and can lead to kidney(肾) failures and death. So condors with high levels of lead are sent to Los Angeles Zoo, where they are treated with calcium EDTA, a chemical that removes lead from the blood over several days. This work is starting to pay off. The annual death rate for adult condors has dropped from 38% in 2000 to 5.4% in 2011.\n" +
        "\n" +
        "　　Rideout’s team thinks that the California condors’ average survival time in the wild is now just under eight years. “Although these measures are not effective forever, they are vital for now,” he says. “They are truly good birds that are worth every effort we put into recovering them. ”",
              item2:'11',
              paths:'',
              item:'',
              textarea: 666,
              times:1,
            }
   },
  created(){
      this.get();//需要触发的函数
    },
   methods:{
    get(){
        console.log(this.times);
      this.type=this.$route.query.type;
       if(this.type==='choice_question')
       {
        this.item='单项选择';
        this.paths='/question/multiplechoice';
       }
       else if(this.type==='cloze_question')
       {
        this.item='完型填空';
        this.paths='/question/cloze';
       }
       else
       {
         this.item='阅读理解';
         this.paths='/question/readingcomprehension';
       }
  }
   }
}
</script>

<style scoped>
  .text{
    font-size: 14px;
  }
  .textbox{
    margin:0 50px;
  }
</style>
