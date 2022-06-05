import axios from 'axios';

const state = {
    players: null
};

const getters = {
    statePlayers: state => state.players,
};

const actions = {
    async getPlayers({commit}) {
        let {data} = await axios.get('players');
        commit('setPlayers', data);
    }
};

const mutations = {
    setPlayers(state, players){
        state.players = players;
    }
};

export default {
    state,
    getters,
    actions,
    mutations
};
