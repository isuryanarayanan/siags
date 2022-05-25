export default function ({ rootGetters, commit }, PAYLOAD) {
  let xhr = new XMLHttpRequest();
  let promise = new Promise((resolve, reject) => {
    xhr.open(
      "POST",
      rootGetters.endpoints("BASE") + rootGetters.endpoints("GET_TOKEN")
    );
    xhr.setRequestHeader("Content-Type", "Application/json");
    xhr.onload = () => {
      resolve(xhr);
    };
    xhr.onerror = () => {
      reject(xhr);
    };
    xhr.send(JSON.stringify(PAYLOAD));
  });
  promise.then(data => {
    commit("set_accessToken", JSON.parse(data.response).access);
    commit("set_refreshToken", JSON.parse(data.response).refresh);
  });
  return promise;
}
