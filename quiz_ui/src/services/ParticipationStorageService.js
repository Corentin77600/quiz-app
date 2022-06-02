export default {
  clear() {
    // todo : implement
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("playerName", playerName);
  },
  getPlayerName() {
    var player = window.localStorage.setItem("playerName", playerName);
    return player;
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem("Score", participationScore);
  },
  getParticipationScore() {
    var score = window.localStorage.setItem("Score", participationScore);
    return score;
  }
};