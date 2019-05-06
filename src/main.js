import Vue from 'vue';

import '@ionic/core/css/core.css';
import '@ionic/core/css/ionic.bundle.css';
import IonicVue from '@ionic/vue';
import App from './App.vue';
import router from './router';

Vue.use(IonicVue);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
