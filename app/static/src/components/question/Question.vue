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

      <el-button type="primary">提交答案</el-button>

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
        this.questions = this.questions.concat(data.data);
        console.log(this.questions);
      });
      const data = {
num_pages: 1,
cur_page: 1,
data: [
{
_type: 2,
ctime: {
$date: 1496268902176
},
options: [
{
topic: "选项二",
ctime: {
$date: 1496321578888
},
id: 2,
is_right: true
},
{
topic: "选项一",
ctime: {
$date: 1496321566186
},
id: 1,
is_right: true
}
],
topic: "电力网络是指在电力系统中由变压器、电力线路等变换、输送、分配电能设备所组成的部分 ",
difficulty: 0.3,
score: 3,
answer: "没有答案",
id: 2,
points: 1
},
{
_type: 5,
ctime: {
$date: 1496230905215
},
options: [ ],
topic: "电力系统是指由发电机、各类变电所和输电线路以及电力用户组成的整体",
difficulty: 0.6,
score: 6,
answer: "12",
id: 1,
points: 4
}
]
};
this.questions = this.questions.concat(data.data);
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
