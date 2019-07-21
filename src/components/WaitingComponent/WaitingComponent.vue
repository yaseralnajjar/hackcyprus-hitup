<template>
<div class="container">
  <v-btn icon fab class="back-icon" @click="goBack">
    <v-icon>arrow_back_ios</v-icon>
  </v-btn>
  <div class="hello-logo">{{ counter }}</div>
  <h1 class="ma-3" v-if="counter != 0">Wating...</h1>
  <h1 class="ma-3" v-else>Wating...</h1>
  <v-btn round dark large @click="goBack">Cancel</v-btn>
</div>
</template>

<script src="./WaitingComponent.js"></script>

<style src="./WaitingComponent.scss" lang="scss" scoped></style>
