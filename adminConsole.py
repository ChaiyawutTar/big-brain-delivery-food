import os
import json
shopStatus = 'on'

def greenText(text : str):
    return "\x1B[38;2;0;200;51m"+ text +"\x1b[0m"

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
                    print("Extract Menu Name")
                    quotationIndex = command.index('"')
                    menuName = command[quotationIndex + 1:-1]
                    menuName = menuName[0:menuName.index('"')]

                    print(menuName)
                else:
                    print("Stock remove invalid")
                    raise
            
            elif (commandStrip[1].lower().strip() == 'view'):
                # Load Stock JSON
                with open('stock.json','r') as file:
                    fileReadText : dict = json.load(file)
                    stock = fileReadText.items()
                    print(greenText("\nCurrent Stock:"))
                    for item in stock:
                        print(f"\t{item[0]}\t:\t{item[1]}")
                    print()
                    # print(f'Current Stock : {fileReadText}')
                # print("Stock View")


        elif (commandStrip[0].lower().strip() == 'shop'):
            # print("Shop related command here")

            if (commandStrip[1].lower().strip() == 'on'):
                shopStatus = 'on'
                print("Shop ON")

            if (commandStrip[1].lower().strip() == 'off'):
                shopStatus = 'off'
                print("Shop Off")
            
            if (commandStrip[1].lower().strip() == 'status'):
                # load shop status
                print(f"Shop status {shopStatus}")
        elif (command == ""):
            pass
        else:
            print("Unknown command")
        
        
    except:
        print("Invalid Command")
        pass
        # print(e)

    if command.lower().strip() == 'clear':
        os.system('cls')   