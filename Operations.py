import random
from Enemy import Enemy
from Role import Role
from Stage import Stage
from Story import Story
import time
from colored import stylize
r = Role()
r.choose_role()
r.update_stat()
e = Enemy()
r.update_enemy_stats()


class Operations:
    
    def __init__(self): 
        self.max_hp = r.stat['Health']
        if(r.your_role == r.role[0] or r.your_role == r.role[2] or r.your_role == r.role[4]):
            self.max_stamina = r.stat['Stamina']

        else:
            self.max_magicka = r.stat['Magicka']

        self.steps = [0]

    def fight_equations(self, player_turn):
        atk = r.stat["Attack"]
        dfs = r.stat["Defense"]
        en_dfs = r.enemies_stat["Defense"]
        en_atk = r.enemies_stat["Attack"]
        if player_turn == True:
            equation = (atk*atk)//(atk+en_dfs)
            return equation
        else:
            equation = (en_atk*en_atk)//(en_atk+dfs)
            return equation

    def rest_equations(self):
        remaining_hp = self.max_hp-r.stat["Health"]
        r.stat["Health"] += remaining_hp
        if(r.your_role == r.role[0] or r.your_role == r.role[2] or r.your_role == r.role[4]):
            remaining_stamina = self.max_stamina-r.stat['Stamina']
            r.stat['Stamina'] += (remaining_stamina)

        elif(r.your_role == r.role[1] or r.your_role == r.role[3]):
            remaining_magicka = self.max_magicka-r.stat['Magicka']
            r.stat['Magicka'] += remaining_magicka

    def ask_player(self):
        a = 0
        while True:
            ask = input("\nDo you want to :  0.walk, 1.rest, 2.quit  ? ")
            if ask == '0' or ask == 'walk' or ask == 'w':
                self.steps[0] += 1
                if(self.steps[0] % 3 == 0):
                    w = random.choice(e.enemies)
                    r.update_enemy_stats(w)
                    if (self.steps[0] % 9 == 0):
                        w = random.choice(e.boss)
                        r.update_boss_stats(w)

                    print(f"\nYou have come across  {w} , FIGHT!!")

                    player_turn = True
                    enemy_turn = True
                    while player_turn or enemy_turn:

                        if r.your_role == "Knight":

                            while player_turn:
                                print(stylize("Your stats : ", colored.fg('green')))
                                for i, j in r.stat.items():
                                    print(f"{i} : {j} || ", end=" ")
                                i = input(
                                    "\nChoose an option : 1.Attack, 2.Dodge , 3.quit().....(Choose a number.)   ")
                                a = i
                                if i == '1':
                                    r.enemies_stat["Health"] -= self.fight_equations(
                                        player_turn)
                                    if(r.stat['Stamina'] < 1):
                                        r.stat['Health'] -= 2
                                    else:
                                        r.stat['Stamina'] -= 1

                                elif i == '2':
                                    print(
                                        "You will dodge some damage of the next attack and deal 60'%' of attack damage")
                                    r.enemies_stat['Health'] -= self.fight_equations(
                                        player_turn)*0.6
                                    r.enemies_stat['Health'] = int(
                                        r.enemies_stat['Health'])

                                    if(r.stat['Stamina'] < 1):
                                        r.stat['Health'] -= 2
                                    else:
                                        r.stat['Stamina'] -= 1
                                elif i == '3':
                                    q = input(
                                        "Are you sure you want to quit ? , all progress will be lost (Yes,No?) ")
                                    if q == "0" or q == "no":
                                        continue
                                    elif q == "1" or q == "yes":
                                        quit()

                                else:
                                    if i != '1' or i != '2' or i != '3':
                                        continue
                                enemy_turn = True
                                player_turn = False
                            print(stylize(f"{w} stats is : ",colored.fg('red')))
                            for i, j in r.enemies_stat.items():
                                print(f'{i}: {j} || ', end=" ")
                            if r.enemies_stat["Health"] <= 0:
                                print(f"\nYou have defeated {w}")

                                for i, j in r.stat.items():
                                    print(f"{i} : {j} || ", end=" ")
                                r.update_enemy_stats()
                                enemy_turn = False

                            while(enemy_turn):
                                print(f"\n{w} turn now!")
                                time.sleep(2)
                                if a == '1':
                                    r.stat['Health'] -= self.fight_equations(
                                        player_turn)
                                    if(w == e.enemies[0] or w == e.enemies[2] or w == e.enemies[3]):
                                        if(r.enemies_stat['Stamina'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Stamina'] -= 1
                                    elif(w == e.enemies[1]):

                                        if(r.enemies_stat['Magicka'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Magicka'] -= 1

                                elif a == '2':
                                    r.stat['Health'] -= (self.fight_equations(player_turn) //
                                                         r.stat['Dodge'])
                                    print(
                                        "You have dodged some damage of the attack")
                                    if(w == e.enemies[0] or w == e.enemies[2] or w == e.enemies[3]):
                                        if(r.enemies_stat['Stamina'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Stamina'] -= 1
                                    elif(w == e.enemies[1]):

                                        if(r.enemies_stat['Magicka'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Magicka'] -= 1
                                player_turn = True
                                enemy_turn = False
                            if(r.stat["Health"] <= 0):

                                print("You Died")
                                for i, j in r.stat.items():
                                    print(f"{i} : {j} || ", end=" ")
                                print(
                                    "\nYou lost, run the game again to restart it.")
                                quit()

                        elif r.your_role == "Warrior":
                            while player_turn:
                                print("Your stats : ")
                                for i, j in r.stat.items():
                                    print(f"{i} : {j} || ", end=" ")
                                i = input(
                                    "\nChoose an option : 1.Attack , 3.quit().....(Choose a number.)")

                                a = i
                                if i == '1':
                                    r.enemies_stat["Health"] -= self.fight_equations(
                                        player_turn)
                                    if(r.stat['Stamina'] < 1):
                                        r.stat['Health'] -= 2
                                    else:
                                        r.stat['Stamina'] -= 1
                                elif i == '2':
                                    print(
                                        f"You will endure 50'%' of {w} attack and deal 50'%' of attack damage.")
                                    r.enemies_stat['Health'] -= self.fight_equations(
                                        player_turn)*0.5
                                    r.enemies_stat['Health'] = int(
                                        r.enemies_stat['Health'])
                                    if(r.stat['Stamina'] < 1):
                                        r.stat['Health'] -= 2
                                    else:
                                        r.stat['Stamina'] -= 1

                                    if(r.stat['Stamina'] < 1):
                                        r.stat['Health'] -= 2
                                    else:
                                        r.stat['Stamina'] -= 1
                                elif i == '3':
                                    q = input(
                                        "Are you sure you want to quit ? , all progress will be lost (Yes,No?) ")
                                    if q == "0" or q == "no":
                                        continue
                                    elif q == "1" or q == "yes":
                                        quit()

                                else:
                                    if i != '1' or i != '2' or i != '3':
                                        continue

                                enemy_turn = True
                                player_turn = False
                            print(f'{w} stats is : ')
                            for i, j in r.enemies_stat.items():
                                print(f"{i}: {j} || ", end=" ")
                            if r.enemies_stat["Health"] <= 0:
                                print(f"\nYou have defeated {w}")

                                for i, j in r.stat.items():
                                    print(f"{i} : {j}", end=" ")
                                enemy_turn = False

                            while(enemy_turn):
                                print(f"\n{w} turn now!")
                                time.sleep(2)
                                if a == '1':
                                    r.stat['Health'] -= self.fight_equations(
                                        player_turn)
                                    if(w == e.enemies[0] or w == e.enemies[2] or w == e.enemies[3]):
                                        if(r.enemies_stat['Stamina'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Stamina'] -= 1
                                    elif(w == e.enemies[1]):

                                        if(r.enemies_stat['Magicka'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Magicka'] -= 1
                                elif a == '2':
                                    r.stat['Health'] -= self.fight_equations(player_turn) * \
                                        0.5
                                    if(w == e.enemies[0] or w == e.enemies[2] or w == e.enemies[3]):
                                        if(r.enemies_stat['Stamina'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Stamina'] -= 1
                                    elif(w == e.enemies[1]):

                                        if(r.enemies_stat['Magicka'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Magicka'] -= 1
                                player_turn = True
                                enemy_turn = False

                            if(r.stat["Health"] <= 0):

                                print("You Died")
                                for i, j in r.stat.items():
                                    print(f"{i} : {j} || ", end=" ")
                                print(
                                    "\nYou lost, run the game again to restart it.")
                                quit()

                        elif r.your_role == "Magician":
                            while player_turn:
                                print("Your stats : ")
                                for i, j in r.stat.items():
                                    print(f"{i} : {j} || ", end=" ")
                                i = input(
                                    "\nChoose an option : 1.Attack , 3.quit().....(Choose a number.)   ")
                                a = i
                                if i == '1':
                                    r.enemies_stat["Health"] -= self.fight_equations(
                                        player_turn)
                                    if(r.stat['Magicka'] < 1):
                                        r.stat['Health'] -= 2
                                    else:
                                        r.stat['Magicka'] -= 1

                                elif i == '3':
                                    q = input(
                                        "Are you sure you want to quit ? , all progress will be lost (Yes,No?) ")
                                    if q == "0" or q == "no":
                                        continue
                                    elif q == "1" or q == "yes":
                                        quit()

                                else:
                                    if i != '1' or i != '3':
                                        continue
                                enemy_turn = True
                                player_turn = False

                            print(f"{w} stats is : ")
                            for i, j in r.enemies_stat.items():
                                print(f'{i}: {j} || ', end=" ")
                            if r.enemies_stat["Health"] <= 0:
                                print(f"\nYou have defeated {w}")
                                for i, j in r.stat.items():
                                    print(f"{i} : {j}", end=" ")
                                enemy_turn = False

                            while(enemy_turn):
                                print(f"\n{w} turn now!")
                                time.sleep(2)
                                if a == '1':
                                    r.stat['Health'] -= self.fight_equations(
                                        player_turn)
                                    if(w == e.enemies[0] or w == e.enemies[2] or w == e.enemies[3]):
                                        if(r.enemies_stat['Stamina'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Stamina'] -= 1
                                    elif(w == e.enemies[1]):

                                        if(r.enemies_stat['Magicka'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Magicka'] -= 1

                                    player_turn = True
                                    enemy_turn = False
                            if(r.stat["Health"] <= 0):

                                print("You Died")
                                for i, j in r.stat.items():
                                    print(f"{i} : {j}", end=" ")
                                print(
                                    "\nYou lost, run the game again to restart it.")
                                quit()

                        elif r.your_role == "Healer":
                            while player_turn:
                                print("Your stats : ")
                                for i, j in r.stat.items():
                                    print(f"{i} : {j} || ", end=" ")
                                i = input(
                                    "\nChoose an option : 1.Attack , 2.Heal, 3.quit().....(Choose a number.)  ")
                                a = i
                                if i == '1':
                                    r.enemies_stat["Health"] -= self.fight_equations(
                                        player_turn)
                                    if(r.stat['Magicka'] < 1):
                                        r.stat['Health'] -= 2
                                    else:
                                        r.stat['Magicka'] -= 1
                                elif i == '2':
                                    while(r.stat['Health'] < self.max_hp):
                                        if(r.stat['Health'] > self.max_hp-r.stat['Healing']):
                                            r.stat['Health'] += (self.max_hp -
                                                                 r.stat['Health'])
                                        else:
                                            r.stat['Health'] += r.stat['Healing']
                                    if(r.stat['Magicka'] < 1):
                                        r.stat['Health'] -= 2
                                    else:
                                        r.stat['Magicka'] -= 1

                                elif i == '3':
                                    q = input(
                                        "Are you sure you want to quit ? , all progress will be lost (Yes,No?) ")
                                    if q == "0" or q == "no":
                                        continue
                                    elif q == "1" or q == "yes":
                                        quit()

                                else:
                                    if i != '1' or i != '2' or i != '3':
                                        continue
                                enemy_turn = True
                                player_turn = False
                            print(f"{w} stats is : ")
                            for i, j in r.enemies_stat.items():
                                print(f'{i}: {j} || ', end=" ")
                            if r.enemies_stat["Health"] <= 0:
                                print(f"\nYou have defeated {w}")

                                for i, j in r.stat.items():
                                    print(f"{i} : {j}", end=" ")
                                enemy_turn = False

                            while(enemy_turn):
                                print(f"\n{w} turn now!")
                                time.sleep(2)
                                if a == '1':
                                    r.stat['Health'] -= self.fight_equations(
                                        player_turn)
                                    if(w == e.enemies[0] or w == e.enemies[2] or w == e.enemies[3]):
                                        if(r.enemies_stat['Stamina'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Stamina'] -= 1
                                    elif(w == e.enemies[1]):

                                        if(r.enemies_stat['Magicka'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Magicka'] -= 1
                                elif a == '2':
                                    r.stat['Health'] -= self.fight_equations(
                                        player_turn)
                                    if(w == e.enemies[0] or w == e.enemies[2] or w == e.enemies[3]):
                                        if(r.enemies_stat['Stamina'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Stamina'] -= 1
                                    elif(w == e.enemies[1]):

                                        if(r.enemies_stat['Magicka'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Magicka'] -= 1
                                player_turn = True
                                enemy_turn = False
                            if(r.stat["Health"] <= 0):

                                print("You Died")
                                for i, j in r.stat.items():
                                    print(f"{i} : {j} || ", end=" ")
                                print(
                                    " \nYou lost, run the game again to restart it.")
                                quit()

                        elif r.your_role == "Assassin":
                            while player_turn:
                                print("Your stats : ")
                                for i, j in r.stat.items():
                                    print(f"{i} : {j} || ", end=" ")
                                i = input(
                                    "\nChoose an option : 1.Attack, 2.Flee , 3.quit().....(Choose a number.)   ")
                                a = i
                                if i == '1':
                                    r.enemies_stat["Health"] -= self.fight_equations(
                                        player_turn)
                                    if(r.stat['Stamina'] < 1):
                                        r.stat['Health'] -= 2
                                    else:
                                        r.stat['Stamina'] -= 1

                                elif i == '2':
                                    print(
                                        "You have 5'%' to flee from the battle and win it")

                                    if random.choice(range(1, 50)) == 4:
                                        print("FLEE SUCESS!!")
                                        print(f"{w} is defeated.")
                                        r.enemies_stat["Health"] = 0
                                    else:
                                        print("Flee failed")
                                    if(r.stat['Stamina'] < 1):
                                        r.stat['Health'] -= 2
                                    else:
                                        r.stat['Stamina'] -= 3
                                elif i == '3':
                                    q = input(
                                        "Are you sure you want to quit ? , all progress will be lost (Yes,No?) ")
                                    if q == "0" or q == "no":
                                        continue
                                    elif q == "1" or q == "yes":
                                        quit()

                                else:
                                    if i != '1' or i != '2' or i != '3':
                                        continue
                                player_turn = False
                                enemy_turn = True
                            print(f"{w} stats is : ")
                            for i, j in r.enemies_stat.items():
                                print(f'{i}: {j} || ', end=" ")

                            if r.enemies_stat["Health"] <= 0:
                                print(f"\nYou have defeated {w}")
                                for i, j in r.stat.items():
                                    print(f"{i} : {j}", end=" ")
                                enemy_turn = False

                            while(enemy_turn):
                                print(f"\n {w} turn now!")
                                time.sleep(2)
                                if a == '1':
                                    r.stat['Health'] -= self.fight_equations(
                                        player_turn)
                                    if(w == e.enemies[0] or w == e.enemies[2] or w == e.enemies[3]):
                                        if(r.enemies_stat['Stamina'] < 3):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Stamina'] -= 1
                                    elif(w == e.enemies[1]):

                                        if(r.enemies_stat['Magicka'] < 1):
                                            r.stat['Health'] -= 5
                                        else:
                                            r.enemies_stat['Magicka'] -= 3

                                elif a == '2':
                                    r.stat['Health'] -= self.fight_equations(
                                        player_turn)
                                    if(w == e.enemies[0] or w == e.enemies[2] or w == e.enemies[3]):
                                        if(r.enemies_stat['Stamina'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Stamina'] -= 1
                                    elif(w == e.enemies[1]):

                                        if(r.enemies_stat['Magicka'] < 1):
                                            r.stat['Health'] -= 2
                                        else:
                                            r.enemies_stat['Magicka'] -= 1
                                player_turn = True
                                enemy_turn = False
                            if(r.stat["Health"] <= 0):
                                print("You Died")
                                for i, j in r.stat.items():
                                    print(f"{i} : {j} || ", end=" ")
                                print(
                                    "\nYou lost, run the game again to restart it.")
                                quit()

                    continue
                S = Story()
                st = Stage()
                if(self.steps[0] == 1):
                    for i in S.the_beginning:
                        print(i, end="")
                        time.sleep(0.1)
                if(self.steps[0] == 2):
                    for i in S.step2:
                        print(i, end="")
                        time.sleep(0.1)
                if(self.steps[0] == 4):
                    for i in S.step4:
                        print(i, end="")
                        time.sleep(0.1)
                if(self.steps[0] == 10):
                    st.stage += 1
                    st.stage_up()
                if(self.steps[0] == 13):

                    for i in S.step13:
                        print(i, end="")
                        time.sleep(0.1)

                if(self.steps[0] == 19):
                    st.stage += 2
                    st.stage_up()
                if(self.steps[0] == 20):
                    for i in S.step20:
                        print(i, end="")
                        time.sleep(0.1)
                if(self.steps[0] == 22):

                    for i in S.step22:
                        print(i, end="")
                        time.sleep(0.1)
                if(self.steps[0] == 23):
                    print(
                        "CONGRATULATIONS, THIS IS YOUR LAST STEP, YOU HAVE COMPLETED THE GAME.")
                    quit()
            elif ask == '1' or ask == 'rest' or ask == 'r':
                if(r.stat["Health"] >= self.max_hp):
                    print(
                        "You  already have full health, you dont need to rest")
                else:
                    self.rest_equations()
                    print("Stats are refilled!")
            elif ask == '2' or ask == 'quit' or ask == 'q':
                print("Once you quit, you will lose all progress ")
                q = input("Are you sure you want to quit ?  ")
                if q == 'yes' or q == 'y':
                    exit()
                elif q == 'no' or q == 'n':
                    continue
                else:
                    print("I assume this as 'No' ")
                    continue
