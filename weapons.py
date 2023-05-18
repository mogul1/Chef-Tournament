

#This class represents the "Weapons" that the "Players" will be using.
#QTY = Quality (How good the weapon is), SKILL = Skill (Any extra abilities will be defined here), WGT = Weight (How heavy/light the weapon is),FIN = Finesse (How much the weapon scales with AGI/DEX vs STR, higher the number the more it scales with AGI/DEX)
#IMP = Impact (higher the number the more it scales with STR), ID = id (Position of Weapon in Weapon pool).

class Cookware():
    def __init__(self,QTY,SKILL,FIN,IMP, WGT,ID):
        self.QTY = QTY
        self.SKILL = SKILL
        self.WGT = WGT
        self.FIN = FIN
        self.IMP = IMP
        self.ID = ID

#Print out a list for what the current player has equipped (may change later based on how shop is designed)

def check_equipment():
    from __main__ import Player1
    print("Weapon: ",str(Player1.equipment["Weapon"]))
    print("Shield: ",str(Player1.equipment["Shield"]))
    print("Armor: ",str(Player1.equipment["Armor"]))
    print("Leggings: ",str(Player1.equipment["Leggings"]))
    print("Helmet: ",str(Player1.equipment["Helmet"]))
    print("Boots: ",str(Player1.equipment["Boots"]))


