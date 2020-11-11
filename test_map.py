import unittest
from main import read_input, parse_input, init_map, move_adventurers, parse_adventurers

class TestMap(unittest.TestCase):

    def test_read_file(self):
        read = read_input('test_input.txt')
        self.assertEqual(read, ['C - 3 - 4', 'M - 2 - 1', 'T - 1 - 2 - 3', 'A - Lara - 1 - 1 - N - AADA'], "Should be 6")

    def test_parse_input(self):
        parsed = parse_input(['C - 3 - 4', 'M - 2 - 1', 'T - 1 - 2 - 3', 'A - Lara - 1 - 1 - N - AADA'])
        result = {'C': [{1: '3', 2: '4'}], 'M': [{1: '2', 2: '1'}], 'T': [{1: '1', 2: '2', 3: '3'}], 'A': [{1: 'Lara', 2: '1', 3: '1', 4: 'N', 5: 'AADA'}]}
        self.assertEqual(parsed, result, "Should be 6")

    def test_init_map(self):
        parsed = {'C': [{1: '3', 2: '4'}], 'M': [{1: '2', 2: '1'}], 'T': [{1: '1', 2: '2', 3: '3'}], 'A': [{1: 'Lara', 2: '1', 3: '1', 4: 'N', 5: 'AADA'}]}
        t_map = init_map(parsed)
        self.assertEqual(t_map, [['', '', ''], ['', 'A-Lara', 'M'], ['', 'T(3)', ''], ['', '', '']], "Should be 6")
    
    def test_parse_adventurers(self):
        input = {'C': [{1: '3', 2: '4'}], 'M': [{1: '2', 2: '1'}], 'T': [{1: '1', 2: '2', 3: '3'}], 'A': [{1: 'Lara', 2: '1', 3: '1', 4: 'N', 5: 'AADA'}]}
        advens_seq = parse_adventurers(input)
        self.assertEqual(advens_seq, ({'Lara': {'x': '1', 'y': '1', 'direc': 'N', 'seq': ['Lara-A', 'Lara-A', 'Lara-D', 'Lara-A'], 'len_seq': 4, 'treasure': 0}}, ['Lara-A', 'Lara-A', 'Lara-D', 'Lara-A']))

    def test_move_adventurers(self):
        treasure_map = [['', '', ''], ['', 'A-Lara', 'M'], ['', 'T(3)', ''], ['', '', '']]
        positions = {'Lara': {'x': '1', 'y': '1', 'direc': 'N', 'seq': ['Lara-A', 'Lara-A', 'Lara-D', 'Lara-A'], 'len_seq': 4, 'treasure': 0}}
        sequence = ['Lara-A', 'Lara-A', 'Lara-D', 'Lara-A']
        move_adventurers(treasure_map,  positions, sequence)
        self.assertEqual(treasure_map, [['', '', 'A-Lara'], ['', '', 'M'], ['', 'T(3)', ''], ['', '', '']])

if __name__ == '__main__':
    unittest.main()
