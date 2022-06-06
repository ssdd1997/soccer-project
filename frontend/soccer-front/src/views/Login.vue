<template>
  <div className="main-container">
    <form>
      <div className="box-container">
        <div class="login-choice"><span>Sign In with</span></div>
        <Login/>
      </div>
    </form>
  </div>
</template>

<script>
import Login from '@/components/Login'

export default {
  name: 'login',
  components: {
    Login
  }
}
</script>
