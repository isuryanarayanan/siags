<template>
  <div class="get-started p-5 text-left">
    <div class="get-started-wrapper row">
      <div class="signup p-1 col-sm-6">
        <RegisterForm></RegisterForm>
      </div>
      <div class="login p-1 col-sm-6">
        <LoginForm></LoginForm>
      </div>
    </div>
  </div>
</template>

<script>
import RegisterForm from "../components/get-started/registerForm.vue";
import LoginForm from "../components/get-started/loginForm.vue";
export default {
  name: "GetStarted",
  components: { LoginForm, RegisterForm }
};
</script>
