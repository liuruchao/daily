<template>
  <div class="article">
     <h3 class="article__title" @click="showContent(datas.id)">{{datas.title}}</h3>
     <p class="article__time">{{datas.time}}</p>
     <img :src="datas.imgUrl" alt="" class="article__img">
     <p class="aritcle__dec">{{datas.subhead.substr(0,50) + '...'}}</p>
  </div>
</template>

<script>
export default {
  name: 'article',
  data () {
    return {
      
    }
  },
  props:['datas'],
  methods:{
    showContent(post_id){
            this.$router.push({
                path: '/show/'+post_id,
            })
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

  .article{
     width:560px;
     margin:0 auto 30px auto;
     padding-bottom:20px;
     border-bottom:1px solid #BFBFBF;
     .article__title{
       font-size:18px;
       color:#0DA4D3;
       line-height: 1em;
       &:hover{
         color:black;
         text-decoration: underline;
         transition:all 0.3s linear;
         cursor: pointer;
       }
     }
     .article__time{
       font-size:12px;
       color:#BFBFBF;
     }
     .article__img{
       width: 100%;
      //  height:150px;
       border-radius:3px;
     }
     .aritcle__dec{
       font-size:14px;
       color:#868686;
     }
  }
</style>
