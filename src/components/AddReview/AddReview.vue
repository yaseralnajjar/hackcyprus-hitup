<template>
<div class="container">
  <v-btn icon fab class="back-icon" @click="goBack">
    <v-icon>arrow_back_ios</v-icon>
  </v-btn>
  <!-- <div class="hello-logo">{{ counter }}</div> -->
  <h1 class="ma-3 heading">How did you find Mohammed?</h1>

  <div class="rate-points">You have <span>{{counter}}</span> points</div>

  <div class="emojes-bar">
    <div @click="addFriendly">❤️ friendly<span>{{friendly}}</span>
    </div>
    <div @click="addFunny">😆 funny<span>{{funny}}</span>
    </div>
    <div @click="addUnique">🦄 unique<span>{{intelegance}}</span>
    </div>
  </div>

   <v-btn round dark large @click="next">Submit</v-btn>

</div>
</template>

<script src="./AddReview.js"></script>

<style src="./AddReview.scss" lang="scss" scoped></style>
