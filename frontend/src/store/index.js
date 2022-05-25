import Vuex from "vuex";
import user from "./modules/user/index.js";
import chatbot from "./modules/chatbot/index.js";

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
  modules: { user, chatbot },
});
