import sys
from board import Board
from player import Player

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit('USAGE: python3 main.py <input-file.txt>')

    b = Board(sys.argv[1])
    p = Player(b)

    while (p.alive):
        p.print_location()
        p.print_percepts()

        # Check for goal state
        if (p.win):
            print('Congrats, you win!')
            break

        command = input(p.prompt()).strip().upper()

        # Basic command validation
        if command not in ('R', 'L', 'F', 'S'):
            print('Unknown command!\n')
            continue

        p.execute(command)

    print("You scored: {}".format(p.score))

