import 'normalize.css';
import 'element-ui/lib/theme-default/index.css';
import Vue from 'vue';
import VueRouter from 'vue-router';
import Element from 'element-ui';
import App from './App.vue';
import routes from './routes';

Vue.use(Element);
Vue.use(VueRouter);

const router = new VueRouter({
  routes,
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  router,
});
