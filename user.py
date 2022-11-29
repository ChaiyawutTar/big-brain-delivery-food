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
                self.__userData : dict= getUser[userDict['username']]
                self.__userData.update({"status":"authorized"})
                if (self.__userData['password'] == userDict['password']):
                    # print("login Completed")
                    pass
                else:
                    print("login not complete")
            except:
                print("Login Error")

    @property
    def getFname(self):
        try :
            return self.__userData['fname']
        except:
            return ""

    @property
    def getLname(self):
        try :
            return self.__userData['lname']
        except:
            return ""


    @property
    def getAddress(self):
        try :
            return self.__userData['address']
        except:
            return ""


    @property
    def getStatus(self):
        try :
            return self.__userData['status']
        except:
            return ""


    @property
    def isAdmin(self):
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


class Admin(User):

    def __init__(self, userDict: dict):
        super().__init__(userDict)
        self.shopStatus : dict = {"status":self.autoShopStatus,"state" : "Auto"}

    def greenText(self,text : str):
        return "\x1B[38;2;0;200;51m"+ text +"\x1b[0m"

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
                            print("Extract Menu Name")
                            quotationIndex = command.index('"')
                            menuName = command[quotationIndex + 1:-1]
                            menuName = menuName[0:menuName.index('"')]
                            number = commandStrip[-1]
                            print(f'"${menuName}"',number)
                            fileReadText = ''

                            with open('stock.json','r') as file:
                                fileReadText = json.load(file)
                                fileReadText.update({menuName:number})

                            # print(fileReadText)
                            with open('stock.json','w') as file:
                                json.dump(fileReadText,file,indent = 4)
                                print(f'Current Stock : {fileReadText}')
                                
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
                            fileReadText = ''

                            with open('stock.json','r') as file:
                                fileReadText = json.load(file)
                                del fileReadText[menuName]

                            # print(fileReadText)
                            with open('stock.json','w') as file:
                                json.dump(fileReadText,file,indent = 4)
                                print(f'Current Stock : {fileReadText}')
                            print(menuName)
                        else:
                            print("Stock remove invalid")
                            raise
                    
                    elif (commandStrip[1].lower().strip() == 'view'):
                        # Load Stock JSON
                        with open('stock.json','r') as file:
                            fileReadText : dict = json.load(file)
                            stock = fileReadText.items()
                            print(self.greenText("\nCurrent Stock:"))
                            for item in stock:
                                print(f"\t{item[0]}\t:\t{item[1]}")
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
                elif (command == ""):
                    pass
                else:
                    print("Unknown command")
                
                
            except Exception as e:
                print(e)
                print("Invalid Command")
                pass
                # print(e)

            if command.lower().strip() == 'clear':
                os.system('cls')   

# P1 = User().register()
# def register(file):

                
            
