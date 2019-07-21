<template>
  <v-card height="60px" flat>
    <v-bottom-nav
      :active.sync="bottomNav"
      :value="true"
      fixed
      color="white"
    >
      <v-btn
        color="deep-purple "
        flat
        value="nearby"
        to="/"
        active
      >
        <span>nearby</span>
        <v-icon>track_changes</v-icon>
      </v-btn>

      <v-btn
        color="deep-purple"
        flat
        value="me"
        to="/profile"
        
      >
        <span>Me</span>
        <v-icon>person</v-icon>
      </v-btn>
    </v-bottom-nav>
  </v-card>
</template>

<script src="./BottomNav.js"></script>

<style src="./BottomNav.scss" lang="scss" scoped></style>
