class Board(object):
    '''
    Represents the complete game board read from the file
    NOTES: reverse the grid to comply? or not care
    '''

    def __init__(self, filename):
        with open(filename) as f:
            self.grid = [ line.strip().split(',') 
                    for line in f.readlines() ]

            self.percepts = [[self._defaultdict() for i in row] 
                    for row in self.grid]

        # map 'Pit' to 'Breeze' percept, and so on
        self._map = {'P': 'Breeze', 'G': 'Glitter', 'W': 'Stench', 'X': None}

        # insert perceptions to each room
        for x,row in enumerate(self.grid):
            for y,room in enumerate(row):
                percept = self._map[room]
                if percept and percept != 'Glitter':
                    for i,j in self._adjacent(x,y):
                        self.percepts[i][j][percept] = True

                elif percept and percept == 'Glitter':
                    self.percepts[x][y][percept] = True

    def __repr__(self):
        rep = ''
        for row in self.grid:
            rep += ' '.join(row) + '\n'

        return rep.strip()

    def _defaultdict(self):
        return {'Breeze': None, 'Glitter': None, 'Stench': None}

    def _adjacent(self, i,j):
        '''
        Returns a list of tuples (x,y) that represent rooms adjacent to
        i,j (left, right, up, down).
        '''
        candidates = [(i,j), (i-1, j), (i+1, j), (i, j-1), (i, j+1) ]
        return [c for c in candidates 
                if (c[0] > -1 and c[0] < len(self.grid) and \
                    c[1] > -1 and c[1] < len(self.grid)) ]
