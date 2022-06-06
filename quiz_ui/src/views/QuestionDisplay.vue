<template>

  <div class="card text-center text-white bg-secondary mx-auto">
    <div class="card-header">
      <p class="card-text">Question N°{{ question.position }}</p>
    </div>
    <div class="card-body">
      <h5 class="card-title">{{ question.title }}</h5>
      <p class="card-text">{{ question.text }}</p>
      <img class="rounded mx-auto d-bloc w-50 h-50" style="margin-bottom: 10px;" v-if="question.image"
        :src="question.image" />
      <div class="container" v-for="(answer, index) in this.question.possibleAnswers" v-bind:key="answer.text">
        <div class="row">
          <div class="col mx-auto my-1"><button id="reponse"
              class="btn text-dark border border-dark rounded w-100 h-100 mx-auto my-2"
              style="background-color: #B6D3EE;" :disabled="desactiver"
              @click="$emit('answer-selected', index, answer.isCorrect, $event.target, answer.text)">
              {{ answer.text }}
            </button></div>
        </div>
      </div>
    </div>
    <div class="card-footer text-muted">
    </div>
  </div>
</template>

<script>
export default {
  name: "QuestionDisplay",
  emits: ["answer-selected"],

  data() {
    return {
      index: 0,
    };
  },

  async created() {
    console.log("Composant QuestionsDisplay 'created'");
  },
  methods: {},
  props: {
    question: {
      type: Object,
    },
    desactiver: {
      type: Boolean,
    }
  },
};
</script>

<style>
</style> 