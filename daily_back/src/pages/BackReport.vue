<!-- 后台专题 -->
<template>
  <div class='back-report'>
    <el-table :data="tableData" border style="width: 100%" height="500px">
      <el-table-column prop="id" label="id" width="80px" type='index'>
      </el-table-column>
      <el-table-column prop="time" label="日期" width="180px">
      </el-table-column>
      <el-table-column prop="title" label="专题名" width="150px">
      </el-table-column>
      <el-table-column prop="subhead" label="描述">
      </el-table-column>
      <el-table-column fixed="right" label="操作" width="150px">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-button type="primary" plain icon='el-icon-circle-plus-outline'
      style="display:block;width:200px;margin:20px auto;" @click="dialogVisible = true"></el-button>
    <!-- 插入新专题 -->
    <el-dialog title="添加" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
      <el-input v-model="reportTitle" placeholder="请输入专题名"></el-input>
      <el-input v-model="reportDec" placeholder="请输入专题描述" style="margin-top:30px;"></el-input>
       <input type="file" @change="upload" accept="image/*" id="file">
       <img :src="croImgBase64" alt="" style="border:1px solid #dad5d5;border-radius:5px;margin-top:20px;width:100%">
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="insertReport" :loading="load">确 定</el-button>
      </span>
    </el-dialog>
    <vueCropper class="cropper" v-show="croShow" ref="cropper" :img="imageBase64" 
    outputSize=1 outputType="jpeg" autoCrop=true autoCropWidth='450px' 
    autoCropHeight='250px' fixedBox=true canMoveBox=false centerBox=true></vueCropper>
    <el-button type="primary" class='cropper-btn' @click='cropper' v-show="croShow">确认裁剪</el-button>
  </div>
</template>

<script>
  // import 

  export default {
    components: {},
    data() {
      return {
        tableData:[],
        dialogVisible: false,
        reportTitle:'',
        reportDec:'',
        load:false,
        imageBase64: '',
        croShow: false,
        croImgBase64:''
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
      },
      handleDelete(index, row) {
        const id = row['id'];
        const that = this;
        this.$confirm('此操作将永久删除该专题及包含文章, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
            that.axios({
            method:'POST',
            url:'http://127.0.0.1:5000/report/delete',
            data:{
                id:id
            }
            }).then(function(res){
                if(res.data == 'deletSuccess'){
                    that.$message({
                    type: 'success',
                    message: '删除成功!'
                   });
                    that.tableData.forEach( (val,index) =>{
                         if(val['id'] == id){
                             that.tableData.splice(index,1)
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
      insertReport(){
        const that = this;
        that.load = true;
        this.axios({
            method:'POST',
            url:'http://127.0.0.1:5000/report/insert',
            data:{
                title:that.reportTitle,
                subhead:that.reportDec,
                imgUrl:that.croImgBase64
            }
        }).then(function(res){
            that.dialogVisible = false;
            let time = res.data[0]['time']+'+0800';  //中国时间
            res.data[0]['time'] = (new Date(time)).toLocaleDateString() + " " + (new Date(time)).toLocaleTimeString() 
            that.tableData.unshift(res.data[0]);
        }).finally(function(){
            that.load = false;
        })
      },
      //初始化表格数据
      initTable(){
          const that = this;
          this.axios({
            method:'POST',
            url:'http://127.0.0.1:5000/report/init',
            data:{
            }
        }).then(function(res){
            res.data.forEach((val,index) => {
                const time = val['time']+'+0800'; //中国时间
                val['time'] = (new Date(time)).toLocaleDateString() + " " + (new Date(time)).toLocaleTimeString();    
            });
            that.tableData = res.data.reverse()
        }).finally(function(){
        })
      },
      upload() {
        const that = this;
        let input = document.querySelector('#file');
        // console.log(input.files[0]);
        let reader = new FileReader();
        reader.readAsDataURL(input.files[0]); //发起异步请求
        reader.onload = function () {
          //读取完成后，数据保存在对象的result属性中
          console.log(this.result)
          that.croShow = true;
          that.imageBase64 = this.result;
        }

      },
      cropper(){
        const that = this;
        this.$refs.cropper.startCrop() //开始截图
        // 获取截图的base64 数据
        this.$refs.cropper.getCropData((data) => {
          // do something
          console.log(data)  
          that.croImgBase64 = data;
        })
        that.croShow = false;
      }
    },
    //生命周期 - 创建完成（可以访问当前this实例）
    created() {
        this.initTable();
    },
  }

</script>
<style scoped>
  .back-report {
    width: 80%;
    margin:10px auto;
    position: relative;
    padding: 50px;
  }
  .cropper{
      position: absolute;
      width:500px;
      height:350px;
      top:50%;
      left:50%;
      transform:translate(-50%,-50%);
      z-index:3000;
      
  }
  .cropper-btn{
     position:absolute;
     right:20%;
     transform:translateY(-50%);
     top:50%;
     width:100px;
      z-index:3000;

  }
</style>
