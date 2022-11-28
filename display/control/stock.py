import json

class Stock:
    def __init__(self, ordinary):
        self.dict_stock = {}
        self.ordinary = ordinary


    def update_stock(self):
        new_data = 
        with open('stock.json', 'r') as f:
            data =  json.load(f)
            data.update(new_data)
        with open('stock.json', 'w') as f:
            json.dump(data , f, indent = 4)

        # with open("stock.csv", "r") as f:
        #     data = csv.DictReader
        
    def get_menulist(self):
        pass

    def get_amount(self):
        pass
    

