<template>
  <div class="home">
    <div class="home-wrapper">
      <div class="brand p-5 text-center">
        <h1 class="display-4 font1">Student Information And Guidance System</h1>
      </div>
      <div class="sub-brand text-center px-5">
        <p class="font2 px-5"></p>
      </div>
      <div class="call-to-action text-center">
        <router-link to="/get-started" class="text-light px-1">
          <div class="btn btn-dark btn-lg shadow">Get Started</div>
        </router-link>
        <a
          href="https://github.com/isuryanarayanan/siags"
          class="text-light px-1"
        >
          <div class="btn btn-secondary shadow">Source</div>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  components: {},
};
</script>

<style lang="scss" scoped>
.home-wrapper {
  width: 100%;
  .sub-brand {
    font-size: 24px;
  }
}
</style>
