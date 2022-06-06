<template>
  <header>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="/">Champions Players</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <ul v-if="isLoggedIn" class="navbar-nav me-auto mb-2 mb-md-0">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/players">Players</router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link" @click="logout">Log Out</a>
            </li>
          </ul>
          <ul v-else class="navbar-nav me-auto mb-2 mb-md-0">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/login">Log In</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: 'NavBar',
  data() {
    return {gAuth : this.$gAuth}
  },
  computed: {
    isLoggedIn: function() {
      console.log(this.$store.getters.stateUser.isAuthorized)
      return this.$store.getters.stateUser.isAuthorized;
    }
  },
  methods: {
    ...mapActions(['logOut']),
    async logout () {
      try {
        await this.logOut(this.gAuth);
        console.log(this.gAuth)
        this.$router.go()
      }
      catch (error){
        console.log(error);
        this.$alert("Error to log out.");
      }
    }
  },
}
</script>

<style scoped>
a {
  cursor: pointer;
}
</style>
