import os
while True:
    command : str = input("admin@big-brain: ")

    if command.strip().lower() == 'exit':
        print('bye...')
        break

    if command.lower().strip() == 'clear':
        os.system('cls')
