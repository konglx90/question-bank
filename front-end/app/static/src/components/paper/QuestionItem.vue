<template lang="html">
  <div class="question-item">
      <span>{{ index + 1 }}. </span><span>{{ question.topic }} ? ({{question.score}}')</span>
      <div v-if="question._type === 1" class="answer-place">
        <el-radio-group v-model="radio"
                        @change="doChangeRadio">
          <el-radio　v-for="(option, _index) in question.options"
                    :key="_index"
                    class="radio"
                    :label="_index">{{option.topic}}</el-radio>
        </el-radio-group>
      </div>
      <div v-if="question._type === 2" class="answer-place">
        <el-checkbox-group v-model="checkList"
                            @change="doChangeCh">
          <el-checkbox v-for="(option, _index) in question.options"
                       :label="option.topic"
                       :key="_index"
                       class="checkbox"></el-checkbox>
        </el-checkbox-group>
      </div>
      <div v-if="question._type === 3" class="answer-place">
        <el-radio-group v-model="radio"
                        @change="doChangeJu">
          <el-radio　class="radio" :label="1" :key="1">对</el-radio>
          <el-radio　class="radio" :label="2" :key="2">错</el-radio>
        </el-radio-group>
      </div>
      <div v-if="question._type === 4" class="answer-place">
        <el-input
          type="textarea"
          :autosize="{ minRows: 2, maxRows: 8}"
          placeholder="填空"
          v-model="textarea">
        </el-input>
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
        checkAns: [],
      };
    },
    methods: {
      doChangeRadio(val) {
        const ans = parseInt(val, 10);
        this.question.my_answer = this.question.options[ans].is_right;
        console.log(typeof index, ans, this.question,
          this.question.options[ans].is_right);
      },
      doChangeCh(val) {
        const len = this.checkAns.length;
        let flag = true;
        for (let i = 0; i < len; i += 1) {
          if (val.target.value === this.checkAns[i]) {
            this.checkAns.splice(i, 1);
            flag = false;
          }
        }
        if (flag === true) {
          this.checkAns.push(val.target.value);
        }

        let rL = 0;
        const rOL = this.question.options.length;
        for (let i = 0; i < rOL; i += 1) {
          if (this.question.options[i].is_right) {
            rL += 1;
          }
        }

        this.question.my_answer = this.checkAns.length === rL;

        // console.log(this.checkAns, 's', flag, rL);
      },
      doChangeJu(val) {
        let myAns = false;
        if (val === 1) {
          myAns = true;
        }
        this.question.my_answer = this.question.is_right === myAns;
      },
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
