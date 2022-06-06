import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import '@/assets/style.css';
import VueSimpleAlert from "vue-simple-alert";



axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';  // the FastAPI backend

import GAuth from 'vue-google-oauth2'
Vue.use(GAuth, { clientId: '335983696471-2gqntidquc1f2ebhps21sgsk38bc84uu.apps.googleusercontent.com',
  scope: 'email', prompt: 'select_account', fetch_basic_profile: false, plugin_name: "chat" })
Vue.use(VueSimpleAlert);
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');





