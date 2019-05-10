<template>
  <div class="article-show" @click="showContent(datas.id)">
     <div class="article-show__title">{{datas.title}}</div>
     <div class="article-show__content">
         <div class="article-show__content--dec">
             <p>{{datas.subhead.substr(0,50)+'...'}}</p>
             <span>{{datas.time}}</span>
         </div>
         <img :src="datas.imgUrl" alt="" class="article-show__content--img">
     </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      
    }
  },
  created(){
  },
  props:['datas'],
  methods: {
      showContent(post_id){
            this.$router.push({
                path: '/show/'+post_id,
            })
      }
    }
}
</script>

<style lang="scss" scoped>
    .article-show{
        width:500px;
        border:1px solid #ededed;
        padding:1em;
        padding-bottom:2em;
        box-shadow: 1px 1px 10px rgb(177, 175, 175);
        border-radius: 5px;
        background:white;
        box-sizing: border-box;
        margin:20px;
        transition: all 0.2s ease-in;
        &:hover{
            box-shadow:3px 3px 10px rgb(116, 114, 114);
            cursor: pointer;
            transition: all 0.2s ease-out;
            transform: scale(1.02);
            .article-show__title{             
                  color:black;
            }
        }
        
        .article-show__title{
            color:#525252;
            font-weight: bold;
            font-size:20px;
            line-height:32px;
            margin:20px 0;
        }
        .article-show__content{
            display: flex;
            justify-content: space-between;
            align-items: top;
            flex-wrap:wrap;
            
        }
        .article-show__content--dec{
            width:60%;
            flex-grow: 1;

            p{
                color:#606060;
                margin:0 auto 0.5em 0;
            }
            span{
                color:#dddddd;
                font-size:10px;
            }
        }
        .article-show__content--img{
            flex-grow: 1;
            width:30%;
            display: block;
            flex-grow:1;
            height:80px;
            object-fit: contain;
        }
    }
    @media screen and(max-width:700px){
         .article-show{
             width:80vw;
             margin: auto;
             .article-show__content--dec{
                 width:100%;
             }
             .article-show__content--img{
                 width:100%;
             }
         }
    }
</style>
