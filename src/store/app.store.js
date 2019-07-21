import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    view: "HelloComponent"
    // view: "WaitingComponent"
  },
  mutations: {
    // profile(state, payload) {
    //   if (payload.prop === null) {
    //     state.profile = payload.data
    //   } else {
    //     state.profile[payload.prop] = payload.data
    //   }
    // }
  },
  actions: {
    // getImgUrl(state, img) {
    //   return require(`../assets/multimedia/${img}`)
    // },
    // header: ({ commit }, payload) => {
    //   return new Promise((resolve, reject) => {
    //     commit('header', payload)
    //     resolve(true)
    //   })
    // }
  },
  getters: {
    view: state => {
      return state.view
    }
    // header: state => {
    //   return state.header
    // }
  }
})
