<template lang="html">
  <div class="page">
    <h1 v-text="hello"></h1>
    <div class="question">
      <h2>Vuex2 Example</h2>
      <button  @click="decrement">-</button>
      <span v-text="count"></span>
      <button @click="increment">+</button>
    </div>
  </div>
</template>

<script type="text/javascript">
  export default {
    data() {
      return {
        hello: '题库',
        count: 0,
      };
    },
    computed: {
      countNum() { return 1; },
    },
    methods: {
      increment() { console.log('inc'); },
      decrement() { console.log('dec'); },
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
      color: #ff0000;
    }
    .vuex-example {
      margin: 200px auto;
      text-align: center;
      font-size: 16px;
      color: #fff;
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
        background-color: #fff;
      }
    }
  }
</style>
