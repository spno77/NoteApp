import Vue from 'vue'
import App from './App.vue'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import axios from 'axios'

import VueRouter from 'vue-router'

import RegisterUser from './components/RegisterUser.vue'
import LoginUser from './components/LoginUser.vue'
import Navbar from './components/Navbar.vue'
import NoteList from './components/NoteList.vue'
import NoteCreate from './components/NoteCreate.vue'

import Vuex from 'vuex'
import store from './store/index.js'


Vue.use(axios)

Vue.use(Vuex)

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
	{
		path: '/login',
		name: 'login',
		component: LoginUser,
		props: true
	},
	{
		path: '/notes',
		name: 'notes',
		component: NoteList,
		props: true
	},
	{
		path: '/create',
		name: 'create',
		component: NoteCreate,
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
  store
}).$mount('#app')



