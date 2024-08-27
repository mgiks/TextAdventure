import random
import sys
import time

def typeText(text, speed):
    delay = 0
    
    match speed:
        case 2:
            delay = 0.035
        case 3:
            delay = 0.02
        case _:
            delay = 0.05
    
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        if character == " ":
            continue
        time.sleep(delay)

class Player:
    coordinates = [(0,0)]
    
    @classmethod
    def step(cls):
        typeText("\nWhere are you headed?(F,B,L,R): ", 2)
        direction = input().lower()
        
        match direction:
            case "b":
                print("Go back")
                cls.coordinates.append((cls.coordinates[-1][0],cls.coordinates[-1][1] - 1))
            case "l":
                print("Go left")
                cls.coordinates.append((cls.coordinates[-1][0] - 1,cls.coordinates[-1][1]))
            case "r":
                print("Go right")
                cls.coordinates.append((cls.coordinates[-1][0] + 1,cls.coordinates[-1][1]))
            case _:
                print("Go forward")
                cls.coordinates.append((cls.coordinates[-1][0],cls.coordinates[-1][1] + 1))
            
    @classmethod
    def openChest(cls):
        typeText("\nChest in front of you...",0)
        typeText("\nOpen it?(Y/N): ",1)
        choice = input().lower()
        
        if choice == "y":
            if random.randint(1,100) != 1:
                #placeholder for some action
                pass
            else:
                cls.die()
        else:
            pass
    
    @classmethod
    def die(self):
        typeText("\n\nYou are dead...\n", 0)
        typeText("\nDo you want to restart?(Y/N): ",1)
        choice = input().lower()
        if choice == "y":
            pass
        else:
            print(".....")
            
# class Item:
#     def items(self, chest):
#         if random.choices(["lucky", "unlucky"],[self.luck,1]) == "lucky" or chest > 0:
#             itms = {"Gauntlet":20, "Sword":10, "Shield":8, "Necklace":6, "Stone":4, "Fruit":2}
#             attributes = ["Strength", "Health", "Luck"]
#             b_db = ["Mysterious", "Enhanced","Weakened"]
#             cur_itm = random.choice(list(itms.keys()))
#             cur_attribute = random.choice(attributes)
#             cur_b_db = random.choice(b_db) if random.randint(0,10) > 8 else None
#             if cur_attribute == "Strength":
#                 self.attack_min += itms[cur_itm]
#             elif cur_attribute == "Health":
#                 self.hp += itms[cur_itm]
#             else:
#                 self.luck += 0.4
#             item = f"{cur_b_db} {cur_itm} of {cur_attribute}"
#             self.list_of_items.append(item)
#             typeText(f"\nYou've aquired {item}\n",1)
#         else:
#             typeText("\nThis thing had nothing on it\n",1)

class Room():
    element = []
    
    @staticmethod
    def enterStartRoom():  
        Player.coordinates = [(0, 0)]      
        element = random.choice(["Water", "Fire", "Dust"])
        
        match element:
            case "Water":
                text = ("You wake up to the sound of dripping water from the ceiling."
                        "Your eyes barely adjust to the darkness around you.")
            case "Fire":
                text = """You wake up to the sound of crackling fire.
                Your eyes barely adjust to the brightness around you.\n"""
            case "Dust":
                text = """You wake up to the smell of dust.
                        Your rub your itchy eyes.\n"""
                        
        text += """You get up and start planning your next step.
        You realize there're 4 exists out of this room."""
        typeText(text, 1)
                
        Player.step()


# class Enemy:
#     def __init__(self, element, enemy_type, hp, min_attack, max_attack):
#         self.name = element + " " + enemy_type
#         self.hp = hp
#         self.min_attack = min_attack
#         self.max_attack = max_attack

#     def fight(self):

#         while self.hp > 0 and self.cur_enemy_hp > 0:
#             a_f = input(": ").lower()
#             if a_f == "a":
#                 attack = random.randint(self.attack_min, self.attack_max + 1)
#                 self.cur_enemy_hp -= attack
#                 typeText(f"\nYou did {attack} dmg",1)
#             elif a_f == "f" and (random.randint(0,100) <= 50):
#                 typeText("\nYou succesfully fleed the battle!\n",0)
#                 self.step()
#                 break
#             else:
#                 typeText("\nTry again next time",1)
#             if self.cur_enemy_hp > 0:
#                 enemy_attack = random.randint(self.cur_enemy.enemy_attack_min, self.cur_enemy.enemy_attack_max)
#                 self.hp -= enemy_attack
#                 typeText(f"\nYou've been hit with {enemy_attack} dmg",1)

#         if self.hp > 0:
#             typeText("\n\nYou've succesfully defeated the enemy\n",0)
#             self.hp = 100
#             self.items(0)
#         else:
#             self.death()
    
# class Room:
#     def __init__(self):
#         self.start_room = ""
#         self.coordinates = [(0, 0)]
#         self.direction = "f"
#         self.room = 0
#         self.hp = 100
#         self.luck = 0.5
#         self.attack_min = 0
#         self.attack_max = 100
#         self.cur_enemy = None
#         self.cur_enemy_hp = 0
#         self.list_of_items = []
    
  
#     def randomRoom(self):
#         self.room = random.randint(0,2)
#         if self.room == 0:
#             typeText("\nEmpty room...\n",1)
#         elif self.room == 1:
#             self.chest()
#         else:
#             self.enemy()
#         if self.hp > 0:
#             self.step()

#     def enemyRoom(self):
#         typeText(f"\nEnemy hp: {self.cur_enemy_hp} \nPlayer hp: {self.hp}\n",1)
#         typeText("\nAttack or Flee(A/F)",1)
