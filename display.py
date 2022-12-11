from datetime import datetime
import json
import os
from color import Colors
from stock import Stock
import user
from user import Admin
import turtle



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
    
    # def run(self):
    #     self.graphic_interface()


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
            print("  5.Orders management")

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
            self.landingPage(user,userDict)

        elif choice == 5:
            self.graphic_interface(user)
            self.landingPage(user,userDict)
    

    def choiceSelector(self,user : user.Admin) -> int:
        choice = ""
        while True:
            try:
                choice = int(input("Your Choice : "))
                if 1 <= choice <= 5:
                    return int(choice)
                raise ValueError

            except KeyboardInterrupt:
                exit()
            except Exception as e:
                print(e)
                print("Please enter a valid intiger")

    def on_click(self,x,y):
        for index in range(len(self.buttonPosX)):
            if (self.buttonPosX[index] < x < self.buttonPosX[index] + 150):
                if (self.buttonPosY[index] < y < self.buttonPosY[index] + 30):
                    # print("In Button",index)
                    # p
                    user_items : list = self.admin.get_user_list
                    user_list : list = []
                    for i in user_items:
                        if not self.admin.isAdmin(i):
                            user_list.append(i)
                    print(user_list[index])
                    super().deliver_order(user_list[index])
                    self.graphic_interface(self.admin)

    def graphic_interface(self,admin):
        self.admin = admin
        screen = turtle.Screen()
        screen.clearscreen()
        screen.setup(600,600)
        # username = turtle.textinput("Admin Console Login","Enter admin username")
        # password = turtle.textinput("Admin Console Login","Enter admin password")
        # user_form : dict = {
        #     "username" : username,
        #     "password" : password
        # }

        titleStyle = ("Arial",30)
        normalStyle = ("Arial",20)
        dataStyle = ("Arial",11)

        self.buttonPosY = []
        self.buttonPosX = []
        if admin.getStatus == "authorized": # Check if authorized
            screen.tracer(0)
            turtle.speed(0)
            turtle.penup()
            turtle.goto(80 - 250,230)
            turtle.write("Big Brain Delivery",font=titleStyle)
            turtle.goto(40 - 300,200)
            # turtle.begin_fill()
            # turtle.fillcolor("light green")
            # for i in range(2):
            #     turtle.forward(600 - 80)
            #     turtle.right(90)
            #     turtle.forward(600 - 160)
            #     turtle.right(90)
            turtle.goto(20 - 300,180)
            user_items : list = admin.get_user_list
            user_list : list = []
            for i in user_items:
                if not admin.isAdmin(i):
                    user_list.append(i)

            posY = 180
            for i in range(len(list(user_list))):
                posX = 20 - 300
                order_list = admin.get_user_order(user_list[i])
                self.buttonPosY.append(posY)
                self.buttonPosX.append(posX + len(user_list[i]) * 15)
                turtle.goto(posX,posY)
                turtle.write(user_list[i],font=normalStyle)
                turtle.goto(posX + len(user_list[i]) * 15,posY)
                
                turtle.begin_fill()
                turtle.fillcolor("dark green")
                # turtle.penup()
                for i in range(2):
                    turtle.forward(150)
                    turtle.left(90)
                    turtle.forward(30)
                    turtle.left(90)
                turtle.end_fill()
                turtle.pencolor("white")
                turtle.write("Click to Deliver",font=("Arial",14))
                turtle.pencolor("black")

                turtle.goto(posX,posY)
                order_text = ""
                # posY -= 30
                turtle.goto(posX,posY)
                if (len(order_list) != 0):
                    posY -= dataStyle[1] * 1.6
                    posY -= dataStyle[1] * 3 * 1.6 * len(order_list)
                    turtle.goto(posX,posY)
                    for i in order_list:
                        order_text += f"  Order {i['orderNo']}\n"
                        order_text += f"\t{i['dish'][0]}\n"
                        order_text += f"\t{i['drink'][0]}\n"
                    turtle.write(order_text,font=dataStyle)
                    
                    # turtle.pendown()
                    turtle.goto(posX,posY)
                else:
                    posY -= dataStyle[1] * 1.6
                    turtle.goto(posX,posY)
                    turtle.write("  No orders",font=dataStyle)
                
                posY -= titleStyle[1] * 1.3
            # turtle.end_fill()
        screen.onclick(self.on_click)
        screen.mainloop()

