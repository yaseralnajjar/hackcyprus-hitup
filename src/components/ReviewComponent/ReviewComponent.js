import HitupList from '../HitupList/HitupList.vue'

export default {
  name: 'HelloComponent',
  components: {
    HitupList
  },
  data () {
    return {
      counter: 30
    }
  },
  methods: {
    startCountdown(){
      this.counter;
      var interval = setInterval(() => {
        this.counter--;
        if(this.counter == 0 ){
          clearInterval(interval);
        }
      }, 1000);
    },
    goBack(){
      this.$store.state.view = 'HitupList'
    },
    next(){
      this.$route.push('/addreview');
    }
  },
  mounted(){
    this.startCountdown();
  }
}