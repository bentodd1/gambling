<template>
  <div class="hello">
    <ion-header>
      <ion-toolbar>
        <ion-title>Select your league</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-list>
      <ion-item v-for="League in this.list" @click="handleClick(League)">
        <ion-label>{{League }}</ion-label>
      </ion-item>
    </ion-list>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LeagueList',
  props: {
    msg: String
  },
  components:{
  },
  mounted() {
    /*axios.get('https://www.reddit.com/r/aww.json?raw_json=1')
      .then(response => {
        this.posts = response.data.data.children
      }) */
  },
  data() {
    return {
      list: ['NBA','NCAAF','NFL'],
      myInput: ''
    }
  },
  methods: {
    handleClick(League) {
      console.log(League)
      this.$router.push({ name: 'League', params:{  League }})
    }
  }
}
</script>