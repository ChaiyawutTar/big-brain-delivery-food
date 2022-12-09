from datetime import datetime
import json
import os
from stock import Stock
import user
from user import Admin
import turtle

class Color:

    def __init__(self,r = 0,g = 0,b = 0) -> None:
            self.r = r
            self.g = g
            self.b = b

    def greenText(self,text : str):
        return "\x1B[38;2;0;200;51m"+ text +"\x1b[0m"
    
    def coloredText(self,text : str,color) -> str:
        try:
            r = color.r
            g = color.g
            b = color.b
            return f"\x1B[38;2;{r};{g};{b}m"+ text +"\x1b[0m"
        except:
            return text
            
class Colors:

   green = Color(0,200,51)
   yellow = Color(253,253,150)

class Display(Stock):

    def __init__(self) -> None:
        super().__init__()

    def justifyRight(self,text1 : str,text2 : str,length: int = 35):
        text1 = str(text1)
        text2 = str(text2)
        output = str(text1) + " " * (length - len(text1) - len(text2)) + str(text2)
        return output

    def greenText(self,text : str):
        return "\x1B[38;2;0;200;51m"+ text +"\x1b[0m"

    def coloredText(self,text : str,color : Colors) -> str:
        try:
            r = color.r
            g = color.g
            b = color.b
            return f"\x1B[38;2;{r};{g};{b}m"+ text +"\x1b[0m"
        except:
            return text
    
    def run(self):
        # get user input
        print("Welcome to Big Brain Delivery app")
        print("Please Login")
        username = input("Username : ")
        password = input("Password : ")
        userDict : dict =  {"username":username,"password":password}
        # self.userDict = userDict
        user1 : user.User = user.User(userDict)

        if (user1.getStatus == "authorized"):
            print(f"Welcome {user1.getFname}")

        elif (user1.getStatus == "unauthorized"):
            registerAns : str = input("No user with that name do you want to register? [Y/N] ")
            if (registerAns.lower() == "y"):
                user1.register()
                self.run()
            else:
                self.run()
        else:
            print("Incorrect username or password")
            self.run()

        self.landingPage(user1,userDict)   
        
        # print(choice)
    
    def landingPage(self,user : Admin,userDict : dict):
        # to be implemented
        print()
        print(f"There are {super().getNumOrders(user)} orders pending")
        
        print("While waiting what do want to do?")
        print("  1.View Order")
        print("  2.New Order")
        print("  3.Cancel Order")
        if (user.isAdmin):
            user = Admin(userDict)
            print("  4.Shop management")

        choice = self.choiceSelector(user)

        if choice == 1:
            self.viewOrder(user)
            self.landingPage(user,userDict)

        elif choice == 2:
            super().new_order(user)
            self.landingPage(user,userDict)

        elif choice == 3:
            self.viewOrder(user)
            super().cancel_order(user)
            self.landingPage(user,userDict)

        elif choice == 4:
            user.adminConsole()
    

    def choiceSelector(self,user : user.Admin) -> int:
        choice = ""
        while True:
            try:
                choice = int(input("Your Choice : "))
                if choice > 3 + user.isAdmin or choice <= 0:
                    raise
                return int(choice)

            except KeyboardInterrupt:
                exit()
            except Exception as e:
                print(e)
                print("Please enter a valid intiger")
        
    def initTurtle(self):
        pass
