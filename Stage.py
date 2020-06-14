import time


class Stage:
    def __init__(self):
        self.stage = 1
        self.last_stage = 3

    def stage_up(self):
        stage = f"STAGE {self.stage}"
        for i in stage:
            print(i, end="")
            time.sleep(0.1)
