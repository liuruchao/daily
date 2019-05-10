<template>
  <div class="test">
      <div @click="send">测试axios</div>
      <div>{{data}}</div>
      <a href="http://www.xdocin.com/xdoc?_func=to&amp;_format=html&amp;_cache=1&amp;_xdoc=http://www.xdocin.com/demo/demo.docx" target="_blank" rel="nofollow">XDOC</a>
      <iframe src="/Users/liuruchao/daily/daily_control/upload/1555842548.pdf" frameborder="0"></iframe>
  </div>
</template>

<script>
export default {
  data () {
    return {
      radio: 1,
      value1:50,
      currentPage: 4,
      data:'显示数据'
    }
  },
  created(){
    //   console.log('fds');
    //  var exp = new Date();
    //  exp.setTime(exp.getTime() + 1000 * 60 * 60 * 24); //这里表示保存24小时
    //  document.cookie = "music_identify=" + 'id' + ";expires=" + exp.toGMTString();
    //  console.log(document.cookie)
  },
  methods: {
      send(){
          const that = this;
          const formFile = new FormData();
          formFile.append('name', 'config');
          this.axios({
              method:'POST',
              url:'http://127.0.0.1:5000/init',
              headers: {
                  'content-type': 'application/x-www-form-urlencoded'
                },
              data:formFile
          }).then(function(res){
              alert('成功');
              console.log(res);
              that.data = res;
          })
      }
    }
}
</script>

<style lang="scss" scoped>
   iframe{
     border:1px solid red;
     width:80vw;
     height:500px;
     margin:auto;
   }
</style>
