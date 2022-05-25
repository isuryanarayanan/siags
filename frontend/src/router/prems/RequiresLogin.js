import store from "../../store/index.js";

export default record => {
  var response = { satisfied: true, direct: null, index: 0 };
  if ("requiresLogin" in record.meta) {
    if (
      record.meta.requiresLogin &&
      store.getters["user/get_authenticated"] == false
    ) {
      response.satisfied = false;
      response.direct = "/get-started";
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
