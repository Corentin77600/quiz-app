<template>
  <!-- <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1> -->
  <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
  <ScoreDisplay v-show="showPopUp" :username=currentUsername :nbreBonnesReponses=nombreBonnesReponses
    :nbreTotalQuestions=totalNumberOfQuestion @reload="updateQuiz" @close="closeQuiz" />
</template>

<script>
import quizApiService from "../services/quizApiService";
import participationStorageService from "../services/ParticipationStorageService";
import QuestionDisplay from "../views/QuestionDisplay.vue";
import ScoreDisplay from "../views/ScoreDisplay.vue";

export default {
  name: "QuestionsManager",
  components: {
    QuestionDisplay, ScoreDisplay
  },

  data() {
    return {
      currentQuestionPosition: 1,
      currentScore: 0,
      totalNumberOfQuestion: 100,
      currentQuestion: {},
      currentAnswer: [],
      currentUsername: '',
      nombreBonnesReponses: 0,
      showPopUp: false,
    };
  },

  created() {
    console.log("Composant QuestionsManager 'created'");
    this.currentUsername = participationStorageService.getPlayerName();
  },

  async beforeCreate() {
    let tempQuestion = await quizApiService.getQuestion(1);
    let tempQuizInfo = await quizApiService.getQuizInfo();

    this.totalNumberOfQuestion = tempQuizInfo.data.size;
    this.currentQuestion = tempQuestion.data;
  },
  uptated() {

  },
  methods: {
    async loadQuestionByPosition() {
      let tempQuestion = await quizApiService.getQuestion(
        this.currentQuestionPosition
      );

      this.currentQuestion = tempQuestion.data;
    },

    async endQuiz() {
      let payload = {
        playerName: participationStorageService.getPlayerName(),
        answers: this.currentAnswer,
      };
      console.log("payload : ", payload);
      //await quizApiService.postNewParticipation(payload);
      participationStorageService.saveParticipationScore(this.nombreBonnesReponses);
      this.showPopUp = true;
    },

    async answerClickedHandler(Answer, isCorrect, e, text) {
      this.currentAnswer.push(Answer);
      console.log(Answer);
      console.log(isCorrect);
      console.log(e);
      console.log(text);
      if (isCorrect) {
        this.currentScore += 1;
        this.nombreBonnesReponses += 1;

        e.classList.add("rightAnswer");
      } else {
        e.classList.add("wrongAnswer");

        // let cleanAnswer = e.innerHTML; // innerHTML is polluted with decoded HTML entities e.g ' from &#039;
        // /* Clear from pollution with ' */
        // let userAnswer = cleanAnswer.replace(/'/, "&#039;");
        // if (userAnswer != text) {
        //   e.classList.add("showRightAnswer");
        // }
      }
      if (this.currentQuestionPosition < this.totalNumberOfQuestion) {
        this.currentQuestionPosition += 1;
        this.loadQuestionByPosition();
      } else {
        participationStorageService.saveParticipationScore(this.currentScore)
        this.endQuiz();
      }
    },
    updateQuiz() {
      this.showPopUp = false;
      this.currentQuestionPosition = 1;
      this.nombreBonnesReponses = 0;
      window.location.reload();
    },
    closeQuiz() {
      this.showPopUp = false;
      this.currentQuestionPosition = 1;
      this.nombreBonnesReponses = 0;
      this.$router.push('/');
    },
  },
};
</script>

<style>
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