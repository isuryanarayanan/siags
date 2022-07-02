<script>
import { v4 as uuidv4 } from "uuid";
import { mapGetters } from "vuex";
export default {
  name: "CGPACalculator",
  data() {
    return {
      grades: [{ id: uuidv4(), value: 0 }],
      average: 0,
    };
  },
  computed: {
    ...mapGetters({
      course_plan: "course/get_coursePlan",
      selected_student: "course/get_selected_student",
    }),
    formValid() {
      return this.grades.every(({ value }) => !isNaN(+value));
    },
  },
  methods: {
    addGrade() {
      this.grades.push({ id: uuidv4(), value: 0 });
    },
    deleteGrade(index) {
      this.grades.splice(index, 1);
    },
    calculate() {
      if (!this.formValid) {
        return;
      }
      this.average =
        this.grades.map(({ value }) => value).reduce((a, b) => a + b, 0) /
        this.grades.length;
    },
  },
};
</script>
<template>
  <div class="wrap p-1">
    <form @submit.prevent="calculate">
      <div v-for="(grade, index) of grades" class="p-1" :key="grade.id">
        <input class="input" v-model.number="grade.value" />
        <button
          type="button"
          class="btn btn-primary m-1"
          @click="deleteGrade(index)"
        >
          delete grade
        </button>
      </div>
      <button type="button" class="btn btn-success m-1" @click="addGrade">
        add grade
      </button>
      <button type="submit" class="btn btn-primary m-1">
        calculate average
      </button>
    </form>
    <div>Your average grade is {{ average }}</div>
  </div>
</template>


<!-- <script>
import { v4 as uuidv4 } from "uuid";
import { mapGetters } from "vuex";
export default {
  name: "CGPACalculator",
  data() {
    return {
      grades: {
        semester: [],
      },
      average: 0,
    };
  },
  computed: {
    ...mapGetters({
      course_plan: "course/get_coursePlan",
      selected_student: "course/get_selected_student",
    }),
    formValid() {
      return this.grades.every(({ value }) => !isNaN(+value));
    },
  },

  methods: {
    addGrade(value) {
      this.grades.push(value);
    },
  },
};
</script>
<template>
  <div class="wrap">
    <h3 class="font2 p-5">Calculate your cgpa for your course plan</h3>
    <div class="card" v-if="course_plan">
      <ul
        v-for="semester in course_plan.course_plan.semesters"
        :key="semester.id"
      >
        <li>
          <div class="card">
            <h3 class="font2">Semester #{{ semester.sem }}</h3>
            <ul>
              <li v-for="course in semester.courses" :key="course.id">
                <input
                  type="number"
                  name="score"
                  id=""
                  :placeholder="'mark for course ' + course.name"
                />
              </li>

              <li v-for="elective in semester.electives" :key="elective.id">
                <input
                  type="number"
                  name="score"
                  id=""
                  :placeholder="'mark for elective ' + elective.name"
                />
              </li>
            </ul>
          </div>
        </li>
      </ul>
      <input type="submit" placeholder="submit" />
      {{ grades }}
    </div>
  </div>
</template>
 -->
