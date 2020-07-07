import sys
from output_unbuffering import Unbuffered

from operations import Operations
from role import Role

if __name__=='__main__':
    sys.stdout = Unbuffered(sys.stdout)
    O = Operations()
    O.ask_player()
