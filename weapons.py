

#This class represents the "Weapons" that the "Players" will be using.
#QTY = Quality (How good the weapon is), SKILL = Skill (Any extra abilities will be defined here) [Name,Resource, Resource_Cost,Effect_Type, Damage/Effect number,Cooldown(in seconds),Activation_Chance(%)], WGT = Weight (How heavy/light the weapon is),FIN = Finesse (How much the weapon scales with AGI/DEX, higher the number the more it scales with AGI/DEX)
#IMP = Impact (higher the number the more it scales with STR), ID = [Type, Where it is in weapon pool, Gold Cost].

class Cookware():
    def __init__(self,NAME,QTY,SKILL,FIN,IMP, WGT,ID):
        self.NAME = NAME
        self.QTY = QTY
        self.SKILL = SKILL
        self.WGT = WGT
        self.FIN = FIN
        self.IMP = IMP
        self.ID = ID
#Print out a list for what the current player has equipped (may change later based on how shop is designed)

def print_equipment(Weapon,Shield,Armor,Leggings,Helmet,Boots):
    print("Weapon: ",str(Weapon))
    print("Shield: ",str(Shield))
    print("Armor: ",str(Armor))
    print("Leggings: ",str(Leggings))
    print("Helmet: ",str(Helmet))
    print("Boots: ",str(Boots))

#equipment = Player's equipment, weapon_name = Weapon Pool
def look_up_equipment(equipment,weapon_name):
    x = 0
    length = len(weapon_name)
    print(weapon_name[x]["Name"],equipment,length)
    list_to_return =[]
    while x < length:
        wep_chosen = weapon_name[x]["Name"]
        equip_checked = equipment[weapon_name [x]["ID"][0]]
        if ( wep_chosen in equip_checked) is False:
            print(weapon_name[x],equip_checked)
            print("NOT EQUIPPED",wep_chosen)
            print(x,wep_chosen,equip_checked)
            x = x+1
        if (wep_chosen in equip_checked)is True:
            print(weapon_name[x], equip_checked)
            print("IS EQUIPPED",wep_chosen,equip_checked)
            list_to_return.append(weapon_name[x])
            x = x+1
    print("END RESULT",list_to_return)
    return associate_equipment(list_to_return)
    
def associate_equipment(equip):
    global wep_objects
    wep_objects ={}
    x = 0
    for x in range(len(equip)):
        wep_objects[equip[x]["Name"]] = Cookware(equip[x]["Name"],equip[x]["QTY"],equip[x]["SKILL"],equip[x]["WGT"],equip[x]["FIN"],equip[x]["IMP"],equip[x]["ID"])
        print(wep_objects)
        x=x+1
    return wep_objects
