
const state = {
    user: null,
};
const user = JSON.parse(localStorage.getItem('user'));
const initialState = user
    ? {  isAuthorized: true , user}
    : { isAuthorized: false , user: null };

const getters = {
    // eslint-disable-next-line no-unused-vars
    stateUser: state => initialState
};

const actions = {
    // eslint-disable-next-line no-empty-pattern
    // eslint-disable-next-line no-unused-vars
    async logIn({commit}, gAuth) {
        const authCode = await gAuth.getAuthCode()
        if(authCode){
            const gAuthUser = {isAuthorized: gAuth.isAuthorized, authToken: authCode}
            localStorage.setItem('user', JSON.stringify(gAuthUser));
        }
        console.log(gAuth.GoogleAuth.isAuthorized)

    },

    async logOut({commit}, gAuth) {
        gAuth.signOut();
        let user = null;
        commit('logout', user);
    }
};

const mutations = {
    setUser(state, gAuth) {
        state.user = gAuth;
    },
    logout(state, user){
        state.user = user;
        localStorage.removeItem('user');
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};
