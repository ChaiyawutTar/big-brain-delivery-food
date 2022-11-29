<<<<<<< HEAD
import json
class User:
    def __init__(self):
        self.username = str(input('Please Enter your username: '))
        self.password = str(input('Please Enter your password: '))
        self.fname = ''
        self.lname = ''
        # self.password = ''
        self.address = ''
        self.telephone = ''
        self.email = ''
    def login(self):
        with open("user.json", "r") as user_file:
            user = json.load(user_file)
        if self.username not in user:
            User(self).register(self)
        else:
            print('ok')
    def register(self):
        # self.username = str(input('Please Enter your username: '))
        # self.password = str(input('Please Enter your password: '))
        # confirm_password = str(input('Please Enter your password again to confirm your password: '))
        #
        # while confirm_password != self.password:
        #     confirm_password = str(input('Please Enter your password again to confirm your password: '))
        #     if confirm_password == self.password:
        #         self.address = str(input('Please Enter your address: '))
        #         self.district = str(input('Please Enter your district: '))
        #         self.province = str(input('Please Enter your province: '))
        #         self.postalcode = str(input('Please Enter your postal code: '))
        #         self.telephone = str(input('Please Enter your telephone: '))
        #         self.email = str(input('Please Enter your email: '))
        #         if '@' not in self.email:
        #             while True:
        #                 self.email = str(input('Please Enter your email: '))
        #                 if '@' in self.email:
        #                     break
        with open("user.json", "r") as data_file:
            data = json.load(data_file)
            while self.username in data_file:
                self.username = str(input('Please Enter your username: '))
            self.fname = str(input('Please Enter your first name: '))
            self.lname = str(input('Please Enter your last name: '))
            self.address = str(input('Please Enter your address: '))
            self.district = str(input('Please Enter your district: '))
            self.province = str(input('Please Enter your province: '))
            self.postalcode = str(input('Please Enter your postal code: '))
            self.telephone = str(input('Please Enter your telephone: '))
            self.email = str(input('Please Enter your email: '))
            if '@' not in self.email:
                while True:
                    self.email = str(input('Please Enter your email: '))
                    if '@' in self.email:
                        break
        new_data = {
            self.username: {
                "password": self.password,
                "address":
                {
                    "address": self.address,
                    "district": self.district,
                    "province": self.province,
                    "postalcode": self.postalcode
                },
                "telephone": self.telephone,
                "email" : self.email
            }
        }
        with open("user.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)
        with open("user.json", "w") as data_file:
            json.dump(data, data_file, indent = 4)

P1 = User().register()
# def register(file):

                
            
=======
import os


class User:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.verified = False

    def order(self):
        # place some order
        pass

    def cancel_order(self):
        # cancel order
        pass
    
    def register(self):
        # register
        pass

    def login(self,file):
        try :
            found = userdata[self.username]
            if (password != found['password']):
                raise
            print(f"Welcome {userdata[self.username]['fname']}")
        except Exception as e:
            os.system('cls') 
            print("Invalid Login")
            self.run()
        pass

    
>>>>>>> c9ddb6a4444855104aa674e1074ef19524a59af3
