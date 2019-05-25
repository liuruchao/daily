import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import WriteArticle from '@/components/WriteArticle'
import ShowArticle from '@/pages/ShowArticle'
import TopArticle from '@/pages/TopArticle'
import NoAudit from '@/pages/NoAudit'
import HasAudit from '@/pages/HasAudit'
import Login from '@/pages/login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'WriteArticle',
      component: WriteArticle
    },
    {
      path:'/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/article-list',
      name: 'ShowArticle',
      component: ShowArticle
    },
    {
      path: '/top-article',
      name: 'TopArticle',
      component: TopArticle
    },{
      path: '/noaudit',
      name: 'NoAudit',
      component: NoAudit
    },{
      path: '/hasaudit',
      name: 'HasAudit',
      component: HasAudit
    }
  ]
})
