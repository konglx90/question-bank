<template lang="html">
  <div class="page">
    <h1 v-text="hello"></h1>
    <div class="my-data">

    </div>
  </div>
</template>

<script type="text/javascript">
  export default {
    data() {
      return {
        hello: '我的数据',
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
      margin: 200px auto;
      text-align: center;
      font-size: 16px;
      span {
        display: inline-block;
        margin-left: 20px;
        margin-right: 20px;
      }
      button {
        border: none;
        width: 40px;
        height: 40px;
        outline: none;
        border-radius: 50%;
      }
    }
  }
</style>
