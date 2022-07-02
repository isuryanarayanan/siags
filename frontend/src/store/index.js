import Vuex from "vuex";
import user from "./modules/user/index.js";
import chatbot from "./modules/chatbot/index.js";
import course from "./modules/course/index.js";
import assignment from "./modules/assignment/index.js";

export default new Vuex.Store({
  state: {
    endpoints: {
      /* base url for the backend server */
      BASE: "http://127.0.0.1:8000/",
      /* authentication endpoints */
      GET_TOKEN: "accounts/api/token/", // endpoint to get the token
      REF_TOKEN: "accounts/api/token/refresh/", // endpoint to refresh the active access token
      VAL_TOKEN: "accounts/api/token/validate/", // endpoint to validate the active access token
      /* authorization endpoints */
      GET_USER: "accounts/api/v1/get_user/", //endpoint to get user details
      /* create user */
      REG_USER: "accounts/api/v1/create_user/",
      /* chatbot api */
      CHATBOT: "chatbot/simple_chatbot/",
      /* course module api */
      GET_COURSE_PLAN: "academy/api/v1/get_course_plan/",
      CREATE_COURSE_PLAN: "academy/api/v1/create_course_plan/",
      CREATE_SEMESTER: "academy/api/v1/create_semester/",
      SEND_MESSAGE: "academy/api/v1/send_message/",
      GET_MESSAGES: "academy/api/v1/get_messages/",
      GET_BATCHES: "academy/api/v1/get_batch/",
      GET_COURSES: "academy/api/v1/get_courses/",
      /* assignments api */
      GET_ASSIGNMENTS: "assignments/api/v1/get_assignments/",
      SUBMIT_ASSIGNMENT: "assignments/api/v1/submit_assignment/",
    },
  },
  getters: {
    endpoints: (state) => {
      return (key) => {
        return state.endpoints[key];
      };
    },
  },
  mutations: {},
  actions: {},
  modules: { user, chatbot, course, assignment },
});
