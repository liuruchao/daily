<template>
  <div class="report">
      <img src="//image.uisdc.com/wp-content/uploads/2018/07/zt-mftk-0710.jpg" alt="" class="report__img">
      <p class="report__over">3479273看过</p>
      <p class="report__title">免费图库</p>
      <p class="report__dec">高质量的免费可商用图片都在这儿了！</p>
      <div class="report__btn">查看专题</div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      
    }
  },
  created(){
   
  }
}
</script>

<style lang="scss" scoped>
  .report{
      width:270px;
      height:246px;
      border:1px solid #eaeaea;
      color:#555;
      margin:30px auto 0 auto;
      text-align: center;
      &:hover{
          .report__btn{
              background:#409EFF;
              color:white;
          }
      }
      .report__img{
          width:100%;
          height:100px;
      }
      .report__over{
          font-size:12px;
          color:white;
          margin-top:-30px;
          padding-left:1em;
          text-align: left;
      }
      .report__title{
          font-size:17px;
          position: relative;
          padding-left:1.2em;
          margin:30px 0 10px 0;
          text-align: left;
          &::before{
            content:'';
            position: absolute;
            width:5px;
            height:100%;
            background:#409EFF;
            top:0;
            left:0;
          }
      }
      .report__dec{
          font-size:15px;
          padding-left:1.2em;
          text-overflow: ellipsis;
          overflow: hidden;
          white-space: nowrap;
          line-height:1em;
          margin:10px 0;
          text-align: left;
      }
      .report__btn{
          line-height:32px;
          font-size:13px;
          border:1px solid #eaeaea;
          display: inline-block;
          padding:0 1em;
          margin:auto;
          margin-top:10px;
      }

  }
</style>
