import random
from enemy import Enemy
from role import Role
import time
import colored
from colored import stylize
from knight import Knight
from warrior import Warrior
from assassin import Assassin
from story import Story
S=Story()
r = Role()
e = Enemy()
def choose_role():
        while(True):
            print(stylize("->1.KNIGHT\n\n->2.WARRIOR\n\n->3.ASSASSSIN",colored.fg('dark_cyan')))
            role=input("\nPick the role you want to play :  ").lower()
            if role=='k' or role=='knight' or role=='1':
                k=Knight()
                r.stat=k.stat
                r.update_stat()

                break
            elif role=='w' or role=='warrior' or role=='2':
                w=Warrior()
                r.stat=w.stat
                r.update_stat()
                break
            elif role=='a' or role=='assassin' or role=='3':
                a=Assassin()
                r.stat=a.stat
                r.update_stat()
                break
            else:
                print("Wrong input, please pick the number of role or pick its name.")
                continue
choose_role()



class Operations:

    def __init__(self): 
        self.max_hp = r.stat['Health']
        self.max_stamina = r.stat['Stamina']
        self.steps=0
        self.scenario=[S.step2,S.step4,S.step6,S.step8,S.step10]


    def fight_equations(self, player_turn):
        atk = r.stat["Attack"]
        dfs = r.stat["Defense"]
        en_dfs = e.enemies_stat["Defense"]
        en_atk = e.enemies_stat["Attack"]
        if player_turn == True:
            equation = (atk*atk)//(atk+en_dfs)
            return equation
        else:
            equation = (en_atk*en_atk)//(en_atk+dfs)
            return equation

    def rest_equations(self):
        remaining_hp = self.max_hp-r.stat["Health"]
        r.stat["Health"] += remaining_hp/2
        remaining_stamina = self.max_stamina-r.stat['Stamina']
        r.stat['Stamina'] += (remaining_stamina)

    def ask_player(self):
        a = 0
        progression=-1
        enemy_key=0
        while True:
            enemy_turn=False
            player_turn=False
            ask = input(stylize("\nDo you want to :  0.walk, 1.rest, 2.quit  ? ",colored.fg('blue'))).lower()
            if ask == '0' or ask == 'walk' or ask == 'w':
                self.steps += 1
                if self.steps==11:
                    print("CONGRATULATIONS!!!, YOU HAVE COMPLETED THE GAME!!!")
                    break
                elif self.steps==1:
                    for i in S.the_beginning:
                        print(i,end="")
                        #time.sleep(0.1)
                elif self.steps % 2 == 0:
                    if progression<len(self.scenario):
                        progression+=1
                        for i in self.scenario[progression]:
                            print(i,end="")
                if self.steps%3==0 and self.steps/3>self.steps//9:
                    w = random.choice(e.enemies)
                    enemy_key=e.update_enemy_stats(w)
                    enemy_turn,player_turn=True,True        
                    if self.steps % 9 == 0 and self.steps/9<self.steps/3:
                            w = random.choice(e.boss)
                            enemy_key=e.update_boss_stats(w)
                            enemy_turn,player_turn=True,True
                    print(stylize(f"\nyou are facing a {w}",colored.fg('orchid')))  

                while player_turn or enemy_turn:
                        while player_turn:
                                print(stylize("\nYour stats : ",colored.fg('green')))
                                for i, j in r.stat.items():
                                    print(f"{i} : {j} || ", end=" ")
                                i = input(
                                    "\nChoose an option : 1.Attack, 2.quit().....(Choose a number.)   ")
                                a = i
                                if i == '1':
                                    enemy_key["Health"] -= self.fight_equations(
                                        player_turn)
                                    if(r.stat['Stamina'] < 1):
                                        r.stat['Health'] -= 2
                                    else:
                                        r.stat['Stamina'] -= 1

                                elif i == '2':
                                    q = input(
                                        "Are you sure you want to quit ? , all progress will be lost (Yes,No?) ")
                                    if q == "0" or q == "no":
                                        continue
                                    elif q == "1" or q == "yes":
                                        quit()

                                else:
                                    if i != '1' or i != '2' :
                                        continue
                                enemy_turn=True
                                player_turn = False
                        print(stylize(f"\n{w} stats is : ",colored.fg("red")))
                        for i, j in enemy_key.items():
                                print(f'{i}: {j} || ', end=" ")

                        if enemy_key["Health"] <= 0:
                            print(f"\nYou have defeated {w}")
                            for i, j in r.stat.items():
                                print(f"{i} : {j}", end=" ")
                            print('\n')
                            enemy_turn = False

                        while(enemy_turn):
                            print(stylize(f"\n{w} turn now!",colored.fg("plum_4")))
                            time.sleep(1)
                            if a == '1':
                                r.stat['Health'] -= self.fight_equations(
                                    player_turn)
                                if(enemy_key['Stamina'] < 3):
                                    r.stat['Health'] -= 2
                                else:
                                    enemy_key['Stamina'] -= 1
                            player_turn = True
                            enemy_turn = False
                        if(r.stat["Health"] <= 0):
                            print("\nYou Died")
                            for i, j in r.stat.items():
                                print(f"{i} : {j} || ", end=" ")
                            print(stylize(
                                "\nYou lost, run the game again to restart it.",colored.fg('green_yellow')))
                            quit()        
                continue
            if ask == '1' or ask == 'rest' or ask == 'r':

                if(r.stat["Health"] >= self.max_hp/2):
                    print(
                        "\nYou already have 50'%' or more of your health, you dont need to rest")
                else:
                    self.rest_equations()
                    print("\nStats are refilled!")
            elif ask == '2' or ask == 'quit' or ask == 'q':
                print("\nOnce you quit, you will lose all progress ")
                q = input("Are you sure you want to quit ?  ")
                if q == 'yes' or q == 'y':
                    exit()
                elif q == 'no' or q == 'n':
                    continue
                else:
                    print("\nI assume this as 'No' ")
                    continue
