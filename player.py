from copy import deepcopy
from knowledgebase import KnowledgeBase

class Player(object):

    def __init__(self, board):
        self.board = board
        self.kb = KnowledgeBase()
        self.alive = True
        self.win   = False
        self.d     = 'E'
        self.arrows = 1
        self.score  = 0

        # x,y are the 'printed' coordinates, starting at 1,1
        # i,j are the 'actual'  coordinates, starting at len - 1, 0
        self.x = self.y = 1 
        self.i = len(self.board.grid) - 1
        self.j = 0

        # check to see if we started in the goal state
        self.kb.write(self)
        if self.board.percepts[self.i][self.j]['Glitter']:
            self.win = True

    def print_location(self):
        print("You are in room [{}, {}] of the cave. Facing {}".format(
            self.x, self.y, self.direction()))

    def print_percepts(self):
        percepts = [k.upper() 
                for k,v in self.board.percepts[self.i][self.j].items() if v]
        p = " and a ".join(percepts)
        if p:
            print('There is a {} in here!'.format(p))

    def forward(self):
        # get next tile, increment x,y,i,j, check for bump
        move = self.possible_moves().get(self.d)

        if move: 
            self.move(*move)

        else:
            print('BUMP!!!  You hit a wall!')

    def left(self):
        ''' turn player left '''
        cycle = ['N', 'W', 'S', 'E', 'N']
        i = cycle.index(self.d) + 1
        self.d = cycle[i]

    def right(self):
        ''' turn player right '''
        cycle = ['N', 'E', 'S', 'W', 'N']
        i = cycle.index(self.d) + 1
        self.d = cycle[i]

    def execute(self, command):

        if command == 'L':
            self.left()

        elif command == 'R':
            self.right()

        elif command == 'F':
            self.forward()

        elif command == 'S':
            if self.arrows > 0:
                hit = self.shoot()
                if not hit:
                    print('You missed! {} arrows remaining'.format(self.arrows))

            else: 
                print('You have no arrows left!')

    def shoot(self):
        '''
        returns True if player had an arrow and hit the wumpus.
        '''
        self.arrows -= 1 
        self.score -= 10

        candidates = []
        dummy_player = deepcopy(self)
        move = dummy_player.possible_moves().get(dummy_player.d)

        while move:
            candidates.append(move[:2])
            dummy_player.i, dummy_player.j, dummy_player.x, \
                    dummy_player.y = move
            move = dummy_player.possible_moves().get(dummy_player.d)

        for x,y in candidates:
            if self.board.grid[x][y] == 'W':
                self.scream()
                self.score += 500
                return True

        return False

    def scream(self):
        print("You hear a SCREAM!!! The Wumpus is dead!")

    def possible_moves(self):
        i,j,x,y = self.i, self.j, self.x, self.y
        directions = ('N', 'S', 'W', 'E')
        candidates = [(i-1, j, x, y+1), (i+1, j, x, y-1), 
                (i, j-1, x-1, y), (i, j+1, x+1, y) ]
        candidates =  [c if (c[0] > -1 and c[0] < len(self.board.grid) and \
                    c[1] > -1 and c[1] < len(self.board.grid)) else None
                for c in candidates]

        return { d:c for d,c in zip(directions,candidates) }

    def move(self, i,j,x,y):
        ''' update player information. only call move() after validating 
        the move '''

        self.i, self.j, self.x, self.y = i,j,x,y
        self.score -= 1
        self.kb.write(self)

        if self.board.grid[i][j] == 'W':
            print("You were eaten by the Wumpus. Sorry. -1000 Points")
            self.alive = False

        elif self.board.grid[i][j] == 'P':
            print("You fell into a pit. Sorry. -1000 Points")
            self.alive = False

        if not self.alive:
            self.score -= 1000

        if self.board.percepts[i][j]['Glitter']:
            self.score += 1000
            self.win = True

    def prompt(self):
        return "What would you like to do? Please enter command [R,L,F,S]:\n> "

    def direction(self):
        return {
                'E': 'EAST', 
                'W': 'WEST', 
                'S': 'SOUTH', 
                'N': 'NORTH', 
                }.get(self.d)


