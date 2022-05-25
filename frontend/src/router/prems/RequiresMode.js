import store from "../../store/index.js";

export default record => {
  var response = { satisfied: true, direct: null, index: 1 };
  if ("requiresMode" in record.meta) {
    if (
      record.meta.requiresMode.require &&
      store.getters["user/get_mode"] == record.meta.requiresMode.mode
    ) {
      response.satisfied = false;
      response.direct = "/get-farted";
      return response;
    } else {
      response.satisfied = true;
      response.direct = null;
      return response;
    }
  } else {
    return response;
  }
};
