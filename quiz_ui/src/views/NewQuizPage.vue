<template>
  <p></p>
  <div class="card text-white bg-secondary mb-3 ">
    <div class="card-body text-center">
      <form class="d-flex row align-items-center w-50 h-50 mx-auto my-auto">
        <div class="form-group">
          <label for="exampleInputEmail1">Saisissez votre nom:</label>
          <input type="text" v-model="username" class="form-control" id="exampleInputEmail1"
            aria-describedby="emailHelp">
        </div>
        <p></p>
        <p class="text-center text-white" v-if="montrer">Veuillez remplir le champ ci-dessus!</p>
        <div class="col text-center">
          <button type="submit" class="btn btn-danger w-25 h-25" @click.prevent="launchNewQuiz">Go !</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

<script>
import participationStorageService from "../services/ParticipationStorageService";

export default {
  data() {
    return {
      username: '',
      montrer: false
    };
  },
  methods: {
    launchNewQuiz() {
      if (this.username === '' || this.username === null || this.username.value === 0) {
        this.montrer = true;
      }
      else {
        participationStorageService.savePlayerName(this.username);
        this.$router.push('/questions');
      }
    },
  }
}
</script>
