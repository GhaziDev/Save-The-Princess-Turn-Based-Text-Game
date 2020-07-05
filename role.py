from enemy import Enemy
import random
import colored
from colored import stylize


class Role:#only for player
    def __init__(self):
        self.e = Enemy()
        self.role = {0: "Knight", 1: "Magician",
                     2: "Warrior", 3: "Healer", 4: "Assassin"}
        self.stat = {"Attack": 0, "Defense": 0,
                         "Health": 0,"Stamina": 0}
        self.points = 5
    def update_stat(self):
        while self.points > 0:
            print('\n')
            print(
                f"\nYou have {self.points} points to spend and update your stat\n ")
            print(f"\nStat -> 0.Attack : {self.stat['Attack']}, 1.Defense : {self.stat['Defense']}, 2.Health :{self.stat['Health']} ,3.Stamina : {self.stat['Stamina']} ")

            add = input("\nWhat do you want to spend on ? ")

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

        print("\nYou spent all your points , the game has STARTED")

