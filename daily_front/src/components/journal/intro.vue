<!--  -->
<template>
  <div class='intro'>
    <el-breadcrumb separator-class="el-icon-arrow-right" class="nav">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>期刊简介</el-breadcrumb-item>
    </el-breadcrumb>
    <h2>期刊简介</h2>
    <div class="intro__content">
      《长治学院学报》原名《晋东南师范专科学校学报》，本刊创刊于1984年，是经国家科委、新闻出版总署批准的，由长治学院主办的综合性学术双月刊。

      办刊宗旨：科学发展，规范办刊；倡导学术创新，推崇经世致用；发掘元生资源，张扬地域文化；为教学和科研服务，为地方经济建设和社会发展服务。

      主要栏目：政治法律研究、文学研究、语言文字研究、历史研究、教育教学研究及自然科学研究等。

      特色栏目：地方文史研究。本栏目的主要选题有：太行山生态环境与旅游资源研究、上党文化研究、赵树理研究、山西方言研究。

      投稿发至邮箱：czxy0355@163.com
    </div>
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
    
    .intro{
        .nav{
            line-height:3em;
            border-bottom:1px solid gray;
            margin:0 2em;
        }
        .intro__content{
            font-size:16px;
            color:gray;
            padding:0 1em;
            line-height: 2em;
        }
        h2{
            text-align: center;
        }
    }
</style>
