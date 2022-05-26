export default {
    namespaced: true,
    state: {
        coursePlan: null
    },
    getters: {
        get_coursePlan: state => {
            return state.course_plan;
        }
    },
    mutations: {
        set_coursePlan: (state, payload) => {
            state.course_plan = payload;
        }
    },
    actions: {
        SEND_MESSAGE: function ({ rootGetters }, payload) {
            let xhr = new XMLHttpRequest();
            let promise = new Promise((resolve, reject) => {
                xhr.open(
                    "POST",
                    rootGetters.endpoints("BASE") + rootGetters.endpoints("SEND_MESSAGE")
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
                xhr.send(JSON.stringify(payload));
            });

            promise.then(e => {
                console.log(e.response)
            })

            return promise;
        },
        GET_COURSE_PLAN: function ({ rootGetters, commit }) {
            let xhr = new XMLHttpRequest();
            let promise = new Promise((resolve, reject) => {
                xhr.open(
                    "POST",
                    rootGetters.endpoints("BASE") + rootGetters.endpoints("GET_COURSE_PLAN")
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

            promise.then(e => {
                commit("set_coursePlan", JSON.parse(e.responseText));
            })

            return promise;
        }


    }
};

