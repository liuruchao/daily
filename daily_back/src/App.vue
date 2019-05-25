<template>
  <div id="app">
    <nav>
    <el-menu default-active="/" class="el-menu-vertical-demo"
      background-color="#063e5e" text-color="#fff" active-text-color="#ffd04b" router=true>
      <el-menu-item index="/">
        <i class="el-icon-menu"></i>
        <span slot="title">发布文章</span>
      </el-menu-item>
      <el-menu-item index="/article-list">
        <i class="el-icon-document"></i>
        <span slot="title">查看文章</span>
      </el-menu-item>
      <el-menu-item index="/noaudit">
        <i class="el-icon-menu"></i>
        <span slot="title">待审稿</span>
      </el-menu-item>
      <el-menu-item index="/hasaudit">
        <i class="el-icon-menu"></i>
        <span slot="title">已审稿</span>
      </el-menu-item>
      <el-menu-item index="/top-article">
        <i class="el-icon-setting"></i>
        <span slot="title">热度排行榜</span>
      </el-menu-item>
    </el-menu>

    <el-button type="primary" class="exit" @click="exit">登出</el-button>
    </nav>
    <router-view class="router-view"/>
  </div>
</template>

<script>
  export default {
    name: 'App',
    data(){
      return {
          
      }
      
    },
    methods:{
      exit(){
         this.$router.replace({
                        path: '/login',
                    })
      }
    }
  }

</script>
<style>
  body,html{
    padding:0;
    margin:0;
  }
  #app{
     display: flex;
  }
  nav{
    width:15vw;
    min-width:200px;
    height:100vh;
    float:left;
    background:#063e5e;
  }
  .admin{
    width:200px;
    height:40px;
    background:gray;
    float: right;
  }
  .router-view{
    flex-grow: 1;
     float:right;
     width:80vw;
  }
  .exit{
    margin-left:2em;
    margin-top:5em;
  }
</style>
