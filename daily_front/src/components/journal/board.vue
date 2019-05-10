<!--  -->
<template>
<div class='board'>
    <el-breadcrumb separator-class="el-icon-arrow-right" class="nav">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>编委会</el-breadcrumb-item>
    </el-breadcrumb>
    <h2>编委会</h2>
    <div class="board__content">
<pre>
主任委员：  茹文明
副主任委员：赵巨涛  史晓东
委　　　员：（以姓氏笔画为序） 
       　　 王志军   王建华    王璟琳   
           王慧群   史素芬    刘建伟 
           刘瑞祥   孙志刚    许华林  
           李书文   杨晓娟    张桂萍  
　　　　　   张剑妹   周成勇    郝瑞宇  
           段建宏   秦楼月    柴仲学 
           柴广育   铁   军    郭   佳
主     编： 茹文明
副  主 编：王建华（常务）   王璟琳
</pre>
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
    .board{
        .nav{
            line-height:3em;
            border-bottom:1px solid gray;
            margin:0 2em;
        }
        .board__content{
            font-size:16px;
            color:gray;
            padding:0 1em;
            line-height: 2em;
            text-align: center;
            pre{
                display: inline-block;
                text-align: left;
            }
        }
        h2{
            text-align: center;
        }
    }
</style>