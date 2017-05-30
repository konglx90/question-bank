import MyData from './components/data/MyData.vue';
import Question from './components/question/Question.vue';

export default [
  {
    path: '/',
    component: MyData,
  }, {
    path: '/my-data',
    component: MyData,
  }, {
    path: '/question',
    component: Question,
  },
];
