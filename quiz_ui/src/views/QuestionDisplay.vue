<template>
  <form>
    <div class="form-group">
      <label for="exampleInputEmail1">Question :</label>
    </div>

    <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
      <label class="form-check-label" for="defaultCheck1">
        Réponse A:
      </label>
    </div>
    <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
      <label class="form-check-label" for="defaultCheck1">
        Réponse B:
      </label>
    </div>
    <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
      <label class="form-check-label" for="defaultCheck1">
        Réponse C:
      </label>
    </div>
    <div class="form-check">
      <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
      <label class="form-check-label" for="defaultCheck1">
        Réponse D:
      </label>
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>
  </form>

  <div>
    <div class="card mt-2 mb-2">
      <div class="card-body" v-for="question in questions" :key="question.position">
        <h4 class="card-title">{{ question.title }}</h4>
        <p class="card-text">{{ question.text }}</p>
        <div class="d-flex justify-content-between">
          <!-- <button class="btn btn-info text-white" @click="editQuestion(question.id)">
            Edit
          </button>
          <button class="btn btn-danger" @click="deleteQuestion(question.id)">
            Delete
          </button> -->
        </div>
      </div>
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

import quizApiService from "../services/quizApiService";
import axios from 'axios';
// v-for="question in questions" v-bind:key="question.id"
export default {

  data() {
    return {
      questions: [],
    };
  },
  async created() {
    quizApiService.getQuestion(position).then((response) => {
      this.questions = response.data
      console.log(this.questions)
    })
  },
};
</script>
