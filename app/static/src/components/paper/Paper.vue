<template lang="html">
  <div class="page">
    <h1 v-text="school"></h1>
    <div class="paper">
      <h2>电力系统 - 组卷</h2>

      <div class="block pagination">
        <el-pagination
          layout="prev, pager, next"
          :total="total">
        </el-pagination>
      </div>

      <div>
        <el-input class="input" v-model="input1" maxlength=12>
          <template slot="prepend">期望总分</template>
        </el-input>
      </div>
      <div>
        <el-input class="input" v-model="input2">
          <template slot="prepend">期望试卷难度</template>
        </el-input>
      </div>
      <div>
        <el-input class="input" v-model="input3">
          <template slot="prepend">期望试卷知识点覆盖率</template>
        </el-input>
      </div>
      <el-button type="primary">组新卷</el-button>

    </div>
  </div>
</template>

<script type="text/javascript">
  /* eslint-disable */
  // import QuestionItem from './QuestionItem.vue';

  export default {
    components: {
      // QuestionItem,
    },
    data() {
      return {
        school: '电子科技大学',
        input1: 0.0,
        input2: 0.0,
        input3: 0.0,
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
    created() {

    },
  }
</script>

<style lang="scss" scoped>
  .page {
    h1 {
      text-align: center;
    }
    .paper {
      margin: 10px 16px;
      text-align: left;
      font-size: 16px;

      .input {
        width: 256px;
        margin: 4px 0;
      }
    }
    .pagination {
      margin-top: 50px;
    }
  }
</style>
