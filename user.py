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

    