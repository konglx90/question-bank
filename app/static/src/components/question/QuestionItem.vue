<template lang="html">
  <div class="question-item">
      <span>{{ index + 1 }}. </span><span>{{ question.topic }} ?</span>
    </div>
  </div>
</template>

<script type="text/javascript">
  export default {
    props: ['question', 'index'],
    data() {
      return {
        dec: '哈哈',
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
  }
</style>
