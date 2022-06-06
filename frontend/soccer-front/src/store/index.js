import createPersistedState from "vuex-persistedstate";
import Vue from 'vue';
import Vuex from 'vuex';

import players from './modules/players';
import users from './modules/users';


Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        players,
        users
    },
    plugins: [createPersistedState()]
});
