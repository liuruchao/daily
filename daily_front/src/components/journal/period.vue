<!-- ` -->
<template>
  <div class='period'>
    <el-breadcrumb separator-class="el-icon-arrow-right" class="nav">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>期刊导读</el-breadcrumb-item>
    </el-breadcrumb>
    <h2>期刊导读</h2>
    <div class="period__content">
      <el-collapse v-model="activeNames" @change="handleChange">
        <el-collapse-item :title="item['qikan']" :name="index" v-for="(item, index) in data" :key="index">
          <span v-for="(qikanshuItem, index) in item['qikanshu']" :key="index"
            @click="showPer(item['qikan'],qikanshuItem)">{{qikanshuItem}}</span>
        </el-collapse-item>
      </el-collapse>
      <div style="margin:1em 0;">{{selectQikan}}</div>
      <div class="art--list">
        <div v-for="(item, index) in perArr" :key="index" @click="showPoster(item['id'])">{{item['title']}}</div>
      </div>
    </div>

    <el-dialog  :visible.sync="dialogVisible"  width='65%' :before-close="handleClose" class="dialog">
      <div><h3 style="text-align:center;">{{poster['title']}}</h3></div>
      <div><span class="dialog__field">作者：</span><span>{{poster['author']}}</span></div>
      <div><span class="dialog__field">关键字：</span><span>{{poster['keyword']}}</span></div>
      <div><span class="dialog__field">摘要：</span><span>{{poster['digest']}}</span></div>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogVisible = false">关闭</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  // import 

  export default {
    components: {},
    data() {
      return {
        activeNames: ['1'],
        data: [],
        selectQikan: '',
        noClick: true,
        perArr: [],
        dialogVisible: false,
        poster:[]
      };
    },
    //监听属性 类似于data概念
    computed: {},
    //监控data中的数据变化
    watch: {},
    //方法集合
    methods: {
      handleChange(val) {
        console.log(val);
      },
      showPer(qikan, qikanshu) {
        const that = this;
        if (that.noClick) {
          that.noClick = false;
          that.selectQikan = qikan + '/' + qikanshu;
          const form = new FormData();
          form.append('qikan', qikan);
          form.append('qikanshu', qikanshu)
          this.axios({
            method: 'POST',
            url: 'http://127.0.0.1:5000/period/selectAll',
            headers: {
              'content-type': 'application/x-www-form-urlencoded'
            },
            data: form
          }).then(function (res) {
            that.perArr = res.data;
          }).finally(function () {
            that.noClick = true;
          })
        }
      },
      showPoster(id) {
        const that = this;
        const form = new FormData();
        form.append('id', id);
        this.axios({
          method: 'POST',
          url: 'http://127.0.0.1:5000/period/selectPost',
          headers: {
            'content-type': 'application/x-www-form-urlencoded'
          },
          data: form
        }).then(function (res) {
          that.poster = res.data[0];
          that.dialogVisible = true;
        }).finally(function () {
          that.noClick = true;
        })

      }
    },
    //生命周期 - 创建完成（可以访问当前this实例）
    created() {
      const that = this;
      const form = new FormData();
      this.axios({
        method: 'POST',
        url: 'http://127.0.0.1:5000/period/init',
        headers: {
          'content-type': 'application/x-www-form-urlencoded'
        },
      }).then(function (res) {
        const qikanSet = new Set();
        const qikanshuSet = new Set();
        res.data.forEach((val) => {
          qikanSet.add(val['qikan'])
        })
        for (let v of qikanSet.keys()) {
          res.data.forEach((val) => {
            if (v == val['qikan']) {
              qikanshuSet.add(val['qikanshu']);
            }
          });
          that.data.push({
            'qikan': v,
            'qikanshu': [...qikanshuSet]
          });
          qikanshuSet.clear();
        }
      })
    },
  }

</script>
<style lang='scss' scoped>
  .period {
    .nav {
      line-height: 3em;
      border-bottom: 1px solid gray;
      margin: 0 2em;
    }

    .period__content {
      font-size: 16px;
      color: gray;
      padding: 0 1em;
      line-height: 2em;
    }

    h2 {
      text-align: center;
    }
  }

  .el-collapse-item {
    span {
      width: 15%;
      display: inline-block;
      text-align: center;
      margin: 1em 0;

      &:hover {
        cursor: pointer;
        color: #409EFF;
      }
    }
  }

  .art--list {
    font-size: 12px;
    color: black;
  }

  .dialog{
    div{
      line-height: 2em;
    }
    .dialog__field{
      color:black;
      font-weight: 700;
    }
  }
</style>
