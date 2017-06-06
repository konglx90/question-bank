<template lang="html">
  <div class="page">
    <h1 v-text="school"></h1>
    <div class="question">
      <h2>电力系统 - 试卷</h2>

      <QuestionItem
          v-for="(question, index) in questions"
          :key="question.id"
          v-bind:question="question"
          v-bind:index="index"
          v-bind:answer="answer">
      </QuestionItem>

      <el-button type="primary" @click="answer">提交答案</el-button>

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
        id: this.$route.params.id,
      };
    },
    computed: {
      countNum() { return 1; },
    },
    methods: {
      increment() { console.log('inc'); },
      decrement() { console.log('dec'); },
      answer() {
        const len = this.questions.length;
        let score = 0;
        for (let i = 0; i < len; i += 1) {
          if (this.questions[i].my_answer === true) {
            score += this.questions[i].score;
          }
        }
        this.$message({message: '提交成功, 客观题部分: ' + score +
          ' 主观题交给教师批改， 静待佳音', type: 'success'});
      },
    },
    watch: {
      countNum(val) {
        this.count = val;
      },
    },
    created() {
      $.get('/car_manage/dapi/get_one_paper?id='+this.id, (data) => {
        const j_data = JSON.parse(data);
        this.questions = this.questions.concat(j_data.data).reverse();
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
