<template>
  <div class="links">
      <a :href="linkData.href" target="_blank">
         <img :src="linkData.img" alt="">
      <p>{{linkData.dec}}</p>
      </a>     
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
  props:['linkData']
}
</script>

<style lang="scss" scoped>
   .links{
     display:inline-block;
     margin-top:15px;
     a{
         text-decoration: none;
         color:gray;
         width:110px;
         display:inline-block;
         img{
             width:45px;
             height:45px;
             float: left;
         }
         p{
             float:right;
             width:50px;
             margin:0;
             font-size:12px;
             text-align: center;
             margin-top:6px;
         }
     }
   }
</style>
