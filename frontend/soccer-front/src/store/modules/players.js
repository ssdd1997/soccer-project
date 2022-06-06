import axios from 'axios';

const state = {
    players: null,
    player : null
};

const getters = {
    statePlayers: state => state.players,
    statePlayer: state => state.player,
};

const actions = {
    async getPlayers({commit}) {
            let {data} = await axios.get('players')
            commit('setPlayers', data);

    },
    async viewPlayer({commit}, id) {
        console.log(id)
        let {data} = await axios.get(`players/${id}`);
        commit('setPlayer', data);
    },
};

const mutations = {
    setPlayers(state, players){
        state.players = players;
    },
    setPlayer(state, player){
        state.player = player;
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};
