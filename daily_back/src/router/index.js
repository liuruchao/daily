import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import WriteArticle from '@/components/WriteArticle'
import BackReport from '@/pages/BackReport'
import ShowArticle from '@/pages/ShowArticle'
import TopArticle from '@/pages/TopArticle'
import NoAudit from '@/pages/NoAudit'
import HasAudit from '@/pages/HasAudit'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'WriteArticle',
      component: WriteArticle
    },
    // {
    //   path: '/report',
    //   name :'BackReport',
    //   component: BackReport
    // },
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
