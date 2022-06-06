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

export default {
    data() {
        return {
            login: '',
            password: '',
            montrer: false,
        };
    },
    methods: {
        async clickSubmit() {
            var pseudo = this.login;
            var motdepasse = this.password;
            var loginApi;
            var passwordApi;
            // console.log(pseudo);
            // console.log(motdepasse);
            quizApiService.getLogin().then((responseLogin) => {
                loginApi = responseLogin.data;

                quizApiService.getPassword().then((responsePassword) => {
                    passwordApi = responsePassword.data;

                    if (loginApi == pseudo && passwordApi == motdepasse) {
                        console.log("REUSSITE");
                        this.$router.push('/admin');
                    }
                    else {
                        this.montrer = true;
                        console.log("1", loginApi);
                        console.log("2", pseudo);
                        console.log("3", passwordApi);
                        console.log("4", motdepasse);
                        console.log("ECHEC");
                    }

                })
            })




        }
    }

}
</script>

