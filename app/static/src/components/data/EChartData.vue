<template>
   <main>
     <figure><chart :options="bar" ref="bar" auto-resize></chart></figure>

     <figure><chart :options="pie" ref="pie" auto-resize></chart></figure>
   </main>
</template>

<style lang="stylus">
*,
*::before,
*::after
  box-sizing border-box
body
  margin 0
  font-family "Source Sans Pro", "Helvetica Neue", Arial, sans-serif
  color #666
  text-align center
a
  color inherit
  text-decoration none
h1
  margin-bottom 1em
  font-family Dosis, "Source Sans Pro", "Helvetica Neue", Arial, sans-serif
h1,
h2
  color #2c3e50
  font-weight 300
h2
  margin-top 3em
  font-size 1.2em
.desc
  margin-bottom 4em
  color #7f8c8d
h2 small
  opacity .7
p small
  font-size .8em
  color #7f8c8d
p
  line-height 1.5
pre
  display inline-block
  padding .8em
  background-color #f9f9f9
  box-shadow 0 1px 2px rgba(0,0,0,.125)
  line-height 1.1
  color #2973b7
pre,
code
  font-family "Roboto Mono", Monaco, courier, monospace
pre code
  font-size .8em
.attr
  color #e96900
.val
  color #42b983
footer
  margin 5em 0 3em
  font-size .5em
  vertical-align middle
  a
    display inline-block
    margin 0 5px
    padding 3px 0 6px
    color #7f8c8d
    font-size 2em
    text-decoration none
  a:hover
    padding-bottom 3px
    border-bottom 3px solid #42b983
button
  border 1px solid #4fc08d
  border-radius 2em
  background-color #fff
  color #42b983
  cursor pointer
  font inherit
  transition opacity .3s
  &:focus
    outline none
    box-shadow 0 0 1px #4fc08d
  &:active
    background rgba(79, 192, 141, .2)
  &[disabled]
    opacity .5
    cursor not-allowed
button,
label
  font-size .75em
figure
  display inline-block
  margin 2em auto
  border 1px solid rgba(0, 0, 0, .1)
  border-radius 8px
  box-shadow 0 0 45px rgba(0, 0, 0, .2)
  padding 1.5em 2em
  .echarts
    width 40vw
    min-width 400px
    height 300px
#logo
  display inline-block
  width 128px
  height 128px
  pointer-events none
@media (min-width 980px)
  figure.half
    padding 1em 1.5em
    .echarts
      width 28vw
      min-width 240px
      height 180px
    &:not(:last-child)
      margin-right 15px
@media (max-width 980px)
  p
    display flex
    justify-content center
    select
      text-indent calc(50% - 1em)
    select,
    label
      border 1px solid #4fc08d
      border-radius 2em
      background-color #fff
      color #42b983
      cursor pointer
      transition opacity .3s
    button,
    input,
    select,
    label
      flex 1 0
      margin 0 .5em
      padding 0
      line-height 2.4em
      max-width 40vw
      border-radius 2px
      font-size .8em
    select
      -webkit-appearance none
    input[type="checkbox"]
      display none
      &:checked + label
        background #42b983
        color #fff
  figure
    width 100vw
    margin 1em auto
    padding 0 1em
    border none
    border-radius 0
    box-shadow none
    .echarts
      width 100%
      min-width 0
      height 75vw
</style>

<script>
import ECharts from 'vue-echarts/components/ECharts.vue';
import 'echarts/lib/chart/bar';
import 'echarts/lib/chart/pie';
import 'echarts/lib/component/title';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/legend';
// import 'echarts/lib/chart/line';

export default {
  components: {
    chart: ECharts,
  },
  data: function () {
    return {
      bar: {
        title: { text: '小明的成绩' },
        tooltip: {},
        legend: {
          data: ['成绩'],
        },
        xAxis: {
            data: ["试卷一","试卷二","试卷三","试卷四","试卷五","试卷五"],
        },
        yAxis: {},
        series: [{
            name: '销量',
            type: 'bar',
            data: [95, 100, 86, 67, 54, 90],
        }],
      },
      pie: {
        title: {
          text: '试卷一知识点分布',
          x: 'center'
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
          orient: 'vertical',
          left: 'left',
          data: ['短路的基本知识', '标幺制', '无限大电源', '运算曲线法计算短路电流', '对称分量法 ', '其他']
        },
        series: [
          {
            name: '访问来源',
            type: 'pie',
            radius: '55%',
            center: ['50%', '60%'],
            data: [
              {value: 10, name: '短路的基本知识'},
              {value: 15, name: '标幺制'},
              {value: 14, name: '无限大电源'},
              {value: 6, name: '运算曲线法计算短路电流'},
              {value: 25, name: '对称分量法'},
              {value: 30, name: '其他'},
            ],
            itemStyle: {
              emphasis: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      }
    }
  }
}
</script>
