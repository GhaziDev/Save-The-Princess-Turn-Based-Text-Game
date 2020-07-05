from role import Role
class Warrior(Role):
    def __init__(self):
        super().__init__()
        self.stat ={"Attack": 9, "Defense": 15,
                         "Health": 115,"Stamina": 10}

