class Question():
    def __init__(self, title, text, image, position, reponses, id = None):
        self.title = title
        self.text = text
        self.image = image
        self.position = position
        self.reponses = reponses
        self.id = id

    def pythonToJson(self, questionPA):
        json = {}
        dict_rep = []
        print(self.image)
        for rep in questionPA:
            dict_rep.append({
                'text': rep['text'],
                'isCorrect': rep['isCorrect']
            })
        dict_data = {
			'title': self.title,
			'text': self.text,
			'image': self.image,
			'position': self.position,
			'id': self.id,
            'possibleAnswers': dict_rep
        }

        json = dict_data
        return json

    