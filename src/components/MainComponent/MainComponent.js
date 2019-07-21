import HitupList from '../HitupList/HitupList.vue'
import HelloComponent from '../HelloComponent/HelloComponent.vue'
import ProfileComponent from '../ProfileComponent/ProfileComponent.vue'

export default {
  name: 'MainComponent',
  components: {
    HitupList,
    HelloComponent,
    ProfileComponent
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