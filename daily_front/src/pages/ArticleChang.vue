<template>
  <div class="article-list">
    <h2>长院要闻</h2>
    <h3>—— 已发布文章{{count}}篇 ——</h3>
    <img src="" alt="">
    <section class="article-list--show" v-loading="loading">
      <article-show v-for="(item, index) in articles" :key="index" class="show-item" :datas="item"></article-show>
    </section>
    <section class="noData" v-show="noData">
         oo! 还没有任何文章发布！
    </section>
    <el-pagination
    background
    layout="prev, pager, next,jumper"
    :total="pages" class="article-list__page" @current-change="select">
  </el-pagination>
  </div>
</template>

<script>
  import ArticleShow from '@/components/ArticleShow'
  export default {
    data() {
      return {
         count:0,
         pages:0,
         articles:[],
         loading:false,
         noData:false
      }
    },
    created() {
       this.init();
    },
    components: {
      ArticleShow
    },
    methods:{
      init() {
          const that = this;
          const formFile = new FormData();
          formFile.append('classes', '长院要闻');
          that.loading = true;
          this.axios({
              method:'POST',
              url:'http://127.0.0.1:5000/article',
              headers: {
                  'content-type': 'application/x-www-form-urlencoded'
                },
              data:formFile
          }).then(function(res){
              that.$notify({
                title: '成功',
                message: '数据加载成功',
                type: 'success',
                showClose: false
              });
              that.count=res.data[0]['count(1)'];
              that.pages = Math.ceil(that.count / 6)*10;
              that.articles = res.data[1];
              if(that.articles.length == 0){
                that.noData = true;
              }
          }).catch(function(){
            //  alert('失败')
              that.$notify({
                title: '失败',
                message: '数据加载失败',
                type: 'error',
                showClose: false
              });
              that.noData = true;
          }).finally(function(){
             that.loading = false;
          })
      },
      select(val) {
          const that = this;
          const formFile = new FormData();
          formFile.append('classes', '长院要闻');
          formFile.append('pages',val)
          that.loading = true;
          this.axios({
              method:'POST',
              url:'http://127.0.0.1:5000/select',
              headers: {
                  'content-type': 'application/x-www-form-urlencoded'
                },
              data:formFile
          }).then(function(res){
              that.$notify({
                title: '成功',
                message: '数据加载成功',
                type: 'success',
                showClose: false
              });
              that.articles = res.data;
          }).catch(function(){
            //  alert('失败')
            that.$notify({
                title: '失败',
                message: '数据加载失败',
                type: 'error',
                showClose: false
              });
          }).finally(function(){
             that.loading = false;
          })
      }
    }
  }

</script>

<style lang="scss" scoped>
  .article-list {
    min-height: calc(100vh - 60px - 100px);
    box-sizing: border-box;
    &>h2 {
      font-size: 28px;
      font-weight: bold;
      color: #ff5a00;
      text-align: center;
      margin-top: 45px;
    }

    &>h3 {
      font-size: 14px;
      color: #888;
      text-align: center;
      font-weight: 400;
    }

    .article-list--show {
      width: 80vw;
      margin: auto;
      display: flex;
      flex-wrap: wrap;
      box-sizing: border-box;
      justify-content: space-between;

      .show-item {
        width: 45%;
      }
    }
    .article-list__page{
      text-align: center;
      margin:45px 0;
      font-size:20px;
    }
    .noData{
         text-align: center;
         height: 300px;
         font-size: 20px;
    }
  }

  @media screen and(max-width: 700px) {
    .show-item {
      width: 100% !important;
      margin: 20px 0 !important;
    }
  }

</style>
