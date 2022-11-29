import json
import os
import login
import turtle
class Display:

    def authUser(self,__username,__password):
        user1 : login.User() = login.User()
        user1.authorize({"username":__username,"password":__password})
        print(user1.getStatus)

    def run(self):
        # get user input
        print("Welcome to Big Brain Delivery app")
        print("Please Login")
        username = input("Username : ")
        password = input("Password : ")
        self.authUser(username,password)

    def initTurtle(self):
        pass
