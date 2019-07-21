import Vue from 'vue'
import '@/plugins/vuetify'
import App from '@/App.vue'
import router from '@/router'
import $backend from '@/backend'
Vue.prototype.$backend = $backend
Vue.config.productionTip = false

import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css' 
Vue.use(Vuetify)

import store from './store/app.store'

// Vue.use(VueRouter)

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')
