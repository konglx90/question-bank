import Home from './components/home/home.vue';
import MyData from './components/data/MyData.vue';
import Question from './components/question/Question.vue';

export default [
  {
    path: '/',
    component: Home,
  }, {
    path: '/my-data',
    component: MyData,
  }, {
    path: '/question',
    component: Question,
  },
];
