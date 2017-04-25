<template lang="html">
  <div class="question-item">
      <span>{{ index + 1 }}. </span><span>{{ question.date }}</span>
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
