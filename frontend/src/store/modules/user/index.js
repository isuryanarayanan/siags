import GET_JWT_TOKEN from "../user/actions/GET_JWT_TOKEN.js";
import VALIDATE_TOKEN from "../user/actions/VALIDATE_TOKEN.js";
import REFRESH_TOKEN from "../user/actions/REFRESH_TOKEN.js";
import REGISTER_USER from "../user/actions/REGISTER_USER.js";
import GET_USER from "../user/actions/GET_USER.js";
import LOGOUT from "./actions/LOGOUT.js";

export default {
  namespaced: true,
  state: {
    accessToken: localStorage.getItem("ACCTOKEN"),
    refreshToken: localStorage.getItem("REFTOKEN"),
    authenticated: false,
    user: {
      loaded: false,
      _ID: null,
      _USERNAME: null,
      _EMAIL: null,
      _MODE: null,
    }
  },
  getters: {
    get_authenticated: function (state) {
      return state.authenticated;
    },
    get_accessToken: function (state) {
      return state.accessToken;
    },
    get_refreshToken: function (state) {
      return state.refreshToken;
    },
    get_if_user_loaded: function (state) {
      return state.user.loaded;
    },
    get_user: function (state) {
      return state.user;
    }
  },
  mutations: {
    set_authenticated: function (state, st) {
      state.authenticated = st;
    },
    set_accessToken: function (state, token) {
      state.accessToken = token;
      localStorage.setItem("ACCTOKEN", token);
    },
    set_refreshToken: function (state, token) {
      state.refreshToken = token;
      localStorage.setItem("REFTOKEN", token);
    },
    set_user_if_loaded: function (state, st) {
      state.user.loaded = st.loaded;
      state.user._EMAIL = st._EMAIL;
      state.user._USERNAME = st._USERNAME;
      state.user._ID = st._ID;
      state.user._MODE = st._MODE
    }
  },
  actions: {
    GET_JWT_TOKEN,
    VALIDATE_TOKEN,
    REFRESH_TOKEN,
    REGISTER_USER,
    GET_USER,
    LOGOUT
  }
};
