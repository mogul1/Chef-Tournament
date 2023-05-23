#random module for RNG fun :)
import random

#Importing code from other py files in the same directory.
import questions as input_h
import fighters as fi
import shop_events as sh
import creator as cr
import weapons as wep

#This is the "Pool" of "Players" that will be pulled from when the game is first generated, you can add characters to it.
characters = [[5,2,3,15,"Tester1","Earth",20,4,0],[10,7,26,30,"Tester2","Discord",73,22,0]]
#Pool of weapons
weapons =[{"Name": "Golden Pan","QTY": 100,"SKILL":["Mana",40,"Fire",150],"WGT":15,"FIN":10,"IMP":75,"ID":["Weapon",0,500]},{"Name": "Chef Hat","QTY": 20,"SKILL":[],"WGT":2,"FIN":70,"IMP":15,"ID":["Helmet",1,250]}]
skills = []
round_count = 0
#This method handles the "Main Menu" where the user can choose to play a game, create a character or change any misc. settings.

def menu():
    while True:
        print(" ")
        Main_Menu = input_h.int_input("Tournament Game | 1: Play Game 2: Create Character Data ")
        print(" ")
        if Main_Menu > 0 and Main_Menu < 3:
            choose(Main_Menu)
        if Main_Menu > 3 or Main_Menu == 3:
            print("Not a valid choice, try again!")
            continue


def choose(option):
    choice = option
    Player_Total = 0
    length = len(characters)
    rng1= random.randrange(length)
    rng2= random.randrange(length)
    Stat_Names = ["VIT","AGI","STR","DEX","ATR","WIN"]

    print(option)

    #Duplicate protection, every fighter should be unique since it'd be boring to have the same person fighting each other (may change later)

    while rng2 == rng1:
        rng2 = random.randrange(length)
    Loop = 0
    
    #Choice 1 = "Play Game", choose characters from the pool, list them, create inventories for them and (of course) start the game.

    if choice == 1:
        print("RNG1: ",rng1,"RNG2: ",rng2)
        print(characters,"LENGTH: ",(len(characters)))
        global Player1
        global Player2
        Player1=fi.Chef(characters[rng1] [0],characters[rng1][1],characters[rng1][2],characters[rng1][3],characters[rng1][4],characters[rng1][5],characters[rng1][6],characters[rng1][7],characters[rng1][8])
        Player2=fi.Chef(characters[rng2] [0],characters[rng2][1],characters[rng2][2],characters[rng2][3],characters[rng2][4],characters[rng2][5],characters[rng2][6],characters[rng2][7],characters[rng2][8])
        Chef1_Properties= [Player1.VIT, Player1.AGI,Player1.STR, Player1.DEX, Player1.ATR, Player1.WIN]
        Chef2_Properties = [Player2.VIT, Player2.AGI,Player2.STR, Player2.DEX, Player2.ATR, Player2.WIN]
        if Player_Total < 2:
            print("PLAYER TOTAL:",Player_Total)
        if Player_Total == 0:
            print(Player1.NAME,"from ",Player1.HOME)
            print("-----")
            print("LVL: ",Player1.LVL)
            while Loop < len(Chef1_Properties):
                print(Stat_Names [Loop],": ",Chef1_Properties[Loop])
                Loop = Loop + 1  
            Player_Total = Player_Total+1
            print("PLAYER TOTAL:",Player_Total)
            Loop = 0
            print("-------------------")

        if Player_Total == 1:
            print(Player2.NAME,"from ",Player2.HOME)
            print("-----")
            print("LVL: ",Player2.LVL)
            while Loop < len(Chef2_Properties):
                print(Stat_Names [Loop],": ",Chef2_Properties[Loop])
                Loop = Loop + 1
            Player_Total = Player_Total+1
            print("PLAYER TOTAL:",Player_Total)
            Loop = 0
            print("-------------------")
        Player1.init_inv()
        Player2.init_inv()
        input("Press enter to start the game!")
        game_start()

    #Choice 2 = Create a character, self explanatory

    if choice == 2:
        characters.append(cr.create_character())

#Loads equipment for player and interacts with the shop_events.py
#This is where the pre fighting game stuff should happen.

def game_start():
    global round_count
    sh.data_load(Player1.equipment)
    choice = sh.enter_shop()
    if choice == "Cancel":
        menu()
    if round_count == 0:
        print("FIRST ROUND BONUS")
        print("-----------------")
        Player1.add_gold(500)
        round_count=round_count+1
    while True:
        new_bal = sh.browse_shop(Player1.money,weapons)
        if new_bal == "Continue":
            continue
        if new_bal == "Play":
            battle_start()
            break
        if new_bal == "Cancel":
            game_start()
        if type(new_bal) == list:
            if new_bal[0] == "GOLD":
                print(Player1.money,new_bal[1])
                Player1.money = new_bal[1]
                Player1.add_gold (2000)
                continue
        else:
            Player1.money = new_bal
            battle_start()
            break
#This is where all the fighting should happen
def battle_start():
    print("WHERE THE GAME TAKES PLACE")
    print(Player1.equipment["Weapon"],Player1.equipment["Shield"],Player1.equipment["Armor"],Player1.equipment["Leggings"],Player1.equipment["Helmet"],Player1.equipment["Boots"])
    input("TEST")
menu()
