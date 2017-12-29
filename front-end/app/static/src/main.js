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
  Radio,
  Checkbox,
  Table,
  TableColumn,
  Message,
  Loading,
  RadioGroup,
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
Vue.use(Radio);
Vue.use(Checkbox);
Vue.use(Table);
Vue.use(TableColumn);
Vue.use(RadioGroup);
// Vue.use(Message);

Vue.use(Loading.directive);
Vue.prototype.$message = Message;

Vue.use(VueRouter);

const router = new VueRouter({
  routes,
});

// export default function go(path, params) {
//   router.push({ path: path, params: params });
// }

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  router,
});
