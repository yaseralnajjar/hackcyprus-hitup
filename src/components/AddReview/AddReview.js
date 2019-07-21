import HitupList from '../HitupList/HitupList.vue'

export default {
  name: 'HelloComponent',
  components: {
    HitupList
  },
  data () {
    return {
      counter: 5,
      friendly: 0,
      funny: 0,
      intelegance: 0
    }
  },
  methods: {
    goBack(){
      this.$store.state.view = 'HitupList'
    },
    addFriendly(){
      if(this.counter > 0){
        this.friendly++;
        this.counter--;
      }
      
    },
    addFunny(){
      if(this.counter > 0){
        this.funny++;
        this.counter--;
      }
      
    },
    addUnique(){
      if(this.counter > 0){
        this.intelegance++;
        this.counter--;
      }
      
    }
  },
  mounted(){
    this.startCountdown();
  }
}