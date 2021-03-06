import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from "../components/Home";
import S1 from "../components/S1";
import Login from "../components/Login";
import Login2 from "../components/Login2";
import MainPage from "../components/MainPage";
import Index from "../layout/Menu/index";
import Home2 from "../components/Home2";
import Home3 from "../layout/Home/index";
const routerPush = Router.prototype.push
Router.prototype.push = function push(location) {
  return routerPush.call(this, location).catch(error=> error)
}
const Announcement = () => import('../layout/Announcement/Announcement')
const Question = () => import('../layout/Questions/Questions')
const User = () => import('../layout/User/User')
const Details = () => import('../layout/Questions/Details/details')
const ReadingComprehension = () => import('../layout/Questions/ReadingComprehension/ReadingComprehension')
const MultipleChoice = () => import('../layout/Questions/MultipleChoice/MultipleChoice')
const Cloze = () => import('../layout/Questions/Cloze/cloze')
const Upload = () => import('../layout/Upload/Upload')

Vue.use(Router)
const originalPush = Router.prototype.push
Router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}
export default new Router({
  routes: [
    {
      path: '/', redirect: '/login'
    },
    {
      path: '/home', component: Home
    },
    {
      path: '/s1', component: S1
    },
    {
      path: '/login', component: Login2
    },
    {
      path: '/mainpage', component: MainPage
    },
    {
      path: '/index', component: Index,
      children: [
        {
          path: '/home3', component: Home3, name: 'home3'
        },
        {
          path: '/announcement', component: Announcement
        },
        {
          path: '/upload', component: Upload
        },
        {
          path: '/question', component: Question,
          children: [
            {
              path: 'readingcomprehension', component: ReadingComprehension
            },
            {
              path: 'multiplechoice', component: MultipleChoice
            },
            {
              path: 'cloze', component: Cloze
            }
          ]
        },
        {
          path: '/user', component: User
        },
        {
          path: '/details', component: Details, name: 'details'
        }
      ]
    },
    {
      path: '/home', component: Home2
    }
  ]
})
