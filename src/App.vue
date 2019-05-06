<template>
<div id="app">
<router-view/>
</div>
 <!-- <ion-app>
  <ion-header>
    <ion-toolbar color="primary">
      <ion-title>
          Stuff
      </ion-title>
    </ion-toolbar>
    </ion-header>
    <ion-content>
    <ion-card>
      <ion-card-header>
        <ion-card-subtitle>
          Make Bet
        </ion-card-subtitle>
      </ion-card-header>
    </ion-card>
    <LeagueList/>
    </ion-content>
    </ion-app> -->
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue';
import LeagueList from '@/components/LeagueList.vue';

export default {
  name: 'app',
  components: {
    LeagueList
  },
};
</script>

<style>
/*#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
