<template>
  <section>
    <p>Page with info about Champions League 2021/2022.</p>

    <div v-if="isLoggedIn" id="logout">
      <p id="logout">Click <a href="/players">here</a> to view all players.</p>
    </div>
    <p v-else>
      <span><a href="/login">Log In</a></span>
    </p>
  </section>
</template>
<script>

import {mapGetters} from "vuex";

export default {
  name: 'Home',
  computed : {
    ...mapGetters({ players: 'stateUser'}),
    isLoggedIn: function() {
      console.log(this.$store.getters.stateUser.isAuthorized)
      return this.$store.getters.stateUser.isAuthorized;
    }
  },
}
</script>
