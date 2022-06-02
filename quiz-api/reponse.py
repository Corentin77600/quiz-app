class Reponse():
    def __init__(self, idQuestion:int, text:str, isCorrect:bool):
        self.idQuestion = idQuestion
        self.text = text
        self.isCorrect = isCorrect

    def pythonToJson(self):
        return {
            'idQuestion': self.idQuestion,
            'text': self.text,
            'isCorrect': self.isCorrect
        }

    def jsonToPython(json):
        return Reponse(json['idQuestion'], json['text'], json['isCorrect'])