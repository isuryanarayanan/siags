export default {
  namespaced: true,
  state: {
    course_plan: null,
    batches: null,
    selected_student: null,
    courses: null,
  },
  getters: {
    get_coursePlan: (state) => {
      return state.course_plan;
    },
    get_batches: (state) => {
      return state.batches;
    },
    get_selected_student: (state) => {
      return state.selected_student;
    },
    get_courses: (state) => {
      return state.courses;
    },
  },
  mutations: {
    set_coursePlan: (state, payload) => {
      state.course_plan = payload;
    },
    set_batches: (state, payload) => {
      state.batches = payload;
    },
    select_student: (state, payload) => {
      state.selected_student = payload;
    },
    set_courses: (state, payload) => {
      state.courses = payload;
    },
  },
  actions: {
    SEND_MESSAGE: function ({ rootGetters, commit }, payload) {
      let xhr = new XMLHttpRequest();
      let promise = new Promise((resolve, reject) => {
        xhr.open(
          "POST",
          rootGetters.endpoints("BASE") + rootGetters.endpoints("SEND_MESSAGE")
        );
        xhr.setRequestHeader("Content-Type", "Application/json");
        xhr.setRequestHeader(
          "Authorization",
          "Bearer " + rootGetters["user/get_accessToken"]
        );
        xhr.onload = () => {
          resolve(xhr);
        };
        xhr.onerror = () => {
          reject(xhr);
        };
        xhr.send(JSON.stringify(payload));
      });

      promise.then((e) => {
        console.log(e.response);
      });

      return promise;
    },
    CREATE_COURSE_PLAN: function ({ rootGetters, commit }, payload) {
      let xhr = new XMLHttpRequest();
      let promise = new Promise((resolve, reject) => {
        xhr.open(
          "POST",
          rootGetters.endpoints("BASE") +
            rootGetters.endpoints("CREATE_COURSE_PLAN")
        );
        xhr.setRequestHeader("Content-Type", "Application/json");
        xhr.setRequestHeader(
          "Authorization",
          "Bearer " + rootGetters["user/get_accessToken"]
        );
        xhr.onload = () => {
          resolve(xhr);
        };
        xhr.onerror = () => {
          reject(xhr);
        };
        xhr.send(JSON.stringify(payload));
      });
      promise.then((e) => {
        console.log(e.response);
      });
      return promise;
    },

    GET_COURSE_PLAN: function (
      { rootGetters, commit, getters },
      payload = null
    ) {
      let xhr = new XMLHttpRequest();
      let promise = new Promise((resolve, reject) => {
        xhr.open(
          "POST",
          rootGetters.endpoints("BASE") +
            rootGetters.endpoints("GET_COURSE_PLAN")
        );
        xhr.setRequestHeader("Content-Type", "Application/json");
        xhr.setRequestHeader(
          "Authorization",
          "Bearer " + rootGetters["user/get_accessToken"]
        );
        xhr.onload = () => {
          resolve(xhr);
        };
        xhr.onerror = () => {
          reject(xhr);
        };
        // if payload then send payload
        if (payload) {
          xhr.send(JSON.stringify({ student: payload }));
        } else {
          xhr.send();
        }
      });

      promise.then((e) => {
        if (e.status == 200) {
          commit("set_coursePlan", JSON.parse(e.responseText));
        } else {
          commit("set_coursePlan", null);
          // update selected_student with course_plan as null
          var selected_student = getters.get_selected_student;
          selected_student.course_plan = null;
          commit("set_selected_student", selected_student);
        }
      });

      return promise;
    },
    GET_BATCHES: function ({ rootGetters, commit }) {
      let xhr = new XMLHttpRequest();
      let promise = new Promise((resolve, reject) => {
        xhr.open(
          "GET",
          rootGetters.endpoints("BASE") + rootGetters.endpoints("GET_BATCHES")
        );
        xhr.setRequestHeader("Content-Type", "Application/json");
        xhr.setRequestHeader(
          "Authorization",
          "Bearer " + rootGetters["user/get_accessToken"]
        );
        xhr.onload = () => {
          resolve(xhr);
        };
        xhr.onerror = () => {
          reject(xhr);
        };
        xhr.send();
      });
      promise.then((e) => {
        if (e.status === 200) {
          commit("set_batches", JSON.parse(e.response).batch_list);
        } else {
          commit("set_batches", null);
        }
      });
      return promise;
    },
    SELECT_STUDENT: function ({ commit, dispatch }, payload) {
      commit("select_student", payload);

      dispatch("GET_COURSE_PLAN", payload.id).then((e) => {
        payload.course_plan = JSON.parse(e.responseText);
        commit("select_student", payload);
      });
    },
    GET_COURSES: function ({ rootGetters, commit }, payload) {
      let xhr = new XMLHttpRequest();
      let promise = new Promise((resolve, reject) => {
        xhr.open(
          "POST",
          rootGetters.endpoints("BASE") + rootGetters.endpoints("GET_COURSES")
        );
        xhr.setRequestHeader("Content-Type", "Application/json");
        xhr.setRequestHeader(
          "Authorization",
          "Bearer " + rootGetters["user/get_accessToken"]
        );
        xhr.onload = () => {
          resolve(xhr);
        };
        xhr.onerror = () => {
          reject(xhr);
        };
        // if payload send payload
        if (payload) {
          xhr.send(JSON.stringify({ course: payload }));
        } else {
          xhr.send();
        }
      });
      promise.then((e) => {
        if (e.status === 200) {
          commit("set_courses", JSON.parse(e.response).course_list);
        } else {
          commit("set_courses", null);
        }
      });
      return promise;
    },
    CREATE_SEMESTER: function ({ rootGetters, commit }, payload) {
      let xhr = new XMLHttpRequest();
      let promise = new Promise((resolve, reject) => {
        xhr.open(
          "POST",
          rootGetters.endpoints("BASE") +
            rootGetters.endpoints("CREATE_SEMESTER")
        );
        xhr.setRequestHeader("Content-Type", "Application/json");
        xhr.setRequestHeader(
          "Authorization",
          "Bearer " + rootGetters["user/get_accessToken"]
        );
        xhr.onload = () => {
          resolve(xhr);
        };
        xhr.onerror = () => {
          reject(xhr);
        };
        xhr.send(JSON.stringify(payload));
      });
      promise.then((e) => {
        console.log(e.response);
      });
      return promise;
    },
  },
};
