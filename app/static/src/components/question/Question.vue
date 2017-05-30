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
  import QuestionItem from './QuestionItem.vue';

  export default {
    components: {
      QuestionItem,
    },
    data() {
      return {
        school: '电子科技大学',
        count: 0,
        questions: [{
          topic: '我国国家标准规定的额定电压有',
          type: '解答题',
          score: '3',
        }, {
          topic: '电力网络是指在电力系统中由变压器、电力线路等变换、输送、分配电能设备所组成的部分',
          type: '解答题',
          score: '3',
        }, {
          topic: '电力系统是指由发电机、各类变电所和输电线路以及电力用户组成的整体',
          type: '解答题',
          score: '3',
        }, {
          topic: '总装机容量是指电力系统中实际安装的发电机组额定百功功率的总和',
          type: '解答题',
          score: '3',
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
