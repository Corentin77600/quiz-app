<template>
  <div class="popup-mask">
    <div class="popup-wrapper">
      <div class="popup-container">
        <h2 class="text-center text-danger">Félicitations {{ username }}!<br />Le Quiz est terminé!</h2>

        <div class="card-body">
          <div class="text-center text-secondary">
            Vous avez eu
            <span class="text-danger">
              {{ nbreBonnesReponses }}
            </span> bonnes réponses sur
            <span class="text-danger">
              {{ nbreTotalQuestions }}
            </span>
            questions.
          </div>
        </div>

        <div class="btn-toolbar" style="justify-content: space-between;">
          <button class="btn btn-primary" @click="$emit('reload')">
            Rejouer
          </button>
          <button class="btn btn-danger" @click="$emit('close')">
            Quitter
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    nbreBonnesReponses:
    {
      type: Number
    },
    nbreTotalQuestions: {
      type: Number
    },
    username: {
      type: String
    }
  },
};
</script>

<style scoped>
.popup-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.popup-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.popup-container {
  width: 90vw;
  max-width: 650px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}
</style>