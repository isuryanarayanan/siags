<script>
const getFormData = (object) =>
  Object.keys(object).reduce((formData, key) => {
    formData.append(key, object[key]);
    return formData;
  }, new FormData());
export default {
  data() {
    return {
      assignments: [],
      selectedFile: null,
    };
  },
  methods: {
    submit: function () {
      console.log(this.selectedFile);
      const formData = new FormData();
      formData.append("file", this.selectedFile);

      this.$store
        .dispatch("assignment/SUBMIT_ASSIGNMENT", getFormData(formData))
        .then((e) => {
          console.log(e.response);
        });
    },
    onFileSelected: function (event) {
      this.selectedFile = event.target.files[0];
    },
    getTimeLeft: function (due_time) {
      var now = new Date();
      var due = new Date(due_time);
      var timeLeft = due - now;
      return timeLeft;
    },
    getTimeLeftInWords: function (due_time) {
      var timeLeft = this.getTimeLeft(due_time);
      var days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
      var hours = Math.floor(
        (timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
      );
      var minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);
      // if time is over then return expired
      if (timeLeft < 0) {
        return "Expired";
      }
      return (
        days +
        " days, " +
        hours +
        " hours, " +
        minutes +
        " minutes, " +
        seconds +
        " seconds"
      );
    },
  },
  mounted() {
    this.$store.dispatch("assignment/GET_ASSIGNMENTS").then((e) => {
      this.assignments = JSON.parse(e.response);
    });
  },
};
</script>
<template>
  <div class="assignments-wrapper row">
    <div class="assignments-list col-sm-12">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Title</th>
            <th scope="col">Description</th>
            <th scope="col">Due</th>
            <th scope="col">By</th>
            <th scope="col">Attempt</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(assignment, index) in assignments.assignments"
            :key="index"
          >
            <th scope="row">{{ index + 1 }}</th>
            <td>{{ assignment.title }}</td>
            <td>{{ assignment.description }}</td>
            <td>{{ getTimeLeftInWords(assignment.due_date) }}</td>
            <td>{{ assignment.owner }}</td>
            <td>
              <div class="">
                <input type="file" @change="onFileSelected" />
                <div class="btn btn-primary" @click="submit()">submit</div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="assignments-detail col-sm-6"></div>
  </div>
</template>