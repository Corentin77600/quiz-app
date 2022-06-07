<template>
  <p></p>
  <div class="card text-white bg-secondary mx-auto">
    <div class="card-header">
      <div class="row">
        <div class="col-6">
          <h5 class="card-title mt-3">Liste de questions:</h5>
        </div>
        <div class="col-6">
          <button type="button" class="btn btn-warning" style="float:right;"
            @click.prevent="clickDeconnexion">Déconnexion</button>
          <button type="button" class="btn btn-success" style="float:right;"
            @click.prevent="clickFormAjouter">Créer</button>
        </div>
      </div>
      <form id="montrer" class="card-header bg-dark rounded">
        <div class="form-row">
          <div class="form-group col-md-6">
            <label for="inputEmail4">Titre:</label>
            <input v-model="titre" type="text" class="form-control" id="inputTitre" placeholder="Titre">
          </div>
          <div class="form-group col-md-6">
            <label for="inputPassword4">Texte:</label>
            <input v-model="texte" type="text" class="form-control" id="inputTexte" placeholder="Texte">
          </div>
        </div>
        <div class="form-group">
          <label for="inputAddress">Image:</label>
          <input v-model="image" type="text" class="form-control" id="inputImage" placeholder="Image">
        </div>

        <!-- REPONSES 1, 2, 3 & 4 ! -->

        <div class="row">
          <div class="form-group col-md-3">
            <label for="inputZip">Réponse 1:</label>
            <input v-model="rep1" type="text" class="form-control" id="inputZip">
          </div>
          <div class="form-group col-md-3">
            <label for="inputZip">Réponse 2:</label>
            <input v-model="rep2" type="text" class="form-control" id="inputZip">
          </div>
          <div class="form-group col-md-3">
            <label for="inputZip">Réponse 3:</label>
            <input v-model="rep3" type="text" class="form-control" id="inputZip">
          </div>
          <div class="form-group col-md-3">
            <label for="inputZip">Réponse 4:</label>
            <input v-model="rep4" type="text" class="form-control" id="inputZip">
          </div>
        </div>
        <!-- FIN REPONSES 1, 2, 3 & 4 ! -->

        <!-- TRUE OR FALSE 1, 2, 3 & 4 ! -->
        <div class="row">
          <div class="form-group col-md-3">
            <label for="inputZip">Vrai ou Faux 1:</label>
            <input v-model="tof1" type="text" class="form-control" id="inputZip">
          </div>
          <div class="form-group col-md-3">
            <label for="inputZip">Vrai ou Faux 2:</label>
            <input v-model="tof2" type="text" class="form-control" id="inputZip">
          </div>
          <div class="form-group col-md-3">
            <label for="inputZip">Vrai ou Faux 3:</label>
            <input v-model="tof3" type="text" class="form-control" id="inputZip">
          </div>
          <div class="form-group col-md-3">
            <label for="inputZip">Vrai ou Faux 4:</label>
            <input v-model="tof4" type="text" class="form-control" id="inputZip">
          </div>
          <p></p>
          <p></p>
          <p class="text-center text-danger" v-if="montrer">Veuillez remplir tous les champs!</p>
          <p class="text-center text-success" v-if="success">Succès!</p>
          <div class="col text-center">
            <button type="submit" class="btn btn-success w-25" @click.prevent="clickAjouter">Valider</button>
          </div>
        </div>
        <!-- FIN TRUE OR FALSE 1, 2, 3 & 4 ! -->

      </form>
    </div>
    <div class="card-body">
      <div class="container" v-for="(question, index) in questions" :key="question.position">
        <div class="row">
          <div class="card text-white bg-dark mb-3 text-center">
            <div class="card-body text-center">
              <h5 class="card-title">
                Question N°{{ question.position }}: {{ question.text }}
                <br />-<br />
                {{ question.title }}
              </h5>
              <button type="button" class="btn btn-info w-25"
                @click.prevent="clickFormInfo(index, question.position)">Info</button>
              <button type="button" class="btn btn-warning w-25">Editer</button>
              <button type="button" class="btn btn-danger w-25"
                @click="clickSupprimer(question.position, index)">Supprimer</button>

              <!-- INFO FORM -->
              <p></p>
              <form class="card-header bg-secondary rounded">
                <div class="container">
                  <div>
                    <h5 class="font-weight-bold">Informations: </h5>
                  </div>
                  <div class="form-group row">
                    <label for="staticEmail"
                      class="col-sm-2 col-form-label border border-dark bg-dark rounded mb-2">Texte:</label>
                    <div class="col-sm-10">
                      <input type="text" readonly class="form-control-plaintext text-white" id="staticEmail"
                        :value="question.text">
                    </div>
                  </div>
                  <div class="form-group row">
                    <label for="staticEmail"
                      class="col-sm-2 col-form-label border border-dark bg-dark rounded mb-2">Titre:</label>
                    <div class="col-sm-10">
                      <input type="text" readonly class="form-control-plaintext text-white" id="staticEmail"
                        :value="question.title">
                    </div>
                  </div>
                  <div class="form-group row">
                    <label for="staticEmail"
                      class="col-sm-2 col-form-label border border-dark bg-dark rounded mb-2">Image:</label>
                    <div class="col-sm-10">
                      <input type="text" readonly class="form-control-plaintext text-white" id="staticEmail"
                        :value="question.image">
                    </div>
                  </div>
                  <!-- v-for="(answer, i) in possibleAnswers" -->
                  <div class="form-group row text-center" v-for="(simpleAnswer, i) in possibleAnswers[index].answers">
                    <label for="staticEmail"
                      class="col-sm-2 col-form-label border border-dark bg-dark rounded mb-2">Réponse
                      {{ i + 1 }} :</label>
                    <div class="col-sm-10">
                      <input type="text" readonly class="form-control-plaintext text-white" id="staticEmail"
                        :value="simpleAnswer.text + ' (' + simpleAnswer.isCorrect + ')'">
                    </div>
                  </div>
                </div>
              </form>
              <!-- FIN INFO FORM -->

              <!-- DEBUT FORM UPDATE -->
              <p></p>
              <form class="card-header bg-secondary rounded">
                <div class="container">
                  <div>
                    <h5 class="font-weight-bold">Editer: </h5>
                  </div>
                  <div class="form-row">
                    <div class="form-group col-md-6">
                      <label for="inputEmail4">Titre:</label>
                      <input v-model="uTitre" type="text" class="form-control" id="inputTitre">
                    </div>
                    <div class="form-group col-md-6">
                      <label for="inputPassword4">Texte:</label>
                      <input v-model="uTexte" type="text" class="form-control" id="inputTexte">
                    </div>
                  </div>
                  <div class="form-group">
                    <label for="inputAddress">Image:</label>
                    <input v-model="uImage" type="text" class="form-control" id="inputImage">
                  </div>

                  <!-- REPONSES 1, 2, 3 & 4 ! -->

                  <div class="row">
                    <div class="form-group col-md-3">
                      <label for="inputZip">Réponse 1:</label>
                      <input v-model="uRep1" type="text" class="form-control" id="inputZip">
                    </div>
                    <div class="form-group col-md-3">
                      <label for="inputZip">Réponse 2:</label>
                      <input v-model="uRep2" type="text" class="form-control" id="inputZip">
                    </div>
                    <div class="form-group col-md-3">
                      <label for="inputZip">Réponse 3:</label>
                      <input v-model="uRep3" type="text" class="form-control" id="inputZip">
                    </div>
                    <div class="form-group col-md-3">
                      <label for="inputZip">Réponse 4:</label>
                      <input v-model="uRep4" type="text" class="form-control" id="inputZip">
                    </div>
                  </div>
                  <!-- FIN REPONSES 1, 2, 3 & 4 ! -->

                  <!-- TRUE OR FALSE 1, 2, 3 & 4 ! -->
                  <div class="row">
                    <div class="form-group col-md-3">
                      <label for="inputZip">Vrai ou Faux 1:</label>
                      <input v-model="uTof1" type="text" class="form-control" id="inputZip">
                    </div>
                    <div class="form-group col-md-3">
                      <label for="inputZip">Vrai ou Faux 2:</label>
                      <input v-model="uTof2" type="text" class="form-control" id="inputZip">
                    </div>
                    <div class="form-group col-md-3">
                      <label for="inputZip">Vrai ou Faux 3:</label>
                      <input v-model="uTof3" type="text" class="form-control" id="inputZip">
                    </div>
                    <div class="form-group col-md-3">
                      <label for="inputZip">Vrai ou Faux 4:</label>
                      <input v-model="uTof4" type="text" class="form-control" id="inputZip">
                    </div>
                    <p></p>
                    <p></p>
                    <p class="text-center" v-if="uMontrer">Veuillez remplir tous les champs!</p>
                    <p class="text-center" v-if="uSuccess">Succès!</p>
                    <div class="col text-center">
                      <button type="submit" class="btn btn-success w-25"
                        @click.prevent="clickUpdate(question.position)">Valider</button>
                    </div>
                  </div>
                  <!-- FIN TRUE OR FALSE 1, 2, 3 & 4 ! -->
                </div>
              </form>
              <!-- FIN FORM UPDATE -->

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/quizApiService";
import axios from "axios";
import { isLogged, setLogged } from '../App.vue';

export default {
  data() {
    return {
      questions: [],
      possibleAnswers: [],
      nombreTotalDeQuestions: 0,

      titre: '',
      texte: '',
      image: '',
      rep1: '',
      rep2: '',
      rep3: '',
      rep4: '',
      tof1: 'True',
      tof2: 'False',
      tof3: 'False',
      tof4: 'False',

      uTitre: '',
      uTexte: '',
      uImage: '',
      uRep1: '',
      uRep2: '',
      uRep3: '',
      uRep4: '',
      uTof1: 'True',
      uTof2: 'False',
      uTof3: 'False',
      uTof4: 'False',

      reponsesPossibles: [],
      uReponsesPossibles: [],
      montrer: false,
      success: false,
      uSuccess: false,
      uMontrer: false,
    };
  },
  async created() {
    console.log("Composant Admin page 'created'");
    console.log("Connecté", isLogged);

    if (isLogged == false) {
      this.$router.push('/login');
    }

    if (isLogged == true) {
      this.$router.push('/admin');
    }

    quizApiService.getNbreQuestion().then((response) => {
      this.nombreTotalDeQuestions = response.data;

      for (let i = 1; i <= this.nombreTotalDeQuestions; i++) {
        quizApiService.getQuestion(i).then(rep =>
          this.questions.push(
            { title: rep.data.text, text: rep.data.title, position: rep.data.position, image: rep.data.image, possibleAnswers: rep.data.possibleAnswers }
          ))
        quizApiService.getAnswers(i).then((response) => {
          this.possibleAnswers.push(
            { answers: response.data.answer }
          )
        })
      }
    })
  },
  async update() {
    if (isLogged == false) {
      this.$router.push('/login');
    }

    if (isLogged == true) {
      this.$router.push('/admin');
    }
  },
  methods: {
    async clickSupprimer(position, index) {
      let finalIndex = index + 1;
      if (finalIndex == position) {
        this.questions.splice(index, 1);

        var headers = {
          "Content-Type": "application/json",
        };
        var token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTQ1MjYxODYsImlhdCI6MTY1NDUyMjU4Niwic3ViIjoicXVpei1hcHAtYWRtaW4ifQ.45UHjzUwYks4wzOMmW5G3KAnfMvOsTzyW9E_LEVCkus";
        headers.authorization = "Bearer " + token;
        await axios.delete(("http://localhost:5000/questions/").concat((position).toString()), { headers })
          .then(reponse => console.log("REPONSE API", reponse));

        this.$router.push('/admin');
      }
      else {
        console.log("ELSE", this.questions);
      }
    },
    async clickFormAjouter() {
      var montrer = document.getElementById("montrer");
      if (montrer.style.display === "block") {
        montrer.style.display = "none";
      } else {
        montrer.style.display = "block";
      }
    },
    async clickAjouter() {

      if ((this.titre === '' || this.titre === null || this.titre === 0) ||
        (this.texte === '' || this.texte === null || this.texte === 0) ||
        (this.image === '' || this.image === null || this.image === 0) ||
        (this.rep1 === '' || this.rep1 === null || this.rep1 === 0) ||
        (this.rep2 === '' || this.rep2 === null || this.rep2 === 0) ||
        (this.rep3 === '' || this.rep3 === null || this.rep3 === 0) ||
        (this.rep4 === '' || this.rep4 === null || this.rep4 === 0) ||
        (this.tof1 === '' || this.tof1 === null || this.tof1 === 0) ||
        (this.tof2 === '' || this.tof2 === null || this.tof2 === 0) ||
        (this.tof3 === '' || this.tof3 === null || this.tof3 === 0) ||
        (this.tof4 === '' || this.tof4 === null || this.tof4 === 0)) {
        this.montrer = true;
      }
      else {
        let setupReponses1 = {
          text: this.rep1,
          isCorrect: this.tof1
        };

        this.reponsesPossibles.push(setupReponses1);

        let setupReponses2 = {
          text: this.rep2,
          isCorrect: this.tof2
        };

        this.reponsesPossibles.push(setupReponses2);

        let setupReponses3 = {
          text: this.rep3,
          isCorrect: this.tof3
        };

        this.reponsesPossibles.push(setupReponses3);

        let setupReponses4 = {
          text: this.rep4,
          isCorrect: this.tof4
        };

        this.reponsesPossibles.push(setupReponses4);

        let newPosition = this.nombreTotalDeQuestions + 1;

        let payload = {
          text: this.texte,
          title: this.titre,
          image: this.image,
          position: newPosition,
          possibleAnswers: this.reponsesPossibles
        };

        var headers = {
          "Content-Type": "application/json",
        };
        var token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTQ1MjYxODYsImlhdCI6MTY1NDUyMjU4Niwic3ViIjoicXVpei1hcHAtYWRtaW4ifQ.45UHjzUwYks4wzOMmW5G3KAnfMvOsTzyW9E_LEVCkus";
        headers.authorization = "Bearer " + token;
        await axios.post("http://localhost:5000/questions", payload, { headers })
          .then(reponse => console.log("REPONSE API", reponse));

        this.success = true;
        setLogged(true);
        console.log(isLogged);
        this.$router.go();
      }
    },
    async clickUpdate(index) {

      if ((this.uTitre === '' || this.uTitre === null || this.uTitre === 0) ||
        (this.uTexte === '' || this.uTexte === null || this.uTexte === 0) ||
        (this.uImage === '' || this.uImage === null || this.uImage === 0) ||
        (this.uRep1 === '' || this.uRep1 === null || this.uRep1 === 0) ||
        (this.uRep2 === '' || this.uRep2 === null || this.uRep2 === 0) ||
        (this.uRep3 === '' || this.uRep3 === null || this.uRep3 === 0) ||
        (this.uRep4 === '' || this.uRep4 === null || this.uRep4 === 0) ||
        (this.uTof1 === '' || this.uTof1 === null || this.uTof1 === 0) ||
        (this.uTof2 === '' || this.uTof2 === null || this.uTof2 === 0) ||
        (this.uTof3 === '' || this.uTof3 === null || this.uTof3 === 0) ||
        (this.uTof4 === '' || this.uTof4 === null || this.uTof4 === 0)) {
        this.uMontrer = true;
      }
      else {
        let uSetupReponses1 = {
          text: this.uRep1,
          isCorrect: this.uTof1
        };

        this.uReponsesPossibles.push(uSetupReponses1);

        let uSetupReponses2 = {
          text: this.uRep2,
          isCorrect: this.uTof2
        };

        this.uReponsesPossibles.push(uSetupReponses2);

        let uSetupReponses3 = {
          text: this.uRep3,
          isCorrect: this.uTof3
        };

        this.uReponsesPossibles.push(uSetupReponses3);

        let uSetupReponses4 = {
          text: this.uRep4,
          isCorrect: this.uTof4
        };

        this.uReponsesPossibles.push(uSetupReponses4);

        let payload = {
          text: this.uTexte,
          title: this.uTitre,
          image: this.uImage,
          position: index,
          possibleAnswers: this.uReponsesPossibles
        };

        var headers = {
          "Content-Type": "application/json",
        };
        var token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTQ1MjYxODYsImlhdCI6MTY1NDUyMjU4Niwic3ViIjoicXVpei1hcHAtYWRtaW4ifQ.45UHjzUwYks4wzOMmW5G3KAnfMvOsTzyW9E_LEVCkus";
        headers.authorization = "Bearer " + token;
        await axios.put(("http://localhost:5000/questions/").concat((index).toString()), payload, { headers })
          .then(reponse => console.log("REPONSE API", reponse));

        this.uSuccess = true;
        setLogged(true);
        console.log(isLogged);
        this.$router.go();
      }
    },
    async clickDeconnexion() {
      setLogged(false);
      console.log(isLogged);
      this.$router.push('/login');
    }
    // async clickFormInfo(index, position) {
    //   var index1 = index + 1;
    //   if (position == index1) {
    //     var montrer2 = document.getElementById("montrer2");
    //     if (montrer2.style.display === "block") {
    //       montrer2.style.display = "none";
    //     } else {
    //       montrer2.style.display = "block";
    //     }
    //   }
    //   else {
    //     console.log("ELSE", index, position);
    //   }

    //   //console.log("INDEX Form Info", index);
    // },
  }
}
</script>

<style>
#montrer {
  display: none;
}

#montrer2 {
  display: none;
}
</style>