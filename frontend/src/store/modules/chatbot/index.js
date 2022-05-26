export default {
    namespaced: true,
    state: {
        messages: []
    },
    getters: {
        get_messages: state => state.messages
    },
    mutations: {
        add_message(state, message) {
            state.messages.push(message);
        }
    },
    actions: {
        TALK_TO_BOT: function ({ rootGetters, commit }, PAYLOAD) {
            let xhr = new XMLHttpRequest();
            let promise = new Promise((resolve, reject) => {
                xhr.open(
                    "POST",
                    rootGetters.endpoints("BASE") + rootGetters.endpoints("CHATBOT")
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
            return promise;
        }
    }
};
