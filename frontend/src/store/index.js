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

}

const actions = {
	
	loginUser ({ commit }, user) {
		axios.post('http://127.0.0.1:8000/api/v1/rest-auth/login/',user).then((response) => {
		commit('LOGIN_USER', response.data)
		});
	},
}

const getters = {
	loggedUser:  state => state.user,
}


const store = new Vuex.Store({
	state,
	mutations,
	actions,
	getters
})

export default store