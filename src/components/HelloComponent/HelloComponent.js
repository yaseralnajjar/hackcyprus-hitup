import HitupList from '../HitupList/HitupList.vue'

export default {
  name: 'HelloComponent',
  components: {
    HitupList
  },
  data () {
    return {
      
    }
  },
  methods: {
    next(){
      this.$store.state.view = 'HitupList'
    }
  }
}