import Home from './components/home/home.vue';
import Page1 from './components/page1/Page1.vue';
import Question from './components/question/question.vue';

export default [
  {
    path: '/',
    component: Home,
  }, {
    path: '/page1',
    component: Page1,
  }, {
    path: '/question',
    component: Question,
  },
];
