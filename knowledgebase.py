import pprint
from copy import deepcopy

class KnowledgeBase(object):
    '''
    Represent the board by mapping a tuple (i,j) to a dictionary of 
    percepts.

    For example
    (1, 2) : { 'Breeze': None, 'Stench': True, 'Glitter': None }
    '''

    def __init__(self):
        self.kb = {}

        # clear out the KB from any previous runs 
        f = open('KB.dat', 'w').close()

    def write(self, player):
        '''Write the current state of the player to the KB'''
        key = player.x, player.y
        i,j = player.i, player.j
        if key not in self.kb:
            self.kb[key] = deepcopy(player.board.percepts[i][j]) 
            with open('KB.dat', 'a') as f:
                f.write(str(key) + ' : ' + str(self.kb[key]) + '\n')

    def __repr__(self):
        '''Print nicely'''
        return pprint.pformat(self.kb)







