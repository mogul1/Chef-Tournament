#Enters the shop where you can use your gold to buy things before a round starts.
import questions as input_h
import weapons as wep
data = {}

def data_load(equipment):
    global data
    data=equipment
def shop():
    print ("-------------------------------------------")
    print ("You have  now entered the blacksmith's store.")
    print ("-------------------------------------------")
    while True:
        x = input_h.int_input("You can either enter the store (by typing 1) or check your current equipment (by typing 2).")
        if x == 1:
            print ("You have entered the store.")
            from main import menu
            menu()
        if x == 2:
            print ("This is what your character currently has equipped.")
            print("------------------------------------------------------")
            wep.check_equipment(data["Weapon"],data["Shield"],data["Armor"],data["Leggings"],data["Helmet"],data["Boots"])
            print("------------------------------------------------------")
            input("press any key to go back to the previous menu.")
        else:
            print ("1 or 2 only!")
