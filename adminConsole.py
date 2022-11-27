import os
shopStatus = 'on'
while True:
    command : str = input("admin@big-brain: ")

    if command.strip().lower() == 'exit':
        print('bye...')
        break

    if command.lower().strip() == 'clear':
        os.system('cls')

    commandStrip = command.split(" ")
    try:
        if (commandStrip[0].lower().strip() == 'stock'):
            print("Stock related command here")

            if (commandStrip[1].lower().strip() == 'add'):
                print("Stock add")

            if (commandStrip[1].lower().strip() == 'remove'):
                print("Stock remove")
            
            if (commandStrip[1].lower().strip() == 'view'):
                # Load Stock JSON
                print("Stock View")

        if (commandStrip[0].lower().strip() == 'shop'):
            print("Stock related command here")

            if (commandStrip[1].lower().strip() == 'on'):
                shopStatus = 'on'
                print("Shop ON")

            if (commandStrip[1].lower().strip() == 'off'):
                print("Shop Off")
            
            if (commandStrip[1].lower().strip() == 'status'):
                # load shop status
                print("Stock View")
                
    except Exception as e:
        print(e.message)
