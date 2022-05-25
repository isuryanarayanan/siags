<template>
  <div class="dashboard text-left p-5">
    <div class="dashboard-greet">
      <h1 class="font1">Hey {{ $store.getters["user/get_user"]._USERNAME }}</h1>
      <h5 class="font2">Welcome to your dashboard.</h5>
    </div>
    <div class="dashboard-main">
      <TeacherDashboard v-if="$store.getters['user/get_user']._MODE == 2" />
      <StudentDashboard v-if="$store.getters['user/get_user']._MODE == 1" />
    </div>
  </div>
</template>

<script>
// imoprt teacherdashboard and studendashboard
import TeacherDashboard from "../components/dashboard/teacher.vue";
import StudentDashboard from "../components/dashboard/student.vue";

export default {
  name: "Dashboard",
  components: {
    TeacherDashboard,
    StudentDashboard,
  },
  data() {
    return {
      tabs: null,
    };
  },
};
</script>
