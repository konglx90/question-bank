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
          @current-change="handleCurrentChange"
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
      <el-button type="primary" @click="openFullScreen" v-loading.fullscreen.lock="fullscreenLoading">组新卷</el-button>

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
        papers:  [],
        input1: 100,
        input2: 0.72,
        total: 0,
        fullscreenLoading: false,
      };
    },
    computed: {
      countNum() { return 1; },
    },
    methods: {
      increment() { console.log('inc'); },
      decrement() { console.log('dec'); },
      handleClick() { console.log('dd') },
      openFullScreen() {
        this.fullscreenLoading = true;
        $.get('/car_manage/dapi/create_paper?difficulty='+this.input2+'&total_score='+this.input1, (data) => {
          const j_data = JSON.parse(data);
          console.log(j_data);
          if (j_data !== 0) {
              this.papers.pop();
              console.log('papers', this.papers)
              this.papers = this.papers.unshift(j_data.paper);
              console.log('papers', this.papers)
              this.$message({message: '成功', type: 'success'});
          } else {
              this.$message({message: '失败， 请重新输入参数', type: 'error'});
          }
          this.fullscreenLoading = false;
        });
      },
      handleCurrentChange(val) {
        $.get('/car_manage/dapi/paper?page='+val, (data) => {
          const j_data = JSON.parse(data);
          this.papers = j_data.data;
        });
      },
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
