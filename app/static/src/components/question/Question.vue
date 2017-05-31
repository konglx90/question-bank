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
      $.get('/car_manage/dapi/question', (data) => {
        console.log(data);
      });
      const data = [
        {
          "fields":
          {
            "_type": 2,
            "ctime": "2017-05-31T13:13:58.594",
            "topic": "\u7535\u529b\u7f51\u7edc\u662f\u6307\u5728\u7535\u529b\u7cfb\u7edf\u4e2d\u7531\u53d8\u538b\u5668\u3001\u7535\u529b\u7ebf\u8def\u7b49\u53d8\u6362\u3001\u8f93\u9001\u3001\u5206\u914d\u7535\u80fd\u8bbe\u5907\u6240\u7ec4\u6210\u7684\u90e8\u5206",
            "difficulty": 0.3,
            "score": 5,
            "answer": "",
            "points": 4
          },
          "model": "car_manage.question",
          "pk": 3
        },
      ];
      this.questions = this.questions.concat(data);
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
