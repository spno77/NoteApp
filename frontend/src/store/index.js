import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

Vue.use(Vuex)

const state = {
	user: {
		username: '',
		password: '',
	},
	isLoggedIn: false
}

const mutations = {
	
	LOGIN_USER(state,payload){
		state.user = payload
	},
	IS_LOGGED_IN(state){
		state.isLoggedIn = true
	},
	IS_NOT_LOGGED_IN(state) {
		state.isLoggedIn = false
	},

}

const actions = {
	
	loginUser ({ commit }, user) {
		axios.post('http://127.0.0.1:8000/api/v1/rest-auth/login/',user).then((response) => {
		commit('LOGIN_USER', response.data)
		});
		commit('IS_LOGGED_IN')
	},
	logoutUser({ commit }){
		axios.post('http://127.0.0.1:8000/api/v1/rest-auth/logout/').then((response) => {
		commit('LOGIN_USER',null)
		});
		commit('IS_NOT_LOGGED_IN')
	},	
}

const getters = {
	loggedUser:  state => state.user,
	isLoggedIn:  state => state.isLoggedIn,
}


const store = new Vuex.Store({
	state,
	mutations,
	actions,
	getters
})

export default store