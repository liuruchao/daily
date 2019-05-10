<template>
  <div class="article-cont">
     <h3 class="title">{{data.title}}</h3>
     <h4 class="subhead">{{new Date(data.time+'+0800').toLocaleDateString() + '  ' + data.classes}}</h4>
     <div icon='el-icon-star-on' class="btn" @click="giveLikes" :style="likesSty">点赞数{{likes}}</div>
     <div icon='el-icon-goods' class="btn" @click="collect" :style="collectSty">收藏</div>
     <img :src="data.imgUrl" alt=""  class="img-dec">
     <div id="content">
     </div>
     <div class="pinglun">
         
     </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      id:'',
      likesNum:false,
      collectNum:false,
      likesSty:'',
      collectSty:'',
      data:{},
      likes:0,
    }
  },
  beforeRouteUpdate (to, from, next) {
    // next();
    // console.log(this.$route.params)
    // this.id = this.$route.params['post_id'];
    // this.send();
  },
  created(){
    this.id = this.$route.params['post_id'];
    this.send('http://127.0.0.1:5000/page/init','init');
  },
  methods: {
      send(url,type){
          const that = this;
          if(!that.id){
            return false;
          }
          const formFile = new FormData();
          formFile.append('id', that.id);
          formFile.append('uid',sessionStorage.uid);
          this.axios({
              method:'POST',
              url:url,
              headers: {
                  'content-type': 'application/x-www-form-urlencoded'
                },
              data:formFile
          }).then(function(res){
              console.log(res.data);
              if(type == 'init'){
                  that.data = res.data[0];
                  that.likes = res.data[0]['likes'];
                  document.querySelector('#content').innerHTML = res.data[0]['content'];
              }else if(type == 'likes'){
                  if(res.data == 'success'){
                      that.$message({
                        message: '谢谢您的喜欢',
                        type: 'success',
                        center: true
                      });
                      that.likesSty = 'background:#F56C6C;color:white';
                      that.likes++;
                  }else{
                     that.$message({
                        message: '您已点赞',
                        type: 'error',
                        center: true
                      });
                  }
              }else if(type == 'collect'){
                  if(res.data == 'success'){
                      that.$message({
                        message: '谢谢您的收藏',
                        type: 'success',
                        center: true
                      });
                      that.collectSty = 'background:#F56C6C;color:white';
                  }else{
                     that.$message({
                        message: '您已收藏',
                        type: 'error',
                        center: true
                      });
                  }
              }

          })
      },
      // 点赞
      giveLikes(){
        const uid = sessionStorage.uid;
        const that = this;
        if(!uid){
           that.$message({
              message: '请先登陆',
              type: 'warning',
              center: true
            });
            return false;
        }
        this.send('http://127.0.0.1:5000/page/likes','likes');

      },
      collect(){
        const uid = sessionStorage.uid;
        const that = this;
        if(!uid){
           that.$message({
              message: '请先登陆',
              type: 'warning',
              center: true
            });
            return false;
        }
        this.send('http://127.0.0.1:5000/page/collect','collect');       
      }
    }
}
</script>

<style lang="scss" scoped>
    .article-cont{
      min-height: calc(100vh - 60px - 100px);
      text-align: center;
      .title{
         font-size:28px;
         font-weight: blod;
      }
      .subhead{
        font-size:14px;
        color:#888;
      }
      #content{
        width:80vw;
        margin:auto;
        text-align: left;
      }
      .btn{
        padding:9px 35px;
        display:inline-block;
        border:1px solid #ff5a00;
        border-radius:5px;
        color:gray;
        cursor: pointer;
        &:hover{
          background:#ff5a00;
          color:white;
        }
      }
      .img-dec{
        width:70vw;
        display: block;
        position: relative;
        left:50%;
        transform: translateX(-50%);
        margin:40px 0;
      }
      .pinglun{
        margin:50px auto;
        padding-top:50px;
        text-align: center;
        border-top:1px solid gray;
        width:70vw;
      }
    }
</style>
