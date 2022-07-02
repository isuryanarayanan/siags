<script>
import { mapGetters } from "vuex";
export default {
  data() {
    return {
      new_semester: {
        sem: "",
        course: [],
        elective: [],
        student: "",
      },
      proxy_semester: {
        sem: "",
        course: [],
        elective: [],
        student: "",
      },
      new_sem: "",
      new_course: "",
      new_elective: "",
    };
  },
  computed: {
    ...mapGetters({
      course_plan: "course/get_coursePlan",
      courses: "course/get_courses",
      selected_student: "course/get_selected_student",
    }),
  },
  methods: {
    addNewCourse() {
      this.new_semester.course.push(this.new_course.id);
      this.proxy_semester.course.push(this.new_course);
    },
    addNewElective() {
      this.new_semester.elective.push(this.new_elective.id);
      this.proxy_semester.elective.push(this.new_elective);
    },
    addSemester() {
      this.new_semester.sem = this.new_sem;
      this.proxy_semester.sem = this.new_sem;
      this.new_semester.student = this.selected_student.id;
      this.proxy_semester.student = this.selected_student.id;
      console.log(this.new_semester);
      this.$store
        .dispatch("course/CREATE_SEMESTER", this.new_semester)
        .then((e) => {
          this.new_semester = {
            sem: "",
            course: [],
            elective: [],
            student: "",
          };
          this.proxy_semester = {
            sem: "",
            course: [],
            elective: [],
            student: "",
          };
          this.new_sem = "";

          this.$store.dispatch(
            "course/GET_COURSE_PLAN",
            this.selected_student.id
          );
        });
    },
    createCoursePlan() {
      this.$store
        .dispatch("course/CREATE_COURSE_PLAN", {
          name: "Strategic course plan",
          description: "Course Plan for " + this.selected_student.username,
          student: this.selected_student.id,
        })
        .then((e) => {
          if (e.status == 200) {
            this.$store.dispatch(
              "course/GET_COURSE_PLAN",
              this.selected_student.id
            );
          }
        });
    },
  },
  mounted() {
    this.$store.dispatch("course/GET_COURSE_PLAN", this.selected_student.id);
    this.$store.dispatch("course/GET_COURSES").then((e) => {});
  },
};
</script>
<template>
  <div class="plan p-5">
    <link
      href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
      rel="stylesheet"
    />

    <section class="timeline_area section_padding_130">
      <div class="container">
        <div class="row justify-content-left pb-5">
          <div class="col-12 col-sm-8 col-lg-6">
            <div class="section_heading text-left">
              <h6 class="font2">Course plan</h6>
              <h3 class="font2" v-if="course_plan">
                Here is the course plan curated by you for
                {{ selected_student.username }}
              </h3>
              <h3
                class="font2"
                v-if="!course_plan && selected_student.course_plan"
              >
                {{ selected_student.course_plan.message }}
              </h3>

              <a
                href=""
                @click.prevent="createCoursePlan()"
                class="btn btn-success"
                v-if="!course_plan && selected_student.course_plan"
              >
                Create new course plan for {{ selected_student.username }}</a
              >
              <div class="line"></div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-12 bg-dark row p-5" v-if="course_plan">
            <div class="view-semester col-6 text-light">
              <h3>Semester{{ new_semester.sem }}</h3>
              <ul>
                <h5>Courses</h5>
                <li v-for="course in proxy_semester.course" :key="course.id">
                  {{ course.name }}
                </li>
              </ul>
              <ul>
                <h5>Electives</h5>
                <li
                  v-for="elective in proxy_semester.elective"
                  :key="elective.id"
                >
                  {{ elective.name }}
                </li>
              </ul>
            </div>
            <div class="add-semester col-6">
              <ul>
                <li>
                  <input
                    type="number"
                    placeholder="semester"
                    class="m-1"
                    v-model="new_sem"
                  />
                </li>
                <li>
                  <div class="add-courses">
                    <select id="course" name="course" v-model="new_course">
                      <option value="">Choose a course</option>
                      <option
                        v-for="course in courses"
                        :key="course.id"
                        :value="course"
                      >
                        {{ course.name }}
                      </option>
                    </select>

                    <button class="btn btn-primary m-1" @click="addNewCourse()">
                      Add
                    </button>
                  </div>
                </li>
                <li>
                  <div class="add-electives">
                    <select
                      id="elective"
                      name="elective"
                      v-model="new_elective"
                    >
                      <option value="">Choose an elective</option>
                      <option
                        v-for="elective in courses"
                        :key="elective.id"
                        :value="elective"
                      >
                        {{ elective.name }}
                      </option>
                    </select>
                    <button
                      class="btn btn-primary m-1"
                      @click="addNewElective()"
                    >
                      Add
                    </button>
                  </div>
                </li>
                <li>
                  <div class="btn btn-success" @click="addSemester()">
                    Add semester
                  </div>
                </li>
              </ul>
            </div>
          </div>
          <div class="col-12 py-5">
            <div v-if="course_plan" class="apland-timeline-area">
              <div
                class="single-timeline-area"
                v-for="semester in course_plan.course_plan.semesters"
                :key="semester.sem"
              >
                <div
                  class="timeline-date wow fadeInLeft"
                  data-wow-delay="0.1s"
                  style="
                    visibility: visible;
                    animation-delay: 0.1s;
                    animation-name: fadeInLeft;
                  "
                >
                  <p>Semester {{ semester.sem }}</p>
                </div>

                <div class="row">
                  <div
                    class="col-12 col-md-6 col-lg-4"
                    v-for="course in semester.courses"
                    :key="course.id"
                  >
                    <div
                      class="single-timeline-content d-flex wow fadeInLeft"
                      data-wow-delay="0.3s"
                      style="
                        visibility: visible;
                        animation-delay: 0.3s;
                        animation-name: fadeInLeft;
                      "
                    >
                      <div class="timeline-icon">
                        <i class="fa fa-address-card" aria-hidden="true"></i>
                      </div>
                      <div class="timeline-text">
                        <h6>{{ course.name }}</h6>
                        <p>{{ course.code }}</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div
                  class="col-12 col-md-6 col-lg-4"
                  v-for="elective in semester.electives"
                  :key="elective.id"
                >
                  <div
                    class="single-timeline-content d-flex wow fadeInLeft"
                    data-wow-delay="0.3s"
                    style="
                      visibility: visible;
                      animation-delay: 0.3s;
                      animation-name: fadeInLeft;
                    "
                  >
                    <div class="timeline-icon">
                      <i class="fa fa-address-card" aria-hidden="true"></i>
                    </div>
                    <div class="timeline-text">
                      <h6>{{ elective.name }}</h6>
                      <p>{{ elective.code }}</p>
                      <p>elective</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<style scoped>
body {
  margin-top: 20px;
}
.nav-link {
  color: #42b983;
}

.timeline_area {
  position: relative;
  z-index: 1;
}
.single-timeline-area {
  position: relative;
  z-index: 1;
  padding-left: 180px;
}
@media only screen and (max-width: 575px) {
  .single-timeline-area {
    padding-left: 100px;
  }
}
.single-timeline-area .timeline-date {
  position: absolute;
  width: 180px;
  height: 100%;
  top: 0;
  left: 0;
  z-index: 1;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: end;
  -ms-flex-pack: end;
  justify-content: flex-end;
  padding-right: 60px;
}
@media only screen and (max-width: 575px) {
  .single-timeline-area .timeline-date {
    width: 100px;
  }
}
.single-timeline-area .timeline-date::after {
  position: absolute;
  width: 3px;
  height: 100%;
  content: "";
  background-color: #ebebeb;
  top: 0;
  right: 30px;
  z-index: 1;
}
.single-timeline-area .timeline-date::before {
  position: absolute;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background-color: #f1c40f;
  content: "";
  top: 0%;
  right: 26px;
  z-index: 5;
  margin-top: -5.5px;
}
.single-timeline-area .timeline-date p {
  margin-bottom: 0;
  color: #020710;
  font-size: 13px;
  text-transform: uppercase;
  font-weight: 500;
}
.single-timeline-area .single-timeline-content {
  position: relative;
  z-index: 1;
  padding: 30px 30px 25px;
  border-radius: 6px;
  margin-bottom: 15px;
  margin-top: 15px;
  -webkit-box-shadow: 0 0.25rem 1rem 0 rgba(47, 91, 234, 0.125);
  box-shadow: 0 0.25rem 1rem 0 rgba(47, 91, 234, 0.125);
  border: 1px solid #ebebeb;
}
@media only screen and (max-width: 575px) {
  .single-timeline-area .single-timeline-content {
    padding: 20px;
  }
}
.single-timeline-area .single-timeline-content .timeline-icon {
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
  width: 30px;
  height: 30px;
  background-color: #f1c40f;
  -webkit-box-flex: 0;
  -ms-flex: 0 0 30px;
  flex: 0 0 30px;
  text-align: center;
  max-width: 30px;
  border-radius: 50%;
  margin-right: 15px;
}
.single-timeline-area .single-timeline-content .timeline-icon i {
  color: #ffffff;
  line-height: 30px;
}
.single-timeline-area .single-timeline-content .timeline-text h6 {
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
}
.single-timeline-area .single-timeline-content .timeline-text p {
  font-size: 13px;
  margin-bottom: 0;
}
.single-timeline-area .single-timeline-content:hover .timeline-icon,
.single-timeline-area .single-timeline-content:focus .timeline-icon {
  background-color: #020710;
}
.single-timeline-area .single-timeline-content:hover .timeline-text h6,
.single-timeline-area .single-timeline-content:focus .timeline-text h6 {
  color: #3f43fd;
}
</style>