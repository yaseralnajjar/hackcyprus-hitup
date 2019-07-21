<template>
<div>
  <header-component />
  <template>
    <v-flex xs12>
      <v-card class="white--text">
      <v-layout row class="centerlize"> 
          <v-flex xs12>
            <div class="centerize">
              <v-img src='https://cdn.vuetifyjs.com/images/lists/1.jpg' height="125px" class="lolRadio"></v-img>
            </div>
          </v-flex>
          </v-layout>
       <v-flex xs12>
            <v-card-title primary-title>
                  <v-layout row class="centerText">
              <div>
                <h2 class="headline">Mohammed Alhakem</h2>
                <h3>Admired by:<span style="font-weight: bold; margin: 0 0px 0 6px !important">28</span> people</h3>
             
              </div>
                    </v-layout>

            </v-card-title>

          </v-flex>
         

        <div class="emojes-bar">
          <div>
            ❤️ <span>22</span>
          </div>
          <div>
            😆 <span>15</span>
          </div>
          <div>
            🦄 <span>15</span>
          </div>
        </div>
                <v-divider light></v-divider>

        <div class="bio">
          <v-bio>
            <p style="font-size: 15px">I love cofffeeeeeeeeee❤️☕ so much because I'm a software developer. By the way, if you hit me up your life will never be the same
            </p>

          </v-bio>
        </div>
                <v-divider light></v-divider>
 <div class="text-lg-center" style="margin-top: 20%">
      <v-btn round color="primary" dark large>Hit me up 🖐️</v-btn>
    </div>

        </v-card-actions>
      </v-card>
    </v-flex>

   
  </template>

</div>
</template>

<script src="./UserProfile.js"></script>

<style src="./UserProfile.scss" lang="scss" scoped></style>
