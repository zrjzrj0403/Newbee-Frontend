// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from "axios";
import qs from 'qs';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import './assets/css/common.css'
import 'default-passive-events'
import ECharts from 'vue-echarts';
import 'echarts';
// axios.defaults.withCredentials=true;

Vue.config.productionTip = false
axios.defaults.withCredentials = true;
Vue.prototype.$axios=axios
Vue.prototype.$qs=qs
Vue.use(ElementUI);
Vue.component('e-charts', ECharts)


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
