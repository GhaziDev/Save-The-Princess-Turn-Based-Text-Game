import sys
from Output_Unbuffering import Unbuffered
sys.stdout = Unbuffered(sys.stdout)
from Operations import Operations
if __name__=='__main__':
    O = Operations()
    O.ask_player()
