from flask import Flask, request
from db_controller import db_controller
import jwt_utils
from question import Question
from reponse import Reponse
from participants import Participants

def hello_world():
	x = 'world'
	return f"Hello, {x}"

def GetQuizInfo():
    try:
        database = db_controller()
        number = database.getNumberOfQuestion()
        score = database.getNumberOfParticipation()
        participants = []
        if score == 0:
            participants = []
        else:
            #trie par ordre décroissant
            partTrie = database.orderByScore()
            print(partTrie)
            for part in partTrie:
                participants.append({
                    'playerName': part[0],
                    'score': part[1]
                })
        jsonQuiz = {
            "size": number,
            "scores": participants
        }
        
        return jsonQuiz, 200
    except Exception as e:
        print(e)
        return '', 401

def wrongPassword(request):
    payload = request.get_json()
    if payload["password"] == "Vive l'ESIEE !":
        return {"token":jwt_utils.build_token()}, 200
    return '', 401

def creerQuestion():
    token = request.headers.get('Authorization')

    try:
        if token:
            payload = request.get_json()
            qst = Question(payload['title'],payload['text'], payload['image'], payload['position'], payload['possibleAnswers'])
            database = db_controller()
            database.insertQuestion(qst)
            reponses = payload['possibleAnswers']

            for rep in reponses: 
                rep = Reponse(qst.id, rep['text'], rep['isCorrect'])
                database.insertAnswer(rep)
            return '', 200
        else:
             return '', 401
    except Exception as e:
        print(e)
        return '', 401


def supprQuestion(id):
    token = request.headers.get('Authorization')
    try:
        if token:
            if existQuestion(id) == 0:
                return '',404
            database = db_controller()
            idToDelete = database.deleteQuestion(id)
            database.deleteAnswer(idToDelete)
            return '', 204
        else:
            return '', 401
    except Exception as e:
        print(e)
        return '', 401

def existQuestion(position):
    database = db_controller()
    return database.existQuestion(position)
    

def getQuestionID(position):
    try:
        if existQuestion(position) == 0:
            return '',404
        database = db_controller()
        qst = database.getQuestion(position)
        return qst, 200

    except Exception as e:
        return '', 401
    

def updateQuestion(id):
    try:
        if existQuestion(id) == 0:
            return '',404
    
    except Exception as e:
        print(e)
        return '', 401
    token = request.headers.get('Authorization')

    try:
        if token:
            payload = request.get_json()
            database = db_controller()
            title = payload['title']
            text = payload['text']
            image = payload['image']
            position = payload['position']
            reponses = payload['possibleAnswers']
            length =len(payload['possibleAnswers'])
            print(reponses)
            qst = Question(title, text,image, position, reponses)
            database.updateQuestion(id, qst, length)
            return '', 200
    except Exception as e:
        print(e)
        return '', 401


def participation():
    try:
        payload = request.get_json()
        name = payload['playerName']
        score = getScore(payload['answers'])
        if(score!= -1):
            participant = Participants(name, score)
            database = db_controller()
            if database.checkExistParticipant(name) > 0:
                database.updateParticipation(participant)
            else:
                database.insertParticipant(participant)
            return {"playerName": name, "score": score}, 200
        else:
            return '', 400
    except Exception as e:
        print(e)
        return '', 401


def getScore(answers):
    score = 0
    database = db_controller()
    number = database.getNumberOfQuestion()
    if((len(answers) != number) or (number == 0)):
        return -1
    else:
        for i in range(0, number):
            if(answers[i]== getGoodAnswerAtIndex(number, i)):
                score = score+1
    print(score)
    return score

def getGoodAnswerAtIndex(number, i):
    database = db_controller()
    tabAnsw = database.getGoodAnswer(number)
    return tabAnsw[i]

def deleteParticipation():
    try:
        database = db_controller()
        database.deleteParticipant()
        return '', 204  
    except Exception as e:
        print(e)
        return '', 401

def getNumberQuestion():
    try:
        database = db_controller()
        number = database.getNumberOfQuestion()
        return str(number), 200
    except Exception as e:
        print(e)
        return '', 401

def getLogin():
    try:
        database = db_controller()
        login = database.getLogin()
        return str(login), 200
    except Exception as e:
        print(e)
        return '', 401

def getPassword():
    try:
        database = db_controller()
        password = database.getPassword()
        return str(password), 200
    except Exception as e:
        print(e)
        return '', 401

def getAnswers(position):
    try:
        database = db_controller()
        answers = database.getAllAnswers(position)
        return answers, 200
    except Exception as e:
        print(e)
        return '', 401