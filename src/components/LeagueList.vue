<template>
  <div class="hello">
    <ion-header>
      <ion-toolbar>
        <ion-title>Select your league</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-list>
      <ion-item v-for="League in this.list" @click="handleClick(League)">
        <ion-label>{{League.name }}</ion-label>
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
    this.getList()
    /*axios.get('https://www.reddit.com/r/aww.json?raw_json=1')
      .then(response => {
        this.posts = response.data.data.children
      }) */
  },
  data() {
    return {
      list: [],
      myInput: ''
    }
  },
  methods: {
    getList()
    {
      console.log('Calling get list')
      axios.get(`http://localhost:3000/leagues`,{ crossdomain: true })
        .then((response) => {

            this.list = response.data;
        })
    },
    handleClick(League) {
      console.log(League)
      this.$router.push({ name: 'League', params:{League:  League }})
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