#random module for RNG fun :)
import random

#Importing code from other py files in the same directory.
import questions as input_h
import fighters as f
import weapons as wep

#Convenient list of strings that we can reference when we want to print out stats for a character.
Stat_Names = ["VIT","AGI","STR","DEX","ATR","WIN"]

#This is the "Pool" of "Players" that will be pulled from when the game is first generated, you can add characters to it.
characters = [[5,2,3,15,"Tester1","Earth",20,4,0],[10,7,26,30,"Tester2","Discord",73,22,0]]


#This method "Loads" a character to the "Pool" of characters, initially meant for json files but too lazy :P

def create_character():
       print(" ")
       #Initial prompt so you dont make a character by accident or have a chance to decide against it.

       while True:
           choice = input_h.str_input("Are you sure you'd like to create a new character? ")
           print(" ")
           if choice == "Yes" or choice == "yes":
               print("Creating Character....")
               break
           if choice == "No" or choice == "no":
               menu()
               break
       # Loop = local iterate variable, temp_character = local list variable to store character data to be added to the greater "Pool" once completed.

       loop = 0
       temp_character = []

       #Prompt for every stat for the custom character that can't be calculated given existing stats

       while loop < len(Stat_Names)-2:
           temp_number = input_h.int_input("Input a stat for: " + Stat_Names[loop])
           if temp_number > 99 or temp_number < 1:
            print("Invalid Number")
            continue
           temp_character.append(temp_number)
           print (temp_character,loop)
           loop = loop + 1
           print (temp_character)
           
       #Add the name/homeland + Attribute stat (which currently is just the total of all stats)     

       temp_number = sum(temp_character)
       temp_text = input_h.str_input("What will be the character's name?")
       temp_character.append(temp_text)
       temp_text = input_h.str_input("What land does this character come from?")
       temp_character.append(temp_text)    
       temp_character.append(temp_number)
       characters.append(temp_character)
       print("TEST: ",temp_character,"TEST2",characters)
       #Calculates the level based on the total number of stats the character has

       if temp_number == 4:
           temp_character.append(1)
       elif temp_number < 10 or temp_number == 10:
           temp_character.append(int(temp_number/2))
       elif temp_number < 100 and temp_number > 10:
           temp_character.append(int(temp_number/3-2))
       elif temp_number > 100:
           temp_character.append(int(temp_number/4))
       print("TEST: ",temp_character,"TEST2",characters)
       temp_character.append(0)
       print("TEST: ",temp_character,"TEST2:",characters)
       print("Added the character!")
       print(characters)
       menu()

#This method handles the "Main Menu" where the user can choose to play a game, create a character or change any misc. settings.

def menu():
    while True:
        print(" ")
        Main_Menu = input_h.int_input("Tournament Game | 1: Play Game 2: Create Character Data ")
        print(" ")
        if Main_Menu > 0 and Main_Menu < 3:
            choose(Main_Menu)
            break
        if Main_Menu > 3 or Main_Menu == 3:
            print("Not a valid choice, try again!")
            continue


def choose(option):
    choice = option
    Player_Total = 0
    length = len(characters)
    rng1= random.randrange(length)
    rng2= random.randrange(length)

    #Duplicate protection, every fighter should be unique since it'd be boring to have the same person fighting each other (may change later)

    while rng2 == rng1:
        rng2 = random.randrange(length)
    Loop = 0

    #Choice 1 = "Play Game", choose characters from the pool, list them, create inventories for them and (of course) start the game.

    if choice == 1:
        global Player1
        global Player2
        Player1=f.Chef(characters[rng1] [0],characters[rng1][1],characters[rng1][2],characters[rng1][3],characters[rng1][4],characters[rng1][5],characters[rng1][6],characters[rng1][7],characters[0][8])
        Player2=f.Chef(characters[rng2] [0],characters[rng2][1],characters[rng2][2],characters[rng2][3],characters[rng2][4],characters[rng2][5],characters[rng2][6],characters[rng2][7],characters[rng2][8])
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
        create_character()

#Starts the game, currently has the same fuctionality as the shop() but will change later.

def game_start():
    shop()

#Enters the shop where you can use your gold to buy things before a round starts.

def shop():
    print ("-------------------------------------------")
    print ("You have  now entered the blacksmith's store.")
    print ("-------------------------------------------")
    while True:
        x = input_h.int_input("You can either enter the store (by typing 1) or check your current equipment (by typing 2).")
        if x == 1:
            print ("You have entered the store.")
            menu()
        if x == 2:
            print ("This is what your character currently has equipped.")
            print("------------------------------------------------------")
            wep.check_equipment()
            print("------------------------------------------------------")
            input("press any key to go back to the previous menu.")
        else:
            print ("1 or 2 only!")
menu()

