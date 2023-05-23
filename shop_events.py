#Enters the shop where you can use your gold to buy things before a round starts.
import questions as input_h
import weapons as wep
data = {}

# Loads the "equipment" dictionary from a Player entity
def data_load(equipment):
    global data
    data=equipment

# The first menu of the shop
def enter_shop():
    print ("-------------------------------------------")
    print ("You have  now entered the blacksmith's store.")
    print ("-------------------------------------------")
    while True:
        x = input_h.int_input("You can enter the store (by typing 1), check your current equipment (by typing 2) or go back to the previous menu (by typing 3).")
        if x == 1:
            print ("You have entered the store.")
            return True
        if x == 2:
            print ("This is what your character currently has equipped.")
            print("------------------------------------------------------")
            wep.check_equipment(data["Weapon"],data["Shield"],data["Armor"],data["Leggings"],data["Helmet"],data["Boots"])
            print("------------------------------------------------------")
            input("press any key to go back to the previous menu.")
        if x == 3:
            return "Cancel"
        else:
            print ("Not a valid choice.")

# The second menu of the shop, money == current money of the relevant player entity, shop_inv == Pool of weapons
def browse_shop(money,shop_inv):
    while True:
            print("You have",money," Gold.")
            shop_size = len(shop_inv)
            x = 0
            print("------------------------")
            while x < shop_size:
                print(x,": ","NAME: ",shop_inv[x]["Name"],"COST: ",shop_inv[x]["ID"][2])
                x = x + 1
            print("------------------------")
            print("Welcome to the shop!")
            print("------------------------")
            print("Type ",x,"to continue without purchasing, Type ",x+1,"to return to previous menu.")
            print("------------------------")
            choice = input_h.int_input("Would you like to buy any of this equipment? (Type the number of the corresponding equipment.)")
        #Shop size is always +1 of the actual number of weapons due to how len works, so options will always be greater than the list of weapons and wont overlap.
            if choice == shop_size:
                return "Play"
            if choice == shop_size+1:
                return "Cancel"
            elif choice > shop_size or choice < 0:
                continue
            elif choice > -1 or choice < shop_size:
                if money - shop_inv[choice]["ID"][2] < 0:
                    print ("Not enough gold.")
                    end_check = end_shop(money)
                    if end_check == "Continue":
                        continue
                    else:
                        return end_check
                elif shop_inv[choice]["Name"] == data [shop_inv[choice]["ID"][0]]:
                    print ("DUPLICATE: ",data [shop_inv[choice]["ID"][0]],"IS THE SAME AS",shop_inv[choice]["Name"])
                    end_check = end_shop(money)
                    if end_check == "Continue":
                        continue
                    else:
                        return end_check
                else:
                    data [shop_inv[choice]["ID"][0]] = shop_inv[choice]["Name"]
                    money = money - shop_inv[choice]["ID"][2]
                    print("Balance is now: ",money)
                    print(shop_inv[choice]["ID"][0],"is now ",shop_inv[choice]["Name"])
                    end_check = end_shop(money)
                    if end_check == "Continue":
                        continue
                    else:
                        return end_check
        
def end_shop(money):
    while True:
        choice = input_h.str_input("Would you like to continue shopping?")
        if choice == "Yes" or  choice =="yes":
            return "Continue"
        if choice == "No" or choice == "no":
            return money
        if choice == "money":
            new_gold = ["GOLD",money]
            return new_gold
        else:
            print("INVALID")
            continue
    
