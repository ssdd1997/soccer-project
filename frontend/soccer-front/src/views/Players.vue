<template>
  <div v-if="isLoggedIn" id="logout">
  <div class="container">
    <input type="text" v-model="search" placeholder="Search players..." />
    <h3> Players:</h3>
    <table class="table">
      <thead>
      <tr>
        <th scope="col">Player name</th>
        <th scope="col">Club</th>
        <th scope="col">Position</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="player in filteredPlayers" v-bind:key="player.id_player">
        <th scope="row">{{player.player_name}}</th>
        <td>{{player.club.club}}</td>
        <td>{{player.position.position}}</td>
        <td><router-link :to="{name: 'Player', params:{id: player.id_player}}">Detail</router-link></td>
      </tr>
      </tbody>
    </table>
  </div>
  </div>
  <p v-else>
    <span>User not authorized, you can <a href="/login">login</a> to get access.</span>
  </p>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  name: 'Players',
  data() {
    return {search : ''}
  },
  created: function() {
    return this.$store.dispatch('getPlayers').catch((err) => {
      this.$alert(err);
      console.log(err)
    });
  },
  computed: {
    ...mapGetters({ players: 'statePlayers'}),
    filteredPlayers() {
      return this.players.filter(player => {
        return player.player_name.toLowerCase().indexOf(this.search.toLowerCase()) > -1
      })
    },
    isLoggedIn: function() {
      console.log(this.$store.getters.stateUser.isAuthorized)
      return this.$store.getters.stateUser.isAuthorized;
    }
  },

};
</script>
