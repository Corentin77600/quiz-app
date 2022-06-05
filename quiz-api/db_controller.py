import json
from operator import truediv
import sqlite3
from participants import Participants
import question
import reponse
import function

class db_controller():
    def __init__(self):
        connexion = sqlite3.connect("C:\\Users\\Utilisateur\\Documents\\Corentin\\E4\\Fullstack_2\\quiz-app\\quiz-api\\bdd1.db")
        connexion.isolation_level = None
        self.connexion = connexion

    def insertQuestion(self, question: question.Question):
        questionToJson = question.pythonToJson(question.reponses)
        #Change apostrophe for BDD
        for id, element in enumerate(questionToJson):
            #Check if element is string
            if isinstance(questionToJson[element], str):
                questionToJson[element] = questionToJson[element].replace("'", "''")

        queryVerifyPos = (f"SELECT COUNT(*) FROM Question where position="+str(questionToJson['position']))
        queryUpdatePos = (f"UPDATE Question SET position=position+1  WHERE position>="+str(questionToJson['position']))
        query = (
			f"INSERT INTO Question (title, text, image, position) VALUES"
			f"('{questionToJson['title']}', '{questionToJson['text']}', '{questionToJson['image']}', '{questionToJson['position']}')"
		)
        cursor = self.connexion.cursor()
        try:
            cursor.execute("begin")
            cursor.execute(queryVerifyPos)
            nb = cursor.fetchone()[0]
            if nb >= 1:
                print("toUpdate")
                cursor.execute(queryUpdatePos)
            cursor.execute(query)
            cursor.execute("commit")
            question.id = cursor.lastrowid

        except Exception as e:
            print(e)
            cursor.execute('rollback')

    def deleteQuestion(self, position):
        select_Query = (f"SELECT id FROM Question WHERE position="+position)

        delete_Query = (f"DELETE FROM Question WHERE position="+position)
        update_query = (f"UPDATE Question SET position=position-1  WHERE position >"+ position)
        cursor = self.connexion.cursor()
        #nb_Selected = 0
        cursor.execute("begin")
        id = cursor.execute(select_Query)
        idToDelete = id.fetchone()[0]
        cursor.execute(delete_Query)
        cursor.execute(update_query)
        cursor.execute("commit")
        return str(idToDelete)

    def insertAnswer(self, reponse: reponse.Reponse):
        reponseToJson = reponse.pythonToJson()
        #Change apostrophe for BDD
        for id, element in enumerate(reponseToJson):
            #Check if element is string
            if isinstance(reponseToJson[element], str):
                reponseToJson[element] = reponseToJson[element].replace("'", "''")

        query = (
			f"INSERT INTO Reponse (idQuestion, text, isCorrect) VALUES"
			f"('{reponseToJson['idQuestion']}', '{reponseToJson['text']}', '{reponseToJson['isCorrect']}')"
		)
        cursor = self.connexion.cursor()

        cursor.execute("begin")
        cursor.execute(query)
        cursor.execute("commit")

    def deleteAnswer(self, idQuestion):
        query = (f"DELETE FROM Reponse WHERE idQuestion="+ idQuestion)
        cursor = self.connexion.cursor()

        cursor.execute("begin")
        cursor.execute(query)
        cursor.execute("commit")

    def getQuestion(self, position):
        query1 = (f"SELECT * FROM Question WHERE position="+position)
        cursor = self.connexion.cursor()

        cursor.execute("begin")
        q1 = cursor.execute(query1)
        data = q1.fetchall()
        cursor.execute("commit")
        id = data[0][4]
        cursor.execute("begin")
        query2 = (f"SELECT * FROM Reponse WHERE idQuestion="+str(id))
        q2 = cursor.execute(query2)
        data2 = q2.fetchall()
        cursor.execute("commit")
        answer =[]
        isCorrect = False
        for rep in data2:
            print(rep[2])
            if rep[2] == "True":
                 isCorrect = True
            if rep[2] == "False":
                print("false")
                isCorrect = False
            print(isCorrect)
            answer.append({
            'text': rep[1],
            'isCorrect': isCorrect
        })
        #answer as Json format
        answerJson = json.dumps(answer)
        print(answerJson)
        qst = question.Question(data[0][0], data[0][1], data[0][2],  data[0][3], answer)
        jsonQST = qst.pythonToJson(qst.reponses)
        return jsonQST

    #Update Question
    def updateQuestion(self, id, qst:question.Question, length):
        questionToJson = qst.pythonToJson(qst.reponses)
        query1 = (f"UPDATE Question SET title = ?, text=?, image=?, position=? WHERE id="+id)
        queryID = (f"SELECT id FROM Question WHERE position="+id)
        queryDelete = (f"DELETE FROM Reponse WHERE id=(SELECT MAX(id) FROM Reponse WHERE idQuestion="+id+")")
        querySelect = (f"SELECT COUNT(*) FROM Reponse WHERE idQuestion="+id)
        
        queryVerifyPos = (f"SELECT COUNT(*) FROM Question where position="+str(questionToJson['position']))
        queryUpdatePosUp = (f"UPDATE Question SET position=position+1  WHERE (position>="+str(questionToJson['position'])+" AND position<"+id+")")
        queryUpdatePosDown = (f"UPDATE Question SET position=position-1  WHERE (position<="+str(questionToJson['position'])+" AND position>"+id+")")
       
        cursor = self.connexion.cursor()
        cursor.execute("begin")
        #Return number of answers for a question
        cursor.execute(querySelect)
        nbAnswerForQuestion = cursor.fetchone()[0]
        print(nbAnswerForQuestion)
        #Return number of question with a position
        cursor.execute(queryVerifyPos)
        nb = cursor.fetchone()[0]
        #get ID question
        qq = cursor.execute(queryID)
        newID = qq.fetchone()[0]
        cursor.execute("commit")

        #Update Position
        if nb >= 1:
            cursor.execute("begin")
            #Update la position
            if(int(id)>int(questionToJson['position'])):
                cursor.execute(queryUpdatePosUp)
            elif int(id) < int(questionToJson['position']):
                cursor.execute(queryUpdatePosDown)
            else:
                cursor.execute(query1, (questionToJson['title'], questionToJson['text'], questionToJson['image'], questionToJson['position']))
            cursor.execute("commit")
            print("updtaded")
        
        
        #Update la question à la position...
        cursor.execute("begin")
        queryNewPos = (f"UPDATE Question SET position="+str(questionToJson['position'])+" WHERE id="+str(newID))
        cursor.execute(queryNewPos)
        cursor.execute("commit")

        query2 = (f"UPDATE Reponse SET text = ?, isCorrect=? WHERE id=(SELECT MIN(id)+? FROM Reponse WHERE idQuestion="+id+")")

        if int(id)== questionToJson['position']:
            cursor.execute("begin")
            print(qst.reponses[0]['text'])
            if(length < nbAnswerForQuestion):
                #Si moins de rep dans la nouvelle alors on supprime la derniere rep et on remet à jour
                print("DELEEEEEEEEEEEEEEEEEETE")
                cursor.execute(queryDelete)
            cpt = 0
            for rep in qst.reponses:
                #Mise à jour des réponses
                print(rep)
                cursor.execute(query2, (rep['text'], str(rep['isCorrect']), cpt))
                cpt+=1
            cursor.execute("commit")

    #Check if question exit
    def existQuestion(self, position):
        query = ("SELECT COUNT(*) FROM Question WHERE position="+position)
        cursor = self.connexion.cursor()
        cursor.execute("begin")
        cursor.execute(query)
        nb = cursor.fetchone()[0]
        cursor.execute("commit")
        if nb > 0:
            return 1
        else:
            return 0
    
    def insertParticipant(self, participant: Participants):
        query = (f"INSERT INTO Participants (name, answers) VALUES"
			f"('{participant.name}', '{participant.answer}')")
        cursor = self.connexion.cursor()
        cursor.execute("begin")
        cursor.execute(query)
        cursor.execute("commit")

    def deleteParticipant(self):
        query = (f"DELETE FROM Participants")
        cursor = self.connexion.cursor()
        cursor.execute("begin")
        cursor.execute(query)
        cursor.execute("commit")

    def getNumberOfQuestion(self):
        query =  (f"SELECT COUNT(*) FROM Question")
        cursor = self.connexion.cursor()
        cursor.execute("begin")
        numberOfQuestionQuery = cursor.execute(query)
        numberOfQuestion = numberOfQuestionQuery.fetchone()[0]
        cursor.execute("commit")
        return numberOfQuestion

    def getLogin(self):
        query =  (f"SELECT * FROM Administration")
        cursor = self.connexion.cursor()
        cursor.execute("begin")
        getLoginQuery = cursor.execute(query)
        getLogin = getLoginQuery.fetchall()
        cursor.execute("commit")
        return getLogin[0][1]
    
    def getPassword(self):
        query =  (f"SELECT * FROM Administration")
        cursor = self.connexion.cursor()
        cursor.execute("begin")
        getPasswordQuery = cursor.execute(query)
        getPassword = getPasswordQuery.fetchall()
        cursor.execute("commit")
        return getPassword[0][2]


    


