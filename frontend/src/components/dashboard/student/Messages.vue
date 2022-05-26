<script>
import { mapGetters } from "vuex";
export default {
  data() {
    return {
      botMessage: "",
    };
  },
  computed: {
    ...mapGetters({ course_plan: "course/get_coursePlan" }),
  },
  methods: {
    formatTime: function (datetime) {
      // return time passed from now
      var date = new Date(datetime);
      var now = new Date();
      var diff = now.getTime() - date.getTime();
      var seconds = Math.floor(diff / 1000);
      var minutes = Math.floor(seconds / 60);
      var hours = Math.floor(minutes / 60);
      var days = Math.floor(hours / 24);
      var weeks = Math.floor(days / 7);
      var months = Math.floor(days / 30);
      var years = Math.floor(days / 365);
      if (seconds < 60) {
        return "just now";
      } else if (minutes < 60) {
        return minutes + " minutes ago";
      } else if (hours < 24) {
        return hours + " hours ago";
      } else if (days < 7) {
        return days + " days ago";
      } else if (weeks < 4) {
        return weeks + " weeks ago";
      } else if (months < 12) {
        return months + " months ago";
      } else {
        return years + " years ago";
      }
    },
    sendBotMessage: function () {
      this.$store
        .dispatch("course/SEND_MESSAGE", {
          message: this.botMessage,
          plan_id: this.course_plan.course_plan.id,
        })
        .then((e) => {
          this.$store.dispatch("course/GET_COURSE_PLAN");
          this.botMessage = "";
        });
    },
  },
};
</script>
<template>
  <div class="chat-box" v-if="course_plan">
    <div class="messages card p-5">
      <div
        class="message"
        v-for="message in course_plan.course_plan.messages"
        :key="message.id"
      >
        <div class="card border-0">
          <div class="card-message bg-light">
            <h5>{{ message.message }}</h5>
          </div>
          <div class="card-title text-muted">
            ~<i> {{ formatTime(message.created_at) }} </i> |
            {{ message.sender }}
          </div>
        </div>
      </div>
    </div>
    <div class="chat-dialog p-2">
      <input type="text" v-model="botMessage" class="" alt="" />
      <div class="button btn btn-primary mx-1" @click="sendBotMessage()">
        send
      </div>
    </div>
  </div>
</template>

<style scoped>
.messages {
  overflow-y: scroll;
  height: 300px;
}
</style>