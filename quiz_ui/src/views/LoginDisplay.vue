<template>
    <p></p>
    <form class="d-flex row align-items-center w-50 h-50 mx-auto my-auto">
        <div class="form-group">
            <label for="exampleInputEmail1">Identifiant</label>
            <input v-model="login" type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
                placeholder="Entre ton login">
        </div>
        <p></p>
        <div class="form-group">
            <label for="exampleInputPassword1">Mot De Passe</label>
            <input v-model="password" type="password" class="form-control" id="exampleInputPassword1"
                placeholder="Mot de passe">
        </div>
        <p></p>
        <p class="text-center text-danger" v-if="montrer">Mot de passe incorrect!</p>
        <div class="col text-center">
            <button type="submit" class="btn btn-dark w-25 h-25" @click.prevent="clickSubmit">Se connecter</button>
        </div>
    </form>
</template>

<script>
import quizApiService from "../services/quizApiService";
import { isLogged, setLogged } from '../App.vue';

export default {
    data() {
        return {
            login: '',
            password: '',
            montrer: false,
        };
    },
    async created() {

        if (isLogged == false) {
            this.$router.push('/login');
        }

        if (isLogged == true) {
            this.$router.push('/admin');
        }
    },
    methods: {
        async clickSubmit() {
            var pseudo = this.login;
            var motdepasse = this.password;
            var loginApi;
            var passwordApi;
            quizApiService.getLogin().then((responseLogin) => {
                loginApi = responseLogin.data;

                quizApiService.getPassword().then((responsePassword) => {
                    passwordApi = responsePassword.data;

                    if (loginApi == pseudo && passwordApi == motdepasse) {
                        setLogged(true);
                        console.log(isLogged);
                        this.$router.push('/admin');
                    }
                    else {
                        this.montrer = true;
                    }
                })
            })
        }
    }

}
</script>

