<template>
  <div class="about">
    <h1>This is an about page</h1>

    <form>
      <div class="form-group">
        <label for="exampleInputEmail1">Saisissez votre nom:</label>
        <input type="text" v-model="username" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
      </div>
      <button type="submit" class="btn btn-danger" @click="launchNewQuiz">Submit</button>
    </form>
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
      username: ''
    };
  },
  methods: {
    launchNewQuiz() {
      // ...
      participationStorageService.savePlayerName(this.username);
      // ...
      //const playerName = participationStorageService.getPlayerName();
      //console.log("Launch new quiz with", playerName);
      this.$router.push('/questions');
    },
  }
}
</script>
