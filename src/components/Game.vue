<template>
         <ion-item>
       <ion-label>{{homeTeam}} vs {{gameData.visiting_team}}</ion-label>
        <ion-col>{{homeTeam}} vs {{gameData.visiting_team}}</ion-col>
        <ion-col>{{gameData.game_time}}</ion-col>
                <ion-col>
                    <ion-col  @click="handleBet(homeSpread)" >
                        <button ion-button>{{homeSpread}}</button>
                    </ion-col>
                     <ion-col  @click="handleBet(awaySpread)" >
                        <button ion-button>{{awaySpread}}</button>
                    </ion-col>
                </ion-col>
                <ion-col >
                    <ion-col  @click="handleBet(under)" >
                        <button ion-button>{{under}}</button>
                    </ion-col>
                     <ion-col  @click="handleBet(over)" >
                        <button ion-button>{{over}}</button>
                    </ion-col>
                </ion-col>
                  </ion-item>
</template>


<script>
export default {
  props: {
      gameData:{}
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
  },
  mounted() {
  },
  computed: {
      homeTeam(){
          return this.gameData.home_team;
      },
      homeSpread(){
        return this.gameData.betting_scenarios[0].value
      },
      awaySpread(){
        return this.gameData.betting_scenarios[1].value
      },
      under(){
          return this.gameData.betting_scenarios[2].value
      },
      over(){
          return this.gameData.betting_scenarios[3].value
      },
      visitingTeam(){
          return this.gameData.visiting_team;
      }

  }
}
</script>