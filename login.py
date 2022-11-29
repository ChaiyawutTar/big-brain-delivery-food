import json


class User:

    def __init__(self):
        self.__userData : dict = {"status":"unauthorized"}

    def authorize(self,userDict : dict):
        with open("user.json",'r') as file:
            getUser = json.load(file)
            try:
                # print(userDict)
                # print(getUser[userDict['username']])
                self.__userData : dict= getUser[userDict['username']]
                self.__userData.update({"status":"authorized"})
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

    @property
    def getStatus(self):
        return self.__userData['status']