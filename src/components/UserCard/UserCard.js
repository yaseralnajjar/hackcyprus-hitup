export default {
  name: 'UserCard',
  data () {
    return {
      headerTitle: 'People near to you',
      users: [
        {
          name: 'Mohammed Alhakem',
          email: 'alhakeem.prof@gmail.com',
          rate: 5,
          avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
          personality: {
            friendly: 6,
            funny: 10,
            intelegance: 100
          }
        },
        {
          name: 'Hassan Erbilen',
          email: 'hassen@gmail.com',
          rate: 8,
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
          rate: 20,
          avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
          personality: {
            friendly: 25,
            funny: 5,
            intelegance: 12
          }
        }
      ]
    }
  }
}