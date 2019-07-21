import Vue from 'vue'
import Router from 'vue-router'
import HelloComponent from './components/HelloComponent/HelloComponent.vue'
import HitupList from './components/HitupList/HitupList.vue'
import UserProfile from './components/UserProfile/UserProfile.vue'
import MainComponent from './components/MainComponent/MainComponent.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainComponent
    },
    {
      path: '/welcome',
      name: 'hello',
      component: HelloComponent
    },
    // {
    //   path: '/search',
    //   name: 'HitupList',
    //   component: HitupList
    // },
    // {
    //   path: '/profile',
    //   name: 'ProfileComponent',
    //   component: ProfileComponent
    // }
  ]
})
