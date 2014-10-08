import unittest
from board import Board
from player import Player

class simpleTest(unittest.TestCase):

    def setUp(self):
        self.board = Board('input-1.txt')
        self.player = Player(self.board)

    def test_board_integrity(self):
        ''' board must be n x n '''
        n = len(self.board.percepts)
        self.assertTrue(all([n==len(row) for row in self.board.percepts]))

    def test_initial_player_config(self):
        ''' position 1,1 facing east '''
        self.assertTrue(self.player.direction() == 'EAST')
        self.assertTrue(self.player.x == self.player.y == 1)



if __name__ == '__main__':
  unittest.main()
