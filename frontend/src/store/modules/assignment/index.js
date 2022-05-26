export default {
    namespaced: true,
    state: {
    },
    getters: {
    },
    mutations: {
    },
    actions: {
        SUBMIT_ASSIGNMENT: ({ rootGetters }, payload) => {
            let xhr = new XMLHttpRequest();
            let promise = new Promise((resolve, reject) => {
                xhr.open(
                    "POST",
                    rootGetters.endpoints("BASE") + rootGetters.endpoints("SUBMIT_ASSIGNMENT")
                );
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
                // send form data payload
                xhr.send(payload);

            });
            return promise;
        },

        GET_ASSIGNMENTS: function ({ rootGetters },) {
            let xhr = new XMLHttpRequest();
            let promise = new Promise((resolve, reject) => {
                xhr.open(
                    "POST",
                    rootGetters.endpoints("BASE") + rootGetters.endpoints("GET_ASSIGNMENTS")
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
            return promise;
        }
    }
};
