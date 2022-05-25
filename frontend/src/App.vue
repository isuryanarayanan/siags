<template>
  <div class="app">
    <nav class="app-navbar navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand px-5" href="#">SIAGS</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div
        class="collapse navbar-collapse"
        id="navbarSupportedContent"
        v-if="$store.getters['user/get_authenticated'] == false"
      >
        <ul id="nav" class="navbar-nav font2 mr-auto">
          <li class="nav-item btn btn-light active">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li class="nav-item btn btn-light">
            <router-link class="nav-link" to="/get-started"
              >Get Started</router-link
            >
          </li>
        </ul>
      </div>

      <div
        class="collapse navbar-collapse"
        id="navbarSupportedContent"
        v-if="$store.getters['user/get_authenticated'] == true"
      >
        <ul id="nav" class="navbar-nav font2 mr-auto">
          <li class="nav-item m-1 active btn btn-light">
            <router-link class="nav-link" to="/dashboard"
              >Dashboard</router-link
            >
          </li>
          <li class="nav-item m-1 btn btn-light">
            <router-link class="nav-link" to="/profile">Profile</router-link>
          </li>
          <li class="nav-item m-1 btn btn-light">
            <router-link class="nav-link" to="/logout">Logout</router-link>
          </li>
        </ul>
      </div>
    </nav>

    <div class="app-main">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>
<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Francois+One&display=swap");
// font-family: 'Francois One', sans-serif;
@import url("https://fonts.googleapis.com/css2?family=Josefin+Sans&display=swap");
// font-family: 'Josefin Sans', sans-serif;
.font1 {
  font-family: "Francois One", sans-serif;
}
.font2 {
  font-family: "Josefin Sans", sans-serif;
}
#nav {
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
