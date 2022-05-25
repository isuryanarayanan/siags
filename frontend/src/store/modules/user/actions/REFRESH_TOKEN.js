export default function({ rootGetters, getters }) {
  let xhr = new XMLHttpRequest();
  let promise = new Promise((resolve, reject) => {
    xhr.open(
      "POST",
      rootGetters.endpoints("BASE") + rootGetters.endpoints("REF_TOKEN")
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
    xhr.send(JSON.stringify({ refresh: getters["get_refreshToken"] }));
  });

  return promise;
}
