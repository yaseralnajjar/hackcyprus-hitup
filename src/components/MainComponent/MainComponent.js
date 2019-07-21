import HitupList from '../HitupList/HitupList.vue'
import HelloComponent from '../HelloComponent/HelloComponent.vue'
import UserProfile from '../UserProfile/UserProfile.vue'

export default {
  name: 'MainComponent',
  components: {
    HitupList,
    HelloComponent,
    UserProfile
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