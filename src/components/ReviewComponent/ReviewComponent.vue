<template>
<div class="container">
  <v-btn icon fab class="back-icon" @click="goBack">
    <v-icon>arrow_back_ios</v-icon>
  </v-btn>
  <!-- <div class="hello-logo">{{ counter }}</div> -->
  <h1 class="ma-3 heading">How was your experiance?</h1>

  <div class="reactions">
    <router-link to="/addreview">😃</router-link>
    <div>😟</div>
  </div>

</div>
</template>

<script src="./ReviewComponent.js"></script>

<style src="./ReviewComponent.scss" lang="scss" scoped></style>
