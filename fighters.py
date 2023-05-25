#This class is for the "Players" who will be doing the fighting in the "Arena".

class Chef():

#Initializes the stats of a Chef instance

    def __init__(self,VIT,AGI,STR,DEX,NAME,HOME,ATR,LVL,WIN):
        self.VIT =VIT
        self.AGI =AGI
        self.STR = STR
        self.DEX = DEX
        self.NAME = NAME
        self.HOME = HOME
        self.ATR = ATR
        self.LVL = LVL
        self.WIN = WIN

#Initializes an inventory of a Chef instance, Money is an integer that represents the total gold available to a Chef to spend in the shop, Equipment is a dictionary that represents what the Chef is wearing.

    def init_inv(self):
        self.money = 0
        self.equipment = {"Weapon": "Unarmed", "Shield": "None","Armor": "Plain Clothes","Leggings":"Pants","Helmet": "Hat", "Boots":"Leather Sandles" }
#Adds money to the Chef instance's inventory based on value given for Gold.

    def add_gold(self, gold):
        print("CURRENT BALANCE: ",self.money)
        self.money = self.money + gold
        print("--------------------------")
        print("NEW BALANCE: ",self.money,"GOLD ADDED: ",gold)
        print("--------------------------")

#Takes money from the Chef instance's inventory and equips an item that shares the same name to the given equipment type.

    def buy_cookware(self,cost,cookware,equip_type):
        self.money = self.money - cost
        self.equip_item(cookware,equip_type)

#Checks the inventory (which is a dictionary) and updates the value of the given weapon type.

    def equip_item(self,cookware,equip_type):
        self.equipment.update(
            [
                (equip_type, cookware)
            ]
        )
