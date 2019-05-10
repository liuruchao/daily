<!--  -->
<template>
  <div class='journal'>
    <img src="../assets/journal-logo.jpeg" alt="" class="journal--banner">
    <main class="journal__main">
      <div class="journal__main--intro">
        <h2>期刊详情</h2>
        <img src="../assets/jianjie.jpeg" alt="" class="intro--logo">
        <div class="intro--content">
          曾用刊名：晋东南师专学报;晋东南师范专科学校学报<br />

          主办单位：长治学院<br />

          出版周期：双月<br />

          ISSN：1673-2014<br />

          CN：14-1328/Z<br />

          出版地：山西省长治市<br />

          语种：中文<br />

          开本：大16开<br />

          创刊时间：1984<br />
        </div>
      </div>
      <div class="journal__main--nav">
        <router-view class="view"></router-view>
      </div>
    </main>
  </div>
</template>

<script>
  // import 

  export default {
    components: {},
    data() {
      return {

      };
    },
    //监听属性 类似于data概念
    computed: {},
    //监控data中的数据变化
    watch: {},
    //方法集合
    methods: {

    },
    //生命周期 - 创建完成（可以访问当前this实例）
    created() {

    },
  }

</script>
<style lang='scss' scoped>
  .journal {
    min-height: calc(100vh - 60px - 100px);

    .journal--banner {
      width: 80vw;
      display: block;
      border-radius: 5px;
      margin: 20px auto;
    }

    .journal__main {
      width: 80vw;
      margin: 0 auto 20px;
      display: flex;
      //   height:500px;
      justify-content: space-between;

      .journal__main--intro {
        width: 25%;
        background:white;
        padding:2em;
        h2 {
          color: #165fb1;
          font-size: 16px;
          border-bottom: 1px solid;
          padding: 0 1em 5px;
          margin-top:0;
        }

        .intro--logo {
          width: 70%;
          display: block;
          margin: auto;
          border-radius: 5px;
        }
        .intro--content{
            margin-top:2em;
            color:#676975;
            font-size:12px;
            line-height:2.5em;
        }
      }

      .journal__main--nav {
        width: 65%;
        // border:1px solid lime;
        background:white;
        border-radius: 5px;
      }
    }
    
  }

</style>
