export default function({ rootGetters }, payload) {
  let xhr = new XMLHttpRequest();
  let promise = new Promise((resolve, reject) => {
    xhr.open(
      "POST",
      rootGetters.endpoints("BASE") + rootGetters.endpoints("REG_USER")
    );
    xhr.setRequestHeader("Content-Type", "Application/json");
    xhr.onload = () => {
      resolve(xhr);
    };
    xhr.onerror = () => {
      reject(xhr);
    };
    xhr.send(JSON.stringify(payload));
  });

  return promise;
}
