<template>
  <div class="write">
    <h3>发布文章</h3>
    <el-form :model="form" status-icon ref="ruleForm" label-width="100px" class="article--form">
      <el-form-item label="选择类别" required=true>
        <el-cascader :options="options" v-model="form.classes" expand-trigger="hover"></el-cascader>
      </el-form-item>
      <el-form-item label="标题" required=true class="setFormWidth">
        <el-input type="string" v-model="form.title" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="文章描述" required=true class="setFormWidth">
        <el-input type="textarea" v-model="form.subhead" autocomplete="off" rows=5></el-input>
      </el-form-item>
      <el-form-item label="头图选择" required=true>
          <input type="file" @change="upload" accept="image/*" id="file">
           <img :src="form.croImgBase64" alt="" style="border:1px solid #dad5d5;border-radius:5px;margin-top:20px;max-width:700px;">
      </el-form-item>
      <el-form-item label="文章内容" required=true>
        <Editor id="tinymce" v-model="form.content" :init="editorInit"></Editor>
      </el-form-item>
    </el-form>
    <!-- <Editor id="tinymce" v-model="tinymceHtml" :init="editorInit"></Editor> -->
    <el-button type="primary" :loading="loading" icon='el-icon-circle-check-outline' class="submit" @click="submit">提交
    </el-button>
    <vueCropper class="cropper" v-show="croShow" ref="cropper" :img="imageBase64" 
    outputSize=1 outputType="jpeg" autoCrop=true autoCropWidth='450px' 
    autoCropHeight='200px' fixedBox=true canMoveBox=false centerBox=true></vueCropper>
    <el-button type="primary" class='cropper-btn' @click='cropper' v-show="croShow">确认裁剪</el-button>
  </div>
</template>

<script>
  import tinymce from 'tinymce/tinymce'
  import 'tinymce/themes/silver/theme'
  import Editor from '@tinymce/tinymce-vue'
  import 'tinymce/plugins/image'
  import 'tinymce/plugins/link'
  import 'tinymce/plugins/code'
  import 'tinymce/plugins/table'
  import 'tinymce/plugins/lists'
  import 'tinymce/plugins/contextmenu'
  import 'tinymce/plugins/wordcount'
  import 'tinymce/plugins/colorpicker'
  import 'tinymce/plugins/textcolor'

  export default {
    name: 'HelloWorld',
    data() {
      return {
        editorInit: {
          language_url: '/static/tinymce/zh_CN.js',
          language: 'zh_CN',
          skin_url: '/static/tinymce/skins/ui/oxide',
          height: 600,
          plugins: 'link lists image code table colorpicker textcolor wordcount contextmenu',
          toolbar: 'bold italic underline strikethrough | fontsizeselect | forecolor backcolor | alignleft aligncenter alignright alignjustify | bullist numlist | outdent indent blockquote | undo redo | link unlink image code | removeformat',
          // plugins: 'advlist',
        },
        form: {
          classes: '',
          title: '',
          subhead: '',
          content: '',
          croImgBase64:''
        },
        options: [{
          value: '长院要闻',
          label: '长院要闻'
        }, {
          value: '综合新闻',
          label: '综合新闻'
        }, {
          value: '公告通知',
          label: '公告通知'
        }],
        loading: false,
        imageBase64: '',
        croShow: false,

      }
    },
    components: {
      Editor
    },
    methods: {
      submit() {
        const that = this;
        if (!that.form['classes']) {
          this.$message({
            message: '类别不能为空',
            type: 'warning',
            center: true
          });
          return false;
        }
        if (!that.form['title']) {
          this.$message({
            message: '标题不能为空',
            type: 'warning',
            center: true
          });
          return false;
        }
        if (!that.form['subhead']) {
          this.$message({
            message: '副标题不能为空',
            type: 'warning',
            center: true
          });
          return false;
        }
        if (!that.form['content']) {
          this.$message({
            message: '内容不能为空',
            type: 'warning',
            center: true
          });
          return false;
        }
        that.loading = true;
        this.axios({
          method: 'POST',
          url: 'http://127.0.0.1:5000/issue',
          data: that.form
        }).then(function (res) {
          if (res.data == 'issueSuccess') {
            that.$message({
              message: '发布文章成功',
              type: 'success'
            });
          } else {
            that.$message({
              message: '操作失败',
              type: 'error'
            });
          }
        }).finally(function () {
          that.loading = false;
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
          that.form['croImgBase64'] = data;
        })
        that.croShow = false;
      }
    },
    created() {
      // this.initReport();
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .write {
    height: 100vh;
    overflow: auto;
  }

  .write h3 {
    text-align: center;
    font-size: 25px;
    color: gray;
    border-bottom: 1px solid rgb(177, 174, 174);
    padding: 1em 0;
    margin: 0;
  }

  .article--form {
    width: 80%;
    margin: auto;
    padding: 50px 0 0 0;
    border-radius: 5px;
  }

  .setFormWidth {
    width: 30vw;
    min-width: 300px;
  }

  .submit {
    margin: 50px auto;
    display: block;
    width: 200px;
  }

  .uploadPic {
    border: 1px solid red;
    width: 200px;
    height: 200px;
  }
  .cropper{
      position: absolute;
      width:500px;
      height:350px;
      top:50%;
      left:50%;
      transform:translate(-50%,-50%);
      
  }
  .cropper-btn{
     position:absolute;
     right:20%;
     transform:translateY(-50%);
     top:50%;
     width:100px;
  }
</style>
