import json
import os

class Display:
    def run(self):
        # get user input
        print("Welcome to Big Brain Delivery app")
        print("Please Login")
        username = input("Username : ")
        password = input("Password : ")
        userdata : dict = {} # load data from json
        with open("user.json",'r') as user:
            userdata = json.load(user)
            # if userdata[username] 
            try :
                found = userdata[username]
                if (password != found['password']):
                    raise
                print(f"Welcome {userdata[username]['fname']}")
            except Exception as e:
                os.system('cls') 
                print("Invalid Login")
                self.run()
        # while(True):
            
