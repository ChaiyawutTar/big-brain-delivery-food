from datetime import datetime
import json
import os
class User:

    def __init__(self,userDict : dict):
        self.username = userDict['username']
        self.password = userDict['password']
        self.fname = ''
        self.lname = ''
        # self.password = ''
        self.address = ''
        self.telephone = ''
        self.email = ''
        self.__userData : dict = {"status":"unauthorized"}
        self.authorize(userDict)

    def login(self):
        with open("user.json", "r") as user_file:
            user = json.load(user_file)
        if self.username not in user:
            User(self).register(self)
        else:
            print('ok')

    def authorize(self,userDict : dict):
        with open("user.json",'r') as file:
            getUser = json.load(file)
            try:
                # print(userDict)
                # print(getUser[userDict['username']])
                self.__userData : dict = getUser[userDict['username']]
                if (self.__userData['password'] == userDict['password']):
                    # print("login Completed")
                    self.__userData.update({"status":"authorized"})
                    pass
                else:
                    self.__userData.update({"status":"wrongPassword"})
                    print()
                    # print("login not complete")
            except:
                print("Login Error")

    @property
    def getUsername(self) -> str:
        try :
            return self.username
        except:
            return ""

    @property
    def getFname(self) -> str:
        try :
            return self.__userData['fname']
        except:
            return ""

    @property
    def getLname(self) -> str:
        try :
            return self.__userData['lname']
        except:
            return ""


    @property
    def getAddress(self) -> str:
        try :
            return self.__userData['address']
        except:
            return ""


    @property
    def getStatus(self) -> str:
        try :
            return self.__userData['status']
        except:
            return ""


    @property
    def isAdmin(self) -> str:
        try :
            return self.__userData['admin']
        except:
            return ""



    def register(self):
        with open("user.json", "r") as data_file:
            data = json.load(data_file)
            # self.username = str(input('Please Enter your username: '))
            self.fname = str(input('Please Enter your first name: '))
            self.lname = str(input('Please Enter your last name: '))
            # self.password = str(input('Please Enter your password: '))
            self.address = str(input('Please Enter your address: '))
            self.district = str(input('Please Enter your district: '))
            self.province = str(input('Please Enter your province: '))
            self.postalcode = str(input('Please Enter your postal code: '))
            self.telephone = str(input('Please Enter your telephone: '))
            self.email = ""

            while '@' not in self.email:
                self.email = str(input('Please Enter your email: '))

        new_data = {
            self.username: {
                "fname": self.fname,
                "lname": self.lname,
                "admin": False,
                "password": self.password,
                "address":
                {
                    "address": self.address,
                    "district": self.district,
                    "province": self.province,
                    "postalcode": self.postalcode
                },
                "telephone": self.telephone,
                "email": self.email
            }
        }
        with open("user.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)
        with open("user.json", "w") as data_file:
            json.dump(data, data_file, indent = 4)

class Colors:

    def __init__(self,r = 0,g = 0,b = 0) -> None:
        self.r = r
        self.g = g
        self.b = b
    
    @property
    def green(self):
        return Colors(0,200,51)

    @property
    def yellow(self):
        return Colors(253,253,150)


class Admin(User):

    
    def __init__(self, userDict: dict):
        super().__init__(userDict)
        self.shopStatus : dict = {"status":self.autoShopStatus,"state" : "Auto"}

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

    def justifyRight(self,text1 : str,text2 : str,length: int = 35):
        text1 = str(text1)
        text2 = str(text2)
        output = str(text1) + " " * (length - len(text1) - len(text2)) + str(text2)
        return output

    @property
    def autoShopStatus(self) -> str:
        current_time = datetime.now().strftime("%H:%M:%S")
        open_time = 3600*8
        close_time = 3600*20
        timeNow = current_time.split(":")
        timeNowSeconds = int(timeNow[0])*60*60 + int(timeNow[1])*60 + int(timeNow[2])
        if open_time <= timeNowSeconds <= close_time:
            # print("Auto Shop ON")
            return "on"
        else:
            # print("Auto Shop OFF")
            return "off"
        
    #----------------- To be moved to other places -----------------#
    def adminConsole(self):
        while True:
            command : str = input("admin@bigBrainCompany: ")

            if command.strip().lower() == 'exit':
                print('bye...')
                break

            commandStrip = command.split(" ")
            try:
                if (commandStrip[0].lower().strip() == 'stock'):
                    # print("Stock related command here")

                    if (commandStrip[1].lower().strip() == 'add'):
                        if '"' in command:
                            # print("Extract Menu Name")
                            ####----- stock add category name price amount -----####
                            quotationIndex = command.index('"')
                            menuName = command[quotationIndex + 1:-1]
                            menuName = menuName[0:menuName.index('"')]
                            category = commandStrip[2].lower()
                            number = int(commandStrip[-1])
                            price = int(commandStrip[-2])
                            # print(f"Cat : '{category}' Name : {menuName} Number : {number} Price : {price}")
                            # print(f'"${menuName}"',number)
                            stockUpdate : dict = {}
                            menuUpdate : dict = {}

                            with open('stock.json','r') as file:
                                stockUpdate = json.load(file)
                                stockUpdate.update({menuName:number})

                            # print(stockUpdate)
                            with open('stock.json','w') as file:
                                json.dump(stockUpdate,file,indent = 4)
                                # print(f'Current Stock : {stockUpdate}')

                            with open('menu.json','r') as file:
                                menuUpdate = json.load(file)
                                menuUpdate.update({category:menuUpdate[category] | {menuName:price}})

                            with open('menu.json','w') as file:
                                json.dump(menuUpdate,file,indent=4)


                            # print(menuUpdate)
                            # print(menuUpdate)

                            # while True:
                            #     pass    
                            print("Stock add")
                        else:
                            print("Stock add invalid")
                            raise

                    elif (commandStrip[1].lower().strip() == 'remove'):
                        if '"' in command:

                            quotationIndex = command.index('"')
                            menuName = command[quotationIndex + 1:-1]
                            print(menuName)

                            try :
                                menuName = menuName[0:menuName.index('"')]
                            except :
                                pass

                            print(menuName)

                            stockUpdate : dict = {}

                            with open('stock.json','r') as file:
                                stockUpdate = json.load(file)
                                del stockUpdate[menuName]
                                stockUpdate.update({menuName:0})

                            # print(stockUpdate)
                            with open('stock.json','w') as file:
                                json.dump(stockUpdate,file,indent = 4)
                                print(f'Current Stock : {stockUpdate}')

                            menuUpdate : dict = {}

                            # with open('menu.json',"r") as file:
                            #     menuUpdate = json.load(file)

                            
                            # print(menuName)
                        else:
                            print("Stock remove invalid")
                            raise
                    
                    elif (commandStrip[1].lower().strip() == 'view'):
                        # Load Stock JSON
                        with open('stock.json','r') as file:
                            fileReadText : dict = json.load(file)
                            stock = fileReadText.items()
                            print(self.greenText("\nCurrent Stock:"))
                            yellowColor = Colors(253,253,150)
                            print(f"""  {self.coloredText("Name :",yellowColor)}{" " * (50 - (len("Name") + len("Amount") - 1))}{self.coloredText("Amount",yellowColor)}""")
                            for item in stock:
                                print(f"  {self.justifyRight(item[0],item[1],50)}")
                            print()
                            # print(f'Current Stock : {fileReadText}')
                        # print("Stock View")


                elif (commandStrip[0].lower().strip() == 'shop'):
                    # print("Shop related command here")
                    if (commandStrip[1].lower().strip() == 'on'):
                        self.shopStatus['status'] = 'on'
                        self.shopStatus['state'] = 'Manual'

                    elif (commandStrip[1].lower().strip() == 'off'):
                        self.shopStatus['status'] = 'off'
                        self.shopStatus['state'] = 'Manual'

                    elif (commandStrip[1].lower().strip() == 'auto'):
                        self.shopStatus['status'] = self.autoShopStatus
                        self.shopStatus['state'] = 'Auto'

                    elif (commandStrip[1].lower().strip() == 'status'):
                        pass

                    else:
                        raise

                    print(f"Shop status {self.shopStatus['status']} ({self.shopStatus['state']})")

                elif (commandStrip[0].lower().strip() == 'ls'):
                    os.system('dir')

                elif (command == ""):
                    pass
                else:
                    print("Unknown command :",commandStrip[0])
                
                
            except Exception as e:
                print(e)
                print("Invalid Command")
                pass
                # print(e)

            if command.lower().strip() == 'clear' or command.lower().strip() == 'cls':
                os.system('cls')   

# P1 = User().register()
# def register(file):

                
            
