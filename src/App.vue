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
/*:root {

  --ion-background-color: #708090;
  --ion-font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Roboto", sans-serif;

}
ion-title {
  color: 	#00BFFF;
}
ionic-body {
   background-color: 	#708090;
}
ion-label {
  background-color: 	#708090;

  color: 	#00BFFF;
}
button{
  border: solid;
  background-color: 	#708090;
  font-size: 16px;
   width: 140px;
  color: 	#00BFFF;
}
ion-item,item-divider{
background-color: 	#708090;
color: 	#00BFFF;

}
ion-list{
  background-color: 	#708090;
}
div {
  background-color: 	#708090;
} */
</style>

