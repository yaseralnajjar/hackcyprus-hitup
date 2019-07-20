<template>
<v-layout row>
  <v-flex xs12 sm6 offset-sm3>
    <v-list two-line>
      <!-- <v-subheader>
        {{ headerTitle }}
      </v-subheader> -->
      <div class="people-count">
        <span>3</span>
        <span>{{ HeadTitle }}</span>
        </div>
      <v-card flat class="card-item" v-for="user in users" :key="user.name">
        <v-list-tile ripple avatar to="/profile">
          <v-list-tile-avatar>
            <img :src="user.avatar">
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title v-html="user.name" :date-age="user.age" class="user-name"></v-list-tile-title>
            <v-list-tile-sub-title>Admired by <strong>20</strong> people</v-list-tile-sub-title>
          </v-list-tile-content>

        </v-list-tile>
        <div class="emojes-bar" :key="user.name">
          <div>
            ❤️ <span>{{user.personality.friendly}}</span>
          </div>
          <div>
            😆 <span>{{user.personality.funny}}</span>
          </div>
          <div>
            🦄 <span>{{user.personality.intelegance}}</span>
          </div>
        </div>
      </v-card>
    </v-list>
  </v-flex>
</v-layout>
</template>

<script src="./UserCard.js"></script>

<style src="./UserCard.scss" lang="scss" ></style>
