from flask import Flask, request
from db_controller import db_controller
import jwt_utils
import json
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
        return {"size": number, "scores": [1,2,3]}, 200
    except:
        return '', 401
	# return {"size": 2, "scores": [1,2,3]}, 200

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
    except:
        return '', 401


def supprQuestion(id):
    token = request.headers.get('Authorization')
    

    if token:
        if existQuestion(id) == 0:
            return '',404
        database = db_controller()
        idToDelete = database.deleteQuestion(id)
        database.deleteAnswer(idToDelete)
        return '', 204

    return '', 401

def existQuestion(id):
    database = db_controller()
    return database.existQuestion(id)
    

def getQuestionID(id):

    try:
        if existQuestion(id) == 0:
            return '',404
        database = db_controller()
        qst = database.getQuestion(id)
        return qst, 200

    except Exception as e:
        return '', 401
    

def updateQuestion(id):
    try:
        if existQuestion(id) == 0:
            return '',404
    
    except:
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
    except:
        return '', 401


def participation():
    try:
        payload = request.get_json()
        name = payload['playerName']
        score = payload['answer']
        participant = Participants(name, score)
        database = db_controller()
        database.insertParticipant(participant)
        return '', 200
    except:
        return '', 400

def deleteParticipation():
    try:
        database = db_controller()
        database.deleteParticipant()
        return '', 204  
    except:
        return '', 400

def getNumberQuestion():
    try:
        database = db_controller()
        number = database.getNumberOfQuestion()
        return str(number), 200
    except:
        return '', 401

def getLogin():
    try:
        database = db_controller()
        login = database.getLogin()
        return str(login), 200
    except:
        return '', 401

def getPassword():
    try:
        database = db_controller()
        password = database.getPassword()
        return str(password), 200
    except:
        return '', 401