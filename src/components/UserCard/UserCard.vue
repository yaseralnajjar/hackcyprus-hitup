<template>
  <v-layout row>
    <v-flex xs12 sm6 offset-sm3>
        <v-list two-line>
          <v-subheader>
              {{ headerTitle }}
            </v-subheader>
          <template v-for="user in users">
            <v-list-tile
              :key="user.name"
              avatar
              @click=""
            >
              <v-list-tile-avatar>
                <img :src="user.avatar">
              </v-list-tile-avatar>

              <v-list-tile-content>
                <v-list-tile-title v-html="user.name"></v-list-tile-title>
                <v-list-tile-sub-title v-html="user.rate"></v-list-tile-sub-title>
              </v-list-tile-content>
            </v-list-tile>
          </template>
        </v-list>
    </v-flex>
  </v-layout>
</template>


<script src="./UserCard.js"></script>

<style src="./UserCard.scss" lang="scss" ></style>
