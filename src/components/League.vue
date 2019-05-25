<template>

<div>
<!--<ion-content
    :scrollEvents="true"> -->
    <ion-header>
      <ion-toolbar>
        <ion-title>{{this.$props.League.name}}</ion-title>
      </ion-toolbar>
    </ion-header>
     <!-- <ion-content
    :scrollEvents="true"
    @ionScrollStart="logScrollStart()"
    @ionScroll="logScrolling($event)"
    @ionScrollEnd="logScrollEnd()"> -->
 <!--<ion-content
    :scrollEvents="true"
   -->
    <ion-list>
     <!-- <ion-item>
        <ion-col>Game</ion-col>
        <ion-col>Date</ion-col>
        <ion-col>Spread</ion-col>
        <ion-col>Over Under</ion-col>
      </ion-item> -->
      <game v-for="game in this.list" :key="game.id" :gameData="game"></game>
    </ion-list>

   </div>

   <!-- </ion-content> -->

</template>
<script>
import axios from 'axios';
import game from './Game';

export default {
  name: 'LeagueList',

  props: {League:{}}
  ,
  components:{
    game
  },
  mounted() {
    this.getGameList(),
    this.League = this.$props.League
    /*axios.get('https://www.reddit.com/r/aww.json?raw_json=1')
      .then(response => {
        this.posts = response.data.data.children
      }) */

      console.log(this.$props);
  },
  data() {
    return {
      League:{},
      list: [{
          "id": 1,
          "description": "Lions vs bears",
          "date": "1/1/2018",
          "lines": [{
              "id": 1,
              "description": "Point Spread",
              "bets":[{
                  "id": 1,
                 "desciption": "Bears to win by",
                 "value": -7,
                  "shortDesc": "Bears -7"
              },
              { "id": 2,
                "desciption": "Lions to win by",
                 "value": 7,
                 "shortDesc": "Lions +7"
              } ]
          },
          {   "id": 2,
              "description": "Over Under total",
              "bets":[{
                  "id": 3,
                 "desciption": "Under points",
                 "value": 64,
                 "shortDesc": " U 64"
              },
              {
                "id": 4,
                "desciption": "Over points",
                 "value": 64,
                 "shortDesc": "O 64",
              } ]
          }
          ]
      },{
          "id": 2,
          "description": "Broncos vs Chargers",
           "date": "1/1/2018",
          "lines": [{
              "id": 3,
              "description": "Point Spread",
              "bets":[{
                 "id": 5,
                 "shortDesc": 'Broncos -7',
                 "desciption": "Broncos to win by",
                 "value": -3
              },
              {
                 "id": 6,
                 "shortDesc": 'Chargers +7',
                "desciption": "Lions to win by",
                 "value": 7
              } ]
          },
          {   "id": 4,
              "description": "Over Under total",
              "bets":[{
                  "id": 7,
                  "shortDesc": 'U 59',
                 "desciption": "Under points",
                 "value": 59
              },
              {
                "id": 8,
                "shortDesc": 'O 59',
                "desciption": "Over points",
                 "value": 59
              } ]
          }
          ]
      }],
      myInput: ''
    }
  },
  methods: {
      handleBet(shortDesc){
    return this.$ionic.alertController
        .create({
          header: 'Alert',
          subHeader: 'Subtitle',
          message: 'Taking a bet for'+ shortDesc,
          buttons: ['OK'],
        })
        .then(a => a.present())
      },
      async getGameList() {
      const url = `http://localhost:3000/games?leagues_id=`+this.$props.League.id
      axios.get(url,{ crossdomain: true })
        .then((response) => {

            this.list = response.data;
            console.log(response.data)
        })
    }
  }
}
</script>
<style>

:root {

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
}
</style>