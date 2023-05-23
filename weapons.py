

#This class represents the "Weapons" that the "Players" will be using.
#QTY = Quality (How good the weapon is), SKILL = Skill (Any extra abilities will be defined here) [Resource, Resource_Cost,Effect_Type, Damage/Effect number], WGT = Weight (How heavy/light the weapon is),FIN = Finesse (How much the weapon scales with AGI/DEX, higher the number the more it scales with AGI/DEX)
#IMP = Impact (higher the number the more it scales with STR), ID = [Type, Where it is in weapon pool, Gold Cost].

class Cookware():
    def __init__(self,QTY,SKILL,FIN,IMP, WGT,ID):
        self.QTY = QTY
        self.SKILL = SKILL
        self.WGT = WGT
        self.FIN = FIN
        self.IMP = IMP
        self.ID = ID

#Print out a list for what the current player has equipped (may change later based on how shop is designed)

def check_equipment(Weapon,Shield,Armor,Leggings,Helmet,Boots):
    print("Weapon: ",str(Weapon))
    print("Shield: ",str(Shield))
    print("Armor: ",str(Armor))
    print("Leggings: ",str(Leggings))
    print("Helmet: ",str(Helmet))
    print("Boots: ",str(Boots))


