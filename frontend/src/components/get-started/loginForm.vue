<template>
  <div class="py-3">
    <div class="li-brand font1">Login to an existing account</div>
    <div class="li-form">
      <div class="form-group px-3">
        <label for="li-email">Username</label>
        <input
          type="email"
          class="form-control"
          id="li-email"
          aria-describedby="emailHelp"
          placeholder=""
          v-model="email"
        />
      </div>
      <div class="form-group px-3">
        <label for="li-password1">Password</label>
        <input
          type="password"
          class="form-control"
          id="li-password1"
          placeholder=""
          v-model="password"
        />
      </div>

      <div class="p-3">
        <div class="form-group form-check">
          <input type="checkbox" class="form-check-input" id="li-cache-login" />
          <label class="form-check-label" for="li-cache-login"
            >Keep me signed in</label
          >
        </div>

        <button class="btn btn-primary" @click="Login()">Submit</button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "LoginForm",
  data() {
    return {
      email: "",
      password: "",
      response: null,
      status: null,
      errors: [],
    };
  },
  methods: {
    handleLoginErrors: function () {
      if (this.response.username) {
        this.response.username.forEach((element) => {
          this.$toast.warning("username : " + element);
        });
      }
      if (this.response.password) {
        this.response.password.forEach((element) => {
          this.$toast.warning("password : " + element);
        });
      }
      if (this.response.detail) {
        this.$toast.warning(this.response.detail);
      }
    },
    Login: function () {
      this.$store
        .dispatch("user/GET_JWT_TOKEN", {
          username: this.email,
          password: this.password,
        })
        .then((result) => {
          this.response = JSON.parse(result.response);
          this.status = JSON.parse(result.status);
          if (this.status == 200) {
            this.$toast.success("Authenticated");
            this.$router.replace("/dashboard");
          } else {
            this.handleLoginErrors();
          }
        });
    },
  },
};
</script>
<style lang="scss" scoped>
.li-brand {
  font-size: 32px;
  color: #2c3e50;
}
</style>
