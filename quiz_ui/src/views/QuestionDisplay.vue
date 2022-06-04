<template>
  <div class="card text-center text-white bg-secondary mx-auto">
    <div class="card-header">
    <p class="card-text">Question N°{{ questions.position }}</p>
    </div>
    <div class="card-body">
      <h5 class="card-title">{{ questions.title }}</h5>
      <p class="card-text">{{ questions.text }}</p>
      <img class="rounded mx-auto d-bloc" style="margin-bottom: 10px;" v-if="questions.image" :src="questions.image" />
      <form v-if="questions">
        <button v-for="(answer, index) in questions.possibleAnswers" @click.prevent="answerClickedHandler" class="text-white">{{
            answer.text
        }} </button>
      </form>
    </div>
    <div class="card-footer text-muted">
    </div>
  </div>

    <ScoreDisplay
      v-show="showPopUp"
      :nbreBonnesReponses= nombreBonnesReponses
      :nbreTotalQuestions= nombreTotalDeQuestions
      @reload="updateQuiz"
      @close="closeQuiz"
    />

</template>

<script>

import quizApiService from "../services/quizApiService";
import ScoreDisplay from "../views/ScoreDisplay.vue";

var position = 1;
var bonneReponse = 0;
var mauvaiseReponse = 0;
var nbreQuestions = 1;
export default {
  /*props: {
    questions: 
    {
      type: Object,
    },
    nombreTotal: Number,
  },*/
  components: { ScoreDisplay },
  data() {
    return {
      questions: [],
      nombreTotal: 0,
      nombreBonnesReponses:0,
      nombreMauvaisesReponses:0,
      nombreTotalDeQuestions:0,
      showPopUp: false,
    };
  },
  async created() {
    quizApiService.getQuestion(position).then((response) => {
      this.questions = response.data;
      console.log(this.questions);
      //console.log(this.questions.position)
      //console.log(this.questions.title)
      //console.log(this.questions.possibleAnswers[0].isCorrect)
    })
  },
  async updated() {
    this.nombreTotal = position;
    this.nombreBonnesReponses = bonneReponse;
    this.nombreMauvaisesReponses = mauvaiseReponse;
  },
  methods: {
    async answerClickedHandler(e) {
      let index = e.currentTarget;
      let pollutedUserAnswer = e.target.innerHTML; // innerHTML is polluted with decoded HTML entities e.g ' from &#039;
      /* Clear from pollution with ' */
      let userAnswer = pollutedUserAnswer.replace(/'/, "&#039;");
      //set answer
      this.questions.possibleAnswers[index] = userAnswer;
      let allButtons = document.querySelectorAll(`[index="${index}"]`);

      for (let i = 0; i < allButtons.length; i++) {
        if (allButtons[i] === e.target) continue;

        allButtons[i].setAttribute("disabled", "");
      }
      this.checkCorrectAnswer(e, index);
      position = position + 1;
      this.loadQuestionByPosition(e,position);
    },

    async loadQuestionByPosition(e,position)
    {
      var curPosition = this.questions.position + 1;
      quizApiService.getNbreQuestion().then((response) => {
        if(curPosition > response.data) {
            this.showPopUp=true;
            this.nombreTotalDeQuestions = response.data;
            console.log(response.data);
        }
        else
        {
          quizApiService.getQuestion(position).then((rep) => {
            this.questions = rep.data;
            e.target.classList.remove("rightAnswer");
            e.target.classList.remove("wrongAnswer");
          })
        }
      })
    },

    // async getIdRep() {
    //   var idRep = 0;
    //   const bonneReponse = "";
    //   for (var i = 0; i <= this.questions.possibleAnswers.length; i++) {
    //     if (this.questions.possibleAnswers[i].isCorrect == true) {
    //       idRep = i;
    //       break;
    //     }
    //   }
    //   console.log(this.questions.possibleAnswers[idRep].text);
    //   return this.questions.possibleAnswers[idRep].text;
    // },

    async checkCorrectAnswer(e, index) {
      let question = this.questions.possibleAnswers[index];
      var idRep = 0;

      for (var i = 0; i <= this.questions.possibleAnswers.length; i++) {
        if (this.questions.possibleAnswers[i].isCorrect == true) {
          idRep = i;
          break;
        }
      }

      if (question != null) {
        if (this.index < this.questions.possibleAnswers.length - 1) {
          setTimeout(
            function () {
              this.index += 1;
            }.bind(this),
            3000
          );
        }

        if (this.questions.possibleAnswers[index] === this.questions.possibleAnswers[idRep].text) {
          e.target.classList.add("rightAnswer");
          bonneReponse = bonneReponse + 1;
        }

        else {
          e.target.classList.add("wrongAnswer");
          let correctAnswer = this.questions.possibleAnswers[idRep].text;
          let allButtons = document.querySelectorAll(`[index="${index}"]`);
          allButtons.forEach(function (button) {
            if (button.innerHTML === correctAnswer) {
              button.classList.add("showRightAnswer");
            }
          });
          mauvaiseReponse = mauvaiseReponse + 1;
        }
      }
      nbreQuestions = bonneReponse + mauvaiseReponse;
    },
    updateQuiz() {
      this.showPopUp = false;
      position=1;
      bonneReponse=0;
      mauvaiseReponse=0;
      window.location.reload();
    },
    closeQuiz() {
      this.showPopUp = false;
      position=1;
      bonneReponse=0;
      mauvaiseReponse=0;
      this.$router.push('/');
    },
  },
};
</script>

<style>
form {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
}

button {
  font-size: 1.1rem;
  box-sizing: border-box;
  padding: 1rem;
  margin: 0.5rem;
  width: 40%;
  background-color: rgba(100, 100, 100, 0.3);
  border: none;
  border-radius: 0.4rem;
  box-shadow: 3px 5px 5px rgba(0, 0, 0, 0.2);
}

button:hover:enabled {
  transform: scale(1.02);
  box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.14), 0 1px 7px 0 rgba(0, 0, 0, 0.12),
    0 3px 1px -1px rgba(0, 0, 0, 0.2);
  cursor: pointer;
}

button:focus {
  outline: none;
}

button:active:enabled {
  transform: scale(1.05);
}

@keyframes flashButton {
  0% {
    opacity: 1;
    transform: scale(1.01);
  }

  50% {
    opacity: 0.7;
    transform: scale(1.02);
  }

  100% {
    opacity: 1;
    transform: scale(1);
  }
}

button.rightAnswer {
  animation: flashButton;
  animation-duration: 700ms;
  animation-delay: 200ms;
  animation-iteration-count: 3;
  animation-timing-function: ease-in-out;
  color: black;
  background: linear-gradient(210deg,
      rgba(0, 178, 72, 0.25),
      rgba(0, 178, 72, 0.5));
}

button.wrongAnswer {
  color: black;
  background: linear-gradient(210deg,
      rgba(245, 0, 87, 0.25),
      rgba(245, 0, 87, 0.5));
}

button.showRightAnswer {
  animation: flashButton;
  animation-duration: 700ms;
  animation-delay: 200ms;
  animation-iteration-count: 2;
  animation-timing-function: ease-in-out;
  color: black;
  background: linear-gradient(210deg,
      rgba(0, 178, 72, 0.25),
      rgba(0, 178, 72, 0.5));
}
</style>