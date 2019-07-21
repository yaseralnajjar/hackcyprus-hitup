import Vue from 'vue'
import Router from 'vue-router'
import HelloComponent from './components/HelloComponent/HelloComponent.vue'
import HitupList from './components/HitupList/HitupList.vue'
import UserProfile from './components/UserProfile/UserProfile.vue'
import MainComponent from './components/MainComponent/MainComponent.vue'
import WaitingComponent from './components/WaitingComponent/WaitingComponent.vue'
import AcceptComponent from './components/AcceptComponent/AcceptComponent.vue'
import requestProfile from './components/requestProfile/requestProfile.vue'
import ReviewComponent from './components/ReviewComponent/ReviewComponent.vue'
import AddReview from './components/AddReview/AddReview.vue'

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
    //   path: '/wating',
    //   name: 'hello',
    //   component: WaitingComponent
    // },
    // {
    //   path: '/search',
    //   name: 'HitupList',
    //   component: HitupList
    // },
    {
      path: '/profile',
      name: 'UserProfile',
      component: UserProfile
    },
    {
      path: '/accepted',
      name: 'AcceptComponent',
      component: AcceptComponent
    },
    {
      path: '/request',
      name: 'requestProfile',
      component: requestProfile
    },
    {
      path: '/review',
      name: 'ReviewComponent',
      component: ReviewComponent
    },
    {
      path: '/addreview',
      name: 'AddReview',
      component: AddReview
    }    
  ]
})
