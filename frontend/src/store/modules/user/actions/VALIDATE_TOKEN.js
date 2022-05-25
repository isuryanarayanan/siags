export default function({ rootGetters, getters }) {
  let xhr = new XMLHttpRequest();
  let promise = new Promise((resolve, reject) => {
    xhr.open(
      "GET",
      rootGetters.endpoints("BASE") + rootGetters.endpoints("VAL_TOKEN")
    );
    xhr.setRequestHeader("Content-Type", "Application/json");
    xhr.setRequestHeader(
      "Authorization",
      "Bearer " + getters["get_accessToken"]
    );
    xhr.onload = () => {
      resolve(xhr);
    };
    xhr.onerror = () => {
      reject(xhr);
    };
    xhr.send();
  });
  return promise;
}
