import random
import sys
import time

class Enemy:
    
    def __init__(self,hp, attack_min, attack_max, name):
        self.enemy_hp = hp
        self.enemy_attack_min = attack_min
        self.enemy_attack_max = attack_max
        self.enemy_name = name

#Types of enemies 
goblin = Enemy(20, 1, 10,"Goblin")
guardian = Enemy(50, 10, 25, "Guardian")
dragon = Enemy(100,25,50,"Dragon")

class Rooms:

    def __init__(self):
        self.start_room = "Water"
        self.coor = [(0, 0)]
        self.direction = "f"
        self.room = 0
        self.hp = 100
        self.luck = 0.5
        self.attack_min = 0
        self.attack_max = 100
        self.cur_enemy = None
        self.cur_enemy_hp = 0
        self.list_of_items = []
    
    def typ_eff(self, text, speed):
        for char in text:
            if speed > 0:
                if char == " ":
                    print(char, end = "")
                else:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.02)
            else:
                if char == " ":
                    print(char, end = "")
                else:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.05)

    def init_text(self):
        self.start_room = random.choice(["Water", "Fire", "Dust"])
        print("\n")
        if self.start_room == "Water":
            text = "You wake up to a sound of dripping water from the ceiling.\nYour eyes barely adjust to the darkness around you.\nYou realize there're 4 exists out of this room.\nYou get up and start planning your next step.\n"
        elif self.start_room == "Fire":
            text = "You wake up to a sound of cracking fire.\nYour eyes barely adjust to the brightness around you.\nYou realize there're 4 exists out of this room.\nYou get up and start planning your next step.\n"
        elif self.start_room == "Dust":
            text = "You wake up to a smell of dust.\nYour rub your itchy eyes.\nYou realize there're 4 exists out of this room.\nYou get up and start planning your next step.\n"
        self.typ_eff(text, 0)
        self.step()
    
    def death(self):
        self.typ_eff("\n\nYou are dead...\n", 0)
        self.typ_eff("\nDo you want to restart?(Y/N)",1)
        if input(": ").lower() == "y":
            self.hp = 100
            self.luck = 0.5
            self.attack_min = 0
            self.attack_max = 100
            self.init_text()
        else:
            print(".....")
    
    def step(self):
        self.typ_eff("\nWhere are you headed?(F,B,L,R)",1)
        self.direction = input(": ").lower()
        if self.direction == "f":
            self.coor.append((self.coor[-1][0],self.coor[-1][1] + 1))
        elif self.direction == "b":
            self.coor.append((self.coor[-1][0],self.coor[-1][1] - 1))
        elif self.direction == "l":
            self.coor.append((self.coor[-1][0] - 1,self.coor[-1][1]))
        elif self.direction == "r":
            self.coor.append((self.coor[-1][0] + 1,self.coor[-1][1]))
        self.ran_room()
  
    def ran_room(self):
        self.room = random.randint(0,2)
        if self.room == 0:
            self.typ_eff("\nEmpty room...\n",1)
        elif self.room == 1:
            self.chest()
        else:
            self.enemy()
        if self.hp > 0:
            self.step()
    
    def chest(self):
        self.typ_eff("\nChest in front of you...",0)
        self.typ_eff("\nOpen it?(Y/N)",1)
        o_c = input(": ").lower()
        if o_c == "y":
            if random.randint(1,100) != 1:
                self.items(1)
            else:
                self.death()
        else:
            pass
    
    def items(self, chest):
        if random.choices(["lucky", "unlucky"],[self.luck,1]) == "lucky" or chest > 0:
            itms = {"Gauntlet":20, "Sword":10, "Shield":8, "Necklace":6, "Stone":4, "Fruit":2}
            attributes = ["Strength", "Health", "Luck"]
            b_db = ["Mysterious", "Enhanced","Weakened"]
            cur_itm = random.choice(list(itms.keys()))
            cur_attribute = random.choice(attributes)
            cur_b_db = random.choice(b_db) if random.randint(0,10) > 8 else None
            if cur_attribute == "Strength":
                self.attack_min += itms[cur_itm]
            elif cur_attribute == "Health":
                self.hp += itms[cur_itm]
            else:
                self.luck += 0.4
            item = f"{cur_b_db} {cur_itm} of {cur_attribute}"
            self.list_of_items.append(item)
            self.typ_eff(f"\nYou've aquired {item}\n",1)
        else:
            self.typ_eff("\nThis thing had nothing on it\n",1)

    def enemy(self):
        list_of_enemies = [goblin,guardian,dragon]
        self.cur_enemy = random.choice(list_of_enemies)
        self.cur_enemy_hp = self.cur_enemy.enemy_hp
        self.typ_eff(f"\nYou stumble upon a {self.start_room} {self.cur_enemy.enemy_name}\n",1)

        while self.hp > 0 and self.cur_enemy_hp > 0:
            self.typ_eff(f"\nEnemy hp: {self.cur_enemy_hp} \nPlayer hp: {self.hp}\n",1)
            self.typ_eff("\nAttack or Flee(A/F)",1)
            a_f = input(": ").lower()
            if a_f == "a":
                attack = random.randint(self.attack_min, self.attack_max)
                self.cur_enemy_hp -= attack
                self.typ_eff(f"\nYou did {attack} dmg",1)
            elif a_f == "f" and (random.randint(0,100) <= 50):
                self.typ_eff("\nYou succesfully fleed the battle!\n",0)
                self.step()
                break
            else:
                self.typ_eff("\nTry again next time",1)
            if self.cur_enemy_hp > 0:
                enemy_attack = random.randint(self.cur_enemy.enemy_attack_min, self.cur_enemy.enemy_attack_max)
                self.hp -= enemy_attack
                self.typ_eff(f"\nYou've been hit with {enemy_attack} dmg",1)

        if self.hp > 0:
            self.typ_eff("\n\nYou've succesfully defeated the enemy\n",0)
            self.hp = 100
            self.items(0)
        else:
            self.death()

game = Rooms()
game.init_text()

