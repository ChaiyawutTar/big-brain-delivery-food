import json

class Display:
    def run(self):
        # get user input
        print("Welcome to Big Brain Delivery app")
        print("Please Login")
        username = input("Username : ")
        password = input("Password : ")
        userdata : dict = {} # load data from json
        with open("./control/user.json",'r') as user:
            userdata = json.load(user)
            print(userdata)
        # while(True):
            
