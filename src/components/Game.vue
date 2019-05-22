<template>
         <ion-item>
        <ion-col>{{game.home_team}} vs {{game.visiting_team}}</ion-col>
        <ion-col>{{game.game_time}}</ion-col>
               <ion-col>
                    <ion-col  @click="handleBet(game.betting_scenarios[0].value)" >
                        <button ion-button>{{game.betting_scenarios[0].value}}</button>
                    </ion-col>
                     <ion-col  @click="handleBet(game.betting_scenarios[1].value)" >
                        <button ion-button>{{game.betting_scenarios[1].value}}</button>
                    </ion-col>
                </ion-col>
                <ion-col >
                    <ion-col  @click="handleBet(game.betting_scenarios[2].value)" >
                        <button ion-button>{{game.betting_scenarios[2].value}}</button>
                    </ion-col>
                     <ion-col  @click="handleBet(game.betting_scenarios[3].value)" >
                        <button ion-button>{{game.betting_scenarios[3].value}}</button>
                    </ion-col>
                </ion-col>
                  </ion-item>
</template>