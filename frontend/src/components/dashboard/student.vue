<script>
import CoursePlan from "./student/CoursePlan.vue";
import Assignments from "./student/Assignments.vue";
import { mapGetters } from "vuex";
import Messages from "./student/Messages.vue";
import Chatbot from "./student/Chatbot.vue";
export default {
  data() {
    return {
      botMessage: "hi",
    };
  },
  computed: {
    ...mapGetters({ course_plan: "course/get_coursePlan" }),
  },
  methods: {
    sendBotMessage: function () {
      this.$store
        .dispatch("course/SEND_MESSAGE", {
          message: this.botMessage,
          plan_id: this.course_plan.course_plan.id,
        })
        .then((e) => {
          console.log(e.response);
        });
    },
  },

  components: { CoursePlan, Messages, Assignments, Chatbot },
};
</script>
<template>
  <div class="dashboard-wrapper row">
    <div class="col-sm-12 my-5">
      <ul class="nav nav-tabs" id="myTab" role="tablist">
        <li class="nav-item" role="presentation">
          <button
            class="nav-link active"
            id="course-tab"
            data-bs-toggle="tab"
            data-bs-target="#course"
            type="button"
            role="tab"
            aria-controls="course"
            aria-selected="true"
          >
            Course
          </button>
        </li>
        <li class="nav-item" role="presentation">
          <button
            class="nav-link"
            id="messages-tab"
            data-bs-toggle="tab"
            data-bs-target="#messages"
            type="button"
            role="tab"
            aria-controls="messages"
            aria-selected="false"
          >
            Messages
          </button>
        </li>
        <li class="nav-item" role="presentation">
          <button
            class="nav-link"
            id="chatbot-tab"
            data-bs-toggle="tab"
            data-bs-target="#chatbot"
            type="button"
            role="tab"
            aria-controls="chatbot"
            aria-selected="false"
          >
            Chatbot
          </button>
        </li>
        <li class="nav-item" role="presentation">
          <button
            class="nav-link"
            id="assignments-tab"
            data-bs-toggle="tab"
            data-bs-target="#assignments"
            type="button"
            role="tab"
            aria-controls="assignments"
            aria-selected="false"
          >
            Assignments
          </button>
        </li>
        <li class="nav-item" role="presentation">
          <button
            class="nav-link"
            id="quiz-tab"
            data-bs-toggle="tab"
            data-bs-target="#quiz"
            type="button"
            role="tab"
            aria-controls="quiz"
            aria-selected="false"
          >
            Quizzes
          </button>
        </li>
      </ul>
      <div class="tab-content" id="myTabContent">
        <div
          class="tab-pane fade show active"
          id="course"
          role="tabpanel"
          aria-labelledby="course-tab"
        >
          <CoursePlan />
        </div>

        <div
          class="tab-pane fade"
          id="messages"
          role="tabpanel"
          aria-labelledby="messages-tab"
        >
          <Messages />
          <!-- ...
          <div class="input">
            <input
              v-model="botMessage"
              type="text"
              placeholder="talk to the bot"
            />
            <button @click="sendBotMessage()">submit</button>
          </div> -->
        </div>
        <div
          class="tab-pane fade"
          id="chatbot"
          role="tabpanel"
          aria-labelledby="chatbot-tab"
        >
          <Chatbot />
        </div>
        <div
          class="tab-pane fade"
          id="assignments"
          role="tabpanel"
          aria-labelledby="assignments-tab"
        >
          <Assignments />
        </div>
        <div
          class="tab-pane fade"
          id="quiz"
          role="tabpanel"
          aria-labelledby="quiz-tab"
        >
          ...
        </div>
      </div>
    </div>
  </div>
</template>

