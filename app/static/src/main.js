import 'normalize.css';
import 'element-ui/lib/theme-default/index.css';
import Vue from 'vue';
import VueRouter from 'vue-router';
import {
  Button,
  Select,
  Pagination,
  Submenu,
  MenuItem,
  Form,
  FormItem,
  Row,
  Col,
  Input,
  Menu,
} from 'element-ui';
import App from './App.vue';
import routes from './routes';

Vue.use(Button);
Vue.use(Select);
Vue.use(Pagination);
Vue.use(Menu);
Vue.use(Submenu);
Vue.use(MenuItem);
Vue.use(Form);
Vue.use(FormItem);
Vue.use(Row);
Vue.use(Col);
Vue.use(Input);

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
