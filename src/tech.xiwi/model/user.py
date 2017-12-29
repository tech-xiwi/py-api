class User():
    def __init__(self,nickname,birthday,gender):
        self.nickname = nickname
        self.birthday = birthday
        self.gender = gender

    def printUserInfo(self):
        print (self.nickname + " " + self.gender + " " + str(self.birthday))