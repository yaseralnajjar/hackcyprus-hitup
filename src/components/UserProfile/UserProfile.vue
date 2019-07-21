
<template>
  <div>
    <header-component />
    <template>
     <v-flex xs12>
            <v-card  class="white--text">
              <v-layout row>
              <v-flex xs6>
                <div class="centerize">
                <v-img
                    src="https://www.whatsappprofiledpimages.com/wp-content/uploads/2018/07/cool-profile-pictures2-291x300.jpg"
                    height="125px"
                    class = "lolRadio"
                  ></v-img>
                  </div>
                </v-flex>
                <v-flex xs7>
                  <v-card-title primary-title>
                    <div>
                      <h2 class="headline">Jacob Macob</h2>
                      <h3>Developer</h3>
                      <div>
                      <i class="material-icons">face</i>
                      <p style="margin-top: -2px !important">28</p>
                      </div>
                    </div>
                  </v-card-title>
               
                </v-flex>
                
              </v-layout>
              <div class="bio">
                <v-bio>
                <h3>Biography:</h3>
                  <p>skjda lkasd ;lk ;asdlk lk ;askd ;lamsd;oi;lkmalsnd ka dsl j sdalkfj lkjasd
                   l;asdlkas lkjsaldkjalskdjlkajsl ansdnalskdjlk nsldkcjanjlsdkjpqwojdpsomdf 
                   </p>
                  </v-bio>
              </div>
               
              <v-divider light></v-divider>
              <v-card-actions class="pa-3">
                  <i class="large material-icons" >♂️</i>

                <v-spacer></v-spacer>
                <v-icon>mdi-super-chat-for-good</v-icon>
                <v-icon>😄</v-icon>
                <v-icon>❤️</v-icon>
                <v-icon>🧠</v-icon>
              </v-card-actions>
            </v-card>
          </v-flex>

           <div class="text-lg-center" style="margin-top: 20%">
            <v-btn round color="primary" dark large>Hit me up 🖐️</v-btn>
          </div>
 
</template>
        
    </div>
  </template>


<script src="./UserProfile.js"></script>

<style src="./UserProfile.scss" lang="scss" scoped></style>
