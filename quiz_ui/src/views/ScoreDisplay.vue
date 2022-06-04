<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
            <h2 class="text-center text-danger" >Félicitations! <br/>Le Quiz est terminé!</h2>

          <div class="modal-body">
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
            <button
              class="btn btn-primary"
              @click="$emit('reload')"
            >
              Play Again
            </button>
            <button
              class="btn btn-danger"
              @click="$emit('close')"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>

export default {
    props: {
    nbreBonnesReponses:
    {
        type:Number
    }, 
    nbreTotalQuestions:{
        type:Number
    }, 
  },
};
</script>

<style scoped>
.modal-mask {
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

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 90vw;
  max-width: 650px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}

.modal-header {
  text-align: center;
}

.modal-header h2 {
  color: rgb(0, 178, 72);
}

.modal-header h3 {
  color: rgb(0, 178, 72);
}

.modal-body {
  display: flex;
  flex-direction: column;
  margin: 20px 0;
  line-height: 3rem;
}

.modal-body > * {
  margin: 1rem 0;
  padding: 0.25rem 0.5rem;
}


/*
 Modal Transition
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.button-footer {
  padding: 1rem 2rem;
  background: linear-gradient(
    210deg,
    rgba(187, 0, 47, 0.8),
    rgba(245, 0, 87, 0.6)
  );
  border-radius: 7px;
  border: none;
}

.anchor-footer {
  color: black;
  text-decoration: none;
  cursor: default;
}

.button-footer:active,
.button-footer:focus {
  outline: none;
}

.button-footer:hover {
  transform: scale(1.02);
}

</style>