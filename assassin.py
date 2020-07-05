from role import Role
class Assassin(Role):
    def __init__(self):
        super().__init__()
        self.stat ={"Attack": 18, "Defense": 2,
                         "Health": 90,"Stamina": 10}

