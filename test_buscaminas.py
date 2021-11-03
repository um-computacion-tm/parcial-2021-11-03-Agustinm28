import unittest
import unittest.mock

from buscaminas import Buscaminas


class TestBuscaminas(unittest.TestCase):
    def setUp(self):
        self.caso1 = [['2', 'B', '2', ' ', '1', 'B', 'B', '1'],
                      ['3', 'B', '3', ' ', '1', '3', '3', '2'],
                      ['3', 'B', '3', ' ', ' ', '1', 'B', '1'],
                      ['4', 'B', '3', ' ', ' ', '1', '1', '1'],
                      ['B', 'B', '2', ' ', ' ', ' ', ' ', ' '],
                      ['2', '2', '1', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', '1', '1', '1', ' ', ' ', ' '],
                      [' ', ' ', '1', 'B', '1', ' ', ' ', ' ']]
        self.caso2 = [[' ', '1', 'B', 'B', '1', ' ', '1', 'B'],
                      ['1', '2', '2', '2', '1', ' ', '1', '1'],
                      ['B', '3', '2', '1', ' ', ' ', '1', '1'],
                      ['2', 'B', 'B', '2', ' ', ' ', '1', 'B'],
                      ['2', '4', 'B', '2', ' ', ' ', '1', '1'],
                      ['1', 'B', '3', '2', ' ', ' ', ' ', ' '],
                      ['1', '2', 'B', '1', ' ', ' ', ' ', ' '],
                      [' ', '1', '1', '1', ' ', ' ', ' ', ' ']]

    def test_win_caso1(self):
        buscaminas = Buscaminas(8, 8, 10)
        buscaminas.board = self.caso1
        buscaminas.show = [['2', 'F', '2', ' ', '1', 'F', 'F', '1'],
                           ['3', 'F', '3', ' ', '1', '3', '3', '2'],
                           ['3', 'F', '3', ' ', ' ', '1', 'F', '1'],
                           ['4', 'F', '3', ' ', ' ', '1', '1', '1'],
                           ['F', 'F', '2', ' ', ' ', ' ', ' ', ' '],
                           ['2', '2', '1', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', '1', '1', '1', ' ', ' ', ' '],
                           [' ', ' ', '1', 'F', '1', ' ', ' ', ' ']]
        self.assertEqual(buscaminas.win(), True)

    def test_win_caso2(self):
        buscaminas = Buscaminas(8, 8, 10)
        buscaminas.board = self.caso2
        buscaminas.show = [[' ', ' ', 'F', 'F', ' ', ' ', ' ', 'F'],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           ['F', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', 'F', 'F', ' ', ' ', ' ', ' ', 'F'],
                           [' ', ' ', 'F', ' ', ' ', ' ', ' ', ' '],
                           [' ', 'F', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', 'F', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(buscaminas.win(), True)

    def test_lose_caso1(self):
        buscaminas = Buscaminas(8, 8, 10)
        buscaminas.board = self.caso1
        buscaminas.show = [[' ', 'B', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(buscaminas.lose(), True)

    def test_lose_caso2(self):
        buscaminas = Buscaminas(8, 8, 10)
        buscaminas.board = self.caso1
        buscaminas.show = [[' ', '1', 'F', 'F', '1', ' ', '1', 'F'],
                           ['1', '2', '2', '2', '1', ' ', '1', '1'],
                           ['B', '3', '2', '1', ' ', ' ', '1', '1'],
                           ['2', 'F', 'F', '2', ' ', ' ', '1', 'F'],
                           ['2', '4', 'F', '2', ' ', ' ', '1', '1'],
                           ['1', 'F', '3', '2', ' ', ' ', ' ', ' '],
                           ['1', '2', 'F', '1', ' ', ' ', ' ', ' '],
                           [' ', '1', '1', '1', ' ', ' ', ' ', ' ']]
        self.assertEqual(buscaminas.lose(), True)

    @unittest.mock.patch('builtins.input', side_effect=['uncover', 0, 3])
    def test_question_uncover(self, values):
        buscaminas = Buscaminas(5, 5, 8)
        movs = ['flag', 'uncover']
        mov, row, col = buscaminas.question(movs)
        self.assertEqual(mov, 'uncover')
        self.assertEqual(row, 0)
        self.assertEqual(col, 3)

    @unittest.mock.patch('builtins.input', side_effect=['flag', 2, 2])
    def test_question_flag(self, values):
        buscaminas = Buscaminas(5, 5, 8)
        movs = ['flag', 'uncover']
        mov, row, col = buscaminas.question(movs)
        self.assertEqual(mov, 'flag')
        self.assertEqual(row, 2)
        self.assertEqual(col, 2)

    @unittest.mock.patch('builtins.input', return_value='bomb')
    def test_question_error(self, values):
        buscaminas = Buscaminas(5, 5, 8)
        movs = ['flag', 'uncover']
        with self.assertRaises(Exception):
            mov, row, col = buscaminas.question(movs)

    def test_play_uncover(self):
        buscaminas = Buscaminas(8, 8, 10)
        buscaminas.board = self.caso1
        buscaminas.show = [['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-']]
        buscaminas.play('uncover', 2, 2)
        self.assertEqual(buscaminas.show, [['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '3', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-']])
        buscaminas.play('uncover', 3, 3)
        self.assertEqual(buscaminas.show, [['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '3', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', ' ', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-']])

    def test_play_flag(self):
        buscaminas = Buscaminas(8, 8, 10)
        buscaminas.board = self.caso2
        buscaminas.show = [['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-', '-']]
        buscaminas.play('flag', 0, 2)
        self.assertEqual(buscaminas.show, [['-', '-', 'F', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-']])
        buscaminas.play('flag', 5, 1)
        self.assertEqual(buscaminas.show, [['-', '-', 'F', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', 'F', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-'],
                                           ['-', '-', '-', '-', '-', '-', '-', '-']])



if __name__ == '__main__':
    unittest.main()
