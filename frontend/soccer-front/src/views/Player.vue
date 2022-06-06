<template>
  <div v-if="isLoggedIn" id="logout">
  <div v-if="player">
    <p><strong>Name:</strong> {{ player.player_name }}</p>
    <p><strong>Goals:</strong> {{ player.goals }}</p>
    <p><strong>Assists:</strong> {{ player.assists }}</p>
    <p><strong>Minutes played:</strong> {{ player.minutes_played }}</p>
    <p><strong>Match played:</strong> {{ player.match_played }}</p>
    <p><strong>Saved:</strong> {{ player.saved }}</p>
    <p><strong>Conceded:</strong> {{ player.conceded }}</p>
    <p><strong>Club:</strong> {{ player.club.club }}</p>
    <p><strong>Position:</strong> {{ player.position.position }}</p>
  </div>
  </div>
  <p v-else>
    <span>User not authorized, you can <a href="/login">login</a> to get access.</span>
  </p>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'Player',
  props: ['id'],
  async created() {
    try {
      await this.viewPlayer(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/players');
    }
  },
  computed: {
    ...mapGetters({ player: 'statePlayer', user: 'stateUser'}),
    isLoggedIn: function() {
      console.log(this.$store.getters.stateUser.isAuthorized)
      return this.$store.getters.stateUser.isAuthorized;
    }
  },
  methods: {
    ...mapActions(['viewPlayer']),
  },
};
</script>
