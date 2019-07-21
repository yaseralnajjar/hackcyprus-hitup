<template>
<header>
  <div class="header-border"></div>
  <v-layout row>
    <v-flex xs12 sm6 offset-sm3>
      <v-card flat>
        <v-toolbar color="white" flat>
          <!-- <v-toolbar-side-icon></v-toolbar-side-icon> -->
          <!-- <v-btn icon fab class="back-icon" @click="goBack">
            <v-icon>arrow_back_ios</v-icon>
          </v-btn> -->
          <v-toolbar-title class="logo">HitUP</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon class="notifications-icon" to="/notification">
            <v-icon>notifications</v-icon>
          </v-btn>

        </v-toolbar>
      </v-card>
    </v-flex>
  </v-layout>
</header>
</template>

<script src="./Header.js"></script>

<style src="./Header.scss" lang="scss" scoped></style>
