import Vue from 'vue'
import Router from 'vue-router'
import HelloComponent from './components/HelloComponent/HelloComponent.vue'
import HitupList from './components/HitupList/HitupList.vue'
import UserProfile from './components/UserProfile/UserProfile.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'hello',
      component: HelloComponent
    },
    {
      path: '/search',
      name: 'HitupList',
      component: HitupList
    },
    {
      path: '/profile',
      name: 'UserProfile',
      component: UserProfile
    }
  ]
})
