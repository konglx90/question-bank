<template lang="html">
  <div class="question-item">
      <span>{{ index + 1 }}. </span><span>{{ question.topic }} ? ({{question.score}}')</span>
      <div v-if="question._type === 1" class="answer-place">
        <el-radio　v-for="(option, index) in question.options"
                  :key="index"
                  class="radio"
                  v-model="radio"
                  :label="index">{{option.topic}}</el-radio>
      </div>
      <div v-if="question._type === 2" class="answer-place">
        <el-checkbox-group v-model="checkList">
          <el-checkbox v-for="(option, index) in question.options"
                       :label="option.topic"
                       :key="index"
                       class="checkbox"></el-checkbox>
        </el-checkbox-group>
      </div>
      <div v-if="question._type === 3" class="answer-place">
        <el-radio　class="radio" v-model="radio" :label="1">对</el-radio>
        <el-radio　class="radio" v-model="radio" :label="2">错</el-radio>
      </div>
      <div v-if="question._type === 4" class="answer-place">
        填空题
      </div>
      <div v-if="question._type === 5" class="answer-place">
        <el-input
          type="textarea"
          :autosize="{ minRows: 2, maxRows: 8}"
          placeholder="请输入内容"
          v-model="textarea">
        </el-input>
      </div>
    </div>
  </div>
</template>

<script type="text/javascript">
  export default {
    props: ['question', 'index'],
    data() {
      return {
        dec: '哈哈',
        QUESTION_TYPE_CHIOCE: {
          1: '单选题',
          2: '多选题',
          3: '判断题',
          4: '填空题',
          5: '问答题',
        },
        radio: null,
        checkList: [],
        textarea: '',
      };
    },
  };
</script>

<style lang="scss" scoped>
  .question-item {
    text-align: left;
    background-color: #eaeefb;
    min-height: 30px;
    margin-bottom: 10px;
    padding: 8px 10px;
    border: 1px solid #d1dbe5;
    border-radius: 4px;
    box-shadow: 0 2px 4px 0 rgba(0,0,0,.12),0 0 6px 0 rgba(0,0,0,.04);

    .answer-place {
      margin: 8px 0;
    }

    .checkbox, .radio {
      display: block;
      margin: 8px 0;
    }
  }
</style>
