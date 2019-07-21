import HeaderComponent from '../Header/Header.vue'
export default {
  name: 'UserProfile',
  components: {
    HeaderComponent
  },
  methods: {
    hitUp(){
      this.$store.state.view = 'WaitingComponent'
   }
  }
}