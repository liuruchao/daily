import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/pages/index'
import Test from '@/components/test'
import ArticleChang from '@/pages/ArticleChang'
import ArticleAll from '@/pages/ArticleAll'
import GiveNotice from '@/pages/GiveNotice'
import ArticlePost from '@/pages/ArticlePost'
import JournalArticle from '@/pages/JournalArticle'
import Intro from '@/components/journal/intro'
import Board from '@/components/journal/board'
import Period from '@/components/journal/period'
import OnlineDelivery from '@/components/journal/OnlineDelivery'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/test',
      name: 'Test',
      component: Test
    },
    {
      path: '/article_changzhi',
      name: 'ArticleChang',
      component: ArticleChang
    },
    {
      path: '/article_all',
      name: 'ArticleAll',
      component: ArticleAll
    },
    {
      path: '/give_notice',
      name: 'GiveNotice',
      component: GiveNotice
    },
    {
      path: '/show/:post_id',
      name: 'ArticlePost',
      component: ArticlePost,
    },
    {
      path: '/journal',
      name: 'JournalArticle',
      component: JournalArticle,
      children:[
        {
          path:'board',
          name: 'Board',
          component: Board
        },
        {
          path: 'intro',
          name: 'Intro',
          component: Intro
        },
        {
          path: 'delivery',
          name: 'OnlineDelivery',
          component: OnlineDelivery
        },{
          path: 'period',
          name: 'Period',
          component: Period
        }
      ]
    }
    
  ]
})
