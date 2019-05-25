<template>
  <div class='show-article'>
    <el-table :data="tableData" border style="width: 100%" height="700px">
      <el-table-column prop="id" label="id" width="80px" type='index'>
      </el-table-column>
      <el-table-column prop="time" label="日期" width="180px">
      </el-table-column>
      <el-table-column prop="title" label="标题" width="150px">
      </el-table-column>
      <el-table-column prop="classes" label="所属分类" width="120px">
      </el-table-column>
      <el-table-column prop="subhead" label="描述">
      </el-table-column>
      <el-table-column fixed="right" label="操作" width="150px">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">查看</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog title="内容" :visible.sync="dialogVisible" width="70%" :before-close="handleClose">
      <span id="artContent">内容</span>
      <span slot="footer" class="dialog-footer">
        <!-- <el-button @click="dialogVisible = false">取 消</el-button> -->
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
        tableData: [],
        dialogVisible: false,
        reportTitle: '',
        reportDec: '',
        load: false
      };
    },
    //监听属性 类似于data概念
    computed: {},
    //监控data中的数据变化
    watch: {},
    //方法集合
    methods: {
      handleEdit(index, row) {
        console.log(index, row);
        this.dialogVisible = true;
        document.querySelector('#artContent').innerHTML = row['content'];
      },
      handleDelete(index, row) {
        const id = row['id'];
        const that = this;
        this.$confirm('此操作将永久删除该文章, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          that.axios({
            method: 'POST',
            url: 'http://127.0.0.1:5000/articleShow/delete',
            data: {
              id: id
            }
          }).then(function (res) {
            if (res.data == 'deletSuccess') {
              that.$message({
                type: 'success',
                message: '删除成功!'
              });
              that.tableData.forEach((val, index) => {
                if (val['id'] == id) {
                  that.tableData.splice(index, 1)
                  return false;
                }
              })
            }
          })
        }).catch(() => {
          that.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
      },
      handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },
      //初始化表格数据
      initTable() {
        const that = this;
        this.axios({
          method: 'POST',
          url: 'http://127.0.0.1:5000/articleShow/init',
          data: {}
        }).then(function (res) {
          res.data.forEach((val, index) => {
            const time = val['time'] + '+0800'; //中国时间
            val['time'] = (new Date(time)).toLocaleDateString() + " " + (new Date(time)).toLocaleTimeString();
          });
          that.tableData = res.data.reverse()
        }).finally(function () {})
      }
    },
    //生命周期 - 创建完成（可以访问当前this实例）
    created() {
      this.initTable();
    },
  }

</script>
<style scoped>
  .show-article {
    width: 80%;
    margin: 0px auto;
    position: relative;
    padding: 20px 50px;
  }

</style>
