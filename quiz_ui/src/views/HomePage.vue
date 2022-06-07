<template>
  <p></p>
  <div class="card text-white bg-secondary mb-3 ">
    <div class="card-body text-center">
      <h5 class="card-title">Bienvenue sur Quiz-App! <br /> Pour commencer un nouveau Quiz:</h5>
      <button type="submit" class="btn btn-danger w-25 h-25" @click.prevent="this.$router.push('/NewQuizPage')">Start
        !</button>
    </div>
  </div>

  <p></p>
  <div class="card text-center text-white bg-secondary mx-auto">
    <div class="card-header">
      <p class="card-text">Tableau des scores</p>
    </div>
    <div class="card-body">
      <div class="container" v-for="(participant, index) in this.registeredScores.scores"
        v-bind:key="participant.playerName">
        <div class="row" v-if="index < 10">
          <div class="card text-white bg-dark mb-3 text-center ">
            <div class="card-body text-center">
              <h5 class="card-title">{{ participant.playerName }} : {{ participant.score }}</h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import quizApiService from "@/services/quizApiService";

export default {
  data() {
    return {
      registeredScores: [],
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    await quizApiService.getQuizInfo().then((response) => {
      this.registeredScores = response.data;
    })

  }
};
</script>

<style>
</style>