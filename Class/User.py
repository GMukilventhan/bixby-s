class User:
    def __init__(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password
