class Administration():
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def jsonToPython(json):
        login = json[0][0]
        password = json[0][1]
        return Administration(login, password)

    def pythonToJson(self):
        return {
            'login': self.login,
            'password': self.password
        }
