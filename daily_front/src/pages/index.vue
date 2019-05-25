<template>
  <div class="home">
    <!-- 页面上部分（轮播图，发表文章数，热门文章） -->
    <div class="home__banner">
      <el-row :gutter="20" type="flex" class="home__banner--wrap">
        <!-- 轮播图 -->
        <el-col :xs="22" :sm="12">
          <el-carousel height="300px" arrow="always">
            <el-carousel-item v-for="(item, index) in 3" :key="index">
            </el-carousel-item>
          </el-carousel>
        </el-col>
        <el-col :xs="22" :sm="6">
          <div>
            <img src="../assets/home/文章.png" alt="">
            <p>长院要闻</p>
            <p>{{v1}} 篇</p>
          </div>
          <div>
            <img src="../assets/home/新闻 公告.png" alt="">
            <p>综合新闻</p>
            <p>{{v2}} 篇</p>
          </div>
          <div>
            <img src="../assets/home/专题.png" alt="">
            <p>发布期刊</p>
            <p>24 篇</p>
          </div>
          <div>
            <img src="../assets/home/通知.png" alt="">
            <p>公告通知</p>
            <p>{{v4}} 篇</p>
          </div>
        </el-col>
        <el-col :xs="22" :sm="6">
          <h3><img src="../assets/home/热门.png">热门文章</h3>
          <p v-for="(item, index) in artHot" :key="index" @click="showContent(item.id)">
            <i>{{index+1}}</i>
            <span>{{item.title}}</span>
            <span>{{item.likes}}</span>
          </p>
        </el-col>
      </el-row>
    </div>
    <!-- 页面中部通知 -->
    <div class="home__notice">
      <span>最新通知</span>
      <span>免费可商用！收好这个可自定义颜色的矢量插画图库</span>
    </div>
    <!-- 页面下部最新文章 -->
    <main class="home__all">
      <el-row :gutter="80">
        <el-col :xs="8" :sm="4" class="hidden-sm-and-down">
          <p class="myLinks">友情链接</p>
          <home-link v-for="(item, index) in linkData" :key="index" :linkData="item"></home-link>
        </el-col>
        <el-col :xs="20" :sm="20">
           <h2>最新文章</h2>
           <article-module class="article-module" v-for="(item, index) in artNew" :key="index" :datas="item"></article-module>
        </el-col>
        
      </el-row>
    </main>
  </div>
</template>

<script>
  import ArticleModule from '@/components/ArticleModule';
  import HomeLink from '@/components/HomeLink';
  export default {
    data() {
      return {
         linkData:[
             {'href':'http://www.chinaedu.edu.cn/','img':require('../assets/home/logo2.png'),'dec':'中国教育信息网'},
             {'href':'http://www.czc.edu.cn/','img':require('../assets/home/logo1.jpg'),'dec':'长治学院官网'},
             {'href':'https://www.chsi.com.cn/','img':require('../assets/home/logo3.jpg'),'dec':'学信网'}
             ],
          v1:0,       //长院要闻
          v2:0,       //综合新闻篇数
          v3:24,       //发布期刊篇数
          v4:0,       //通知报告篇数
          artHot:[    //热门文章
            {'id':1,'title':'我们学校正在扩招研究剩风刀霜剑了','likes':999},
            {'id':1,'title':'我们学校正在扩招研究剩风刀霜剑了','likes':999},
            {'id':1,'title':'我们学校正在扩招研究剩风刀霜剑了','likes':999},
            {'id':1,'title':'我们学校正在扩招研究剩风刀霜剑了','likes':999},
            {'id':1,'title':'我们学校正在扩招研究剩风刀霜剑了','likes':999},
            {'id':1,'title':'我们学校正在扩招研究剩风刀霜剑了','likes':999},
            {'id':1,'title':'我们学校正在扩招研究剩风刀霜剑了','likes':999},
          ],
          artNew:[
            {
              'id':1,
              'title':'免费可商用！收好这个可自定义颜色的矢量插画图库',
              'time':'2019-04-05',
              'subhead':'今天这个矢量插图网站，不仅可以免费商用下载，而且还可以调整预览矢量插画的颜色，还提供SVG 和PNG 两种常见格式，赶紧来收藏',
              'imgUrl':'https://image.uisdc.com/wp-content/uploads/2019/04/uisdc-banner-20190405-5.jpg',
              }
          ]

      }
    },
    components: {
      ArticleModule,     //最新文章
      HomeLink           //链接
    },
    created() {
       let loading = this.$loading({
         lock:true,
         text:'拼命加载中...'
       });
       this.init(loading);
       
    },
    methods: {
      init(load){
          const that = this;
          this.axios({
              method:'POST',
              url:'http://127.0.0.1:5000/init',
              headers: {
                  'content-type': 'application/x-www-form-urlencoded'
                },
          }).then(function(res){
              that.v1 = res.data[0]['count(1)']
              that.v2 = res.data[1]['count(1)']
              that.v3 = res.data[2]['count(1)']
              that.v4 = res.data[3]['count(1)']
              that.artHot = res.data[4]
              that.artNew = res.data[5]
          }).catch(function(){
              that.$notify({
                title: '失败',
                message: '数据加载失败',
                type: 'error',
                showClose: false
              });
          }).finally(function(){
             load.close();
          })
      },
      showContent(post_id){
            this.$router.push({
                path: '/show/'+post_id,
            })
      }
    }
  }

</script>

<style lang="scss" scoped>
  $borderColor : #d4d2d2;
  $red: #ff5a00;

  .home {
    width: 80vw;
    margin: auto;
    min-width:1000px;

    .home__banner {
      margin-top: 20px;
      box-sizing: border-box;

      &>.el-row {

        //   banner first part
        &>.el-col:nth-of-type(1) {
          border-radius: 4px;

          // 轮播图
          .el-carousel {
            border-radius: 4px;

            .el-carousel__item:nth-of-type(1) {
              background: url(../assets/banner1.jpg) no-repeat;
              background-size: cover;
            }

            .el-carousel__item:nth-of-type(2) {
              background: url(../assets/banner2.jpg) no-repeat;
              background-size: cover;
            }

            .el-carousel__item:nth-of-type(3) {
              background: url(../assets/banner3.jpg) no-repeat;
              background-size: cover;
            }
          }
        }

        // banner second part
        &>.el-col:nth-of-type(2) {
          display: grid;
          grid-template-columns: repeat(2, 1fr);
          grid-template-rows: repeat(2, 1fr);
          grid-gap: 20px;

          // 具体的块元素
          div {
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            border: 1px solid #d4d2d2;
            background: white;

            img {
              width: 30px;
            }

            p:nth-of-type(1) {
              line-height: 0.3em;
            }

            p:nth-of-type(2) {
              color: gray;
              line-height: 0.3em;
            }
            &:hover{
              box-shadow: 1px 1px 10px #d4d2d2;
              cursor: pointer;
            }
          }
        }

        // banner third part
        &>.el-col:nth-of-type(3) {
          border: 1px solid #d4d2d2;

          h3>img {
            width: 20px;
            margin-right: 1em;
          }

          p {
            font-size: 14px;

            &:hover {
              color: $red !important;
              cursor: pointer;

              span {
                color: $red;
              }

              i {
                background: $red;
                color: white;
              }
            }

            i {
              width: 1em;
              line-height: 1em;
              border: 1px solid $red;
              border-radius: 2px;
              display: inline-block;
              text-align: center;
              font-size: 12px;
              margin-right: 1em;
              color: $red;
              box-sizing: border-box;
            }

            span:nth-of-type(1) {
              width: 60%;
              display: inline-block;
              overflow: hidden;
              text-overflow: ellipsis;
              white-space: nowrap;
              vertical-align: middle;
              margin-right: 1em;
            }

            span {
              color: gray;
            }
          }
        }
      }
    }

    .home__notice {
      line-height: 3em;
      border: 1px solid $borderColor;
      background: white;
      font-size: 14px;
      padding: 0 10px;
      margin: 35px auto;

      span:nth-of-type(1) {
        margin: 0 2em;
        color: $red;
      }

      span:nth-of-type(2) {
        color: gray;

        &:hover {
          color: black;
        }
      }
    }
    
    .home__all{
        .el-col:nth-of-type(1){
            .myLinks{
                padding-left:1em;
                font-size:12px;
                color:#aaa;
                background:linear-gradient(left,#aaa 7%,#e8e8e8 7%);
                line-height:2em;
                margin-top:0;
            }
        }
        .el-col:nth-of-type(2){
            background: white;
            display:flex;
            flex-wrap: wrap;
            justify-content: space-between;

            h2{
                color:$red;
                font-size:16px;
                line-height:2em;
                position: relative;
                display:inline-block;
                margin-top:20px;
                width:100%;
                margin-left:50px;
                &:before{
                  content:'';
                  position:absolute;
                  width:70px;
                  height:2px;
                  left:0;
                  bottom:0;
                  background:red;
                }

            }
            .article-module{
                width:40%;
            }
        }
    }
  }

  @media screen and (max-width: 760px){
       .home{
         width:100vw;
         overflow:hidden;
         .home__banner{
           width:100vw;
           .home__banner--wrap{
             flex-direction: column;
             justify-content:center;
             align-items: center;
             &>div{
               margin:20px 0 0;
             }
             &>.el-col:nth-of-type(3){
               background:white;
               h3{
                 text-align: center;
               }
               p{
                 text-align: center;
               }
             }
           }
         }
         .home__all{  
           width:100vw;
           overflow: hidden;
           .el-row{
             .el-col:nth-of-type(2){
              width:90vw !important;
              margin-left:15vw;
              .article-module{
                width:80%;
             }
           }
           }  
           
         }
         .home__notice{
           width:100vw;
         }
       }
  }
</style>
