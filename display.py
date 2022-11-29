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
        user1 = user.User(userDict)

        if (user1.getStatus == "authorized"):
            print(f"Welcome {user1.getFname}")

        elif (user1.getStatus == "unauthorized"):
            registerAns : str = input("No user with that name do you want to register? [Y/N] ")
            if (registerAns.lower() == "y"):
                user1.register()
                self.run()
            else:
                self.run()
            
        # to be implemented
        print("There are ... orders pending")
        
        print("While waiting what do want to do?")
        print("  1.View Order")
        print("  2.New Order")
        print("  3.Cancel Order")
        if (user1.isAdmin):
            admin1 = user.Admin(userDict)
            print("  4.Shop management")

        choice = ""
        while True:
            try:
                choice = int(input("Your Choice : "))
                if choice > 3 + user1.isAdmin or choice <= 0:
                    raise
                break
            except KeyboardInterrupt:
                exit()
            except:
                print("Please enter a valid intiger")

        if choice == 2:
            if (user1.isAdmin):
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
                    print("Drink Menu")
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

                    print("Your order is now processing")
                    print("Here are all your orders.")
                    print(f'  1.{list(dishMenu)[dishChoose - 1]}')
                    print(f'  2.{list(drinkMenu)[drinkChoose - 1]}')

                    print("\nWould be total of ... Baht")
                    # print(dishDict.keys())
                    # print(drinkDict.keys())
                    

        elif choice == 4:
            admin1.adminConsole()
        # print(choice)
        


        # print("Status :",user1.getStatus)


    def initTurtle(self):
        pass
