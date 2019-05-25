<!--  -->
<template>
  <div class='delivery'>
    <el-breadcrumb separator-class="el-icon-arrow-right" class="nav">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>在线投稿</el-breadcrumb-item>
    </el-breadcrumb>
    <h2>在线投稿</h2>
    <div class="delivery__content" v-loading="loading">
      <div class="row">
        <span>姓名：</span>
        <el-input class="elInput" clearable='true' type="text" v-model="name"></el-input>
      </div>
      <div class="row">
        <span>手机号：</span>
        <el-input class="elInput" clearable='true' type="number" v-model="tel"></el-input>
      </div>
      <div class="row">
        <span>邮箱：</span>
        <el-input class="elInput" clearable='true' type="email" v-model="email"></el-input>
      </div>
      <div class="row">
        <span>联系地址：</span>
        <el-input class="elInput" clearable='true' type="text" v-model="adr"></el-input>
      </div>
      <div class="row">
        <span>备注：</span>
        <el-input class="elInput" type="textarea" clearable='true' rows=2 v-model="other"></el-input>
      </div>
      <div class="row">
        <span>投稿文件：</span>
        <input type="file" id='file' @change="upload"
          accept=".pdf">
      </div>
      <el-button type="primary" style="width:100px;" @click="submit">提交</el-button>
    </div>
  </div>
</template>

<script>
  // import 

  export default {
    components: {},
    data() {
      return {
        name: '',
        tel: '',
        adr: '',
        email: '',
        other: '',
        loading:false
      };
    },
    //监听属性 类似于data概念
    computed: {},
    //监控data中的数据变化
    watch: {},
    //方法集合
    methods: {
      submit() {
        const that = this;
        if (!that.name || !that.tel || !that.adr || !that.email || !that.other || !that.file) {
          this.$message({
            message: '请填写完全',
            type: 'error'
          });
          return false;
        }
        that.loading = true;
        const form = new FormData();
        form.append('name',that.name);
        form.append('tel',that.tel);
        form.append('adr',that.adr);
        form.append('email',that.email);
        form.append('other',that.other);
        form.append('file',that.file)
        this.axios({
          method: 'POST',
          url: 'http://127.0.0.1:5000/delivery',
          headers: {
                'content-type': 'application/x-www-form-urlencoded'
            },
          data: form
        }).then(function (res) {
           if(res.data == 'success'){
               that.$message({
                message: '投稿成功',
                type: 'success'
            });
              that.name = '';
              that.tel = '';
              that.email = '';
              that.adr = '';
              that.other = '';
              that.file = '';
            //   document.querySelector('#file').files[0] = '';
           }
        }).finally(function () {
          that.loading = false;
        })
      },
      upload() {
        const that = this;
        let file = document.querySelector('#file').files[0];
        that.file = file;
      }
    },
    //生命周期 - 创建完成（可以访问当前this实例）
    created() {

    },
  }

</script>
<style lang='scss' scoped>
  .delivery {
    .nav {
      line-height: 3em;
      border-bottom: 1px solid gray;
      margin: 0 2em;
    }

    .delivery__content {
      font-size: 16px;
      color: gray;
      padding: 0 1em;
      line-height: 2em;
      width: 55%;
      margin: auto;
      text-align: center;

      .row {
        height: 70px;
        text-align: left;
      }

      .elInput {
        // display: inline-block;
        width: 80%;
        float: right;

        &:after {
          content: '';
          display: block;
          clear: both;
        }

      }

    }

    h2 {
      text-align: center;
    }  
  }

  @media screen and (max-width:760px){
    .delivery{
      
      .delivery__content{
        width:80%;
        box-sizing: border-box;
        .elInput{
          width:66%;
        }
      }
    }
  }

</style>
