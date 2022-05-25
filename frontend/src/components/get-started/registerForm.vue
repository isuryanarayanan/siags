<template>
  <div class="register-form py-3">
    <div class="su-brand font1">Create a new account</div>
    <div class="su-form">
      <div class="form-group px-3">
        <label for="su-username">Username</label>
        <input
          type="text"
          class="form-control"
          id="su-username"
          aria-describedby="usernameHelp"
          placeholder="eg, JohnDoe"
          v-model="username"
        />
        <small id="usernameHelp" class="form-text text-muted"
          >Username should be unique</small
        >
      </div>
      <div class="form-group px-3">
        <label for="su-email">Email address</label>
        <input
          type="email"
          class="form-control"
          id="su-email"
          aria-describedby="emailHelp"
          placeholder="eg, johndoe@gmail.com"
          v-model="email"
        />
        <small id="emailHelp" class="form-text text-muted"
          >We'll never share your email with anyone else.</small
        >
      </div>
      <div class="form-group px-3">
        <label for="su-password1">Password</label>
        <input
          type="password"
          class="form-control"
          id="su-password1"
          placeholder=""
          v-model="password1"
        />
        <ul>
          <li>
            <small id="usernameHelp" class="form-text text-muted"
              >Should contain atleast 8 characters</small
            >
          </li>
          <li>
            <small id="usernameHelp" class="form-text text-muted"
              >Should contain atleast 1 uppercase character</small
            >
          </li>
          <li>
            <small id="usernameHelp" class="form-text text-muted"
              >Should contain atleast 1 numeral</small
            >
          </li>
        </ul>
      </div>
      <div class="form-group px-3">
        <label for="su-password2">Password Confirmation</label>
        <input
          type="password"
          class="form-control"
          id="su-password2"
          v-model="password2"
        />
      </div>
      <div class="p-3">
        <div class="form-group form-check">
          <input type="checkbox" class="form-check-input" id="su-agreement" />
          <label class="form-check-label" for="su-agreement"
            >Accept terms and conditions,
            <span class="text-primary">read.</span></label
          >
        </div>
        <button type="submit" class="btn btn-primary" @click="signup()">
          Submit
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RegisterForm",
  data() {
    return {
      username: null,
      email: null,
      password1: null,
      password2: null,
    };
  },
  methods: {
    signup: function () {
      this.$store
        .dispatch("user/REGISTER_USER", {
          user_type: "customer",
          username: this.username,
          email: this.email,
          password1: this.password1,
          password2: this.password2,
        })
        .then((result) => {
          this.$toast.error(result.response);
        });
    },
  },
};
</script>
<style lang="scss" scoped>
.su-brand {
  font-size: 32px;
  color: #2c3e50;
}
</style>
