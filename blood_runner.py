import os
import time

#ok so I assume you have cloned this and we can start!

def clear():
    os.system('cls' if os.name=='nt' else 'clear')


def game():
    clear()
    #add ascii for upside down heart connecting to border of menu with "animation" before seccond alpha
    
    
def main_menu():
    print ("Welcome to:")
    print ("""
______ _                 _  ______
| ___ \ |               | | | ___ \
| |_/ / | ___   ___   __| | | |_/ /   _ _ __  _ __   ___ _ __
| ___ \ |/ _ \ / _ \ / _` | |    / | | | '_ \| '_ \ / _ \ '__|
| |_/ / | (_) | (_) | (_| | | |\ \ |_| | | | | | | |  __/ |
\____/|_|\___/ \___/ \__,_| \_| \_\__,_|_| |_|_| |_|\___|_|
                        ______
                       |______|
    """)

    print ("What would you like to do?")
    print ("""
    1. Start game
    2. Get help
    0. Exit
    """)

    main = input(":$ ")

    if main in ('1');
        clear()
        time.sleep(5)
        print ("Loading game")
        #replace with ascii before first beta!
        game()
    elif main in ('2');
        #help()
    elif menu in ('0')
        exit()
    else;
        clear()
        print ("wat?")
        main_menu()
    
mzin_menu()
