import time
from player import Player
import colored
from colored import stylize
P = Player()


class Story:
    def __init__(self):
        self.the_beginning = (stylize("\nIn a cave, you were born and around you there are too many books and the 'Holy Sword' , you have learnt about  each era of this world by reading books....though you dont know, which era are you living. You have learnt how to use the 'Holy Sword'.\n\nOne day, you were going to read one last book before taking a journey in this vast cave,in this book you found a note:\n'Please save me from the monsters'\n-The Princess. \n\nYour instinct tells you to save her, and like this you started your journey.\n ",colored.fg('dark_gray')))
        self.step2 = (stylize(
            "\nYou are walking in the cave, trying to collect your bravery , you see an enemy ,you walk slowly toward him and to kill him....\n",colored.fg('indian_red_1a')))
        self.step4 = (stylize("\nYou defeated the enemy, you are so happy that your time that went on reading books as a kid was not a waste!, you start walking more to face a bigger threat.\n",colored.fg('yellow_4b')))
        self.step6 = (stylize(
            "\nYou climb up the stair and you see a new area that you have never seen, it is dark ,and so your mind....because you dont know your reality yet.\n",colored.fg('magenta')))
        self.step8 = (stylize(
            f"\nYour 'Holy sword' is almost broken, you fought so well.\nYou hear the princess shouting for help, you save her, and both of you are happy.\n'Princess':Thanks for saving me!, what is your name ?\nYou :{P.name}.\nAnd now you gotta fight one last enemy and move with the princess\n",colored.fg('chartreuse_3b')))
        self.step10 = (stylize (f"'Princess' : **EVIL LAUGH**.\n'{P.name}': Hm? \n'Princess' : I AM THE ONE WHO TRAPPED YOU IN THIS CAVE SINCE YOU WERE A NEW BORN.\n'{P.name}': Did you really do that?b..but why?.\n'Princess': I SHALL NEVER TELL YOU.....**STABS**.\n'{P.name}': b...bu...but why you stabbed me ? i saved you!\n'The Princess': **Transfer to an evil monster and leaves you **.\n\n You are injured, you look at this monster making a big hole in the cave and it leave the caves. You are confused,but you realize that you gotta save the world from this monster.\n.....To Be Continued.\n\n",colored.fg('dark_orange')))
