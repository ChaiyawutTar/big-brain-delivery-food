from datetime import datetime
import json
import os
import user
import turtle
class Display:

    def justifyRight(self,text1 : str,text2 : str,length: int = 35):
        text1 = str(text1)
        text2 = str(text2)
        output = str(text1) + " " * (length - len(text1) - len(text2)) + str(text2)
        return output
    
    def run(self):
        # get user input
        print("Welcome to Big Brain Delivery app")
        print("Please Login")
        username = input("Username : ")
        password = input("Password : ")
        userDict : dict =  {"username":username,"password":password}
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
    
    def landingPage(self,user : user.Admin,userDict : dict):
        # to be implemented
        print()
        print(f"There are {self.getNumOrders(user)} orders pending")
        
        print("While waiting what do want to do?")
        print("  1.View Order")
        print("  2.New Order")
        print("  3.Cancel Order")
        if (user.isAdmin):
            user = user.Admin(userDict)
            print("  4.Shop management")

        choice = self.choiceSelector(user)

        if choice == 1:
            self.viewOrder(user)
            self.run()

        elif choice == 2:
            self.newOrder(user)
            self.run()

        elif choice == 3:
            self.viewOrder(user)
            self.cancelOrder(user)
            self.run()

        elif choice == 4:
            user.adminConsole()
    
    def getNumOrders(self,user : user.User) -> int:
        with open('user.json','r') as userFile:
            userData : dict = json.load(userFile)
            userData : dict = userData[user.getUsername]
            try :
                orderData : dict = userData['orders']
                return len(orderData)
            except :
                return 0

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
        # print("Status :",user1.getStatus)

    def viewOrder(self,user : user.Admin):
        print()
        print("Your order details :")
        with open('user.json','r') as userFile:
            userData : dict = json.load(userFile)
            userData : dict = userData[user.getUsername]
            try :
                orderData : dict = userData['orders']
                if (len(userData['orders']) == 0):
                    raise "No order"
                bigCounter = 1
                for order in orderData:
                    # print(f"{counter}",end = '.')

                    print(f"  {bigCounter}.Order : {order['orderNo']}")
                    counter = 1
                    for dish in order['dish']:
                        print(f"    {counter}.{dish}")
                        counter += 1
                    # counter = 1
                    for drink in order['drink']:
                        print(f"    {counter}.{drink}")
                    
                    bigCounter += 1
                # print(orderData)
            except :
                print("You have no order yet...")


    def newOrder(self,user : user.User):
        
        if (user.isAdmin):
            print("This command is not available for admin")
        else:
            print("Here are the menu")
            with open("menu.json") as menuFile:
                menuJson : dict = json.load(menuFile)
                dishDict : dict = menuJson['dish']
                drinkDict : dict = menuJson['drink']
                dishMenu = dishDict.keys()
                drinkMenu = drinkDict.keys()
                # print(menuJson.keys())
                print("Dish Menu")
                counter = 1
                for dish in dishMenu:
                    print(f"  {counter}.{self.justifyRight(dish,dishDict[dish],45)} Baht")
                    counter += 1

                print("\nDrink Menu")
                counter = 1
                for drink in drinkMenu:
                    print(f"  {counter}.{self.justifyRight(drink,drinkDict[drink],45)} Baht")
                    counter += 1

                print()
                dishChoose = 0
                drinkChoose = 0
                while True:
                    try:
                        dishChoose = int(input("Choose your dish : "))
                        drinkChoose = int(input("Choose your drink : "))
                        if (dishChoose > len(dishMenu) or drinkChoose > len(drinkMenu)):
                            raise
                        # print("Your ")
                        break
                    except Exception as e:
                        print(e)
                        print("Invalid Input")
                
                print()

                selectedDish = list(dishMenu)[dishChoose - 1]
                selectedDrink = list(drinkMenu)[drinkChoose - 1]
                print("Your order is now processing...")
                print("Here are all your orders.")
                print(f'  1.{selectedDish}')
                print(f'  2.{selectedDrink}')

                ordersMenu : dict = {'dish':[selectedDish],'drink':[selectedDrink]}

                costDish = dishDict[list(dishMenu)[dishChoose - 1]]
                costDrink = drinkDict[list(drinkMenu)[drinkChoose - 1]]

                # print(costDish,costDrink)
                print(f"\nWould be total of {int(costDish)+int(costDrink)} Baht")
                while True:
                    try:
                        confirm : str = input('Confirm? [Y/N] ')
                        if (confirm.lower().strip() == 'y'):
                            self.updateOrderStock(user,ordersMenu)
                            break
                        else:
                            #---- Go back to make order again ----#
                            self.newOrder(user,ordersMenu)
                        # print("Your ")
                    except Exception as e:
                        print(e)
                        print("Invalid Input")

    def cancelOrder(self,user : user.User):
        
        orderData : list = 0
        reWriteData : dict = 0
        with open('user.json','r') as userFile:
            userData : dict = json.load(userFile)
            reWriteData = userData
            userData : dict = userData[user.getUsername]

            while True:
                cancelChoice = input("Choose order you want to cancel : ")
                try :
                    orderData : list = userData['orders']
                    cancelChoice = int(cancelChoice)
                    if (cancelChoice > len(orderData) or cancelChoice < 0):
                        raise "Choice out of range" 
                    
                    # orderData.remove()
                    del orderData[cancelChoice - 1]
                    del reWriteData[user.getUsername]['orders']
                    reWriteData[user.getUsername].update({"orders":orderData})
                    # print(orderData)
                    break
                except Exception as e:
                    print("Exception from cancel :",e)

        with open('user.json','w') as userFile:
            json.dump(reWriteData,userFile,indent=4)
        
                


    def updateOrderStock(self,user : user.User, ordersMenu : dict):
        
        userData : dict = {}
        with open('user.json','r') as userFile:
            userData = json.load(userFile)
            orderDict : dict = {
                "orderNo":str(datetime.now()).split()[1].replace(":","").replace(".",""),
                "dish": ordersMenu['dish'],
                'drink':ordersMenu['drink']
            }
            try :
                userData[user.getUsername]['orders'].append(orderDict)
            except :
                userData[user.getUsername].update({
                    'orders':[orderDict]
                })
            # print(userData[user.getUsername]['orders'])
            # print(userData)
        
        with open('user.json','w') as userFile:
            json.dump(userData,userFile,indent=4)



    def initTurtle(self):
        pass
