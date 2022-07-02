<script>
import { mapGetters } from "vuex";
import CoursePlan from "./teacher/CoursePlan.vue";
import Assignments from "./teacher/Assignments.vue";
import Messages from "./teacher/Messages.vue";
import CGPACalculator from "./teacher/CGPACalculator.vue";
export default {
  components: { CoursePlan, Messages, Assignments, CGPACalculator },
  data() {},
  computed: {
    ...mapGetters({
      batches: "course/get_batches",
      selected_student: "course/get_selected_student",
    }),
  },
  methods: {
    selectStudent(student) {
      this.$store.dispatch("course/SELECT_STUDENT", student);
    },
  },
  mounted() {
    this.$store.dispatch("course/GET_BATCHES");
  },
};
</script>
<template>
  <div class="dashboard-wrapper row">
    <div class="col-sm-4 my-5">
      <div class="batch-list card p-5">
        <div class="batch-list-header font1">
          <h3 v-if="batches">Select a student to get started</h3>
          <h3 v-else>You don't have any batch assigned to you yet</h3>
        </div>
        <div class="batch-list-body" v-if="batches">
          <ul class="list-group">
            <li
              class="list-group-item"
              v-for="batch in batches"
              :key="batch.id"
            >
              <ul>
                <li v-for="student in batch.students" :key="student.id">
                  <a href="" @click.prevent="selectStudent(student)" class="">
                    {{ student.username }}
                  </a>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="col-sm-8 my-5" v-if="selected_student">
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
            id="cgpa-tab"
            data-bs-toggle="tab"
            data-bs-target="#cgpa"
            type="button"
            role="tab"
            aria-controls="cgpa"
            aria-selected="false"
          >
            CGPA Calculator
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
          class="tab-pane fade show active"
          id="cgpa"
          role="tabpanel"
          aria-labelledby="cgpa-tab"
        >
          <CGPACalculator />
        </div>
        <div
          class="tab-pane fade"
          id="messages"
          role="tabpanel"
          aria-labelledby="messages-tab"
        >
          <Messages />
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

