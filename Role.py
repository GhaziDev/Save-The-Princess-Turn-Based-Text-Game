from Enemy import Enemy
import random
from colored import stylize


class Role:
    def __init__(self):
        self.e = Enemy()
        self.role = {0: "Knight", 1: "Magician",
                     2: "Warrior", 3: "Healer", 4: "Assassin"}
        self.your_role = " "
        self.stat = {}
        self.points = 5
        self.enemies_stat = {}
        self.your_level = 1
        self.xp = 0
        self.max_level = 6

    def choose_role(self):
        for i, j in self.role.items():
            print("->",i, j)
        self.roles = input("Choose your Role :  ")
        while True:
            if self.roles == "K".lower() or self.roles == '0' or self.roles == "Knight".lower():
                self.your_role = self.role[0]
                print("You choose 'Knight' role  ")
                break

            elif self.roles == "M".lower() or self.roles == '1' or self.roles == "Magician".lower():
                self.your_role = self.role[1]
                print("You choose 'Magician' role  ")
                break

            elif self.roles == "W".lower() or self.roles == '2' or self.roles == "Warrior".lower():
                self.your_role = self.role[2]
                print("You choose 'Warrior' role")
                break

            elif self.roles == "H".lower() or self.roles == '3' or self.roles == "Healer".lower():
                self.your_role = self.role[3]
                print("You choose 'Healer' role")
                break

            elif self.roles == "A".lower() or self.roles == '4' or self.roles == "Assassin".lower():
                self.your_role = self.role[4]
                print("You choose 'Assassin' role")
                break

            else:
                self.roles = input(
                    "Wrong input, please enter with first role character or with the number assigned to role  : ")

    def update_stat(self):
        if self.your_role == self.role[0]:
            self.stat = {"Attack": 12, "Defense": 5,
                         "Health": 110, "Dodge": 8, "Stamina": 10}
            print(stylize("This is your Stat :  ",colored.fg('green')))
            for i, j in self.stat.items():
                print(f"{i}:{j}",'||',end=" ")

        elif self.your_role == self.role[1]:
            self.stat = {"Attack": 15, "Defense": 9,
                         "Health": 90, "Magicka": 12}
            print("This is your Stat :  ")
            for i, j in self.stat.items():
                print(f"{i}:{j}")

        elif self.your_role == self.role[2]:
            self.stat = {"Attack": 8, "Defense": 10,
                         "Health": 130, "Stamina": 9}
            print("This is your Stat :  ")

            for i, j in self.stat.items():
                print(f"{i}:{j}")

        elif self.your_role == self.role[3]:
            self.stat = {"Attack": 10, "Defense": 4,
                         "Health": 105, "Magicka": 12, "Healing": 15, }
            print("This is your Stat :  ")

            for i, j in self.stat.items():
                print(f"{i}:{j}")

        elif self.your_role == self.role[4]:
            self.stat = {"Attack": 20, "Defense": 2,
                         "Health": 70, "Dodge": 7, "Stamina": 11}
            print("This is your Stat :  ")

            for i, j in self.stat.items():
                print(f"{i}:{j}")

        while self.points > 0:
            print('\n')
            print(
                f"You have {self.points} points to spend and update your stat ")

            if self.your_role == self.role[3]:
                print(
                    f"Stat -> 0.Attack : {self.stat['Attack']}, 1.Defense : {self.stat['Defense']}, 2.Health :{self.stat['Health']} ,3.Magicka : {self.stat['Magicka']},4.Healing :{self.stat['Healing']}")
                add = input("What do you want to spend on ? ")

                if add == '0' or add == "Attack".lower():
                    self.stat['Attack'] += 1
                    self.points -= 1
                elif add == '1' or add == "Defense".lower():
                    self.stat['Defense'] += 1
                    self.points -= 1

                elif add == '2' or add == "Health".lower():
                    self.stat['Health'] += 2
                    self.points -= 1

                elif add == '3' or add == "Magicka".lower():
                    self.stat['Magicka'] += 1
                    self.points -= 1

                elif add == '4' or add == "Healing".lower():
                    self.stat['Healing'] += 1
                    self.points -= 1

                else:
                    continue
            elif self.your_role == self.role[1]:
                print(
                    f"Stat -> 0.Attack : {self.stat['Attack']}, 1.Defense : {self.stat['Defense']}, 2.Health :{self.stat['Health']} ,3.Magicka : {self.stat['Magicka']}")
                add = input("What do you want to spend on ? ")
                if add == '0' or add == "Attack".lower():
                    self.stat['Attack'] += 1
                    self.points -= 1

                elif add == '1' or add == "Defense".lower():
                    self.stat['Defense'] += 1
                    self.points -= 1

                elif add == '2' or add == "Health".lower():
                    self.stat['Health'] += 2
                    self.points -= 1

                elif add == '3' or add == "Magicka".lower():
                    self.stat['Magicka'] += 1
                    self.points -= 1

                else:
                    continue

            elif self.your_role == self.role[0] or self.your_role == self.role[4]:
                print(
                    f"Stat -> 0.Attack : {self.stat['Attack']}, 1.Defense : {self.stat['Defense']}, 2.Health :{self.stat['Health']} ,3.Stamina : {self.stat['Stamina']} ")

                add = input("What do you want to spend on ? ")

                if add == '0' or add == "Attack".lower():
                    self.stat['Attack'] += 1
                    self.points -= 1

                elif add == '1' or add == "Defense".lower():
                    self.stat['Defense'] += 1
                    self.points -= 1

                elif add == '2' or add == "Health".lower():
                    self.stat['Health'] += 2
                    self.points -= 1

                elif add == '3' or add == "Stamina".lower():
                    self.stat['Stamina'] += 1
                    self.points -= 1

                else:
                    continue
            elif self.your_role == self.role[2]:
                print(
                    f"Stat -> 0.Attack : {self.stat['Attack']}, 1.Defense : {self.stat['Defense']}, 2.Health :{self.stat['Health']} ,3.Stamina : {self.stat['Stamina']} ")

                add = input("What do you want to spend on ? ")

                if add == '0' or add == "Attack".lower():
                    self.stat['Attack'] += 1
                    self.points -= 1

                elif add == '1' or add == "Defense".lower():
                    self.stat['Defense'] += 1
                    self.points -= 1

                elif add == '2' or add == "Health".lower():
                    self.stat['Health'] += 2
                    self.points -= 1

                elif add == '3' or add == "Stamina".lower():
                    self.stat['Stamina'] += 1
                    self.points -= 1

                else:
                    continue

        print("You spent all your points , the game has STARTED")

    def update_enemy_stats(self, w=None):
        if w == "Bandit":
            self.enemies_stat = {"Attack": 9, "Defense": 6,
                                 "Health": 75, "Stamina": 9}  # health=75
        if w == "Witch":
            self.enemies_stat = {"Attack": 12, "Defense": 3,
                                 "Health": 70, "Magicka": 12}  # health=70
        if w == "Stone Monster":
            self.enemies_stat = {"Attack": 8, "Defense": 10,
                                 "Health": 90, "Stamina": 8}  # health:100
        if w == "Devassin":
            self.enemies_stat = {"Attack": 15, "Defense": 2,
                                 "Health": 70, "Stamina": 11}  # health=70

    def update_boss_stats(self, w=None):
            if w == "SHIELDOS":
                self.enemies_stat = {"Attack": 8, "Defense": 18,
                                     "Health": 100, "Stamina": 9}
            if w == "SPARTAN":
                self.enemies_stat = {"Attack": 8, "Defense": 10,
                                     "Health": 110, "Stamina": 9}
            if w == "BLODAS":
                self.enemies_stat = {"Attack": 21, "Defense": 2,
                                     "Health": 65, "Stamina": 9}
            if w == "MAGIC-FATHER":
                self.enemies_stat = {"Attack": 15, "Defense": 2,
                                     "Health": 90, "Magicka": 9}
