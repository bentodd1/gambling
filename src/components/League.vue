<template>
  <div class="hello">
    <ion-header>
      <ion-toolbar>
        <ion-title>{{this.$props.League}}</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-list>

      <ion-item v-for="game in this.list" :key="game.id" >
        <ion-label>{{game.id }}</ion-label>
        <ion-label>{{game.description}}</ion-label>
           <ion-list>
               <ion-item v-for="line in game.lines" :key="line.id" >
                   <ion-label>{{line.description}}</ion-label>
                    <ion-item v-for="bet in line.bets" :key="bet.id" @click="handleBet(bet.shortDesc)" >
                        <ion-label>{{bet.shortDesc}}</ion-label>
                    </ion-item>
                </ion-item>
            </ion-list>
      </ion-item>
    </ion-list>

  </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'LeagueList',

  props: {League:String}
  ,
  components:{
  },
  mounted() {
    /*axios.get('https://www.reddit.com/r/aww.json?raw_json=1')
      .then(response => {
        this.posts = response.data.data.children
      }) */
      console.log(this.$props);
  },
  data() {
    return {
      list: [{
          "id": 1,
          "description": "Lions vs bears",
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
      }
  }
}
</script>