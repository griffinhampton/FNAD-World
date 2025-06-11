#Griffin Hampton FNAD world 2D. CSE-120
import sys

from introScreen import *
from src.gameLogic import *

if __name__ == '__main__':
    print(__name__)
    root.mainloop()
    g = Game()
    g.new()
    while g.running:
        g.main()
        g.game_over()

    pygame.quit()
    sys.exit()
