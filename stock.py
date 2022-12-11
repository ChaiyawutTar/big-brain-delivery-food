from datetime import datetime
import json

from display import Colors
class Stock:

    def update_stock(self):
        new_data = ""
        with open('stock.json', 'r') as f:
            data : dict = json.load(f)
            data.update(new_data)
        with open('stock.json', 'w') as f:
            json.dump(data , f, indent = 4)

        # with open("stock.csv", "r") as f:
        #     data = csv.DictReader
        
    def get_menulist(self):
        with open('stock.json','r') as file:
            return json.load(file) 

    def get_amount(self):
        pass

    def get_stock(self):
        with open('stock.json','r') as file:
            return json.load(file) 

    def update_order_stock(self,user, ordersMenu : dict):
        
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
    
    def cancel_order(self,user):
        
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

    
    def new_order(self,user):
        
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
                            self.update_order_stock(user,ordersMenu)
                            break
                        else:
                            #---- Go back to make order again ----#
                            self.newOrder(user,ordersMenu)
                        # print("Your ")
                    except Exception as e:
                        print(e)
                        print("Invalid Input")

    def viewOrder(self,user):
        print()
        print(self.coloredText("Your order details :",Colors.green))
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

                
    def getNumOrders(self,user) -> int:
        with open('user.json','r') as userFile:
            userData : dict = json.load(userFile)
            userData : dict = userData[user.getUsername]
            try :
                orderData : dict = userData['orders']
                return len(orderData)
            except :
                return 0

