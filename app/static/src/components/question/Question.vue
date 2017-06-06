<template lang="html">
  <div class="page">
    <h1 v-text="school"></h1>
    <div class="question">
      <h2>电力系统 - 题库</h2>

      <QuestionItem
          v-for="(question, index) in questions"
          :key="question.id"
          v-bind:question="question"
          v-bind:index="index">
      </QuestionItem>

      <el-button type="primary" @click="answer">提交答案</el-button>

      <div class="block pagination">
        <el-pagination
          @current-change="handleCurrentChange"
          layout="prev, pager, next"
          :total="total">
        </el-pagination>
      </div>

    </div>
  </div>
</template>

<script type="text/javascript">
  /* eslint-disable */
  import QuestionItem from './QuestionItem.vue';

  export default {
    components: {
      QuestionItem,
    },
    data() {
      return {
        school: '电子科技大学',
        count: 0,
        questions: [],
        total: 50,
      };
    },
    computed: {
      countNum() { return 1; },
    },
    methods: {
      increment() { console.log('inc'); },
      decrement() { console.log('dec'); },
      handleCurrentChange(val) {
        $.get('/car_manage/dapi/question?page='+val, (data) => {
          const j_data = JSON.parse(data);
          this.questions = j_data.data;
        });
      },
      answer() {
        this.$message({message: '提交成功, 静待佳音', type: 'success'});
      }
    },
    watch: {
      countNum(val) {
        this.count = val;
      },
    },
    created() {
      $.get('/car_manage/dapi/question', (data) => {
        const j_data = JSON.parse(data);
        this.questions = this.questions.concat(j_data.data);
        this.total = j_data.total;
      });
    },
  }
</script>

<style lang="scss" scoped>
  .page {
    h1 {
      text-align: center;
    }
    .question {
      margin: 10px 16px;
      text-align: center;
      font-size: 16px;
    }
    .pagination {
      margin-top: 50px;
    }
  }
</style>
