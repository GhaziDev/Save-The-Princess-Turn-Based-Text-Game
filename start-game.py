import sys
from output_unbuffering import Unbuffered
sys.stdout = Unbuffered(sys.stdout)
from operations import Operations
from role import Role

if __name__=='__main__':
    r=Role()
    O = Operations()
    O.ask_player()
