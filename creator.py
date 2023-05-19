import questions as input_h

#This method "Loads" a character to the "Pool" of characters, initially meant for json files but too lazy :P
def create_character():
       Stat_Names = ["VIT","AGI","STR","DEX","ATR","WIN"]
       print(" ")
       #Initial prompt so you dont make a character by accident or have a chance to decide against it.
       while True:
           choice = input_h.str_input("Are you sure you'd like to create a new character? ")
           print(" ")
           if choice == "Yes" or choice == "yes":
               print("Creating Character....")
               break
           if choice == "No" or choice == "no":
               from main import menu
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
           
       #Add the name/homeland + Attribute stat (which currently is just the total of all stats)     
       print(temp_character)
       temp_number = sum(temp_character)
       temp_text = input_h.str_input("What will be the character's name?")
       temp_character.append(temp_text)
       temp_text = input_h.str_input("What land does this character come from?")
       temp_character.append(temp_text)    
       temp_character.append(temp_number)
       #Calculates the level based on the total number of stats the character has

       if temp_number == 4:
           temp_character.append(1)
       elif temp_number < 10 or temp_number == 10:
           temp_character.append(int(temp_number/2))
       elif temp_number < 100 and temp_number > 10:
           temp_character.append(int(temp_number/3-2))
       elif temp_number > 100:
           temp_character.append(int(temp_number/4))
       temp_character.append(0)
       print(temp_character)
       print("Added the character!")
       return (temp_character)
