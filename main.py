import sys
from board import Board
from player import Player

if __name__ == '__main__':
    b = Board('input-1.txt')
    p = Player(b)

    while (p.alive):

        # Check for goal state
        if (p.win):
            print('Congrats, you win!')
            break

        p.print_location()
        p.print_percepts()
        command = input(p.prompt()).strip().upper()

        # Basic command validation
        if command not in ('R', 'L', 'F', 'S'):
            print('Unknown command!\n')
            continue

        p.execute(command)

