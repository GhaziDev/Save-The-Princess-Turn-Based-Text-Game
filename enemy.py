
class Enemy:
    def __init__(self):
        self.enemies = ["Bandit", "Stone Monster", "Devassin"]
        self.boss = ["SHIELDOS", "SPARTAN", "BLODAS"]
        self.enemies_stat={}


    def update_enemy_stats(self, w=""):
        if w == "Bandit":
            self.enemies_stat = {"Attack": 10, "Defense": 6,
                                 "Health": 70, "Stamina": 9}  
        if w == "Stone Monster":
            self.enemies_stat = {"Attack": 8, "Defense": 10,
                                 "Health": 100, "Stamina": 8}  
        if w == "Devassin":
            self.enemies_stat = {"Attack": 15, "Defense": 2,
                                 "Health": 70, "Stamina": 11}
        return self.enemies_stat

    def update_boss_stats(self, w=""):
            if w == "SHIELDOS":
                self.enemies_stat = {"Attack": 9, "Defense": 16,
                                     "Health": 100, "Stamina": 9}
            if w == "SPARTAN":
                self.enemies_stat = {"Attack": 12, "Defense": 10,
                                     "Health": 110, "Stamina": 9}
            if w == "BLODAS":
                self.enemies_stat = {"Attack": 21, "Defense": 2,
                                     "Health": 66, "Stamina": 9}
            return self.enemies_stat
