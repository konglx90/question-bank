<template lang="html">
  <div class="page">
    <h1 v-text="school"></h1>
    <div class="paper">
      <h2>电力系统 - 组卷</h2>

      <!-- <PaperItem
          v-for="(paper, index) in papers"
          :key="paper.id"
          v-bind:paper="paper"
          v-bind:index="index">
      </PaperItem> -->
      <el-table
        :data="papers"
        style="width: 100%">
        <el-table-column
          prop="title"
          label="标题"
          width="200">
        </el-table-column>
        <el-table-column
          prop="sum_score"
          label="总分"
          width="180">
        </el-table-column>
        <el-table-column
          prop="difficulty"
          label="难度系数">
        </el-table-column>
        <el-table-column
          prop="question_count"
          label="题数">
        </el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="100">
          <template scope="scope">
            <el-button @click="handleClick" type="text" size="small"><router-link :to="{name: 'one_paper', params: { id: papers[scope.$index].id }}" class="nav-link">查看</router-link></el-button>
          </template>
        </el-table-column>
      </el-table>

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
      <!-- <div>
        <el-input class="input" v-model="input3">
          <template slot="prepend">期望试卷知识点覆盖率</template>
        </el-input>
      </div> -->
      <el-button type="primary">组新卷</el-button>

    </div>
  </div>
</template>

<script type="text/javascript">
  /* eslint-disable */
  import PaperItem from './PaperItem.vue';

  export default {
    components: {
      PaperItem,
    },
    data() {
      return {
        school: '电子科技大学',
        papers:  [
{
ctime: {
$date: 1496573841856
},
title: "电力系统分析(2017-2018)368",
question_list: "[439, 442, 382, 396, 352, 403, 358, 298, 210, 238, 214, 239, 120, 184, 193, 158, 36, 97, 10, 75, 38, 73, 80, 68, 97, 100]",
sum_score: 100,
difficulty: 0.723,
adaptation_degree: 0.925,
p_coverage: 0.756,
id: 4,
question_count: 26
}
],
        input1: 0.0,
        input2: 0.0,
        input3: 0.0,
        total: 0,
      };
    },
    computed: {
      countNum() { return 1; },
    },
    methods: {
      increment() { console.log('inc'); },
      decrement() { console.log('dec'); },
      handleClick() { console.log('dd') },
    },
    watch: {
      countNum(val) {
        this.count = val;
      },
    },
    created() {
      $.get('/car_manage/dapi/paper', (data) => {
        const j_data = JSON.parse(data);
        this.papers = this.papers.concat(j_data.data);
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
