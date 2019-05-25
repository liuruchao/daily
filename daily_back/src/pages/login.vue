<!-- 登录 -->
<template>
  <div class='login'>
     <div class="login__input">
         <h2>管理员登录</h2>
         <el-input v-model="zhanghao" placeholder="请输入账号" prefix-icon='el-icon-s-custom'></el-input>
         <el-input v-model="pwd" placeholder="请输入密码" show-password=true prefix-icon='el-icon-s-cooperation'></el-input>
         <el-button type="primary" @click="submit">登录</el-button>
     </div>
  </div>
</template>

<script>
  // import 

  export default {
    components: {},
    data() {
      return {
         zhanghao:'',
         pwd:''
      };
    },
    //监听属性 类似于data概念
    computed: {},
    //监控data中的数据变化
    watch: {},
    //方法集合
    methods: {
       submit(){
            const that = this;
            that.axios({
            method: 'POST',
            url: 'http://127.0.0.1:5000/cms',
            data: {
                zhanghao: that.zhanghao,
                pwd: that.pwd 
            }
            }).then(function (res) {
                console.log(res.data)
                if(res.data == 'success'){
                    sessionStorage.login = true;
                    that.$notify({
                        title: '成功',
                        message: '登录成功',
                        type: 'success',
                        showClose: false
                    });
                    that.$router.replace({
                        path: '/',
                    })
                }
                else{
                    sessionStorage.clear();
                    that.$notify({
                        title: '失败',
                        message: '密码或账号不正确',
                        type: 'error',
                        showClose: false
                    });
                }
            }).catch(function(){
                sessionStorage.clear();
                that.$notify({
                        title: '失败',
                        message: '密码或账号不正确',
                        type: 'error',
                        showClose: false
                    });
            })
       }
    },
    //生命周期 - 创建完成（可以访问当前this实例）
    created() {

    },
  }

</script>
<style  scoped>
  .login{
      width:100vw;
      height:100vh;
      /* border:900px solid #063e5e; */
      /* z-index:999;
      margin-left:-400px; */
      background:#063e5e;
      /* background:red; */
      outline:1000px solid #063e5e;
      position: relative;
  }
  .login__input{
      width:300px;
      position: absolute;
      left:50%;
      top:50%;
      transform: translate(-50%,-50%);
      text-align: center;
      padding:2em;
      background: #e4e0e0;
      border-radius: 5px;
  }
  .login__input>h2{
      color:gray;
      text-align: center;
  }
  .el-input{
      margin:20px 0;
  }
</style>
