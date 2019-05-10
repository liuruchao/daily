<!--  -->
<template>
  <div class='noAudit'>
      <h4 v-show="!datas.length">暂无未审核投稿</h4>
      <div class="item" v-for="(item, index) in datas" :key="index">
           <div>
               <span>姓名：<span class="item--val">{{item.name}}</span></span>
               <span>手机号：<span class="item--val">{{item.tel}}</span></span>
           </div>
           <div>
               <span>邮箱：<span class="item--val">{{item.email}}</span></span>
               <span>联系地址：<span class="item--val">{{item.adr}}</span></span>
           </div>
           <div>备注：<span style="width:80%" class="item--val">{{item.other}}</span></div>
           <div>
              <el-button type="primary" @click="check('http://localhost/daily_control/upload/' + item.filePath )">查看投稿</el-button>
              <a><el-button type="primary" @click="audit(index,item.id)">确认审核</el-button></a>
           </div>
      </div>
  </div>
</template>

<script>
  // import 

  export default {
    components: {},
    data() {
      return {
         datas:[]
      };
    },
    //监听属性 类似于data概念
    computed: {},
    //监控data中的数据变化
    watch: {},
    //方法集合
    methods: {
        check(url){
            window.open(url)
            // window.location.href = 'www.baidu.com'
        },
        init(){
            const that = this;
            that.axios({
            method: 'POST',
            url: 'http://127.0.0.1:5000/noaudit',
            data: {
            }
          }).then(function (res) {
              console.log(res.data)
              that.datas = res.data;
          })
        },
        audit(index,id){
            const that = this;
            console.log('index',index);
            console.log(id)
            that.axios({
            method: 'POST',
            url: 'http://127.0.0.1:5000/audit',
            data: {
                id:id
            }
          }).then(function (res) {
              if(res.data=='success'){
                  that.datas.splice(index,1)
              }
          })
        }
    },
    //生命周期 - 创建完成（可以访问当前this实例）
    created() {
       this.init();
    },
  }

</script>
<style  scoped>
   
    .noAudit{
        background:#f7f7f7;
        display:flex;
        flex-wrap: wrap;
        justify-content: space-around;
        height:100vh;
        overflow:auto;
        padding:2em;
        box-sizing: border-box;
        align-items: flex-start;
    }
    h4{
        text-align: center;
    }
    .item{
        width:27%;
        background:white;
        min-height: 200px;
        box-shadow: 2px 2px 5px #bfbaba;
        border-radius: 5px;
        /* margin: auto; */
        padding:0.5em 1em;
        color:#409EFF;
        font-weight: bold;
        margin-bottom:2em;
    }
    .item--val{
         color:gray;
         font-weight:400;
    }
    .item>div{
        /* display: flex;
        justify-content: space-around; */
        box-sizing:border-box;
        margin:1em auto;
    }
    .item>div:last-of-type{
        text-align: center;
    }
    .item>div>span{
        width:47%;
        display:inline-block;
        box-sizing: border-box;
        vertical-align: top;
    }
</style>
