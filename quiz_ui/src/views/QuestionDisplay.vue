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

import quizApiService from "@/services/quizApiService";

export default {
  name: "Question",
  props: {
    question: {
      type: Object
    }
  },
  async created() {
    console.log("Composant Question 'created'");
    await quizApiService.getQuestion(1).then((response) => {
      this.question = question.text;
    })
  }
};
</script>
