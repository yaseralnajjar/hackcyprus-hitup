import HitupList from '../HitupList/HitupList.vue'
import HelloComponent from '../HelloComponent/HelloComponent.vue'
import UserProfile from '../UserProfile/UserProfile.vue'
import WaitingComponent from '../WaitingComponent/WaitingComponent.vue'
 
export default {
  name: 'MainComponent',
  components: {
    HitupList,
    HelloComponent,
    UserProfile,
    WaitingComponent
  },
  data () {
    return {
      
    }
  },
  computed: {
    view(){
      return this.$store.getters.view;
    }
  }
}