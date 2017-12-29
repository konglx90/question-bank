<template lang="html">
  <div class="page">
    <h1 v-text="title"></h1>
    <div class="my-data">
      <ul class="my-data">
        <template v-for="data in myData">
          <li><span>{{ data.key }}</span>: <span>{{ data.value }}</span></li>
        </template>
      </ul>
      <EChartData />
    </div>
  </div>
</template>

<script type="text/javascript">
  import EChartData from './EChartData.vue';

  export default {
    components: {
      EChartData,
    },
    data() {
      return {
        title: '我的数据',
        myData: [
          {
            key: '姓名',
            value: '小明',
          },
          {
            key: '学号',
            value: '2013170102009',
          },
          {
            key: '班级排名',
            value: '16',
          },
        ],
      };
    },
    computed: {
      countNum() { return 1; },
    },
    methods: {
      increment() { console.log('inc'); },
    },
    watch: {
      countNum(val) {
        this.count = val;
      },
    },
  };
</script>

<style lang="scss" scoped>
  .page {
    h1 {
      text-align: center;
      color: #20202A;
    }
    .my-data {
      text-align: center;
      color: #898980;
      list-style-type: none;
    }
  }
</style>
