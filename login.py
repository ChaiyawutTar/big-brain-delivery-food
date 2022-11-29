import json


class User:

    def __init__(self):
        self.__userData : dict = {}

    def authorize(self,userDict : dict):
        with open("user.json",'r') as file:
            getUser = json.load(file)
            try:
                # print(userDict)
                # print(getUser[userDict['username']])
                self.__userData = getUser[userDict['username']]
                if (self.__userData['password'] == userDict['password']):
                    print("login Completed")
                else:
                    print("login not complete")
            except:
                print("Login Error")

    @property
    def getFname(self):
        return self.__userData['fname']

    @property
    def getLname(self):
        return self.__userData['lname']

    @property
    def getAddress(self):
        return self.__userData['address']

def getInput():
    user1 = User()
    username = input("input username : ")
    password = input("input password : ")
    user1.authorize({"username":username,"password":password})
    print(user1.getFname)


getInput()