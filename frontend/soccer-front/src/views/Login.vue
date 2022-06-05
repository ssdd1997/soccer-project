<template>
  <div className="main-container">
    <form>
      <div className="box-container">
        <h2 className="heading">Sign In</h2>
        <div className="form-fields">
          <input id="email" name="email" type="text" placeholder="Email Address">
        </div>
        <div className="form-fields">
          <input id="password" name="password" type="text" placeholder="Password">
        </div>
        <div className="form-fields">
          <button className="signIn" name="commit" type="submit">
            Sign In
          </button>
        </div>
        <div className="login-choice"><span>or Sign In with</span></div>
        <Login/>
      </div>
    </form>
    <div className="footer">
      <p>Don't have an account? <a href="/signup"> Create one now</a></p>
    </div>
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
