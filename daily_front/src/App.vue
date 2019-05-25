<template>
  <div id="app">
    <nav class="nav-pc">
      <!-- 导航菜单 -->
      <el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" router=true>
        <img src="./assets/logo.jpg" alt="" class="el-menu__logo">
        <el-menu-item index="/">首页</el-menu-item>
        <el-menu-item index="/journal/intro">期刊简介</el-menu-item>
        <el-menu-item index="/journal/period">期刊导读</el-menu-item>
        <el-menu-item index="/journal/board">委员会</el-menu-item>
        <el-menu-item index="/journal/delivery">在线投稿</el-menu-item>
        <el-menu-item index="/article_changzhi">长院要闻</el-menu-item>
        <el-menu-item index="/article_all">综合新闻</el-menu-item>
        <el-menu-item index="/give_notice">公告通知</el-menu-item>
        <div class="nav-pc__user">
          <img src="./assets/user.png" alt="" class="nav-pc__user__head" @click="isLanding" v-if="meidenglu">
          <img src="./assets/user_l.png" alt="" v-else class="nav-pc__user__head" @click="isLanding">
          <div class="nav-pc__user__login--unhaslogin" v-show="haslogin">
            <!-- <div>{{sno}}<i class="el-icon-success" style="color:#409EFF;margin-left:1em"></i></div> -->
            <div @click="showUserCenter">个人中心</div>
            <div @click="logout">登出</div>
          </div>
          <el-dialog title="您未登陆" type="border-card" :visible.sync="dialogVisible" width="300px"
           class="nav-pc__user__login--haslogin">
            <el-tabs v-model="defaultTab">
              <el-tab-pane label="登陆" name="first">
                <el-input class="el-input" placeholder="学号" v-model="landing_username" clearable prefix-icon="el-icon-edit" maxlength=8 ></el-input>
                <el-input class="el-input" placeholder="请输入密码" v-model="landing_pass" show-password prefix-icon="el-icon-edit-outline"></el-input>
                <el-button type="primary" plain class="login-btn" @click="landing" v-loading="landLoad">登陆</el-button>
              </el-tab-pane>
              <el-tab-pane label="注册" name="second">
                 <el-input class="el-input" placeholder="学号" v-model="login_username" clearable prefix-icon="el-icon-edit" maxlength=8 ></el-input>
                <el-input class="el-input" placeholder="请输入密码" v-model="login_pass1" show-password prefix-icon="el-icon-edit-outline"></el-input>
                <el-input class="el-input" placeholder="请确认密码" v-model="login_pass2" show-password prefix-icon="el-icon-edit-outline"></el-input>
                <el-button type="primary" plain class="login-btn" @click="login" v-loading="logLoad">注册</el-button>
              </el-tab-pane>
            </el-tabs>
          </el-dialog>
        </div>
      </el-menu>
      <aside class="userCenter" :class='isShow' @click='closeCenter'>
           <h3>收藏文章</h3>
           <p v-for="(item, index) in collect" :key="index" @click.stop='showContent(item.postId)'>{{index+1}}.{{item.title}}</p>
      </aside>
    </nav>
    <!-- <nav class="nav-mobile">
      <img src="" alt="" class="nav-mobile__logo">
    </nav> -->
    <router-view />
    <footer>
       Copyright © 2019 长治学院. All rights reserved.<br>
       晋ICP备18000458号
    </footer>
  </div>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {
        defaultTab: 'first',
        haslogin: false,
        dialogVisible: false,
        login_username:'',
        login_pass1:'',
        login_pass2:'',
        landing_username:'',
        landing_pass:'',
        logLoad: false,
        landLoad: false,
        sno:'',
        meidenglu:true,
        isShow:'',
        status:'',
        collect:[]
      }
    },
    methods:{
      // 注册
      login(){
         const that = this;
         if(!that.login_username){
             this.$message({
              message: '请输入学号',
              type: 'warning',
              center: true
            });
            return false;
         }
         if(isNaN(that.login_username)){
             this.$message({
              message: '请输入正确学号',
              type: 'warning',
              center: true
            });
            return false;
         }
         if(!that.login_pass1){
             this.$message({
              message: '请输入密码',
              type: 'warning',
              center: true
            });
            return false;
         }
         if(that.login_pass1 != that.login_pass2){
             this.$message({
              message: '输入的两次密码不正确',
              type: 'warning',
              center: true
            });
            return false;
         }
         that.logLoad = true
         this.send('http://127.0.0.1:5000/login',that.login_username,that.login_pass1)
      },
      landing(){
         const that = this;
         if(!that.landing_username){
             this.$message({
              message: '请输入学号',
              type: 'warning',
              center: true
            });
            return false;
         }
         if(isNaN(that.landing_username)){
             this.$message({
              message: '请输入正确学号',
              type: 'warning',
              center: true
            });
            return false;
         }
         if(!that.landing_pass){
             this.$message({
              message: '请输入密码',
              type: 'warning',
              center: true
            });
            return false;
         }
         that.landLoad = true;
         this.send('http://127.0.0.1:5000/landing',that.landing_username,that.landing_pass)         
      },
      send(url,sno,pwd){
          const that = this;
          const formFile = new FormData();
          formFile.append('sno', sno);
          formFile.append('pwd', pwd);
          this.axios({
              method:'POST',
              url:url,
              headers: {
                  'content-type': 'application/x-www-form-urlencoded'
                },
              data:formFile
          }).then(function(res){
              console.log(res.data)
              if(res.data == 'loginSuccess'){
                  that.$message({
                    message: '注册成功，请登陆',
                    type: 'success',
                    center: true
                  });
                  that.login_username = '';
                  that.login_pass1 = '';
                  that.login_pass2 = '';           
              }else if(res.data == 'hasLogin'){
                  that.$message({
                    message: '该学号已注册',
                    type: 'warning',
                    center: true
                  });
              }else if(res.data == 'noLogin'){
                  that.$message({
                    message: '该学号不存在',
                    type: 'warning',
                    center: true
                  });
              }else if(res.data == 'landingFails'){
                  that.$message({
                    message: '密码不正确',
                    type: 'error',
                    center: true
                  });
              }else if(res.data[0] == 'landingSuccess'){
                  that.$message({
                    message: '登陆成功',
                    type: 'success',
                    center: true
                  });
                  that.uid = res.data[1];
                  sessionStorage.uid = res.data[1];
                  that.dialogVisible = false;
                  that.sno = sno;
                  that.meidenglu = false;
              }
          }).finally(function(){
             that.logLoad = false;
             that.landLoad = false;
          })
      },
      isLanding(){
        let uid = sessionStorage.uid;
        const that = this;
        if(!uid){      //未登陆
            that.dialogVisible=true;
        }else{
            that.haslogin=!that.haslogin;
        }
      },
      // 登出
      logout(){
          sessionStorage.uid = '';
          this.haslogin = false;
          this.$message({
              message: '登出成功',
              type: 'success',
              center: true
            });
          this.meidenglu = true;
      },
      showUserCenter(){
         const that = this;
         this.isShow = this.status.next().value;
         const formFile = new FormData();
         formFile.append('uid',sessionStorage.uid);
         this.axios({
              method:'POST',
              url:'http://127.0.0.1:5000/userCenter',
              headers: {
                  'content-type': 'application/x-www-form-urlencoded'
                },
              data:formFile
          }).then(function(res){
             console.log(res.data)
             that.collect = res.data;
          })
      },
      // 是否显示个人中心状态机
      * isShowCent (){
          while(1){
             yield 'show';
             yield 'noshow';
          }
      },
      closeCenter(){
         this.isShow = this.status.next().value;
      },
      showContent(post_id){
          let id = post_id;
          // this.$route.params.post_id = id;
          // console.log(this.$router.params.post_id);
          // this.$router.push({
          //     // path: `/show/${id}`
          //     name: 'ArticlePost',
          //     params:{
          //        id
          //     }
          // })
      }
    },
    created(){
        let uid = sessionStorage.uid;
        const that = this;
        if(uid){      //已登陆
            that.meidenglu=false;
        }
        this.status = this.isShowCent();
    }
  }

</script>

<style lang="scss" scoped>
  
  .nav-pc {
    .el-menu-demo {
      padding: 0 80px;
    }

    .el-menu-item {
      padding: 0 20px;
    }

    .el-menu__logo {
      float: left;
      height: 60px;
      margin-right: 60px;
    }

    .nav-pc__user {
      height: 50px;
      width: 50px;
      float: right;
      position: relative;
      outline:none;

      .nav-pc__user__head {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        outline: none;
        margin-top:5px;
      }

      // 已登陆
      .nav-pc__user__login--unhaslogin {
        position: absolute;
        top: 60px;
        left: -60px;
        width: 180px;
        box-shadow: 1px 1px 10px #caced2;
        border-radius: 8px;
        color: gray;
        font-size: 14px;
        background: white;

        &>div {
          text-align: center;
          line-height: 50px;
          height: 50px;
          border-bottom: 1px solid#f1ebeb;
          background: white;
          z-index: 10;
          cursor: pointer;
        }

        &>div:hover {
          color: #409EFF;
        }

        &>div:last-of-type {
          border: none;
        }
      }

      // 未登陆
      .nav-pc__user__login--haslogin {
        border: 1px solid;

        .el-tabs__nav {
          width: 100%;
        }

        .el-tabs__item {
          width: 50%;
          text-align: center;
          padding: 0;
        }
        .login-btn{
          width:100% !important;
          border-radius:8px;
        }
        .el-input {
          margin-bottom:20px;
        }
      }

    }
  }
  .userCenter{
    width:300px;
    height:100vh;
    background: rgb(223, 222, 222);
    position: fixed;
    transform:translateX(100%);
    transition:all 0.3s linear;
    top:0;
    right:0;
    z-index: 999;
    padding:0 1.5em 1.5em;
    h3{
      text-align: center;
      border-bottom:1px solid gray;
      padding-bottom:1em;
    }
    p{
      text-overflow:ellipsis;
      overflow: hidden;
      white-space: nowrap;
      &:hover{
        color:orange;
      }
      cursor:pointer;
    }
  }
  // 展开个人中心
  .show{
    transform:translateX(0);
    transition:all 0.3s linear;
  }
  .noshow{
    transform:translateX(100%);
    transition:all 0.3s linear;
  }
  footer{
     height:100px;
     background:black;
     color:white;
     text-align: center;
     font-size:14px;
     box-sizing: border-box;
     padding-top:1.5em;
     
  }
</style>
