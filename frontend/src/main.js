import Vue from 'vue'
import App from './App.vue'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import axios from 'axios'

import VueRouter from 'vue-router'

import RegisterUser from './components/RegisterUser.vue'
import Navbar from './components/Navbar.vue'


Vue.use(axios)

Vue.use(BootstrapVue)

Vue.use(IconsPlugin)

Vue.use(VueRouter)

Vue.config.productionTip = false

Vue.use(Navbar)

const routes = [
	{
		path: '/register',
		name: 'register',
		component: RegisterUser,
		props: true
	},

]

const router = new VueRouter({
    routes,
	mode: 'history'
})


new Vue({
  render: h => h(App),
  router,
}).$mount('#app')



