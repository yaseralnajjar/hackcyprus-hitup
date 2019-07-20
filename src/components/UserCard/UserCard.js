export default {
  name: 'UserCard',
  data () {
    return {
      headerTitle: 'People near you',
      HeadTitle: 'People near you, let\'s make Firends.',
      users: [
        {
          name: 'Mohammed Alhakem',
          email: 'alhakeem.prof@gmail.com',
          age: 15,
          gender: 'male',
          avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
          personality: {
            friendly: 6,
            funny: 10,
            intelegance: 100
          }
        },
        {
          name: 'Hassan Erbilen',
          email: 'hassen@gmail.com',
          age: 20,
          gender: 'male',
          avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
          personality: {
            friendly: 10,
            funny: 9,
            intelegance: 200
          }
        },
        {
          name: 'Abdulrhaman Bekawi',
          email: 'Abdulrhaman@gmail.com',
          age: 25,
          gender: 'female',
          avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
          personality: {
            friendly: 25,
            funny: 5,
            intelegance: 12
          }
        }
      ],
      methods: {
       
      }
    }
  }
}