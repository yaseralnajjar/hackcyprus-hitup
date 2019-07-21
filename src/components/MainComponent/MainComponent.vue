<template>
<transition name="component-fade" mode="out-in">
  <component v-bind:is="view"></component>
</transition>
</template>

<script src="./MainComponent.js"></script>

<style src="./MainComponent.scss" lang="scss" scoped></style>
