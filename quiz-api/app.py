from flask import Flask, request
from flask_cors import CORS
import function

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
CORS(app)

@app.route('/')
def hello_world():
    return function.hello_world()

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return function.GetQuizInfo()

@app.route('/login', methods=['POST'])
def wrongPassword():
    return function.wrongPassword(request)

@app.route('/questions', methods=['POST'])
def creerQuestion():
    return function.creerQuestion()

@app.route('/questions/<id>', methods=['DELETE'])
def deleteQuestion(id):
    return function.supprQuestion(id)

@app.route('/questions/<position>', methods=['GET'])
def getQuestionID(position):
    return function.getQuestionID(position)

@app.route('/questions/<id>', methods=['PUT'])
def updateQuestion(id):
    return function.updateQuestion(id)

@app.route('/participations', methods=['POST'])
def participation():
    return function.participation()

@app.route('/participations', methods=['DELETE'])
def deleteParticipation():
    return function.deleteParticipation()

@app.route('/questions', methods = ['GET'])
def getNumberOfQuestion():
    return function.getNumberQuestion()

@app.route('/login', methods = ['GET'])
def getLogin():
    return function.getLogin()

@app.route('/password', methods = ['GET'])
def getPassword():
    return function.getPassword()

@app.route('/answers/<position>', methods = ['GET'])
def getAnswers(position):
    return function.getAnswers(position)

if __name__ == "__main__":
    app.run()

