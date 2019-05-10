<!--  -->
<template>
  <div class='echart'>
    <div id="main"></div>
  </div>
</template>

<script>
  // import 

  import echarts from 'echarts'; //这里是你必须的，千万不能忘记！
  export default {
    data() {
      return {
        // 初始化空对象  
        chart: null,
        // 初始化图表配置  
        opinion: ['A', 'B', 'C', 'D', 'E','F'],
        opinionData: []
      }
    },
    methods: {
      // 绘图  
      drawGraph(id) {
        // 绘图方法  
        this.chart = echarts.init(document.getElementById(id))
        // 皮肤添加同一般使用方式  
        this.chart.showLoading();
        // 返回到data中  
        const that = this; 
         
        that.axios({
            method:'POST',
            url:'http://127.0.0.1:5000/topAritcle',
            data:{
            }
        }).then(function(res){
            console.log(res.data)
            that.opinionData.push()
            let order=[4,0,5,1,3,2];
            for (let index in order){
                let option = {
                    value: res.data[index]['likes'],
                    name: res.data[index]['title']
                };
                that.opinionData[order[index]] = option;

            }
            that.chart.setOption({
                series: [{
                    name: '文章点赞数',
                    type: 'pie',
                    // 内圆半径，外圆半径  
                    radius: [50, 170],
                    // 位置，左右，上下  
                    center: ['50%', '50%'],
                    roseType: 'area',
                    data: that.opinionData, // this  
                }]
            })
            
        });
        this.chart.setOption({
          title: {
            text: 'top6热度文章',
            subtext: '基于点赞数排序',
            x: 'center'
          },
          tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
          },
        //   legend: {
        //     x: 'center',
        //     y: 'bottom',
        //     data: this.opinion // this  
        //   },
          toolbox: {
            show: true,
            feature: {
              mark: {
                show: true
              },
              dataView: {
                show: true,
                readOnly: false
              },
              magicType: {
                show: true,
                type: ['pie']
              },
              restore: {
                show: true
              },
              saveAsImage: {
                show: true
              }
            }
          },
          calculable: true,
        //   series: [{
        //     name: '文章点赞数',
        //     type: 'pie',
        //     // 内圆半径，外圆半径  
        //     radius: [50, 170],
        //     // 位置，左右，上下  
        //     center: ['50%', '50%'],
        //     roseType: 'area',
        //     data: this.opinionData, // this  
        //   }]
        })
        this.chart.hideLoading()
      }
    },
    mounted() {
      this.$nextTick(function () {
        this.drawGraph('main')
      })
    }
  }

</script>

<style scoped>
    .echart{
        height:100vh;
        background:rgb(241, 243, 245);
    }
    #main{
        height:600px;
        width:100%;
        margin-top:100px;
    }
</style>
