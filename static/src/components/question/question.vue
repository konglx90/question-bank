<template lang="html">
  <div class="page">
    <h1 v-text="school"></h1>
    <div class="question">
      <h2>电力系统 - 题库</h2>

      <QuestionItem
          v-for="(question, index) in questions"
          :key="question.date"
          v-bind:question="question"
          v-bind:index="index">
      </QuestionItem>

      <div class="block pagination">
        <el-pagination
          layout="prev, pager, next"
          :total="50">
        </el-pagination>
      </div>

    </div>
  </div>
</template>

<script type="text/javascript">
  import QuestionItem from './questionItem.vue';

  export default {
    components: {
      QuestionItem,
    },
    data() {
      return {
        school: '郫县男子技术专修学校',
        count: 0,
        questions: [{
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄',
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄',
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄',
        }, {
          date: '2016-05-09',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄',
        }],
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
    .question {
      margin: 10px auto;
      text-align: center;
      font-size: 16px;
    }
    .pagination {
      margin-top: 50px;
    }
  }
</style>
